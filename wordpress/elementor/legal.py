"""Texts of the legal pages (Turkish): Yasal Bilgiler (Impressum), Gizlilik Politikası, Çerez Politikası.

The operator's personal data is NOT stored in this repository. The texts contain placeholders such as
{{lmp:name}}; they are filled in on the WordPress server from the option `lmp_operator` when the pages
are imported. The optional VAT block sits between <!--lmp:vat--> and <!--/lmp:vat--> and is dropped when
no VAT ID is set. The same applies to <!--lmp:phone--> and <!--lmp:authority-->
(the data protection authority responsible for the operator's place of business).

Facts the texts rely on (checked on 24.09.2026, re-check after changes to the site):
- Hosting: Hostinger International Ltd. (Cyprus), server in Frankfurt (de-fra-web1812.main-hosting.eu).
- No cookies, no localStorage/sessionStorage and no external requests for visitors
  (Hostinger Reach deactivated, WordPress emoji script switched off via mu-plugin lmp-privacy.php).
- Font Instrument Sans is served from the site itself (Elementor local Google Fonts).
- The signup form asks only for the email address. Emails via Brevo (Sendinblue SAS, Paris) with double
  opt-in, without open/click tracking (to be configured that way when Brevo is connected).
"""

UPDATED = "24 Eylül 2026"

CONTACT = (
    "<p>{{lmp:name}}<br>{{lmp:street}}<br>{{lmp:city}}<br>Almanya</p>"
    '<p>E-posta: <a href="mailto:{{lmp:email}}">{{lmp:email}}</a>'
    "<!--lmp:phone--><br>Telefon: {{lmp:phone}}<!--/lmp:phone--></p>"
)


def _updated():
    return f'<p class="lmp-updated">Son güncelleme: {UPDATED}</p>'


def imprint_html():
    return "".join([
        "<p>Almanya Dijital Hizmetler Kanunu (Digitale-Dienste-Gesetz, DDG) § 5 uyarınca bilgiler.</p>",
        "<h2>Hizmet sağlayıcı ve iletişim</h2>",
        CONTACT,
        "<!--lmp:vat--><h2>KDV kimlik numarası</h2>"
        "<p>Almanya Katma Değer Vergisi Kanunu (UStG) § 27a uyarınca KDV kimlik numarası: {{lmp:vat}}</p>"
        "<!--/lmp:vat-->",
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
        "açıklar. Verilerini Avrupa Birliği Genel Veri Koruma Tüzüğü'ne (GDPR) uygun olarak işliyoruz.</p>",

        "<h2>Kısaca</h2><ul>",
        "<li>Siteyi ziyaret ettiğinde sunucu, sayfayı gösterebilmek için teknik erişim verilerini kısa süreliğine "
        "kaydeder.</li>",
        "<li>Ziyaretçiler için çerez, analiz, takip veya reklam aracı kullanmıyoruz.</li>",
        "<li>Kayıt olursan e-posta adresini, planı ve e-postalarımızı gönderebilmek için e-posta hizmeti Brevo ile "
        "işliyoruz. Onayını istediğin zaman geri alabilirsin.</li>",
        "<li>Verilerini satmıyoruz.</li></ul>",

        "<h2>1. Veri sorumlusu</h2>",
        CONTACT,

        "<h2>2. Barındırma ve sunucu kayıtları</h2>",
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

        "<h2>3. Şifreli bağlantı</h2>",
        "<p>Site, SSL/TLS ile şifrelenmiş bir bağlantı (https) üzerinden sunulur. Böylece formda girdiğin veriler "
        "aktarım sırasında başkaları tarafından okunamaz.</p>",

        "<h2>4. Çerezler ve tarayıcı depolaması</h2>",
        "<p>Bu site ziyaretçiler için çerez kullanmaz ve tarayıcında (ör. localStorage) bilgi saklamaz. Ayrıntılar "
        'için <a href="/cerez-politikasi/">Çerez Politikası</a>\'na bakabilirsin.</p>',

        "<h2>5. Yazı tipleri</h2>",
        "<p>Sitede kullanılan yazı tipi (Instrument Sans) kendi sunucumuzdan yüklenir. Bu sırada Google'a veya başka "
        "bir yazı tipi sağlayıcısına bağlantı kurulmaz.</p>",

        "<h2>6. Ücretsiz plan ve e-posta bülteni</h2>",
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
        "veri işleyen olarak bizim adımıza işler. E-postalarımızın açılıp açılmadığını veya içindeki "
        "bağlantılara tıklanıp tıklanmadığını ölçmüyoruz. Brevo'nun gizlilik politikası: "
        '<a href="https://www.brevo.com/legal/privacypolicy/" target="_blank" rel="noopener">'
        "brevo.com/legal/privacypolicy</a></p>",
        "<h3>Abonelikten çıkma ve saklama süresi</h3>",
        "<p>Onayını istediğin zaman geri alabilirsin: her e-postanın sonundaki abonelikten çıkma bağlantısıyla "
        "veya bize yazarak. Geri alma, o ana kadar yapılan işlemenin hukuka uygunluğunu etkilemez. E-posta "
        "adresini abonelikten çıkana kadar saklarız. Çıktıktan sonra, sana yanlışlıkla yeniden e-posta "
        "gönderilmemesi için adresin bir engelleme listesinde tutulabilir (GDPR md. 6/1-f).</p>",

        "<h2>7. E-kitabın indirilmesi</h2>",
        "<p>Kaydını onayladıktan sonra e-kitabı doğrudan sunucumuzdan indirebilirsin. Bu sırada yalnızca 2. "
        "bölümde açıklanan sunucu kayıtları oluşur.</p>",

        "<h2>8. E-posta ile iletişim</h2>",
        "<p>Bize e-posta yazarsan, e-posta adresini ve mesajındaki bilgileri yalnızca talebini yanıtlamak için "
        "işleriz (GDPR md. 6/1-b veya 6/1-f). Talebin sonuçlandıktan sonra, yasal bir saklama yükümlülüğü yoksa "
        "bu verileri sileriz.</p>",

        "<h2>9. Verilerin aktarılması</h2>",
        "<p>Verilerini satmıyoruz ve reklam amacıyla başkalarıyla paylaşmıyoruz. Yasal bir zorunluluk olmadıkça "
        "veriler yalnızca bu politikada adı geçen hizmet sağlayıcılara aktarılır. Hostinger ve Brevo, Avrupa "
        "Birliği'nde kurulu şirketlerdir. Otomatik karar verme veya profil oluşturma yapmıyoruz.</p>",

        "<h2>10. Hakların</h2>",
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
        "<!--lmp:authority--><p>Bizim için yetkili denetim makamı: {{lmp:authority}}.</p><!--/lmp:authority-->",

        "<h2>11. Değişiklikler</h2>",
        "<p>Siteyi veya kullandığımız hizmetleri değiştirirsek bu gizlilik politikasını güncelleriz. Her zaman bu "
        "sayfadaki güncel sürüm geçerlidir.</p>",
        _updated(),
    ])


