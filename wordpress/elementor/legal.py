"""Texts of the legal pages (Turkish): Yasal Bilgiler (Impressum), Gizlilik Politikası, KVKK Aydınlatma Metni,
Çerez Politikası.

The operator's personal data is NOT stored in this repository. The texts contain placeholders such as
{{lmp:name}}; they are filled in on the WordPress server from the option `lmp_operator` when the pages
are imported. Optional blocks (they may be nested; the filler repeats until none is left):

- <!--lmp:X--> … <!--/lmp:X-->   is kept only when the option field X is set
  (vat, phone, authority, kvkkrep, tracking, meta, ga, gads, google)
- <!--lmp:!X--> … <!--/lmp:!X--> is kept only when X is empty

`tracking` switches between two states of the site, and `meta`, `ga`, `gads` (Google Analytics, Google Ads)
plus `google` (= ga or gads) name the tools that are actually installed:
- empty: no cookies, no browser storage, no external requests for visitors (state checked on 24.09.2026:
  Hostinger Reach deactivated, WordPress emoji script switched off via mu-plugin lmp-privacy.php).
- set:   cookie banner (consent before any non-essential tag loads; consent cookie `lmp_consent`, 12 months),
  link "Çerez ayarları" in the footer. Since 06.10.2026 (again): Meta Pixel only (meta = 1).
  Google Analytics 4 (retention 14 months) and Google Ads need Consent Mode v2 "basic" when added.

`kvkkrep` is the data controller representative in Turkey (KVKK), empty until one is appointed.

Other facts the texts rely on:
- Hosting: Hostinger International Ltd. (Cyprus, party of Hostinger's DPA), server in Frankfurt
  (de-fra-web1812.main-hosting.eu). Domain registrar: HOSTINGER operations, UAB (Vilnius, RDAP 11.10.2026).
- No WP Statistics and no social share buttons (Shariff) on the site, so the privacy policy has no sections
  for them (the e-recht24 template the operator supplied on 11.10.2026 had both). Add them if they get installed.
- Font Instrument Sans is served from the site itself (Elementor local Google Fonts).
- The signup form asks only for the email address. It posts to a Brevo signup form (Sendinblue SAS, Paris,
  contracting party in Brevo's terms since 16.10.2025) with double opt-in. Brevo measures opens and clicks
  of the emails (tracking pixel, redirected links).
"""

UPDATED = "6 Ekim 2026"          # cookie policy
PRIVACY_UPDATED = "14 Ekim 2026"
KVKK_UPDATED = "14 Ekim 2026"

CONTACT = (
    "<p>{{lmp:name}}<br>{{lmp:street}}<br>{{lmp:city}}<br>Almanya</p>"
    '<p>E-posta: <a href="mailto:{{lmp:email}}">{{lmp:email}}</a>'
    "<!--lmp:phone--><br>Telefon: {{lmp:phone}}<!--/lmp:phone--></p>"
)

