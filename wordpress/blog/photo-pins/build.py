"""Builds the 30 Pinterest pins with real photos from pins.json.

    python3 build.py --fetch                      # download the Pexels photos into photos/ (not in git)
    PW_PATH=/path/to/playwright python3 build.py  # render all pins into pins/
    PW_PATH=... python3 build.py 4 8              # only pins 4 and 8
    python3 build.py --photos /other/dir ...      # photos from another folder

Photos: Pexels license (free, commercial use, no credit needed). Only the finished pins go into git, never the
original photos.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PEXELS = 'https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&h=1500'


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def out_name(pin):
    return f"{pin['n']:02d}-{slugify(pin['headline'])}.jpg"


def main(argv):
    photos = os.path.join(HERE, 'photos')
    if '--photos' in argv:
        i = argv.index('--photos')
        photos = os.path.abspath(argv[i + 1])
        del argv[i:i + 2]
    pins = json.load(open(os.path.join(HERE, 'pins.json'), encoding='utf-8'))
    only = {int(a) for a in argv if a.isdigit()}
    if only:
        pins = [p for p in pins if p['n'] in only]

    if '--fetch' in argv:
        os.makedirs(photos, exist_ok=True)
        for p in pins:
            path = os.path.join(photos, f"{p['pexels']}.jpg")
            if not os.path.exists(path):
                req = urllib.request.Request(PEXELS.format(p['pexels']), headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=60) as r, open(path, 'wb') as f:
                    f.write(r.read())
            print('photo', p['n'], path)
        return

    os.makedirs(os.path.join(HERE, 'pins'), exist_ok=True)
    jobs = []
    for p in pins:
        photo = os.path.join(photos, f"{p['pexels']}.jpg")
        if not os.path.exists(photo):
            sys.exit(f"missing photo {photo} (run: python3 build.py --fetch)")
        job = {k: p.get(k) for k in ('layout', 'pos', 'kicker', 'headline', 'hl', 'sub', 'card')}
        job['photo'] = 'file://' + photo
        jobs.append({'out': os.path.join(HERE, 'pins', out_name(p)), 'job': job})
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
        json.dump(jobs, f)
    try:
        subprocess.run(['node', os.path.join(HERE, 'render.mjs'), f.name], check=True)
    finally:
        os.unlink(f.name)


if __name__ == '__main__':
    main(sys.argv[1:])
