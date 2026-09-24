"""Raw HTML/CSS/JS used inside Elementor HTML widgets."""

ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>'
ARROW_DOWN = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 5v14"/><path d="m6 13 6 6 6-6"/></svg>'
CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
CAL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17"/><path d="M8 3v4"/><path d="M16 3v4"/></svg>'

CONSENT = ("Kayıt olarak ücretsiz planı almayı ve LEAN MODE PRO'dan e-posta yoluyla faydalı içerikler ve teklifler "
           "almayı kabul ediyorum. İstediğim zaman abonelikten çıkabilirim.")

LOGO_MASK = (
    "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E"
    "%3Crect x='3' y='13' width='4.5' height='8' rx='1.25'/%3E"
    "%3Crect x='9.75' y='8.5' width='4.5' height='12.5' rx='1.25'/%3E"
    "%3Crect x='16.5' y='3' width='4.5' height='18' rx='1.25'/%3E%3C/svg%3E\")"
)

CSS = """
html{scroll-behavior:smooth;scroll-padding-top:96px}
body{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:optimizeLegibility}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{transition-duration:.01ms!important;animation-duration:.01ms!important}}
[hidden]{display:none!important}
::selection{background:#E3EDE7;color:#101614}
.elementor .elementor-heading-title{text-wrap:balance}
.elementor-widget-text-editor p{margin:0 0 .75em}
.elementor-widget-text-editor p:last-child{margin-bottom:0}
.elementor a:focus-visible,.elementor button:focus-visible,.elementor input:focus-visible{outline:2px solid #1D5A48;outline-offset:3px}
.lmp-assets{position:absolute!important;width:1px;height:1px;overflow:hidden;margin:0!important}

/* Header */
.lmp-header{position:sticky;top:0;z-index:50;border-bottom:1px solid transparent;transition:background-color .25s ease,border-color .25s ease}
.admin-bar .lmp-header{top:32px}
@media (max-width:782px){.admin-bar .lmp-header{top:46px}}
@media (max-width:600px){.admin-bar .lmp-header{top:0}}
.lmp-header.is-scrolled{background:rgba(246,245,241,.86);border-bottom-color:#E3E2DB;-webkit-backdrop-filter:saturate(160%) blur(14px);backdrop-filter:saturate(160%) blur(14px)}
.lmp-logo .elementor-heading-title{display:inline-flex;align-items:center;gap:10px;white-space:nowrap}
.lmp-logo .elementor-heading-title a{color:inherit;text-decoration:none}
.lmp-logo .elementor-heading-title::before{content:"";flex:none;width:22px;height:22px;background:#1D5A48;-webkit-mask:MASK center/contain no-repeat;mask:MASK center/contain no-repeat}
.lmp-pro{color:#1D5A48}
.lmp-header-cta .elementor-button{white-space:nowrap}
@media (max-width:479px){.lmp-header-cta .elementor-button-icon{display:none}}
@media (max-width:399px){.lmp-logo .elementor-heading-title::before{display:none}}

/* Small elements */
.lmp-badge .elementor-heading-title{display:inline-flex;align-items:center;gap:8px}
.lmp-badge .elementor-heading-title::before{content:"";width:8px;height:8px;border-radius:50%;background:#1D5A48;box-shadow:0 0 0 3px #E3EDE7}
.lmp-eyebrow .elementor-heading-title{display:inline-flex;align-items:center;gap:8px}
.lmp-eyebrow .elementor-heading-title::before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
.lmp-accent-word{color:#1D5A48}
.lmp-chips .elementor-icon-list-items{gap:8px!important}
.lmp-chips .elementor-icon-list-item{margin:0!important;padding:6px 12px!important;border-radius:999px;background:#EEF4F0}
.lmp-chips .elementor-icon-list-item::after{display:none!important}
.lmp-card{transition:border-color .2s ease,box-shadow .2s ease}
.lmp-card:hover{border-color:#D2D1C9!important;box-shadow:0 1px 2px rgba(16,22,20,.04),0 10px 30px -12px rgba(16,22,20,.12)!important}
.lmp-steps ol{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:14px;counter-reset:lmp-step}
.lmp-steps li{counter-increment:lmp-step;display:flex;align-items:center;gap:14px}
.lmp-steps li::before{content:counter(lmp-step);flex:none;display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:#101614;color:#fff;font-size:14px;font-weight:600}
.lmp-daynum{color:#101614;font-size:28px;letter-spacing:-.02em;margin:0 4px}
.lmp-progress .elementor-progress-wrapper{border-radius:4px}
.lmp-progress .elementor-progress-bar{border-radius:4px;transition:none!important}
@media (min-width:1025px){.lmp-sticky{position:sticky;top:120px;align-self:flex-start}}

/* Noise -> one step */
.lmp-shift{display:grid;justify-items:center;gap:20px}
.lmp-shift__noise{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;max-width:26rem;margin:0;padding:0;list-style:none}
.lmp-shift__noise li{padding:8px 14px;border:1px solid rgba(238,242,239,.12);border-radius:999px;color:rgba(167,182,175,.75);font-size:14px;text-decoration:line-through;text-decoration-color:rgba(167,182,175,.6)}
.lmp-shift__arrow{display:grid;place-items:center;width:40px;height:40px;border:1px solid rgba(238,242,239,.14);border-radius:50%;color:#EEF2EF}
.lmp-shift__one{display:inline-flex;align-items:center;gap:10px;margin:0;padding:14px 22px;border-radius:999px;background:#EEF2EF;color:#0F1D19;font-size:17px;font-weight:600;box-shadow:0 20px 40px -16px rgba(0,0,0,.5)}
.lmp-shift__one svg{color:#1D5A48}
@media (max-width:1024px){.lmp-shift{justify-items:start}.lmp-shift__noise{justify-content:flex-start}}

/* Timeline */
.lmp-timeline{position:relative}
.lmp-milestone{position:relative;border-top:2px solid #D2D1C9}
.lmp-milestone::before{content:"";position:absolute;top:-9px;left:0;width:16px;height:16px;border-radius:50%;background:#1D5A48;box-shadow:0 0 0 4px #EFEEE8}
@media (max-width:767px){
.lmp-timeline{padding-left:36px!important}
.lmp-timeline::before{content:"";position:absolute;left:7px;top:10px;bottom:10px;width:2px;border-radius:2px;background:linear-gradient(#1D5A48,#E3EDE7)}
.lmp-milestone{border-top:0}
.lmp-milestone::before{top:12px;left:-36px}
}

/* Signup form */
.lmp-signup{container-type:inline-size;width:100%}
.lmp-signup__form{display:grid;gap:10px;margin:0}
.lmp-signup__label{color:#101614;font-size:15px;font-weight:600}
.lmp-signup__field{display:grid;gap:10px}
.lmp-signup__input{width:100%;min-height:60px;padding:0 22px;border:1px solid #D2D1C9;border-radius:999px;background:#fff;color:#101614;font:inherit;font-size:16px;outline:none;box-shadow:0 1px 2px rgba(16,22,20,.05);transition:border-color .2s ease,box-shadow .2s ease}
.lmp-signup__input::placeholder{color:#838c87}
.lmp-signup__input:focus{border-color:#1D5A48;box-shadow:0 0 0 4px rgba(29,90,72,.14)}
.lmp-signup__input[aria-invalid=true]{border-color:#B3261E}
.lmp-signup__button{display:inline-flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:60px;padding:14px 28px;border:0;border-radius:999px;background:#1D5A48;color:#fff;font:inherit;font-size:16px;font-weight:600;line-height:1.2;cursor:pointer;box-shadow:0 1px 2px rgba(16,22,20,.12),inset 0 1px 0 rgba(255,255,255,.12);transition:background-color .2s ease,transform .2s ease}
.lmp-signup__button:hover{background:#164A3B}
.lmp-signup__button:active{transform:translateY(1px)}
.lmp-signup__button svg{flex:none;transition:transform .2s ease}
.lmp-signup__button:hover svg{transform:translateX(3px)}
.lmp-signup__button:disabled{cursor:progress;opacity:.8}
@container (min-width:500px){
.lmp-signup__field{display:flex;gap:6px;padding:6px;border:1px solid #D2D1C9;border-radius:999px;background:#fff;box-shadow:0 1px 2px rgba(16,22,20,.04),0 10px 30px -12px rgba(16,22,20,.12);transition:border-color .2s ease,box-shadow .2s ease}
.lmp-signup__field:focus-within{border-color:#1D5A48;box-shadow:0 0 0 4px rgba(29,90,72,.14),0 10px 30px -12px rgba(16,22,20,.12)}
.lmp-signup__field:has([aria-invalid=true]){border-color:#B3261E}
.lmp-signup__input,.lmp-signup__input:focus,.lmp-signup__input[aria-invalid=true]{flex:1;min-width:0;min-height:52px;padding:0 8px 0 18px;border:0;box-shadow:none}
.lmp-signup__button{width:auto;min-height:52px}
}
.lmp-signup__error{margin:0;color:#B3261E;font-size:14px;font-weight:500}
.lmp-signup__error:empty{display:none}
.lmp-signup__consent{max-width:36rem;margin:0;padding:0 4px;color:#5D6762;font-size:12.5px;line-height:1.55}
.lmp-signup__consent a{color:inherit;text-decoration:underline;text-decoration-color:#D2D1C9;text-underline-offset:2px}
.lmp-signup__consent a:hover{color:#101614;text-decoration-color:currentColor}
.lmp-signup__hp{position:absolute;left:-10000px;width:1px;height:1px;overflow:hidden}
.lmp-signup__success{display:flex;align-items:flex-start;gap:16px;padding:22px 24px;border:1px solid #E3EDE7;border-radius:24px;background:#EEF4F0;outline:none}
.lmp-signup__success-icon{display:grid;flex:none;place-items:center;width:40px;height:40px;border-radius:50%;background:#1D5A48;color:#fff}
.lmp-signup__success-title{margin:0;color:#101614;font-size:17px;font-weight:600}
.lmp-signup__success-text{margin:4px 0 0;color:#414B46;font-size:15px}

/* E-book mockup */
.lmp-mockup{--book-w:min(66vw,300px);position:relative;display:grid;place-items:center;padding:32px 16px 40px;isolation:isolate}
.lmp-mockup--sm{--book-w:min(64vw,260px);padding:16px 8px 24px}
@media (min-width:1025px){.lmp-mockup:not(.lmp-mockup--sm){--book-w:360px}}
.lmp-mockup::before{content:"";position:absolute;inset:4% 0;z-index:-1;border-radius:50%;background:radial-gradient(closest-side,#dce8e0 0%,rgba(220,232,224,.55) 55%,rgba(220,232,224,0) 100%)}
.lmp-book{position:relative;width:var(--book-w);aspect-ratio:5/7;container-type:inline-size;filter:drop-shadow(0 30px 40px rgba(15,29,25,.22)) drop-shadow(0 6px 10px rgba(15,29,25,.12))}
.lmp-book__pages{position:absolute;inset:1.6% -3.2% 1.6% 4%;border-radius:3px 8px 8px 3px;background:linear-gradient(90deg,rgba(0,0,0,.08),transparent 30%),repeating-linear-gradient(90deg,#fbfaf6 0 1.5px,#e2e1d9 1.5px 2.5px)}
.lmp-book__cover{position:absolute;inset:0;display:flex;flex-direction:column;padding:9cqi 9cqi 8cqi 11cqi;border-radius:4px 10px 10px 4px;overflow:hidden;background:radial-gradient(120% 70% at 85% 0%,rgba(255,255,255,.1),transparent 60%),linear-gradient(160deg,#24604d 0%,#174537 48%,#0f3027 100%);color:#f1f5f2;line-height:1.2}
.lmp-book__cover::before{content:"";position:absolute;inset:0 auto 0 0;width:5cqi;background:linear-gradient(90deg,rgba(0,0,0,.32) 0%,rgba(255,255,255,.1) 55%,rgba(0,0,0,.12) 100%)}
.lmp-book__cover::after{content:"";position:absolute;inset:4cqi 4cqi 4cqi 7cqi;border:1px solid rgba(255,255,255,.12);border-radius:3px 6px 6px 3px;pointer-events:none}
.lmp-cover__top{display:flex;align-items:center;justify-content:space-between;font-size:3.4cqi;font-weight:700;letter-spacing:.18em}
.lmp-cover__ed{color:rgba(241,245,242,.6);font-weight:600}
.lmp-cover__title{display:grid;gap:2.5cqi;margin-top:auto}
.lmp-cover__kicker{color:#A9D4BF;font-size:5.6cqi;font-weight:600;letter-spacing:.16em}
.lmp-cover__main{font-size:12.2cqi;font-weight:700;line-height:.98;letter-spacing:-.02em}
.lmp-cover__sub{margin-top:5cqi;padding-top:4.5cqi;border-top:1px solid rgba(255,255,255,.2);font-size:5cqi;font-weight:500}
.lmp-cover__days{display:grid;grid-template-columns:repeat(10,1fr);gap:1.8cqi;margin-top:7cqi}
.lmp-cover__days i{aspect-ratio:1;border-radius:50%;border:1px solid rgba(255,255,255,.26)}
.lmp-cover__days i.is-active{border-color:#A9D4BF;background:#A9D4BF}
.lmp-cover__tags{margin-top:auto;color:rgba(241,245,242,.72);font-size:3.3cqi;font-weight:500;letter-spacing:.02em}
.lmp-daycard{position:absolute;top:55%;right:max(0px,calc(50% - var(--book-w)/2 - 3rem));display:grid;gap:8px;width:200px;padding:14px 16px;border:1px solid #E3E2DB;border-radius:16px;background:#fff;box-shadow:0 2px 6px rgba(16,22,20,.04),0 30px 70px -28px rgba(16,22,20,.28);line-height:1.3}
.lmp-daycard__head{display:flex;align-items:center;gap:8px;color:#5D6762;font-size:12px;font-weight:600;letter-spacing:.1em}
.lmp-daycard__head svg{color:#1D5A48}
.lmp-daycard__head strong{color:#101614}
.lmp-daycard__bar{display:grid;grid-template-columns:repeat(30,1fr);gap:2px}
.lmp-daycard__bar i{height:6px;border-radius:2px;background:#EFEEE8}
.lmp-daycard__bar i.is-done{background:#1D5A48}
.lmp-daycard__text{color:#101614;font-size:14px;font-weight:600}
@media (max-width:479px){.lmp-daycard{width:176px;padding:12px 14px}}
""".replace("MASK", LOGO_MASK)