def cookies_html():
    return "".join([
        "<p>Bu sayfa, leanmodepro.com'un çerezleri ve benzeri teknolojileri nasıl kullandığını açıklar.</p>",
        "<h2>Çerez nedir?</h2>",
        "<p>Çerezler, bir web sitesinin tarayıcına kaydettiği küçük metin dosyalarıdır. Siteler benzer şekilde "
        "tarayıcının depolama alanına (ör. localStorage) da bilgi yazabilir.</p>",
        "<h2>Bu sitede kullanılan çerezler</h2>",
        "<p><strong>Ziyaretçiler için hiçbir çerez kullanılmaz.</strong> Analiz, takip, reklam veya sosyal medya "
        "çerezleri yoktur ve tarayıcının depolama alanına bilgi yazılmaz. Bu yüzden bir çerez onay penceresi de "
        "göstermiyoruz.</p>",
        "<p>Yalnızca site yöneticileri WordPress'e giriş yaptığında, oturumu açık tutmak için teknik olarak gerekli "
        "çerezler oluşturulur. Bunlar ziyaretçileri etkilemez.</p>",
        "<h2>Değişiklikler</h2>",
        "<p>İleride çerez kullanan bir hizmet eklersek bu sayfayı güncelleriz ve gerekiyorsa önceden onayını "
        "isteriz.</p>",
        '<p>Kişisel verilerinin nasıl işlendiğini <a href="/gizlilik-politikasi/">Gizlilik Politikası</a>\'nda, '
        'iletişim bilgilerimizi <a href="/yasal-bilgiler/">Yasal Bilgiler</a> sayfasında bulabilirsin.</p>',
        _updated(),
    ])


BODIES = {
    "yasal-bilgiler": imprint_html,
    "gizlilik-politikasi": privacy_html,
    "cerez-politikasi": cookies_html,
}