GOOGLE = "Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, İrlanda"
META = "Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, İrlanda"
HOSTER = "Hostinger International Ltd.<br>61 Lordou Vironos str.<br>6023 Larnaca, Kıbrıs"
REGISTRAR = "HOSTINGER operations, UAB<br>Švitrigailos str. 34<br>03230 Vilnius, Litvanya"
BREVO = "Sendinblue SAS (Brevo), 9–17 rue Salneuve, 75017 Paris, Fransa"
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
        "<p>Bu gizlilik politikası, <strong>leanmodepro.com</strong> sitesini ziyaret ettiğinde, ücretsiz "
        "<strong>30 Günlük Kilo Verme Planı</strong> için kayıt olduğunda ve bizimle iletişime geçtiğinde hangi kişisel "
        "verilerini, hangi amaçla ve hangi hukuki dayanakla işlediğimizi açıklar. Verilerini Avrupa Birliği Genel Veri "
        "Koruma Tüzüğü'ne (GDPR), Almanya Federal Veri Koruma Kanunu'na (BDSG) ve Almanya Telekomünikasyon ve Dijital "
        "Hizmetlerde Veri Koruma Kanunu'na (TDDDG) uygun olarak işliyoruz.</p>",

        # 1 ------------------------------------------------------------------------------------------------
        "<h2>1. Bir bakışta veri koruma</h2>",
        "<h3>Kısaca</h3><ul>",
        "<li>Siteyi ziyaret ettiğinde sunucu, sayfayı gösterebilmek için teknik erişim verilerini kısa süreliğine "
        "kaydeder.</li>",
        _if("!tracking", "<li>Ziyaretçiler için çerez, analiz, takip veya reklam aracı kullanmıyoruz.</li>"),
        _if("tracking", "<li>Reklam ve analiz araçlarını ve bunların çerezlerini yalnızca onay verirsen "
                        "kullanıyoruz. Onayını istediğin zaman sayfanın altındaki <strong>Çerez ayarları</strong> "
                        "bağlantısından geri alabilirsin.</li>"),
        "<li>Kayıt olursan e-posta adresini, çift onay (double opt-in) ile doğruladıktan sonra sana planı ve "
        "bültenimizi gönderebilmek ve e-postalarımızın açılıp tıklanmasını ölçebilmek için e-posta hizmeti Brevo ile "
        "işliyoruz. Onayını istediğin zaman geri alabilirsin.</li>",
        "<li>Formda yalnızca e-posta adresini istiyoruz; sağlık bilgisi sormuyoruz.</li>",
        "<li>Verilerini satmıyoruz.</li></ul>",

        "<h3>Genel bilgiler</h3>",
        "<p>Aşağıdaki bilgiler, bu siteyi ziyaret ettiğinde kişisel verilerine ne olduğuna dair basit bir genel bakış "
        "sunar. Kişisel veriler, seni kişisel olarak tanımlamaya yarayan tüm verilerdir (ör. e-posta adresin veya IP "
        "adresin). Ayrıntılı bilgileri bu özetin altındaki bölümlerde bulabilirsin.</p>",

        "<h3>Bu sitede veri toplama</h3>",
        "<p><strong>Bu sitede veri toplamadan kim sorumlu?</strong><br>Bu sitedeki veri işleme, site işletmecisi "
        "tarafından yapılır. İletişim bilgilerini bu politikadaki “Veri sorumlusu” bölümünde bulabilirsin.</p>",
        "<p><strong>Verilerini nasıl topluyoruz?</strong><br>Verilerinin bir kısmı, bunları bize bildirmen yoluyla "
        "toplanır; örneğin kayıt formuna girdiğin e-posta adresi veya bize yazdığın bir e-posta. Diğer veriler, siteyi "
        "ziyaret ettiğinde sistemlerimiz tarafından otomatik olarak"
        + _if("tracking", " veya onay verirsen onayın üzerine") +
        " toplanır. Bunlar özellikle teknik verilerdir (ör. tarayıcı, işletim sistemi veya sayfanın açıldığı saat). "
        "Teknik erişim verileri, siteye girdiğin anda otomatik olarak toplanır.</p>",
        "<p><strong>Verilerini ne için kullanıyoruz?</strong><br>Verilerin bir kısmı, sitenin hatasız sunulabilmesi "
        "için toplanır. Kayıt olursan e-posta adresini, sana ücretsiz planı ve bültenimizi göndermek için kullanırız."
        + _if("tracking", " Onay verirsen bazı veriler, reklamlarımızın etkisini ölçmek ve sana uygun reklamlar "
                          "göstermek için de kullanılır.") + "</p>",
        "<p><strong>Verilerinle ilgili hangi haklara sahipsin?</strong><br>Kayıtlı kişisel verilerinin kaynağı, "
        "alıcıları ve işlenme amacı hakkında istediğin zaman ücretsiz bilgi alma hakkına sahipsin. Ayrıca bu verilerin "
        "düzeltilmesini veya silinmesini isteme hakkın vardır. Veri işlemeye onay verdiysen, bu onayı istediğin zaman "
        "gelecekte geçerli olmak üzere geri alabilirsin. Belirli durumlarda kişisel verilerinin işlenmesinin "
        "kısıtlanmasını da isteyebilirsin. Ayrıca yetkili denetim makamına şikâyette bulunma hakkın vardır. Bu "
        "konularda ve veri korumayla ilgili diğer sorularında bize istediğin zaman ulaşabilirsin.</p>",

        "<h3>Analiz araçları ve üçüncü taraf araçları</h3>",
        _if("tracking", "<p>Onay verirsen, bu siteyi ziyaret ettiğinde gezinme davranışın reklam ve analiz "
                        "araçlarıyla değerlendirilebilir. Bu araçları yalnızca onayınla yükleriz. Ayrıntıları "
                        "“Analiz araçları ve reklam” bölümünde bulabilirsin.</p>"),
        _if("!tracking", "<p>Bu sitede analiz, istatistik veya reklam aracı kullanmıyoruz.</p>"),

        # 2 ------------------------------------------------------------------------------------------------
        "<h2>2. Barındırma (hosting)</h2>",
        "<p>Sitemizin içeriklerini aşağıdaki hizmet sağlayıcıda barındırıyoruz.</p>",
        "<h3>Harici barındırma</h3>",
        "<p>Bu site harici olarak barındırılmaktadır. Bu sitede toplanan kişisel veriler, barındırma hizmeti "
        "sağlayıcısının sunucularında saklanır. Bunlar özellikle IP adresleri, iletişim talepleri, meta ve iletişim "
        "verileri, iletişim bilgileri, site erişimleri ve bir web sitesi aracılığıyla oluşan diğer veriler "
        "olabilir.</p>",
        "<p>Barındırma, olası ve mevcut kullanıcılarımıza karşı yükümlülüklerimizi yerine getirmek (GDPR md. 6/1-b) ve "
        "çevrim içi hizmetimizin profesyonel bir sağlayıcı tarafından güvenli, hızlı ve verimli şekilde sunulmasına "
        "yönelik meşru menfaatimiz (GDPR md. 6/1-f) amacıyla yapılır. Barındırma hizmeti sağlayıcımız verilerini "
        "yalnızca hizmet yükümlülüklerini yerine getirmek için gerekli olduğu ölçüde işler ve bu verilerle ilgili "
        "talimatlarımıza uyar.</p>",
        f"<p>Kullandığımız barındırma hizmeti sağlayıcısı:</p><p>{HOSTER}</p>",
        f"<p>Alan adımızın kayıt kuruluşu (Hostinger grubu):</p><p>{REGISTRAR}</p>",
        "<p>Sitenin sunucusu Frankfurt'ta (Almanya) bulunur. Hostinger'in gizlilik politikası: "
        f"{_link('https://www.hostinger.com/legal/privacy-policy', 'hostinger.com/legal/privacy-policy')}</p>",
        "<h3>Veri işleme sözleşmesi</h3>",
        "<p>Yukarıda adı geçen hizmetin kullanımı için bir veri işleme sözleşmesi (GDPR md. 28) yaptık. Bu, veri "
        "koruma mevzuatının öngördüğü ve hizmet sağlayıcının sitemizi ziyaret edenlerin kişisel verilerini yalnızca "
        "talimatlarımız doğrultusunda ve GDPR'ye uygun olarak işlemesini güvence altına alan bir sözleşmedir.</p>",

        # 3 ------------------------------------------------------------------------------------------------
        "<h2>3. Genel bilgiler ve zorunlu bilgiler</h2>",
        "<h3>Veri koruma</h3>",
        "<p>Kişisel verilerinin korunmasını çok ciddiye alıyoruz. Kişisel verilerini gizli tutar, yasal veri koruma "
        "düzenlemelerine ve bu gizlilik politikasına uygun olarak işleriz.</p>",
        "<p>Bu siteyi kullandığında çeşitli kişisel veriler toplanır. Bu gizlilik politikası, hangi verileri "
        "topladığımızı ve bunları ne için kullandığımızı açıklar. Ayrıca bunun nasıl ve hangi amaçla yapıldığını da "
        "açıklar.</p>",
        "<p>İnternet üzerinden veri aktarımının (ör. e-posta ile iletişimde) güvenlik açıkları taşıyabileceğini "
        "belirtmek isteriz. Verilerin üçüncü kişilerin erişimine karşı eksiksiz korunması mümkün değildir.</p>",

        "<h3>Veri sorumlusu</h3>",
        "<p>Bu sitedeki veri işlemeden sorumlu kişi (veri sorumlusu):</p>",
        CONTACT,
        "<p>Veri sorumlusu, kişisel verilerin (ör. adlar, e-posta adresleri) işlenmesinin amaç ve araçlarına tek "
        "başına veya başkalarıyla birlikte karar veren gerçek veya tüzel kişidir. Yasal olarak bir veri koruma "
        "görevlisi atamakla yükümlü değiliz.</p>",

        "<h3>Saklama süresi</h3>",
        "<p>Bu gizlilik politikasında daha özel bir saklama süresi belirtilmediyse, kişisel verilerin işleme amacı "
        "ortadan kalkana kadar bizde kalır. Haklı bir silme talebinde bulunursan veya veri işlemeye verdiğin onayı "
        "geri alırsan, verilerini saklamak için yasal olarak izin verilen başka gerekçelerimiz (ör. vergi veya ticaret "
        "hukukundan doğan saklama süreleri) yoksa verilerin silinir; bu son durumda silme işlemi, söz konusu "
        "gerekçeler ortadan kalktıktan sonra yapılır.</p>",

        "<h3>Hukuki dayanaklara ilişkin genel bilgiler</h3>",
        "<p>Veri işlemeye onay verdiysen, kişisel verilerini GDPR md. 6/1-a temelinde işleriz. Verilerinin üçüncü "
        "ülkelere aktarılmasına açıkça onay verdiysen, işleme ayrıca GDPR md. 49/1-a'ya dayanır. Çerezlerin "
        "saklanmasına veya cihazındaki bilgilere erişime (ör. cihaz parmak izi) onay verdiysen, işleme ayrıca TDDDG "
        "§ 25/1'e dayanır. Onay istediğin zaman geri alınabilir. Verilerin bir sözleşmenin ifası veya sözleşme öncesi "
        "önlemlerin uygulanması için gerekliyse, verilerini GDPR md. 6/1-b temelinde işleriz. Verilerin yasal bir "
        "yükümlülüğün yerine getirilmesi için gerekliyse, bunları GDPR md. 6/1-c temelinde işleriz. Veri işleme, GDPR "
        "md. 6/1-f uyarınca meşru menfaatimize de dayanabilir. Her bir durumda geçerli hukuki dayanak hakkında bu "
        "gizlilik politikasının ilgili bölümlerinde bilgi veriyoruz.</p>",
        "<p>Sağlık verileri gibi özel nitelikli kişisel verileri (GDPR md. 9) sormuyor ve işlemiyoruz.</p>",

        "<h3>Kişisel verilerin alıcıları</h3>",
        "<p>Faaliyetimiz kapsamında çeşitli harici kuruluşlarla çalışıyoruz. Bu sırada kişisel verilerin bu "
        "kuruluşlara aktarılması da kısmen gereklidir. Kişisel verileri harici kuruluşlara yalnızca bir sözleşmenin "
        "ifası için gerekliyse, yasal olarak yükümlüysek (ör. vergi makamlarına aktarım), aktarımda GDPR md. 6/1-f "
        "uyarınca meşru bir menfaatimiz varsa veya başka bir hukuki dayanak aktarıma izin veriyorsa aktarırız. Veri "
        "işleyen hizmet sağlayıcılar kullandığımızda kişisel verileri yalnızca geçerli bir veri işleme sözleşmesine "
        "dayanarak aktarırız. Ortak işleme durumunda bir ortak sorumluluk anlaşması yapılır.</p>",
        "<p>Bu sitede verilerin şu alıcılara aktarılabilir: barındırma hizmeti sağlayıcımız Hostinger ve e-posta "
        "hizmeti sağlayıcımız Brevo (her ikisi de veri işleyen olarak)."
        + _if("meta", " Onay verirsen verilerin ayrıca Meta'ya aktarılır (bkz. “Meta Pixel”).")
        + _if("google", " Onay verirsen verilerin ayrıca Google'a aktarılır (bkz. “Analiz araçları ve reklam”).")
        + " Verilerini satmıyoruz.</p>",

        "<h3>Üçüncü ülkelere aktarım</h3>",
        "<p>Hostinger ve Brevo, Avrupa Birliği'nde kurulu şirketlerdir ve verilerini AB'deki sunucularda işler.</p>",
        "<p>Meta (Facebook, Instagram), verileri ABD'deki ana şirketi Meta Platforms, Inc.'e de aktarabilir."
        + _if("google", " Google, verileri ABD'deki ana şirketi Google LLC'ye de aktarabilir.")
        + " Meta Platforms, Inc." + _if("google", " ve Google LLC")
        + ", AB-ABD Veri Gizliliği Çerçevesi (EU-U.S. Data Privacy Framework) kapsamında sertifikalıdır. AB Komisyonu "
        "bu çerçeve için bir yeterlilik kararı almıştır (GDPR md. 45). Ayrıca AB Standart Sözleşme Maddeleri (GDPR "
        "md. 46/2-c) kullanılır.</p>",

        "<h3>Otomatik karar verme</h3>",
        "<p>GDPR md. 22 anlamında otomatik karar verme yapmıyoruz.",
        _if("tracking", " Onay verirsen reklam ortaklarımız, reklamları ilgi alanlarına göre göstermek için verileri "
                        "kullanabilir (profil oluşturma)."),
        _if("!tracking", " Profil oluşturma da yapmıyoruz."),
        "</p>",

        "<h3>Hakların – genel bakış</h3>",
        "<p>GDPR kapsamında şu haklara sahipsin:</p><ul>",
        "<li>verilerin hakkında bilgi alma (md. 15)</li>",
        "<li>yanlış verilerin düzeltilmesini isteme (md. 16)</li>",
        "<li>verilerinin silinmesini isteme (md. 17)</li>",
        "<li>işlemenin kısıtlanmasını isteme (md. 18)</li>",
        "<li>verilerini yaygın bir formatta alma (veri taşınabilirliği, md. 20)</li>",
        "<li>işlemeye itiraz etme (md. 21)</li>",
        "<li>verdiğin onayı istediğin zaman geri alma (md. 7/3)</li>",
        "<li>bir denetim makamına şikâyette bulunma (md. 77)</li></ul>",
        "<p>Bunun için bize e-posta göndermen yeterli. Türkiye'de yaşıyorsan, 6698 sayılı Kişisel Verilerin Korunması "
        "Kanunu (KVKK) kapsamındaki bilgileri ve haklarını "
        '<a href="/kvkk-aydinlatma-metni/">KVKK Aydınlatma Metni</a>\'nde bulabilirsin.</p>',

        "<h3>Onayın geri alınması</h3>",
        "<p>Birçok veri işleme işlemi yalnızca açık onayınla mümkündür. Daha önce verdiğin bir onayı istediğin zaman "
        "geri alabilirsin. Geri alma, o ana kadar yapılan veri işlemenin hukuka uygunluğunu etkilemez."
        + _if("tracking", " Çerez onayını sayfanın altındaki <strong>Çerez ayarları</strong> bağlantısından,")
        + " e-posta onayını her e-postadaki abonelikten çıkma bağlantısıyla veya bize yazarak geri alabilirsin.</p>",

        "<h3>Özel durumlarda veri toplamaya ve doğrudan pazarlamaya itiraz hakkı (GDPR md. 21)</h3>",
        "<p><strong>Veri işleme GDPR md. 6/1-e veya 6/1-f'ye dayanıyorsa, özel durumundan kaynaklanan sebeplerle "
        "kişisel verilerinin işlenmesine istediğin zaman itiraz etme hakkına sahipsin; bu, söz konusu hükümlere "
        "dayanan profil oluşturma için de geçerlidir. Bir işlemenin dayandığı hukuki dayanağı bu gizlilik "
        "politikasında bulabilirsin. İtiraz edersen, işlemeye yönelik, senin menfaatlerinden, haklarından ve "
        "özgürlüklerinden üstün gelen zorlayıcı meşru gerekçeler kanıtlayamadığımız veya işleme hukuki taleplerin ileri "
        "sürülmesi, kullanılması ya da savunulması amacına hizmet etmediği sürece, ilgili kişisel verilerini artık "
        "işlemeyiz (GDPR md. 21/1 uyarınca itiraz).</strong></p>",
        "<p><strong>Kişisel verilerin doğrudan pazarlama amacıyla işleniyorsa, bu tür pazarlama amacıyla seninle ilgili "
        "kişisel verilerin işlenmesine istediğin zaman itiraz etme hakkına sahipsin; bu, doğrudan pazarlamayla "
        "bağlantılı olduğu ölçüde profil oluşturma için de geçerlidir. İtiraz edersen, kişisel verilerin bundan sonra "
        "doğrudan pazarlama amacıyla kullanılmaz (GDPR md. 21/2 uyarınca itiraz).</strong></p>",

        "<h3>Yetkili denetim makamına şikâyet hakkı</h3>",
        "<p>GDPR ihlali durumunda ilgili kişiler, özellikle mutat meskenlerinin, işyerlerinin veya iddia edilen ihlalin "
        "gerçekleştiği yerin bulunduğu üye devlette bir denetim makamına şikâyette bulunma hakkına sahiptir. Şikâyet "
        "hakkı, diğer idari veya yargısal başvuru yollarını etkilemez.</p>",
        _if("authority", "<p>Bizim için yetkili denetim makamı: {{lmp:authority}}.</p>"),

        "<h3>Veri taşınabilirliği hakkı</h3>",
        "<p>Onayına dayanarak veya bir sözleşmenin ifası kapsamında otomatik olarak işlediğimiz verileri, kendine veya "
        "üçüncü bir kişiye yaygın, makine tarafından okunabilir bir formatta teslim ettirme hakkına sahipsin. "
        "Verilerin doğrudan başka bir veri sorumlusuna aktarılmasını istersen, bu yalnızca teknik olarak mümkün olduğu "
        "ölçüde yapılır.</p>",

        "<h3>Bilgi alma, düzeltme ve silme</h3>",
        "<p>Yürürlükteki yasal düzenlemeler çerçevesinde, kayıtlı kişisel verilerin, bunların kaynağı ve alıcıları ile "
        "veri işlemenin amacı hakkında istediğin zaman ücretsiz bilgi alma ve gerekirse bu verilerin düzeltilmesini "
        "veya silinmesini isteme hakkına sahipsin. Bu konuda ve kişisel verilerle ilgili diğer sorularında bize "
        "istediğin zaman ulaşabilirsin.</p>",

        "<h3>İşlemenin kısıtlanmasını isteme hakkı</h3>",
        "<p>Kişisel verilerinin işlenmesinin kısıtlanmasını isteme hakkına sahipsin. Bunun için bize istediğin zaman "
        "ulaşabilirsin. Bu hak şu durumlarda geçerlidir:</p><ul>",
        "<li>Bizde kayıtlı kişisel verilerinin doğruluğuna itiraz edersen, bunu kontrol etmek için genellikle zamana "
        "ihtiyaç duyarız. Kontrol süresince işlemenin kısıtlanmasını isteme hakkına sahipsin.</li>",
        "<li>Kişisel verilerinin işlenmesi hukuka aykırı olduysa veya hâlâ hukuka aykırıysa, silme yerine işlemenin "
        "kısıtlanmasını isteyebilirsin.</li>",
        "<li>Kişisel verilerine artık ihtiyacımız yoksa ancak sen bunlara hukuki taleplerin kullanılması, savunulması "
        "veya ileri sürülmesi için ihtiyaç duyuyorsan, silme yerine işlemenin kısıtlanmasını isteme hakkına "
        "sahipsin.</li>",
        "<li>GDPR md. 21/1 uyarınca itiraz ettiysen, senin menfaatlerinle bizim menfaatlerimiz arasında bir "
        "değerlendirme yapılması gerekir. Kimin menfaatlerinin üstün geldiği henüz belli değilse, işlemenin "
        "kısıtlanmasını isteme hakkına sahipsin.</li></ul>",
        "<p>Kişisel verilerinin işlenmesini kısıtladıysan, bu veriler – saklanmaları dışında – yalnızca onayınla veya "
        "hukuki taleplerin ileri sürülmesi, kullanılması ya da savunulması için veya başka bir gerçek ya da tüzel "
        "kişinin haklarının korunması için ya da Avrupa Birliği'nin veya bir üye devletin önemli bir kamu yararı "
        "nedeniyle işlenebilir.</p>",

        "<h3>SSL/TLS şifreleme</h3>",
        "<p>Bu site, güvenlik nedeniyle ve bize gönderdiğin bilgiler gibi gizli içeriklerin aktarımını korumak için "
        "SSL/TLS şifrelemesi kullanır. Şifreli bir bağlantıyı, tarayıcının adres satırının “http://” yerine “https://” "
        "ile başlamasından ve adres satırındaki kilit simgesinden anlayabilirsin. SSL/TLS şifrelemesi etkin olduğunda, "
        "bize ilettiğin veriler (ör. kayıt formuna girdiğin e-posta adresi) üçüncü kişiler tarafından okunamaz.</p>",

        "<h3>Reklam e-postalarına itiraz</h3>",
        "<p>Yasal Bilgiler (künye) yükümlülüğü kapsamında yayımlanan iletişim bilgilerimizin, açıkça talep edilmemiş "
        "reklam ve bilgilendirme materyallerinin gönderilmesi için kullanılmasına itiraz ediyoruz. Spam e-postalar gibi "
        "istenmeyen reklam bilgilerinin gönderilmesi durumunda yasal yollara başvurma hakkımızı açıkça saklı "
        "tutarız.</p>",

        # 4 ------------------------------------------------------------------------------------------------
        "<h2>4. Bu sitede veri toplama</h2>",
        _if("!tracking",
            "<h3>Çerezler ve tarayıcı depolaması</h3>"
            "<p>Bu site ziyaretçiler için çerez kullanmaz ve tarayıcında (ör. localStorage) bilgi saklamaz. "
            'Ayrıntılar için <a href="/cerez-politikasi/">Çerez Politikası</a>\'na bakabilirsin.</p>'),
        _if("tracking",
            "<h3>Çerezler</h3>"
            "<p>Sitemiz “çerez” adı verilen teknolojileri kullanır. Çerezler küçük veri paketleridir ve cihazına zarar "
            "vermez. Ya bir oturum süresince geçici olarak (oturum çerezleri) ya da kalıcı olarak (kalıcı çerezler) "
            "cihazında saklanırlar. Oturum çerezleri ziyaretinin sonunda otomatik olarak silinir. Kalıcı çerezler, sen "
            "silene veya tarayıcın tarafından otomatik olarak silinene kadar cihazında kalır.</p>"
            "<p>Çerezler bizden (birinci taraf çerezleri) veya başka şirketlerden (üçüncü taraf çerezleri) gelebilir. "
            "Üçüncü taraf çerezleri, başka şirketlerin belirli hizmetlerinin sitelere entegre edilmesini sağlar "
            "(ör. reklam ölçümü).</p>"
            "<p>Çerezlerin farklı işlevleri vardır. Bazı çerezler teknik olarak zorunludur, çünkü belirli site "
            "işlevleri onlar olmadan çalışmaz (bu sitede: çerez seçiminin hatırlanması). Diğer çerezler kullanıcı "
            "davranışını değerlendirmek veya reklam amacıyla kullanılabilir.</p>"
            "<p>Elektronik iletişim sürecinin yürütülmesi veya istediğin belirli işlevlerin sağlanması için gerekli "
            "olan çerezler (zorunlu çerezler), başka bir hukuki dayanak belirtilmedikçe GDPR md. 6/1-f temelinde "
            "saklanır; cihazında saklanmaları için onay gerekmez (TDDDG § 25/2 no. 2). Hizmetlerimizin teknik olarak "
            "hatasız sunulması için zorunlu çerezlerin saklanmasında meşru menfaatimiz vardır. Çerezlerin ve benzeri "
            "tanıma teknolojilerinin saklanması için onay istendiyse, işleme yalnızca bu onaya dayanır (GDPR md. 6/1-a "
            "ve TDDDG § 25/1); onay istediğin zaman geri alınabilir.</p>"
            "<p>Tarayıcını, çerezlerin yerleştirilmesinden haberdar olacağın ve çerezlere yalnızca tek tek izin "
            "vereceğin şekilde ayarlayabilir, çerezlerin kabulünü belirli durumlar için veya genel olarak "
            "engelleyebilir ve tarayıcıyı kapattığında çerezlerin otomatik olarak silinmesini etkinleştirebilirsin. "
            "Çerezleri engellersen site yine çalışır; yalnızca çerez penceresi her ziyarette yeniden görünür.</p>"
            '<p>Hangi çerezleri kullandığımızı <a href="/cerez-politikasi/">Çerez Politikası</a>\'nda, bu sitede '
            "kullanılan diğer hizmetleri bu gizlilik politikasında bulabilirsin.</p>"
            "<h3>Onay yönetimi (çerez penceresi)</h3>"
            "<p>Siteyi ilk kez ziyaret ettiğinde bir çerez penceresi gösteririz. Bu pencere kendi çözümümüzdür; bunun "
            "için harici bir onay yönetimi hizmeti kullanılmaz ve seçimin üçüncü kişilere aktarılmaz. Analiz ve reklam "
            "amaçlı çerezler ve benzeri teknolojiler ancak <strong>Kabul et</strong>'e tıklarsan yüklenir. "
            "<strong>Reddet</strong>'e tıklarsan veya bir seçim yapmazsan yüklenmez; site yine eksiksiz çalışır.</p>"
            "<p>Seçimini hatırlamak için tarayıcında <code>lmp_consent</code> adlı zorunlu bir çerez 12 ay süreyle "
            "saklanır. Bu çerez yalnızca seçimini (kabul veya ret) içerir. Bu çerez için onay gerekmez (TDDDG § 25/2 "
            "no. 2); hukuki dayanak, onay durumunu kanıtlama yükümlülüğümüz (GDPR md. 7/1 ile bağlantılı olarak md. "
            "6/1-c) ve buna yönelik meşru menfaatimizdir (GDPR md. 6/1-f).</p>"
            "<p>Seçimini istediğin zaman sayfanın altındaki <strong>Çerez ayarları</strong> bağlantısından "
            "değiştirebilir veya geri alabilirsin."
            "<!--lmp:meta--> Onayını geri alırsan Meta çerezleri (<code>_fbp</code>, <code>_fbc</code>) tarayıcından "
            "silinir.<!--/lmp:meta--></p>"),

        "<h3>Sunucu kayıt dosyaları</h3>",
        "<p>Siteyi açtığında tarayıcın sunucuya otomatik olarak bazı bilgiler gönderir. Barındırma hizmeti "
        "sağlayıcımız bunları kayıt dosyalarına (log) yazar:</p>",
        "<ul><li>IP adresi</li><li>tarih ve saat</li><li>açılan sayfa veya dosya</li>"
        "<li>daha önce ziyaret edilen sayfa (referrer)</li><li>tarayıcı ve işletim sistemi</li>"
        "<li>aktarılan veri miktarı ve sunucunun yanıt kodu</li></ul>",
        "<p>Bu verileri siteyi gösterebilmek, güvenliğini sağlamak ve hataları ya da saldırıları tespit edebilmek için "
        "işleriz. Bu veriler başka veri kaynaklarıyla birleştirilmez. Hukuki dayanak, teknik olarak hatasız ve güvenli "
        "bir web sitesine yönelik meşru menfaatimizdir (GDPR md. 6/1-f). Kayıt dosyaları kısa bir süre sonra otomatik "
        "olarak silinir.</p>",

        "<h3>E-posta ile iletişim</h3>",
        "<p>Bize e-posta yazarsan, talebin ve içerdiği tüm kişisel veriler (ör. adın, e-posta adresin, mesajın) "
        "talebinin işlenmesi amacıyla tarafımızca saklanır ve işlenir. Bu verileri onayın olmadan başkalarına "
        "aktarmayız.</p>",
        "<p>Bu verilerin işlenmesi, talebin bir sözleşmenin ifasıyla ilgiliyse veya sözleşme öncesi önlemler için "
        "gerekliyse GDPR md. 6/1-b'ye, diğer tüm durumlarda bize yöneltilen taleplerin etkili şekilde yanıtlanmasına "
        "yönelik meşru menfaatimize (GDPR md. 6/1-f) dayanır.</p>",
        "<p>Bize gönderdiğin veriler, silmemizi istemene veya amaç ortadan kalkana (ör. talebin sonuçlandıktan sonra) "
        "kadar bizde kalır. Zorunlu yasal hükümler, özellikle yasal saklama süreleri, saklı kalır.</p>",

        "<h3>Yazı tipleri</h3>",
        "<p>Sitede kullanılan yazı tipi (Instrument Sans) kendi sunucumuzdan yüklenir. Bu sırada Google'a veya başka "
        "bir yazı tipi sağlayıcısına bağlantı kurulmaz.</p>",

        "<h3>E-kitabın indirilmesi</h3>",
        "<p>Kaydını onayladıktan sonra e-kitabı doğrudan sunucumuzdan indirebilirsin. Bu sırada yalnızca yukarıda "
        "açıklanan sunucu kayıtları oluşur.</p>",

        # 5 ------------------------------------------------------------------------------------------------
        "<h2>5. Sosyal medya</h2>",
        "<h3>Sitede sosyal medya eklentisi yok</h3>",
        "<p>Bu sitede Facebook “Beğen” düğmesi, paylaşım düğmeleri veya Instagram akışı gibi sosyal medya eklentileri "
        "kullanmıyoruz. Sayfalarımızı açtığında bu yolla sosyal ağlara veri aktarılmaz."
        + _if("meta", " Onay verirsen kullanılan Meta Pixel'i “Analiz araçları ve reklam” bölümünde açıklıyoruz.")
        + "</p>",
        "<h3>Facebook ve Instagram'daki sayfamız</h3>",
        "<p>Reklamlarımızı yayınlamak ve içeriklerimizi duyurmak için Facebook ve Instagram'da bir sayfa veya profil "
        f"kullanıyoruz. Sağlayıcı: {META}. Bu platformların kullanımı için Meta'nın kullanım koşulları ve gizlilik "
        "politikası geçerlidir.</p>",
        "<p>Sayfamızı veya reklamlarımızı görüntülediğinde ya da bunlarla etkileşime geçtiğinde Meta verilerini (ör. IP "
        "adresi, cihaz bilgileri, etkileşimler ve Facebook veya Instagram hesabınla ilişkili veriler) kendi amaçları "
        "için işler ve bu sırada çerezler kullanabilir. Meta bize bu verilerden yalnızca anonim istatistikler (Sayfa "
        "İstatistikleri / Page Insights) sunar; bunlardan tek tek kişileri tanıyamayız.</p>",
        "<p>Sayfa istatistikleri için kişisel verilerin işlenmesinden Meta ile birlikte sorumluyuz (GDPR md. 26). Bunun "
        "için Meta ile bir anlaşma yapılmıştır: "
        f"{_link('https://www.facebook.com/legal/terms/page_controller_addendum', 'facebook.com/legal/terms/page_controller_addendum')}. "
        "Bu anlaşmaya göre, haklarının kullanılması ve bilgilendirme konusundaki birincil sorumluluk Meta'ya aittir. "
        "Haklarını hem Meta'ya hem de bize karşı kullanabilirsin; bize gelen talepleri gerekirse Meta'ya iletiriz.</p>",
        "<p>Hukuki dayanak, kullanıcılarla iletişim kurmaya ve tekliflerimizi tanıtmaya yönelik meşru menfaatimizdir "
        "(GDPR md. 6/1-f). Meta senden bir onay istediyse (ör. çerezler için), hukuki dayanak bu onaydır (GDPR md. "
        "6/1-a, TDDDG § 25/1). Meta verileri ABD'ye de aktarabilir (bkz. “Üçüncü ülkelere aktarım”). Gizlilik "
        f"politikaları: {_link('https://www.facebook.com/privacy/policy/', 'Facebook')} ve "
        f"{_link('https://privacycenter.instagram.com/policy/', 'Instagram')}.</p>",

        # 6 ------------------------------------------------------------------------------------------------
        "<h2>6. Analiz araçları ve reklam</h2>",
        _if("!tracking", "<p>Bu sitede analiz, istatistik veya reklam aracı kullanmıyoruz.</p>"),
        _if("ga",
            "<h3>Google Analytics</h3>"
            "<p>Onay verirsen, sitenin nasıl kullanıldığını anlamak ve geliştirmek için Google Analytics 4 "
            f"kullanırız. Sağlayıcı: {GOOGLE}.</p>"
            "<p>Google Analytics çerezler yardımıyla örneğin şu bilgileri toplar: ziyaret edilen sayfalar ve "
            "sayfalarda geçirilen süre, siteye nereden geldiğin, kullandığın cihaz, tarayıcı ve işletim sistemi, "
            "yaklaşık konum (ülke, şehir) ve formun gönderilmesi gibi etkileşimler. IP adresin Google Analytics'te "
            "saklanmaz. Biz bu bilgileri yalnızca istatistik olarak görürüz; kim olduğunu göremeyiz.</p>"
            f"<p>{CONSENT_BASIS} Veriler ABD'ye de aktarılabilir (bkz. “Üçüncü ülkelere aktarım”). Analytics "
            "verilerini en fazla 14 ay saklarız. Google'ın gizlilik politikası: "
            f"{_link('https://policies.google.com/privacy', 'policies.google.com/privacy')}</p>"),
        _if("gads",
            "<h3>Google Ads</h3>"
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
            "<h3>Meta Pixel (Facebook ve Instagram reklamları)</h3>"
            "<p>Facebook ve Instagram'da reklam veriyoruz. Onay verirsen sitemizde Meta Pixel'i kullanırız. "
            f"Sağlayıcı: {META}.</p>"
            "<p><strong>Amaçlar</strong></p><ul>"
            "<li><strong>Dönüşüm ölçümü:</strong> Bir Facebook veya Instagram reklamından sonra sitemizi ziyaret edip "
            "etmediğini veya kayıt olup olmadığını ölçeriz. Böylece reklamlarımızın işe yarayıp yaramadığını görür ve "
            "reklam bütçemizi buna göre yönetiriz.</li>"
            "<li><strong>Yeniden pazarlama (Özel Hedef Kitleler):</strong> Sitemizi ziyaret etmiş kişilere daha sonra "
            "Facebook ve Instagram'da reklamlarımızı gösterebiliriz.</li>"
            "<li><strong>Benzer hedef kitleler:</strong> Meta, ziyaretçilerimize benzeyen kişileri belirleyip "
            "reklamlarımızı onlara da gösterebilir.</li>"
            "<li><strong>Reklam optimizasyonu:</strong> Meta, reklamlarımızın gösterimini bu bilgilerle otomatik olarak "
            "iyileştirir.</li></ul>"
            "<p><strong>İşlenen veriler</strong><br>Meta Pixel, tarayıcında Meta'nın bir betiğini yükler ve çerezler "
            "(<code>_fbp</code>, <code>_fbc</code>) yerleştirir. Bu sırada Meta'ya özellikle şu veriler aktarılır: açılan "
            "sayfanın adresi ve önceki sayfa (referrer), sayfa görüntüleme gibi olaylar ve tıklamalar gibi "
            "etkileşimler, ziyaretin tarihi ve saati, IP adresi, tarayıcı, işletim sistemi ve cihaz bilgileri, çerez "
            "kimlikleri ve bir reklama tıklayarak geldiysen reklam tıklama kimliği (fbclid). Meta'nın “gelişmiş "
            "eşleştirme” işlevi etkinse, formlara girilen bilgiler (ör. e-posta adresi) tarayıcında karma değere (hash) "
            "dönüştürülerek eşleştirme amacıyla Meta'ya aktarılabilir. Facebook veya Instagram hesabında oturum açıksa "
            "veya daha sonra açarsan, Meta bu bilgileri hesabınla ilişkilendirebilir. Biz yalnızca toplu istatistikler "
            "ve tek tek kişileri tanımadığımız hedef kitleler görürüz.</p>"
            "<p><strong>Ortak sorumluluk</strong><br>Bu verilerin sitemizde toplanması ve Meta'ya aktarılması için Meta "
            "ile birlikte sorumluyuz (GDPR md. 26). Bunun için Meta ile bir anlaşma yapılmıştır: "
            f"{_link('https://www.facebook.com/legal/controller_addendum', 'facebook.com/legal/controller_addendum')}. "
            "Aktarımdan sonraki işlemeden yalnızca Meta sorumludur. Haklarını Meta'ya karşı da kullanabilirsin.</p>"
            "<p><strong>Hukuki dayanak ve geri alma</strong><br>Meta Pixel'i yalnızca çerez penceresinde "
            f"<strong>Kabul et</strong>'e tıklarsan yükleriz. {CONSENT_BASIS} Veriler ABD'ye de aktarılabilir (bkz. "
            "“Üçüncü ülkelere aktarım”). Onayını istediğin zaman sayfanın altındaki "
            "<strong>Çerez ayarları</strong> bağlantısından geri alabilirsin; bundan sonra Meta Pixel yüklenmez ve Meta "
            "çerezleri tarayıcından silinir.</p>"
            "<p><strong>Saklama süresi</strong><br><code>_fbp</code> ve <code>_fbc</code> çerezleri tarayıcında 3 ay "
            "saklanır. Reklamlar için oluşturduğumuz hedef kitleler, en fazla son 180 gün içinde sitemizi ziyaret etmiş "
            "kişileri kapsar. Meta'nın aktarılan verileri ne kadar sakladığını Meta belirler.</p>"
            "<p>Meta'nın gizlilik politikası: "
            f"{_link('https://www.facebook.com/privacy/policy/', 'facebook.com/privacy/policy')}. Facebook ve "
            "Instagram'da hangi reklamları gördüğünü "
            f"{_link('https://www.facebook.com/adpreferences', 'Reklam Tercihleri')} sayfasından da yönetebilirsin.</p>"),

        # 7 ------------------------------------------------------------------------------------------------
        "<h2>7. Ücretsiz plan ve e-posta bülteni</h2>",
        "<h3>Bülten verileri</h3>",
        "<p>Kayıt formuna e-posta adresini girdiğinde, sana ücretsiz <strong>30 Günlük Kilo Verme Planı</strong>'nı "
        "ve ardından LEAN MODE PRO'dan faydalı içerikler ve teklifler içeren e-postalar (bülten) göndermek için e-posta "
        "adresini işleriz. Ücretsiz planı bültenimize kayıtla birlikte sunuyoruz; bu, kayıt formunda açıkça "
        "belirtilir. Formda yalnızca e-posta adresini istiyoruz; adın, kilon, boyun veya sağlık durumun gibi "
        "bilgileri sormuyoruz. Bu verileri e-postaları göndermek için kullanırız ve e-posta hizmetimiz Brevo dışında "
        "kimseye aktarmayız.</p>",

        "<h3>Kayıt süreci adım adım (çift onay / double opt-in)</h3>",
        "<ol>",
        "<li>Formda e-posta adresini girip düğmeye tıklarsın. Düğmenin hemen altında neye onay verdiğin "
        "açıklanır.</li>",
        "<li>E-posta adresin, tarayıcından şifreli bağlantıyla doğrudan Brevo'nun kayıt formuna (sibforms.com) "
        "gönderilir. Bu sırada Brevo teknik olarak IP adresini, kayıt zamanını ve tarayıcı bilgilerini de alır. "
        "Sitemiz bunun için Brevo'dan betik veya çerez yüklemez; Brevo ile bağlantı yalnızca formu gönderdiğinde "
        "kurulur.</li>",
        "<li>Ardından seni bir bilgi sayfasına yönlendiririz ve Brevo sana bir onay e-postası gönderir.</li>",
        "<li>Onay e-postasındaki bağlantıya tıkladığında kaydın tamamlanır ve planı indirebileceğin sayfaya "
        "yönlendirilirsin. Bundan sonra sana bülten gönderebiliriz.</li>",
        "<li>Onay bağlantısına tıklamazsan e-posta adresin listemize eklenmez ve sana başka e-posta "
        "gönderilmez.</li>",
        "</ol>",
        "<p>Bu süreçle, başka birinin senin e-posta adresinle kayıt olmasını önleriz. Onayını kanıtlayabilmek için "
        "kayıt ve onay zamanını, bu sırada kullanılan IP adreslerini ve kullanılan kayıt formunu Brevo'da kaydederiz "
        "(kayıt protokolü).</p>",

        "<h3>Hukuki dayanak</h3>",
        "<p>E-posta adresinin işlenmesi ve e-postaların gönderilmesi, kayıt sırasında verdiğin onaya dayanır (GDPR md. "
        "6/1-a). Kayıt protokolünün saklanması, onayını kanıtlama yükümlülüğümüze (GDPR md. 7/1 ile bağlantılı olarak "
        "md. 6/1-c) ve hukuki taleplere karşı kendimizi savunabilmeye yönelik meşru menfaatimize (GDPR md. 6/1-f) "
        "dayanır.</p>",

        "<h3>E-posta hizmeti: Brevo</h3>",
        f"<p>Onay e-postasını ve bülteni Brevo ile gönderiyoruz. Sağlayıcı: {BREVO}. Brevo kayıt formunu, e-posta "
        "adreslerini ve kayıt protokolünü saklar, e-postaları gönderir ve nasıl kullanıldıklarını ölçer (bkz. "
        "aşağısı).</p>",
        "<p>Brevo bu verileri veri işleyen olarak yalnızca bizim adımıza ve talimatlarımız doğrultusunda işler; Brevo "
        "ile bir veri işleme sözleşmesi (GDPR md. 28) yaptık. Brevo verileri AB'deki sunucularda saklar. Brevo'nun alt "
        "işleyenleri verileri istisnai olarak AB dışına aktarırsa, bu bir yeterlilik kararına (GDPR md. 45) veya AB "
        "Standart Sözleşme Maddelerine (GDPR md. 46/2-c) dayanır. Brevo'nun kullanılması, onayına (GDPR md. 6/1-a) ve "
        "e-postaların güvenli ve verimli şekilde gönderilmesine yönelik meşru menfaatimize (GDPR md. 6/1-f) dayanır. "
        f"Brevo'nun gizlilik politikası: {_link('https://www.brevo.com/legal/privacypolicy/', 'brevo.com/legal/privacypolicy')}</p>",

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
        "veya bize yazarak. Geri alma, o ana kadar yapılan işlemenin hukuka uygunluğunu etkilemez.</p>",
        "<p>Bülten için verdiğin verileri, abonelikten çıkana kadar bizde veya Brevo'da saklarız; abonelikten "
        "çıktıktan veya amaç ortadan kalktıktan sonra dağıtım listesinden sileriz. Dağıtım listemizdeki e-posta "
        "adreslerini meşru menfaatimiz çerçevesinde (GDPR md. 6/1-f) kendi takdirimizle silme veya engelleme hakkımızı "
        "saklı tutarız. Bizde başka amaçlarla saklanan veriler bundan etkilenmez.</p>",
        "<p>Abonelikten çıktıktan sonra, gelecekte sana e-posta gönderilmesini önlemek için gerekliyse e-posta "
        "adresin bizde veya Brevo'da bir engelleme listesinde saklanabilir. Engelleme listesindeki veriler yalnızca bu "
        "amaçla kullanılır ve başka verilerle birleştirilmez. Bu, hem senin menfaatine hem de e-posta gönderiminde "
        "yasal gerekliliklere uymaya yönelik meşru menfaatimize hizmet eder (GDPR md. 6/1-f). Engelleme listesinde "
        "saklama süreyle sınırlı değildir. Menfaatlerin meşru menfaatimizden üstünse bu saklamaya itiraz "
        "edebilirsin.</p>",
        "<p>Kayıt protokolünü, onayını kanıtlayabilmek için aboneliğin sona ermesinden sonra da olası hukuki "
        "taleplerin zamanaşımı süresince (genellikle üç yıl) saklarız.</p>",

        # 8 ------------------------------------------------------------------------------------------------
        "<h2>8. Değişiklikler</h2>",
        "<p>Siteyi veya kullandığımız hizmetleri değiştirirsek bu gizlilik politikasını güncelleriz. Her zaman bu "
        "sayfadaki güncel sürüm geçerlidir.</p>",
        f'<p class="lmp-updated">Son güncelleme: {PRIVACY_UPDATED}<br>Bazı bölümler e-recht24.de şablonundan '
        f"çevrilip uyarlanmıştır. Kaynak: {_link('https://www.e-recht24.de', 'e-recht24.de')}</p>",
    ])


