"""Texts of the legal pages (Turkish): Yasal Bilgiler (Impressum), Gizlilik Politikası, Çerez Politikası.

The operator's personal data is NOT stored in this repository. The texts contain placeholders such as
{{lmp:name}}; they are filled in on the WordPress server from the option `lmp_operator` when the pages
are imported. Optional blocks (they may be nested; the filler repeats until none is left):

- <!--lmp:X--> … <!--/lmp:X-->   is kept only when the option field X is set
  (vat, phone, authority, tracking, meta, ga, gads, google)
- <!--lmp:!X--> … <!--/lmp:!X--> is kept only when X is empty

`tracking` switches between two states of the site, and `meta`, `ga`, `gads` (Google Analytics, Google Ads)
plus `google` (= ga or gads) name the tools that are actually installed:
- empty: no cookies, no browser storage, no external requests for visitors (state checked on 24.09.2026:
  Hostinger Reach deactivated, WordPress emoji script switched off via mu-plugin lmp-privacy.php).
- set:   cookie banner (consent before any non-essential tag loads; consent cookie `lmp_consent`, 12 months),
  link "Çerez ayarları" in the footer. Since 05.10.2026: Meta Pixel only (meta = 1).
  Google Analytics 4 (retention 14 months) and Google Ads need Consent Mode v2 "basic" when added.

Other facts the texts rely on:
- Hosting: Hostinger International Ltd. (Cyprus), server in Frankfurt (de-fra-web1812.main-hosting.eu).
- Font Instrument Sans is served from the site itself (Elementor local Google Fonts).
- The signup form asks only for the email address. It posts to a Brevo signup form (Sendinblue SAS, Paris)
  with double opt-in. Brevo measures opens and clicks of the emails (tracking pixel, redirected links).
"""

UPDATED = "5 Ekim 2026"          # cookie policy
PRIVACY_UPDATED = "5 Ekim 2026"

CONTACT = (
    "<p>{{lmp:name}}<br>{{lmp:street}}<br>{{lmp:city}}<br>Almanya</p>"
    '<p>E-posta: <a href="mailto:{{lmp:email}}">{{lmp:email}}</a>'
    "<!--lmp:phone--><br>Telefon: {{lmp:phone}}<!--/lmp:phone--></p>"
)

GOOGLE = "Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, İrlanda"
META = "Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, İrlanda"
CONSENT_BASIS = "Hukuki dayanak onayındır (GDPR md. 6/1-a, TDDDG § 25/1)."


def _updated(date=UPDATED):
    return f'<p class="lmp-updated">Son güncelleme: {date}</p>'


def _if(flag, html):
    return f"<!--lmp:{flag}-->{html}<!--/lmp:{flag}-->"


def _link(url, label):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


def imprint_html():
    return "".join([
        "<p>Almanya Dijital Hizmetler Kanunu (Digitale-Dienste-Gesetz, DDG) § 5 uyarınca bilgiler.</p>",
        "<h2>Hizmet sağlayıcı ve iletişim</h2>",
        CONTACT,
        _if("vat", "<h2>KDV kimlik numarası</h2>"
                   "<p>Almanya Katma Değer Vergisi Kanunu (UStG) § 27a uyarınca KDV kimlik numarası: {{lmp:vat}}</p>"),
        "<h2>Sağlıkla ilgili önemli not</h2>",
        "<p>Bu sitedeki ve ücretsiz e-kitaptaki bilgiler genel bilgilendirme amaçlıdır; tıbbi tavsiye, teşhis "
        "veya tedavinin yerini tutmaz. Kronik bir hastalığın varsa, düzenli ilaç kullanıyorsan, hamile ya da "
        "emziriyorsan veya yeme bozukluğu geçmişin varsa beslenme ve egzersiz düzenini değiştirmeden önce "
        "doktoruna veya bir diyetisyene danış. Sonuçlar kişiden kişiye farklılık gösterir.</p>",
        "<h2>İçerikler için sorumluluk</h2>",
        "<p>Bu sitedeki içerikleri özenle hazırlıyoruz. Yine de içeriklerin doğruluğu, eksiksizliği ve "
        "güncelliği için garanti veremeyiz. Hizmet sağlayıcı olarak kendi içeriklerimizden genel yasalar "
        "çerçevesinde sorumluyuz.</p>",
        "<h2>Telif hakkı</h2>",
        "<p>Bu sitedeki metinler, tasarım ve <strong>30 Günlük Kilo Verme Planı</strong> e-kitabı telif hakkıyla "
        "korunmaktadır. E-kitabı kişisel kullanımın için indirebilir ve yazdırabilirsin. İzin almadan "
        "çoğaltılması, satılması veya başka yerlerde yayımlanması yasaktır.</p>",
        '<p>Kişisel verilerinin nasıl işlendiğini <a href="/gizlilik-politikasi/">Gizlilik Politikası</a>\'nda '
        "bulabilirsin.</p>",
    ])


