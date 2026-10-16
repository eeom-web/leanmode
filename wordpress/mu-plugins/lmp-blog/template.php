<?php
/**
 * Lean Mode Pro blog template (single posts, blog index, archives). Loaded by ../lmp-blog.php.
 * Brand CSS/JS, the signup form and the cover come from the option `lmp_blog` (see dist/blog.json).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$lmp       = get_option( 'lmp_blog', array() );
$lmp_links = array(
	'Blog'           => '/blog/',
	'Contact'        => '/contact/',
	'Privacy Policy' => '/privacy-policy/',
	'Legal Notice'   => '/legal-notice/',
	'Disclaimer'     => '/disclaimer/',
);
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
<style id="lmp-blog">
body.lmp-blog{margin:0;background:#F6F5F1;color:#414B46;font-family:"Instrument Sans",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
.lmp-blog *,.lmp-blog *::before,.lmp-blog *::after{box-sizing:border-box}
.lmp-blog a{color:#1D5A48}
.lmp-wrap{width:100%;max-width:1180px;margin:0 auto;padding:0 32px}
@media (max-width:767px){.lmp-wrap{padding:0 16px}}
.lmp-bhead{position:sticky;top:0;z-index:50;background:rgba(246,245,241,.92);backdrop-filter:saturate(1.4) blur(10px);-webkit-backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid #E3E2DB}
.admin-bar .lmp-bhead{top:32px}
@media (max-width:782px){.admin-bar .lmp-bhead{top:46px}}
.lmp-bhead .lmp-wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:64px}
.lmp-brand{display:inline-flex;align-items:center;gap:10px;color:#101614!important;font-size:15px;font-weight:700;letter-spacing:.14em;text-decoration:none}
.lmp-brand::before{content:"";width:18px;height:18px;background:#1D5A48;-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect x='3' y='13' width='4.5' height='8' rx='1.25'/%3E%3Crect x='9.75' y='8.5' width='4.5' height='12.5' rx='1.25'/%3E%3Crect x='16.5' y='3' width='4.5' height='18' rx='1.25'/%3E%3C/svg%3E") center/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect x='3' y='13' width='4.5' height='8' rx='1.25'/%3E%3Crect x='9.75' y='8.5' width='4.5' height='12.5' rx='1.25'/%3E%3Crect x='16.5' y='3' width='4.5' height='18' rx='1.25'/%3E%3C/svg%3E") center/contain no-repeat}
.lmp-brand span{color:#1D5A48}
.lmp-cta{display:inline-flex;align-items:center;padding:10px 18px;border-radius:999px;background:#101614;color:#fff!important;font-size:14px;font-weight:600;line-height:1.2;text-decoration:none;white-space:nowrap}
.lmp-cta:hover{background:#2A3430}
.lmp-bmain{padding:56px 0 72px}
.lmp-post{max-width:720px;margin:0 auto}
.lmp-crumb{margin:0 0 16px;font-size:14px;font-weight:600}
.lmp-crumb a{text-decoration:none}
.lmp-post h1,.lmp-archive h1{margin:0 0 12px;color:#101614;font-size:clamp(32px,5vw,46px);font-weight:600;line-height:1.1;letter-spacing:-.025em}
.lmp-post__meta{margin:0 0 28px;color:#5D6762;font-size:14px}
.lmp-post__image{margin:0 0 28px}
.lmp-post__image img{display:block;width:100%;height:auto;border-radius:20px}
.lmp-post__disclosure,.lmp-post__health{margin:0 0 28px;padding:12px 16px;border-left:3px solid #1D5A48;border-radius:0 12px 12px 0;background:#EEF4F0;color:#414B46;font-size:14px;line-height:1.55}
.lmp-post__health{margin:40px 0 0;border-left-color:#B9A676;background:#FFFFFF}
.lmp-content{font-size:18px;line-height:1.72}
.lmp-content>*{margin-top:0;margin-bottom:1.1em}
.lmp-content h2{margin:1.8em 0 .6em;color:#101614;font-size:28px;font-weight:600;line-height:1.2;letter-spacing:-.015em}
.lmp-content h3{margin:1.5em 0 .5em;color:#101614;font-size:21px;font-weight:600;line-height:1.3}
.lmp-content ul,.lmp-content ol{padding-left:1.3em}
.lmp-content li{margin:0 0 .45em}
.lmp-content strong{color:#101614;font-weight:600}
.lmp-content img{max-width:100%;height:auto;border-radius:16px}
.lmp-content figure{margin-left:0;margin-right:0}
.lmp-content figcaption{color:#5D6762;font-size:14px}
.lmp-content blockquote{margin:1.6em 0;padding:4px 0 4px 20px;border-left:3px solid #1D5A48;color:#101614;font-size:20px}
.lmp-content table{width:100%;border-collapse:collapse;font-size:16px}
.lmp-content th,.lmp-content td,.lmp-content .wp-block-table th,.lmp-content .wp-block-table td{padding:10px 14px 10px 0;border:0;border-bottom:1px solid #E3E2DB;text-align:left;vertical-align:top}
.lmp-content .wp-block-table thead{border-bottom:2px solid #101614}
.lmp-content th{color:#101614;font-weight:600}
.lmp-content a{text-decoration:underline;text-underline-offset:2px}
.lmp-content .lmp-aff{color:#5D6762;font-size:.8em;white-space:nowrap}
.lmp-box{display:grid;grid-template-columns:150px 1fr;gap:28px;align-items:center;margin:48px 0 0;padding:28px;border:1px solid #D5E4DA;border-radius:28px;background:#E3EDE7}
.lmp-box__visual .lmp-mockup{--book-w:130px;padding:0}
.lmp-box__visual .lmp-mockup::before{display:none}
.lmp-box__label{margin:0 0 6px;color:#1D5A48;font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
.lmp-box__title{margin:0 0 8px;color:#101614;font-size:26px;font-weight:600;line-height:1.15;letter-spacing:-.02em}
.lmp-box__text{margin:0 0 16px;color:#2A3430}
@media (max-width:640px){.lmp-box{grid-template-columns:1fr;padding:22px 18px}.lmp-box__visual{display:none}}
.lmp-archive__intro{max-width:640px;margin:0 0 36px;font-size:19px}
.lmp-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
@media (max-width:1024px){.lmp-cards{grid-template-columns:repeat(2,1fr)}}
@media (max-width:600px){.lmp-cards{grid-template-columns:1fr}}
.lmp-card{display:flex;flex-direction:column;overflow:hidden;border:1px solid #E3E2DB;border-radius:24px;background:#fff;text-decoration:none!important;color:inherit!important;transition:transform .2s ease,box-shadow .2s ease}
.lmp-card:hover{transform:translateY(-2px);box-shadow:0 18px 40px -24px rgba(16,22,20,.35)}
.lmp-card__img{aspect-ratio:4/5;background:#E3EDE7}
.lmp-card__img img{display:block;width:100%;height:100%;object-fit:cover}
.lmp-card__body{padding:20px 22px 24px}
.lmp-card__title{margin:0 0 8px;color:#101614;font-size:20px;font-weight:600;line-height:1.25}
.lmp-card__excerpt{margin:0;color:#5D6762;font-size:15px;line-height:1.55}
.lmp-empty{padding:32px;border:1px dashed #D2D1C9;border-radius:24px;color:#5D6762;text-align:center}
.lmp-pagination{margin:40px 0 0;text-align:center}
.lmp-pagination .page-numbers{display:inline-block;margin:0 4px;padding:8px 14px;border-radius:999px;color:#101614;text-decoration:none}
.lmp-pagination .current{background:#101614;color:#fff}
.lmp-bfoot{border-top:1px solid #E3E2DB;padding:40px 0 48px;color:#5D6762;font-size:14px}
.lmp-bfoot .lmp-wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px}
.lmp-bfoot nav{display:flex;flex-wrap:wrap;gap:12px 28px}
.lmp-bfoot nav a{color:#5D6762;text-decoration:none}
.lmp-bfoot nav a:hover{color:#101614}
.lmp-bfoot p{width:100%;margin:8px 0 0}
</style>
</head>
<body <?php body_class( 'lmp-blog' ); ?>>
<?php wp_body_open(); ?>
<?php echo $lmp['assets'] ?? ''; // phpcs:ignore WordPress.Security.EscapeOutput -- trusted brand CSS/JS from our own build ?>
<header class="lmp-bhead"><div class="lmp-wrap">
<a class="lmp-brand" href="<?php echo esc_url( home_url( '/' ) ); ?>">LEAN MODE <span>PRO</span></a>
<a class="lmp-cta" href="<?php echo esc_url( home_url( '/#signup' ) ); ?>">Get the Free Plan</a>
</div></header>

<main class="lmp-bmain"><div class="lmp-wrap">
<?php if ( is_singular( 'post' ) ) : ?>
	<?php while ( have_posts() ) : the_post(); ?>
	<article class="lmp-post">
		<p class="lmp-crumb"><a href="<?php echo esc_url( home_url( '/blog/' ) ); ?>">← Blog</a></p>
		<h1><?php the_title(); ?></h1>
		<p class="lmp-post__meta"><?php echo esc_html( get_the_date( 'F j, Y' ) ); ?></p>
		<?php if ( has_post_thumbnail() ) : ?>
			<div class="lmp-post__image"><?php the_post_thumbnail( 'large', array( 'loading' => 'eager', 'fetchpriority' => 'high' ) ); ?></div>
		<?php endif; ?>
		<?php echo lmp_affiliate_note(); // phpcs:ignore WordPress.Security.EscapeOutput ?>
		<div class="lmp-content"><?php the_content(); ?></div>
		<section class="lmp-box" aria-labelledby="lmp-box-title">
			<div class="lmp-box__visual"><?php echo $lmp['mockup'] ?? ''; // phpcs:ignore WordPress.Security.EscapeOutput ?></div>
			<div>
				<p class="lmp-box__label">Free e-book</p>
				<h2 class="lmp-box__title" id="lmp-box-title">Get the free 30-Day Weight Loss Plan</h2>
				<p class="lmp-box__text">One clear step every day: meals, movement, workouts and habits in one simple plan.</p>
				<?php echo $lmp['form'] ?? ''; // phpcs:ignore WordPress.Security.EscapeOutput ?>
			</div>
		</section>
		<?php echo lmp_health_note(); // phpcs:ignore WordPress.Security.EscapeOutput ?>
	</article>
	<?php endwhile; ?>
<?php else : ?>
	<section class="lmp-archive">
		<?php if ( is_home() ) : ?>
			<h1>Blog</h1>
			<p class="lmp-archive__intro">Simple, practical tips for eating better, moving more and losing weight step by step.</p>
		<?php else : ?>
			<h1><?php echo esc_html( wp_strip_all_tags( get_the_archive_title() ) ); ?></h1>
			<div class="lmp-archive__intro"><?php the_archive_description(); ?></div>
		<?php endif; ?>
		<?php if ( have_posts() ) : ?>
			<div class="lmp-cards">
			<?php while ( have_posts() ) : the_post(); ?>
				<a class="lmp-card" href="<?php the_permalink(); ?>">
					<div class="lmp-card__img"><?php if ( has_post_thumbnail() ) { the_post_thumbnail( 'medium_large' ); } ?></div>
					<div class="lmp-card__body">
						<h2 class="lmp-card__title"><?php the_title(); ?></h2>
						<p class="lmp-card__excerpt"><?php echo esc_html( wp_trim_words( get_the_excerpt(), 22, '…' ) ); ?></p>
					</div>
				</a>
			<?php endwhile; ?>
			</div>
			<div class="lmp-pagination"><?php echo paginate_links(); // phpcs:ignore WordPress.Security.EscapeOutput ?></div>
		<?php else : ?>
			<p class="lmp-empty">The first articles are on their way.</p>
		<?php endif; ?>
	</section>
<?php endif; ?>
</div></main>

<footer class="lmp-bfoot"><div class="lmp-wrap">
<a class="lmp-brand" href="<?php echo esc_url( home_url( '/' ) ); ?>">LEAN MODE <span>PRO</span></a>
<nav aria-label="Footer">
<?php foreach ( $lmp_links as $lmp_label => $lmp_href ) : ?>
<a href="<?php echo esc_url( home_url( $lmp_href ) ); ?>"><?php echo esc_html( $lmp_label ); ?></a>
<?php endforeach; ?>
</nav>
<p>© <?php echo esc_html( gmdate( 'Y' ) ); ?> Lean Mode Pro. All rights reserved.</p>
</div></footer>
<?php wp_footer(); ?>
</body>
</html>