def _activity(title, items):
    rows = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in items)
    return f"<h3>{title}</h3><ul>{rows}</ul>"


def kvkk_html():
    """Information notice under KVKK art. 10 and the Aydınlatma Tebliği, for visitors in Turkey. It informs only:
    no consent is asked for here (KVKK Board principle decision 2026/347: notice and consent texts stay separate)."""
    return "".join([
        "<p>6698 sayılı Kişisel Verilerin Korunması Kanunu'nun (KVKK) 10. maddesi ve Aydınlatma Yükümlülüğünün Yerine "
        "Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ uyarınca, Türkiye'de bulunan ziyaretçilerimizi ve "
        "kayıt olan kullanıcılarımızı kişisel verilerinin işlenmesi hakkında bilgilendiriyoruz. Bu metin yalnızca "
        "bilgilendirme amaçlıdır ve herhangi bir onay gerektirmez.</p>",
        "<p>Avrupa Birliği Genel Veri Koruma Tüzüğü (GDPR) kapsamındaki ayrıntılı bilgileri "
        '<a href="/gizlilik-politikasi/">Gizlilik Politikası</a>\'nda, kullanılan çerezleri '
        '<a href="/cerez-politikasi/">Çerez Politikası</a>\'nda bulabilirsin.</p>',

        "<h2>1. Veri sorumlusu</h2>",
        "<p>Kişisel verilerin, veri sorumlusu sıfatıyla aşağıdaki kişi tarafından işlenir:</p>",
        CONTACT,
        "<p>Veri sorumlusu Almanya'da yerleşiktir.</p>",
        _if("kvkkrep", "<p>Türkiye'deki veri sorumlusu temsilcimiz: {{lmp:kvkkrep}}</p>"),

        "<h2>2. İşlenen kişisel veriler, işleme amaçları ve hukuki sebepler</h2>",
        "<p>Kişisel verilerini yalnızca aşağıda belirtilen amaçlarla ve KVKK'nın 5. maddesinde sayılan hukuki sebeplere "
        "dayanarak işleriz. Sağlık verileri gibi özel nitelikli kişisel verileri (KVKK md. 6) istemiyor ve "
        "işlemiyoruz; kayıt formunda yalnızca e-posta adresin istenir.</p>",
        _activity("Siteyi ziyaret ettiğinde", [
            ("Veriler", "İşlem güvenliği verileri: IP adresi, tarih ve saat, açılan sayfa veya dosya, daha önce ziyaret "
                        "edilen sayfa, tarayıcı ve işletim sistemi bilgisi"),
            ("Amaç", "Siteyi sunmak, bilgi güvenliğini sağlamak, hataları ve saldırıları tespit etmek"),
            ("Hukuki sebep", "Temel hak ve özgürlüklerine zarar vermemek kaydıyla veri sorumlusunun meşru menfaati "
                             "(KVKK md. 5/2-f)"),
            ("Toplama yöntemi", "Siteyi açtığında tarayıcın tarafından otomatik olarak gönderilir ve sunucu "
                                "kayıtlarına yazılır"),
        ]),
        _activity("Ücretsiz plan için kayıt olduğunda", [
            ("Veriler", "İletişim verisi: e-posta adresi; işlem güvenliği verileri: kayıt ve onay zamanı, bu sırada "
                        "kullanılan IP adresi"),
            ("Amaç", "E-posta adresini doğrulamak (çift onay) ve talep ettiğin ücretsiz planı sana sunmak"),
            ("Hukuki sebep", "Bir sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması (KVKK md. 5/2-c)"),
            ("Toplama yöntemi", "Sitedeki kayıt formu ve onay e-postasındaki bağlantı aracılığıyla elektronik ortamda"),
        ]),
        _activity("E-posta bülteni ve teklifler", [
            ("Veriler", "İletişim verisi: e-posta adresi"),
            ("Amaç", "LEAN MODE PRO'nun faydalı içeriklerini ve tekliflerini e-postayla göndermek"),
            ("Hukuki sebep", "Açık rızan (KVKK md. 5/1) ve 6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında "
                             "Kanun kapsamında verdiğin ticari elektronik ileti onayı"),
            ("Toplama yöntemi", "Sitedeki kayıt formu aracılığıyla elektronik ortamda"),
        ]),
        _activity("E-postaların açılma ve tıklanma ölçümü", [
            ("Veriler", "Pazarlama verileri: bir e-postanın açılıp açılmadığı, içindeki hangi bağlantılara tıklandığı, "
                        "bunların zamanı, IP adresi, e-posta programı ve cihaz hakkında teknik bilgiler"),
            ("Amaç", "E-postalarımızın ne kadar ilgi gördüğünü ölçmek ve içeriklerimizi iyileştirmek"),
            ("Hukuki sebep", "Veri sorumlusunun meşru menfaati (KVKK md. 5/2-f); abonelikten çıktığında ölçüm de "
                             "sona erer"),
            ("Toplama yöntemi", "E-postalardaki küçük, görünmez bir görsel (izleme pikseli) ve Brevo üzerinden "
                                "yönlendirilen bağlantılar aracılığıyla otomatik olarak"),
        ]),
        _if("meta", _activity("Meta Pixel (Facebook ve Instagram reklamları)", [
            ("Veriler", "Pazarlama ve işlem güvenliği verileri: çerez kimlikleri (<code>_fbp</code>, <code>_fbc</code>), "
                        "ziyaret edilen sayfalar, sayfa görüntüleme gibi olaylar ve etkileşimler, IP adresi, tarayıcı ve "
                        "cihaz bilgileri, reklam tıklama kimliği"),
            ("Amaç", "Facebook ve Instagram reklamlarımızın etkisini ölçmek, siteyi ziyaret etmiş kişilere bu "
                     "platformlarda reklam göstermek ve reklamlarımızı iyileştirmek"),
            ("Hukuki sebep", "Açık rızan (KVKK md. 5/1); çerez penceresinde <strong>Kabul et</strong>'e tıklamadıkça Meta "
                             "Pixel yüklenmez"),
            ("Toplama yöntemi", "Çerezler ve benzeri teknolojiler aracılığıyla otomatik olarak"),
        ])),
        _if("ga", _activity("Google Analytics", [
            ("Veriler", "Ziyaret edilen sayfalar ve süreleri, siteye nereden gelindiği, cihaz, tarayıcı ve işletim "
                        "sistemi, yaklaşık konum, etkileşimler, çerez kimlikleri"),
            ("Amaç", "Sitenin nasıl kullanıldığını istatistiksel olarak anlamak ve siteyi geliştirmek"),
            ("Hukuki sebep", "Açık rızan (KVKK md. 5/1)"),
            ("Toplama yöntemi", "Çerezler aracılığıyla otomatik olarak"),
        ])),
        _if("gads", _activity("Google Ads", [
            ("Veriler", "Çerez kimlikleri, reklam tıklamaları, ziyaret edilen sayfalar ve kayıt gibi dönüşümler"),
            ("Amaç", "Google reklamlarımızın etkisini ölçmek ve siteyi ziyaret etmiş kişilere yeniden reklam göstermek"),
            ("Hukuki sebep", "Açık rızan (KVKK md. 5/1)"),
            ("Toplama yöntemi", "Çerezler aracılığıyla otomatik olarak"),
        ])),
        _if("tracking", _activity("Çerez tercihin", [
            ("Veriler", "Çerez penceresindeki seçimin (kabul veya ret)"),
            ("Amaç", "Seçimini hatırlamak ve onay verip vermediğini ispat edebilmek"),
            ("Hukuki sebep", "Veri sorumlusunun hukuki yükümlülüğünü yerine getirebilmesi için zorunlu olması "
                             "(KVKK md. 5/2-ç) ve meşru menfaat (KVKK md. 5/2-f)"),
            ("Toplama yöntemi", "Tarayıcında saklanan zorunlu bir çerez (<code>lmp_consent</code>) aracılığıyla"),
        ])),
        _activity("Onay kayıtları", [
            ("Veriler", "Hukuki işlem verileri: kayıt ve onay zamanı, bu sırada kullanılan IP adresi, kullanılan kayıt "
                        "formu, abonelikten çıkma zamanı"),
            ("Amaç", "Ticari elektronik ileti onayını ispat etmek ve olası uyuşmazlıklarda haklarımızı korumak"),
            ("Hukuki sebep", "Kanunlarda açıkça öngörülmesi ve hukuki yükümlülük (KVKK md. 5/2-a ve 5/2-ç; 6563 sayılı "
                             "Kanun ve Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik) ile bir hakkın "
                             "tesisi, kullanılması veya korunması (KVKK md. 5/2-e)"),
            ("Toplama yöntemi", "Kayıt, onay ve abonelikten çıkma sırasında otomatik olarak"),
        ]),
        _activity("Bize e-posta yazdığında", [
            ("Veriler", "Kimlik ve iletişim verileri: adın, e-posta adresin ve mesajında paylaştığın bilgiler"),
            ("Amaç", "Talebini veya başvurunu yanıtlamak"),
            ("Hukuki sebep", "Veri sorumlusunun meşru menfaati (KVKK md. 5/2-f); KVKK kapsamındaki başvurularda "
                             "hukuki yükümlülük (KVKK md. 5/2-ç)"),
            ("Toplama yöntemi", "E-posta yoluyla"),
        ]),

        "<h2>3. Kişisel verilerin aktarılması</h2>",
        "<p>Kişisel verilerini satmıyoruz. Verilerini yalnızca yukarıdaki amaçlar için gerekli olduğu ölçüde şu "
        "alıcılara aktarırız:</p><ul>",
        "<li><strong>Barındırma hizmeti sağlayıcısı:</strong> Hostinger International Ltd., Kıbrıs (sunucu: Frankfurt, "
        "Almanya). Amaç: sitenin barındırılması. Veri işleyen olarak, yalnızca talimatlarımız doğrultusunda.</li>",
        "<li><strong>E-posta hizmeti sağlayıcısı:</strong> Sendinblue SAS (Brevo), Paris, Fransa. Amaç: kayıt formu, onay "
        "e-postası, bülten gönderimi ve ölçüm. Veri işleyen olarak, yalnızca talimatlarımız doğrultusunda.</li>",
        _if("meta", f"<li><strong>Meta:</strong> {META}; ana şirketi Meta Platforms, Inc., ABD. Amaç: reklam ölçümü ve "
                    "reklamların hedeflenmesi, yalnızca açık rızanla. Verilerin sitemizde toplanması ve Meta'ya "
                    "aktarılmasından Meta ile birlikte sorumluyuz.</li>"),
        _if("google", f"<li><strong>Google:</strong> {GOOGLE}; ana şirketi Google LLC, ABD. Amaç: istatistik ve reklam "
                      "ölçümü, yalnızca açık rızanla.</li>"),
        "<li><strong>Yetkili kamu kurum ve kuruluşları ile mahkemeler:</strong> kanunen yükümlü olduğumuz hâllerde.</li>",
        "</ul>",
        "<h3>Türkiye dışında işleme</h3>",
        "<p>Veri sorumlusu Almanya'da yerleşik olduğundan kişisel verilerin Türkiye dışında, Avrupa Birliği'nde işlenir. "
        "Yukarıdaki hizmet sağlayıcılar AB'de kuruludur ve AB Genel Veri Koruma Tüzüğü'ne tabidir; veri işleyenler "
        "verileri yazılı veri işleme sözleşmelerine dayanarak işler."
        + _if("meta", " Meta, verileri ABD'deki ana şirketi Meta Platforms, Inc.'e de aktarabilir; bu şirket AB-ABD "
                      "Veri Gizliliği Çerçevesi kapsamında sertifikalıdır.")
        + _if("google", " Google, verileri ABD'deki ana şirketi Google LLC'ye de aktarabilir; bu şirket AB-ABD Veri "
                        "Gizliliği Çerçevesi kapsamında sertifikalıdır.")
        + "</p>",

        "<h2>4. Saklama süreleri</h2><ul>",
        "<li>Sunucu kayıtları kısa bir süre sonra otomatik olarak silinir.</li>",
        "<li>E-posta adresini bültenden çıkana kadar saklarız. Çıktıktan sonra, sana yeniden e-posta gönderilmemesi için "
        "adresin bir engelleme listesinde tutulabilir.</li>",
        "<li>Onay kayıtlarını, mevzuatta öngörülen süre boyunca ve olası hukuki taleplerin zamanaşımı süresince "
        "(genellikle onayın sona ermesinden itibaren üç yıl) saklarız.</li>",
        "<li>E-posta yazışmalarını, yasal saklama yükümlülükleri saklı kalmak kaydıyla talebin sonuçlanana kadar "
        "saklarız.</li>",
        _if("tracking", "<li>Çerez tercihin (<code>lmp_consent</code>) tarayıcında 12 ay saklanır.</li>"),
        _if("meta", "<li>Meta çerezleri (<code>_fbp</code>, <code>_fbc</code>) tarayıcında 3 ay saklanır.</li>"),
        "</ul>",
        "<p>Süreler sona erdiğinde veya işleme amacı ortadan kalktığında kişisel verilerin silinir, yok edilir veya "
        "anonim hâle getirilir.</p>",

        "<h2>5. Onayının ve açık rızanın geri alınması</h2>",
        "<p>Ticari elektronik ileti onayını istediğin zaman, gerekçe göstermeden ve ücretsiz olarak geri alabilirsin: her "
        "e-postadaki abonelikten çıkma bağlantısıyla veya "
        '<a href="mailto:{{lmp:email}}">{{lmp:email}}</a> adresine yazarak. Ret bildirimin en geç üç iş günü içinde '
        "işleme alınır."
        + _if("tracking", " Çerezler için verdiğin açık rızayı sayfanın altındaki <strong>Çerez ayarları</strong> "
                          "bağlantısından geri alabilirsin.")
        + " Geri alma, o ana kadar yapılan işlemenin hukuka uygunluğunu etkilemez.</p>",

        "<h2>6. KVKK'nın 11. maddesi kapsamındaki hakların</h2>",
        "<p>Veri sorumlusuna başvurarak şu haklarını kullanabilirsin:</p><ul>",
        "<li>kişisel verilerinin işlenip işlenmediğini öğrenme,</li>",
        "<li>kişisel verilerin işlenmişse buna ilişkin bilgi talep etme,</li>",
        "<li>kişisel verilerinin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme,</li>",
        "<li>yurt içinde veya yurt dışında kişisel verilerinin aktarıldığı üçüncü kişileri bilme,</li>",
        "<li>kişisel verilerinin eksik veya yanlış işlenmiş olması hâlinde bunların düzeltilmesini isteme,</li>",
        "<li>KVKK'nın 7. maddesinde öngörülen şartlar çerçevesinde kişisel verilerinin silinmesini veya yok edilmesini "
        "isteme,</li>",
        "<li>düzeltme, silme veya yok etme işlemlerinin kişisel verilerinin aktarıldığı üçüncü kişilere bildirilmesini "
        "isteme,</li>",
        "<li>işlenen verilerin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle aleyhine bir sonucun "
        "ortaya çıkmasına itiraz etme,</li>",
        "<li>kişisel verilerinin kanuna aykırı olarak işlenmesi sebebiyle zarara uğraman hâlinde zararın giderilmesini "
        "talep etme.</li></ul>",
        "<p>Münhasıran otomatik sistemlerle senin aleyhine sonuç doğuran kararlar almıyoruz.</p>",

        "<h2>7. Başvuru yöntemi</h2>",
        "<p>Haklarını kullanmak için başvurunu Türkçe olarak şu yollardan biriyle iletebilirsin:</p><ul>",
        "<li>bize daha önce bildirdiğin ve sistemimizde kayıtlı olan e-posta adresinden (ör. bültene kayıtlı adresin) "
        '<a href="mailto:{{lmp:email}}">{{lmp:email}}</a> adresine e-posta göndererek,</li>',
        "<li>ıslak imzalı yazılı bir dilekçeyle yukarıdaki posta adresine göndererek.</li></ul>",
        "<p>Başvurunda adın ve soyadın, yazılı başvurularda imzan, Türk vatandaşıysan T.C. kimlik numaran (yabancıysan "
        "uyruğun ve pasaport ya da varsa kimlik numaran), tebligata esas yerleşim yeri veya iş yeri adresin ve talep "
        "konun bulunmalıdır; varsa bildirime esas e-posta adresini ve telefon numaranı da ekleyebilirsin (Veri "
        "Sorumlusuna Başvuru Usul ve Esasları Hakkında Tebliğ).</p>",
        "<p>Başvurunu niteliğine göre en kısa sürede ve en geç 30 gün içinde ücretsiz olarak sonuçlandırırız. İşlemin "
        "ayrıca bir maliyet gerektirmesi hâlinde Kişisel Verileri Koruma Kurulu'nun belirlediği tarifedeki ücret "
        "alınabilir. Başvurunun reddedilmesi, verilen cevabı yetersiz bulman veya süresinde cevap verilmemesi hâlinde, "
        "cevabı öğrendiğin tarihten itibaren 30 gün ve her hâlde başvuru tarihinden itibaren 60 gün içinde Kişisel "
        "Verileri Koruma Kurulu'na şikâyette bulunabilirsin (KVKK md. 14).</p>",

        "<h2>8. Değişiklikler</h2>",
        "<p>Veri işleme faaliyetlerimiz değişirse bu metni güncelleriz. Her zaman bu sayfadaki güncel sürüm "
        "geçerlidir.</p>",
        _updated(KVKK_UPDATED),
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
    "kvkk-aydinlatma-metni": kvkk_html,
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