JS = r"""
(function(){
  /* Formular-Einstellungen: endpoint leer = Demo-Modus (es wird nichts gesendet). */
  var CONFIG = { endpoint: '', successUrl: '/tesekkurler/', timeoutMs: 15000 };
  var TEXT = {
    empty: 'Lütfen e-posta adresini gir.',
    invalid: 'Lütfen geçerli bir e-posta adresi gir.',
    failed: 'Şu anda kaydını alamadık. Lütfen birazdan tekrar dene.',
    loading: 'Gönderiliyor…'
  };
  var EMAIL = /^[^\s@]+@[^\s@.]+(?:\.[^\s@.]+)*\.[^\s@.]{2,}$/;
  function isValid(v){ return v.length <= 254 && EMAIL.test(v); }

  function setError(form, input, msg){
    var el = form.querySelector('[data-error]');
    if (el) el.textContent = msg;
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
  }
  function setLoading(form, on){
    var btn = form.querySelector('button[type=submit]');
    var label = btn && btn.querySelector('[data-label]');
    if (!btn || !label) return;
    if (!btn.dataset.idle) btn.dataset.idle = label.textContent;
    btn.disabled = on;
    form.setAttribute('aria-busy', on ? 'true' : 'false');
    label.textContent = on ? TEXT.loading : btn.dataset.idle;
  }
  function showSuccess(form){
    if (CONFIG.successUrl) { window.location.assign(CONFIG.successUrl); return; }
    var root = form.closest('[data-lmp-root]');
    var ok = root && root.querySelector('[data-success]');
    if (!ok) return;
    form.hidden = true; ok.hidden = false; ok.focus({ preventScroll: true });
  }
  function send(payload){
    if (!CONFIG.endpoint) {
      console.info('[Lean Mode Pro] Demo-Modus: kein Endpoint gesetzt, es wurde nichts gesendet.', payload);
      return new Promise(function(r){ setTimeout(r, 600); });
    }
    var ctrl = new AbortController();
    var t = setTimeout(function(){ ctrl.abort(); }, CONFIG.timeoutMs);
    return fetch(CONFIG.endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload),
      signal: ctrl.signal
    }).then(function(res){ clearTimeout(t); if (!res.ok) throw new Error('HTTP ' + res.status); });
  }
  function init(){
    var header = document.querySelector('.lmp-header');
    if (header) {
      var upd = function(){ header.classList.toggle('is-scrolled', window.scrollY > 8); };
      upd(); window.addEventListener('scroll', upd, { passive: true });
    }
    document.querySelectorAll('form[data-lmp-signup]').forEach(function(form){
      var input = form.querySelector('input[name=email]');
      input.addEventListener('input', function(){
        if (input.getAttribute('aria-invalid') === 'true' && isValid(input.value.trim())) setError(form, input, '');
      });
      form.addEventListener('submit', function(e){
        e.preventDefault();
        if (form.getAttribute('aria-busy') === 'true') return;
        var email = input.value.trim();
        var hp = form.querySelector('input[name=website]');
        if (hp && hp.value) { showSuccess(form); return; }
        if (!email || !isValid(email)) {
          setError(form, input, email ? TEXT.invalid : TEXT.empty);
          input.focus(); return;
        }
        setError(form, input, '');
        setLoading(form, true);
        var source = (form.querySelector('input[name=source]') || {}).value || 'unknown';
        send({ email: email, source: source })
          .then(function(){ setLoading(form, false); showSuccess(form); })
          .catch(function(err){ console.error(err); setLoading(form, false); setError(form, input, TEXT.failed); });
      });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
"""