def privacy_html():
    return "".join([
        "<p>Bu gizlilik politikası, <strong>leanmodepro.com</strong> sitesini ziyaret ettiğinde ve ücretsiz planı "
        "almak için kayıt olduğunda hangi kişisel verilerini, hangi amaçla ve hangi hukuki dayanakla işlediğimizi "
        "açıklar. Verilerini Avrupa Birliği Genel Veri Koruma Tüzüğü'ne (GDPR) ve Almanya Telekomünikasyon ve "
        "Dijital Hizmetlerde Veri Koruma Kanunu'na (TDDDG) uygun olarak işliyoruz.</p>",

        "<h2>Kısaca</h2><ul>",
        "<li>Siteyi ziyaret ettiğinde sunucu, sayfayı gösterebilmek için teknik erişim verilerini kısa süreliğine "
        "kaydeder.</li>",
        _if("!tracking", "<li>Ziyaretçiler için çerez, analiz, takip veya reklam aracı kullanmıyoruz.</li>"),
        _if("tracking", "<li>Reklam ve analiz araçlarını ve bunların çerezlerini yalnızca onay verirsen "
                        "kullanıyoruz. Onayını istediğin zaman sayfanın altındaki <strong>Çerez ayarları</strong> "
                        "bağlantısından geri alabilirsin.</li>"),
        "<li>Kayıt olursan e-posta adresini, planı ve e-postalarımızı gönderebilmek ve e-postalarımızın açılıp "
        "tıklanmasını ölçebilmek için e-posta hizmeti Brevo ile işliyoruz. Onayını istediğin zaman geri "
        "alabilirsin.</li>",
        "<li>Verilerini satmıyoruz.</li></ul>",

        "<h2>Veri sorumlusu</h2>",
        CONTACT,

        "<h2>Barındırma ve sunucu kayıtları</h2>",
        "<p>Bu site, Hostinger International Ltd., 61 Lordou Vironos str., 6023 Larnaca, Kıbrıs tarafından "
        "barındırılır. Sunucu Frankfurt'ta (Almanya) bulunur. Hostinger bu verileri veri işleyen olarak bizim "
        "adımıza işler.</p>",
        "<p>Siteyi açtığında tarayıcın sunucuya otomatik olarak bazı bilgiler gönderir. Sunucu bunları kayıt "
        "dosyalarına (log) yazar:</p>",
        "<ul><li>IP adresi</li><li>tarih ve saat</li><li>açılan sayfa veya dosya</li>"
        "<li>daha önce ziyaret edilen sayfa (referrer)</li><li>tarayıcı ve işletim sistemi</li>"
        "<li>aktarılan veri miktarı ve sunucunun yanıt kodu</li></ul>",
        "<p>Bu verileri siteyi gösterebilmek, güvenliğini sağlamak ve hataları ya da saldırıları tespit edebilmek "
        "için işleriz. Hukuki dayanak, güvenli ve çalışan bir web sitesine yönelik meşru menfaatimizdir "
        "(GDPR md. 6/1-f). Kayıt dosyaları kısa bir süre sonra otomatik olarak silinir ve başka verilerle "
        "birleştirilmez.</p>",

        "<h2>Şifreli bağlantı</h2>",
        "<p>Site, SSL/TLS ile şifrelenmiş bir bağlantı (https) üzerinden sunulur. Böylece formda girdiğin veriler "
        "aktarım sırasında başkaları tarafından okunamaz.</p>",

        _if("!tracking",
            "<h2>Çerezler ve tarayıcı depolaması</h2>"
            "<p>Bu site ziyaretçiler için çerez kullanmaz ve tarayıcında (ör. localStorage) bilgi saklamaz. "
            'Ayrıntılar için <a href="/cerez-politikasi/">Çerez Politikası</a>\'na bakabilirsin.</p>'),
        _if("tracking",
            "<h2>Çerezler ve onay yönetimi</h2>"
            "<p>Siteyi ilk kez ziyaret ettiğinde bir çerez penceresi gösteririz. Analiz ve reklam amaçlı "
            "çerezler ve benzeri teknolojiler ancak onay verirsen yüklenir. Onay vermesen de site eksiksiz "
            "çalışır.</p>"
            "<p>Seçimini hatırlamak için tarayıcında zorunlu bir çerez saklanır. Bu çerez için onay gerekmez "
            "(TDDDG § 25/2 no. 2); hukuki dayanak, onay durumunu kanıtlama yükümlülüğümüz ve buna yönelik meşru "
            "menfaatimizdir (GDPR md. 6/1-c ve 6/1-f).</p>"
            f"<p>Zorunlu olmayan çerezler için {CONSENT_BASIS[0].lower()}{CONSENT_BASIS[1:]} Onayını istediğin "
            "zaman sayfanın altındaki <strong>Çerez ayarları</strong> bağlantısından değiştirebilir veya geri "
            'alabilirsin. Hangi çerezlerin kullanıldığını <a href="/cerez-politikasi/">Çerez Politikası</a>\'nda '
            "bulabilirsin.</p>"),

        "<h2>Yazı tipleri</h2>",
        "<p>Sitede kullanılan yazı tipi (Instrument Sans) kendi sunucumuzdan yüklenir. Bu sırada Google'a veya başka "
        "bir yazı tipi sağlayıcısına bağlantı kurulmaz.</p>",

        _if("ga",
            "<h2>Google Analytics</h2>"
            "<p>Onay verirsen, sitenin nasıl kullanıldığını anlamak ve geliştirmek için Google Analytics 4 "
            f"kullanırız. Sağlayıcı: {GOOGLE}.</p>"
            "<p>Google Analytics çerezler yardımıyla örneğin şu bilgileri toplar: ziyaret edilen sayfalar ve "
            "sayfalarda geçirilen süre, siteye nereden geldiğin, kullandığın cihaz, tarayıcı ve işletim sistemi, "
            "yaklaşık konum (ülke, şehir) ve formun gönderilmesi gibi etkileşimler. IP adresin Google Analytics'te "
            "saklanmaz. Biz bu bilgileri yalnızca istatistik olarak görürüz; kim olduğunu göremeyiz.</p>"
            f"<p>{CONSENT_BASIS} Veriler ABD'ye de aktarılabilir (bkz. <em>Verilerin aktarılması</em>). Analytics "
            "verilerini en fazla 14 ay saklarız. Google'ın gizlilik politikası: "
            f"{_link('https://policies.google.com/privacy', 'policies.google.com/privacy')}</p>"),
        _if("gads",
            "<h2>Google Ads</h2>"
            "<p>Google'da reklam veriyoruz. Onay verirsen, reklamlarımızın işe yarayıp yaramadığını ölçmek "
            "(dönüşüm izleme) ve siteyi ziyaret etmiş kişilere Google'da ve iş ortağı sitelerde yeniden reklam "
            f"gösterebilmek (yeniden pazarlama) için Google Ads etiketini kullanırız. Sağlayıcı: {GOOGLE}.</p>"
            "<p>Bir Google reklamına tıklayıp sitemize geldiğinde tarayıcına bir çerez kaydedilir. Böylece Google, "
            "örneğin reklamdan sonra kayıt formunun gönderilip gönderilmediğini ölçebilir. Biz yalnızca toplu "
            "istatistikler görürüz. Google hesabında oturum açıksa, Google bu bilgileri hesabınla "
            "ilişkilendirebilir.</p>"
            f"<p>{CONSENT_BASIS} Veriler ABD'ye de aktarılabilir. Google'daki kişiselleştirilmiş reklamları "
            f"{_link('https://myadcenter.google.com/', 'Reklam Merkezim')} sayfasından da yönetebilirsin.</p>"),
        _if("meta",
            "<h2>Meta Pixel (Facebook ve Instagram)</h2>"
            "<p>Facebook ve Instagram'da reklam veriyoruz. Onay verirsen sitemizde Meta Pixel'i kullanırız. "
            f"Sağlayıcı: {META}.</p>"
            "<p>Meta Pixel ile reklamlarımızın etkisini ölçeriz (ör. bir reklamdan sonra kayıt olunup olunmadığı) "
            "ve siteyi ziyaret eden kişilere Facebook ve Instagram'da reklam gösterebiliriz. Bunun için ziyaret "
            "edilen sayfalar, etkileşimler (ör. kayıt), tarayıcı bilgileri, IP adresi ve çerez kimlikleri Meta'ya "
            "aktarılır. Facebook veya Instagram hesabında oturum açıksa, Meta bu bilgileri hesabınla "
            "ilişkilendirebilir.</p>"
            "<p>Bu verilerin sitemizde toplanması ve Meta'ya aktarılması için Meta ile birlikte sorumluyuz "
            "(GDPR md. 26). Bunun için Meta ile bir anlaşma yaptık: "
            f"{_link('https://www.facebook.com/legal/controller_addendum', 'facebook.com/legal/controller_addendum')}. "
            "Aktarımdan sonraki işlemeden yalnızca Meta sorumludur. "
            f"{CONSENT_BASIS} Veriler ABD'ye de aktarılabilir. Meta'nın gizlilik politikası: "
            f"{_link('https://www.facebook.com/privacy/policy/', 'facebook.com/privacy/policy')}</p>"),

        "<h2>Ücretsiz plan ve e-posta bülteni</h2>",
        "<p>Kayıt formuna e-posta adresini girdiğinde, sana <strong>30 Günlük Kilo Verme Planı</strong>'nı "
        "göndermek ve LEAN MODE PRO'dan faydalı içerikler ve teklifler içeren e-postalar göndermek için e-posta "
        "adresini işleriz. Formda yalnızca e-posta adresini istiyoruz; kilo, boy veya sağlık durumun gibi "
        "bilgileri sormuyoruz.</p>",
        "<h3>Çift onay (double opt-in)</h3>",
        "<p>Kayıt olduktan sonra bir onay e-postası alırsın. Kaydın ancak bu e-postadaki bağlantıya tıkladığında "
        "tamamlanır. Böylece başka birinin senin adresinle kayıt olmasını önleriz. Onayını kanıtlayabilmek için "
        "kayıt ve onay zamanını ve bu sırada kullanılan IP adresini saklarız.</p>",
        "<h3>Hukuki dayanak</h3>",
        "<p>E-postaların gönderilmesinin dayanağı, kayıt sırasında verdiğin onaydır (GDPR md. 6/1-a). Onay "
        "kaydının saklanması, onayını kanıtlama yükümlülüğümüze ve buna yönelik meşru menfaatimize dayanır "
        "(GDPR md. 6/1-f ve md. 7/1).</p>",
        "<h3>E-posta hizmeti: Brevo</h3>",
        "<p>E-postaları Brevo ile gönderiyoruz. Hizmet sağlayıcı: Sendinblue SAS (Brevo), 17 rue Salneuve, "
        "75017 Paris, Fransa. E-posta adresin ve kayıtla ilgili bilgiler Brevo'da saklanır; Brevo bu verileri "
        "veri işleyen olarak bizim adımıza işler. Brevo'nun gizlilik politikası: "
        f"{_link('https://www.brevo.com/legal/privacypolicy/', 'brevo.com/legal/privacypolicy')}</p>",
        "<h3>Açılma ve tıklama ölçümü</h3>",
        "<p>E-postalarımızın ne kadar ilgi gördüğünü anlamak ve içeriklerimizi iyileştirmek için Brevo ile bir "
        "e-postanın açılıp açılmadığını ve içindeki hangi bağlantılara tıklandığını ölçeriz. Bunun için "
        "e-postalarda küçük, görünmez bir görsel (izleme pikseli) ve Brevo üzerinden yönlendirilen bağlantılar "
        "kullanılır. Bu sırada açılma ve tıklama zamanı, IP adresi ile kullanılan e-posta programı ve cihaz "
        "hakkında teknik bilgiler kaydedilir ve e-posta adresinle ilişkilendirilir.</p>",
        "<p>Hukuki dayanak, e-postalarımızı almak için verdiğin onaydır (GDPR md. 6/1-a). Ölçüme ayrıca itiraz "
        "etmek teknik olarak mümkün değildir; ölçümü istemiyorsan abonelikten çıkman gerekir. Abonelikten "
        "çıktığında ölçüm de sona erer.</p>",
        "<h3>Abonelikten çıkma ve saklama süresi</h3>",
        "<p>Onayını istediğin zaman geri alabilirsin: her e-postanın sonundaki abonelikten çıkma bağlantısıyla "
        "veya bize yazarak. Geri alma, o ana kadar yapılan işlemenin hukuka uygunluğunu etkilemez. E-posta "
        "adresini abonelikten çıkana kadar saklarız. Çıktıktan sonra, sana yanlışlıkla yeniden e-posta "
        "gönderilmemesi için adresin bir engelleme listesinde tutulabilir (GDPR md. 6/1-f).</p>",

        "<h2>E-kitabın indirilmesi</h2>",
        "<p>Kaydını onayladıktan sonra e-kitabı doğrudan sunucumuzdan indirebilirsin. Bu sırada yalnızca yukarıda "
        "açıklanan sunucu kayıtları oluşur.</p>",

        "<h2>E-posta ile iletişim</h2>",
        "<p>Bize e-posta yazarsan, e-posta adresini ve mesajındaki bilgileri yalnızca talebini yanıtlamak için "
        "işleriz (GDPR md. 6/1-b veya 6/1-f). Talebin sonuçlandıktan sonra, yasal bir saklama yükümlülüğü yoksa "
        "bu verileri sileriz.</p>",

        "<h2>Verilerin aktarılması</h2>",
        "<p>Verilerini satmıyoruz. Yasal bir zorunluluk olmadıkça veriler yalnızca bu politikada adı geçen hizmet "
        "sağlayıcılara aktarılır. Hostinger ve Brevo, Avrupa Birliği'nde kurulu şirketlerdir.</p>",
        _if("google", "<p>Google, verileri ABD'deki ana şirketi Google LLC'ye de aktarabilir. Google LLC, AB-ABD "
                      "Veri Gizliliği Çerçevesi (EU-U.S. Data Privacy Framework) kapsamında sertifikalıdır.</p>"),
        _if("meta", "<p>Meta, verileri ABD'deki ana şirketi Meta Platforms, Inc.'e de aktarabilir. Meta Platforms, "
                    "Inc., AB-ABD Veri Gizliliği Çerçevesi (EU-U.S. Data Privacy Framework) kapsamında "
                    "sertifikalıdır.</p>"),
        _if("tracking",
            "<p>AB Komisyonu bu çerçeve için bir yeterlilik kararı almıştır (GDPR md. 45).</p>"
            "<p>GDPR md. 22 anlamında otomatik karar verme yapmıyoruz. Onay verirsen reklam ortaklarımız, "
            "reklamları ilgi alanlarına göre göstermek için verileri kullanabilir.</p>"),
        _if("!tracking", "<p>Otomatik karar verme veya profil oluşturma yapmıyoruz.</p>"),

        "<h2>Hakların</h2>",
        "<p>GDPR kapsamında şu haklara sahipsin:</p><ul>",
        "<li>verilerin hakkında bilgi alma (md. 15)</li>",
        "<li>yanlış verilerin düzeltilmesini isteme (md. 16)</li>",
        "<li>verilerinin silinmesini isteme (md. 17)</li>",
        "<li>işlemenin kısıtlanmasını isteme (md. 18)</li>",
        "<li>verilerini yaygın bir formatta alma (veri taşınabilirliği, md. 20)</li>",
        "<li>meşru menfaate dayanan işlemeye itiraz etme (md. 21)</li>",
        "<li>verdiğin onayı istediğin zaman geri alma (md. 7/3)</li></ul>",
        "<p>Bunun için bize e-posta göndermen yeterli. Ayrıca bir veri koruma denetim makamına şikâyette bulunma "
        "hakkın vardır (GDPR md. 77). Türkiye'de yaşıyorsan, 6698 sayılı Kişisel Verilerin Korunması Kanunu'nun "
        "11. maddesindeki haklarını da bize iletebilirsin.</p>",
        _if("authority", "<p>Bizim için yetkili denetim makamı: {{lmp:authority}}.</p>"),

        "<h2>Değişiklikler</h2>",
        "<p>Siteyi veya kullandığımız hizmetleri değiştirirsek bu gizlilik politikasını güncelleriz. Her zaman bu "
        "sayfadaki güncel sürüm geçerlidir.</p>",
        _updated(PRIVACY_UPDATED),
    ])


