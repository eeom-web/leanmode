"""Builds the blog posts from posts/<slug>/post.md.

For every post folder with a post.md this writes:
  post.html      article text in WordPress block markup (Gutenberg)
  post.json      title, excerpt, category, tags, images and pin texts (read by the deploy step)
  featured.webp  featured image (1200 x 1500)
  pin-1.jpg      pin with title band and three points (1000 x 1500)
  pin-2.jpg      pin with a big headline (1000 x 1500)
and posts/manifest.json with the sha256 of every file the deploy step uploads.

post.md starts with a front matter block (key: value lines between ---), then the article in a small Markdown
subset: ## / ### headings, paragraphs, "- " and "1. " lists, tables (| a | b |), "> " tip boxes, **bold**, *italic*
and [links](/url/). Usage: python3 build.py [--no-images] [slug ...]
"""
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.join(HERE, "posts")
CTA = ("Want a simple day-by-day plan that puts all of this together, with meals, short workouts and a shopping "
       "list? [Get the free 30-Day Weight Loss Plan below.](#lmp-box-title)")


def parse(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise SystemExit(f"{path}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if line.strip():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
    return meta, m.group(2).strip()


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s


def paragraph(s):
    return f"<!-- wp:paragraph -->\n<p>{inline(s)}</p>\n<!-- /wp:paragraph -->"


def blocks(md):
    out = []
    for chunk in re.split(r"\n\s*\n", md.strip()):
        lines = [l.rstrip() for l in chunk.strip().splitlines()]
        first = lines[0]
        if first.startswith("### "):
            out.append(f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{inline(first[4:])}</h3>\n<!-- /wp:heading -->')
        elif first.startswith("## "):
            out.append(f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{inline(first[3:])}</h2>\n<!-- /wp:heading -->')
        elif first.startswith("- ") or re.match(r"\d+\. ", first):
            ordered = not first.startswith("- ")
            items = [re.sub(r"^(- |\d+\. )", "", l) for l in lines]
            tag = "ol" if ordered else "ul"
            attrs = ' {"ordered":true}' if ordered else ""
            li = "\n\n".join(f"<!-- wp:list-item -->\n<li>{inline(i)}</li>\n<!-- /wp:list-item -->" for i in items)
            out.append(f'<!-- wp:list{attrs} -->\n<{tag} class="wp-block-list">{li}</{tag}>\n<!-- /wp:list -->')
        elif first.startswith("|"):
            rows = [[c.strip() for c in l.strip("|").split("|")] for l in lines if not re.match(r"^\|[\s:|-]+\|$", l)]
            head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append('<!-- wp:table {"hasFixedLayout":false} -->\n<figure class="wp-block-table"><table>'
                       f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></figure>\n<!-- /wp:table -->")
        elif first.startswith("> "):
            inner = "\n\n".join(paragraph(l[2:]) for l in lines)
            out.append(f'<!-- wp:quote -->\n<blockquote class="wp-block-quote">{inner}</blockquote>\n<!-- /wp:quote -->')
        else:
            out.append(paragraph(" ".join(lines)))
    return "\n\n".join(out) + "\n"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main(argv):
    images = "--no-images" not in argv
    only = [a for a in argv if not a.startswith("--")]
    slugs = sorted(d for d in os.listdir(POSTS) if os.path.isfile(os.path.join(POSTS, d, "post.md")))
    jobs, built = [], []
    tmp = tempfile.mkdtemp(prefix="lmp-blog-")
    for slug in slugs:
        if only and slug not in only:
            continue
        folder = os.path.join(POSTS, slug)
        meta, md = parse(os.path.join(folder, "post.md"))
        if "#lmp-box-title" not in md:
            md += "\n\n" + CTA
        open(os.path.join(folder, "post.html"), "w", encoding="utf-8").write(blocks(md))
        post = {
            "title": meta["title"],
            "slug": slug,
            "excerpt": meta["excerpt"],
            "category": meta["category"],
            "tags": [t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
            "featured_image": {"file": "featured.webp", "alt": meta["title"]},
            "images": {},
            "pins": [
                {"file": f"pin-{n}.jpg", "title": meta[f"pin{n}_title"], "description": meta[f"pin{n}_desc"],
                 "board": meta[f"pin{n}_board"], "link": f"https://leanmodepro.com/{slug}/"}
                for n in (1, 2)
            ],
        }
        json.dump(post, open(os.path.join(folder, "post.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        base = {"category": meta["category"], "icon": meta["icon"]}
        jobs += [
            {"out": os.path.join(tmp, f"{slug}-featured.png"), "w": 1200, "h": 1500,
             "job": {**base, "type": "featured", "title": meta["img_title"], "sub": meta["img_sub"]}},
            {"out": os.path.join(tmp, f"{slug}-pin1.png"), "w": 1000, "h": 1500,
             "job": {**base, "type": "pin1", "title": meta["img_title"], "kicker": meta["kicker"],
                     "points": [p.strip() for p in meta["points"].split(";")]}},
            {"out": os.path.join(tmp, f"{slug}-pin2.png"), "w": 1000, "h": 1500,
             "job": {**base, "type": "pin2", "headline": meta["headline"], "kicker": meta["kicker"],
                     "sub": meta["img_sub"]}},
        ]
        built.append(slug)

    if images and jobs:
        from PIL import Image
        jobs_file = os.path.join(tmp, "jobs.json")
        json.dump(jobs, open(jobs_file, "w"))
        subprocess.run(["node", os.path.join(HERE, "graphics", "render.mjs"), jobs_file], check=True)
        for slug in built:
            folder = os.path.join(POSTS, slug)
            Image.open(os.path.join(tmp, f"{slug}-featured.png")).convert("RGB").save(
                os.path.join(folder, "featured.webp"), "WEBP", quality=84, method=6)
            for n in (1, 2):
                Image.open(os.path.join(tmp, f"{slug}-pin{n}.png")).convert("RGB").save(
                    os.path.join(folder, f"pin-{n}.jpg"), "JPEG", quality=88, optimize=True, progressive=True)

    # Internal links must point to an existing post or page.
    pages = {"", "blog", "contact", "privacy-policy", "legal-notice", "disclaimer", "plate-method-for-weight-loss"}
    known = pages | set(slugs)
    for slug in built:
        for target in re.findall(r'href="/([a-z0-9-]*)/?(?:#[^"]*)?"', open(os.path.join(POSTS, slug, "post.html")).read()):
            if target not in known:
                print(f"WARNING {slug}: link to unknown page /{target}/")

    manifest = {}
    for slug in slugs:
        folder = os.path.join(POSTS, slug)
        files = ["post.json", "post.html", "featured.webp"]
        if all(os.path.isfile(os.path.join(folder, f)) for f in files):
            manifest[slug] = {f: sha(os.path.join(folder, f)) for f in files}
    json.dump(manifest, open(os.path.join(POSTS, "manifest.json"), "w"), indent=1, sort_keys=True)
    print(f"built {len(built)} posts; manifest lists {len(manifest)}")


if __name__ == "__main__":
    main(sys.argv[1:])