def assets_html():
    css = " ".join(line.strip() for line in CSS.strip().splitlines() if line.strip())
    return f"<style id=\"lmp-styles\">{css}</style>\n<script>{JS.strip()}</script>"


def form_html(uid, source, button_label):
    return f"""<div class="lmp-signup" data-lmp-root>
<form class="lmp-signup__form" method="post" novalidate data-lmp-signup>
<label class="lmp-signup__label" for="{uid}-email">E-posta adresin</label>
<div class="lmp-signup__field">
<input class="lmp-signup__input" id="{uid}-email" type="email" name="email" placeholder="E-posta adresini gir" autocomplete="email" inputmode="email" autocapitalize="off" spellcheck="false" enterkeyhint="send" maxlength="254" required aria-describedby="{uid}-error {uid}-consent">
<button class="lmp-signup__button" type="submit"><span data-label>{button_label}</span>{ARROW}</button>
</div>
<p class="lmp-signup__error" id="{uid}-error" aria-live="polite" data-error></p>
<p class="lmp-signup__consent" id="{uid}-consent">{CONSENT} <a href="/gizlilik-politikasi/">Gizlilik Politikası</a>.</p>
<input type="hidden" name="source" value="{source}">
<div class="lmp-signup__hp" aria-hidden="true"><label>Web sitesi <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
</form>
<div class="lmp-signup__success" role="status" tabindex="-1" hidden data-success>
<span class="lmp-signup__success-icon">{CHECK}</span>
<div><p class="lmp-signup__success-title">Teşekkürler, kaydın alındı.</p>
<p class="lmp-signup__success-text">30 günlük planı e-posta adresine gönderiyoruz. Gelen kutunu kontrol et; e-postayı göremezsen spam klasörüne de göz at.</p></div>
</div>
</div>"""