COOKIE_TABLE = [
    # (name, provider and purpose, lifetime, flag)
    ("lmp_consent", "LEAN MODE PRO: çerez seçimini hatırlar (zorunlu).", "12 ay", None),
    ("_ga", "Google Analytics: ziyaretçileri birbirinden ayırt eder (istatistik).", "2 yıl", "ga"),
    ("_ga_&lt;kimlik&gt;", "Google Analytics: oturum durumunu saklar (istatistik).", "2 yıl", "ga"),
    ("_gcl_au", "Google Ads: reklamlardan sonraki dönüşümleri ölçer (pazarlama).", "3 ay", "gads"),
    ("_fbp", "Meta Pixel: ziyaretçileri tanır, reklam ölçümü ve yeniden pazarlama (pazarlama).", "3 ay", "meta"),
    ("_fbc", "Meta Pixel: bir Facebook veya Instagram reklamına tıklandığını saklar (pazarlama).", "3 ay", "meta"),
]


def cookies_html():
    row = "<tr><td><code>{}</code></td><td>{}</td><td>{}</td></tr>"
    rows = "".join(_if(flag, row.format(n, p, d)) if flag else row.format(n, p, d) for n, p, d, flag in COOKIE_TABLE)
    return "".join([
        "<p>Bu sayfa, leanmodepro.com'un çerezleri ve benzeri teknolojileri nasıl kullandığını açıklar.</p>",
        "<h2>Çerez nedir?</h2>",
        "<p>Çerezler, bir web sitesinin tarayıcına kaydettiği küçük metin dosyalarıdır. Siteler benzer şekilde "
        "tarayıcının depolama alanına (ör. localStorage) da bilgi yazabilir.</p>",

        _if("!tracking",
            "<h2>Bu sitede kullanılan çerezler</h2>"
            "<p><strong>Ziyaretçiler için hiçbir çerez kullanılmaz.</strong> Analiz, takip, reklam veya sosyal medya "
            "çerezleri yoktur ve tarayıcının depolama alanına bilgi yazılmaz. Bu yüzden bir çerez onay penceresi "
            "de göstermiyoruz.</p>"),
        _if("tracking",
            "<h2>Onayın ve seçimlerin</h2>"
            "<p>Siteyi ilk kez ziyaret ettiğinde bir çerez penceresi gösteririz. Yalnızca zorunlu çerez hemen "
            "kaydedilir; analiz ve reklam çerezleri ancak onay verirsen yüklenir. Onay vermesen de site "
            "eksiksiz çalışır. Seçimini istediğin zaman sayfanın altındaki <strong>Çerez ayarları</strong> "
            "bağlantısından değiştirebilir veya geri alabilirsin.</p>"
            "<h2>Kullandığımız çerezler</h2>"
            "<p><strong>Zorunlu:</strong> Onay seçimini hatırlamak için gereklidir (TDDDG § 25/2 no. 2)."
            "<!--lmp:ga--><br><strong>İstatistik:</strong> Google Analytics. Sitenin nasıl kullanıldığını "
            "anlamamıza yardımcı olur.<!--/lmp:ga-->"
            "<!--lmp:gads--><br><strong>Pazarlama:</strong> Google Ads. Reklamlarımızın etkisini ölçer ve ilgini "
            "çekebilecek reklamlar gösterir.<!--/lmp:gads-->"
            "<!--lmp:meta--><br><strong>Pazarlama:</strong> Meta Pixel (Facebook, Instagram). Reklamlarımızın "
            "etkisini ölçer ve ilgini çekebilecek reklamlar gösterir.<!--/lmp:meta--></p>"
            f"<table><thead><tr><th>Çerez</th><th>Sağlayıcı ve amaç</th><th>Süre</th></tr></thead>"
            f"<tbody>{rows}</tbody></table>"
            "<p>Reklam ortaklarımız kendi alan adlarında da çerezler kullanabilir. Ayrıntılar ve hukuki dayanaklar "
            'için <a href="/gizlilik-politikasi/">Gizlilik Politikası</a>\'na bakabilirsin.</p>'
            "<h2>Tarayıcı ayarları</h2>"
            "<p>Çerezleri tarayıcının ayarlarından da silebilir veya engelleyebilirsin. Onay çerezini silersen çerez "
            "penceresi yeniden görünür.</p>"),

        "<p>Yalnızca site yöneticileri WordPress'e giriş yaptığında, oturumu açık tutmak için teknik olarak gerekli "
        "çerezler oluşturulur. Bunlar ziyaretçileri etkilemez.</p>",
        "<h2>Değişiklikler</h2>",
        _if("!tracking", "<p>İleride çerez kullanan bir hizmet eklersek bu sayfayı güncelleriz ve gerekiyorsa "
                         "önceden onayını isteriz.</p>"),
        _if("tracking", "<p>Yeni bir hizmet eklersek veya çerezler değişirse bu sayfayı güncelleriz.</p>"),
        '<p>Kişisel verilerinin nasıl işlendiğini <a href="/gizlilik-politikasi/">Gizlilik Politikası</a>\'nda, '
        'iletişim bilgilerimizi <a href="/yasal-bilgiler/">Yasal Bilgiler</a> sayfasında bulabilirsin.</p>',
        _updated(),
    ])


BODIES = {
    "yasal-bilgiler": imprint_html,
    "gizlilik-politikasi": privacy_html,
    "cerez-politikasi": cookies_html,
}


def fill(html, operator):
    """Python twin of the PHP filler that runs on WordPress (used for local previews and tests)."""
    import re
    from html import escape

    def block(m):
        neg, key, body = m.group(1), m.group(2), m.group(3)
        keep = bool(str(operator.get(key, "")).strip()) != bool(neg)
        return body if keep else ""

    pattern = re.compile(r"<!--lmp:(!?)([a-z]+)-->(.*?)<!--/lmp:\1\2-->", re.S)
    while True:                                   # blocks can be nested (e.g. a table row inside `tracking`)
        new = pattern.sub(block, html)
        if new == html:
            break
        html = new
    for key, val in operator.items():
        html = html.replace("{{lmp:" + key + "}}", escape(str(val)))
    return html