def mockup_html(small=False, daycard=True):
    days = "".join('<i class="is-active"></i>' if i == 0 else "<i></i>" for i in range(30))
    bar = "".join('<i class="is-done"></i>' if i == 0 else "<i></i>" for i in range(30))
    card = ""
    if daycard:
        card = (f'<div class="lmp-daycard"><div class="lmp-daycard__head">{CAL}<span>GÜN <strong>01</strong> / 30</span></div>'
                f'<div class="lmp-daycard__bar">{bar}</div><span class="lmp-daycard__text">Her gün bir sonraki adım</span></div>')
    cls = "lmp-mockup lmp-mockup--sm" if small else "lmp-mockup"
    return (f'<div class="{cls}" role="img" aria-label="30 Günlük Kilo Verme Planı e-kitap kapağı: Adım Adım Rehber. Beslenme, Antrenman, Hareket, Alışkanlıklar.">'
            '<div class="lmp-book"><div class="lmp-book__pages"></div><div class="lmp-book__cover">'
            '<div class="lmp-cover__top"><span>LEAN MODE PRO</span><span class="lmp-cover__ed">E-KİTAP</span></div>'
            '<div class="lmp-cover__title"><span class="lmp-cover__kicker">30 GÜNLÜK</span><span class="lmp-cover__main">KİLO VERME PLANI</span></div>'
            '<span class="lmp-cover__sub">Adım Adım Rehber</span>'
            f'<div class="lmp-cover__days">{days}</div>'
            '<span class="lmp-cover__tags">Beslenme • Antrenman • Hareket • Alışkanlıklar</span>'
            f'</div></div>{card}</div>')


def shift_html():
    noise = ["Her gün yeni bir diyet", "Yüzlerce kural", "Mükemmel olma baskısı", "Çelişen bilgiler", "Karmaşık tablolar"]
    items = "".join(f"<li>{n}</li>" for n in noise)
    return (f'<div class="lmp-shift" aria-hidden="true"><ul class="lmp-shift__noise">{items}</ul>'
            f'<span class="lmp-shift__arrow">{ARROW_DOWN}</span>'
            f'<p class="lmp-shift__one">{CHECK}Bugünün adımı</p></div>')
