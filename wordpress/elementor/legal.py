"""Texts of the legal pages (English): Legal Notice (Impressum), Privacy Policy, Disclaimer.

The operator's personal data is NOT stored in this repository. The texts contain placeholders such as
{{lmp:name}}; they are filled in on the WordPress server from the option `lmp_operator` when the pages
are imported. Optional blocks (they may be nested; the filler repeats until none is left):

- <!--lmp:X--> … <!--/lmp:X-->   is kept only when the option field X is set (vat, phone, authority, amazon)
- <!--lmp:!X--> … <!--/lmp:!X--> is kept only when X is empty

`amazon` is set once the operator is accepted into the Amazon Associates program: then the required
statement "As an Amazon Associate I earn from qualifying purchases" and the Amazon section appear.

Facts the texts rely on (state 14.10.2026, English site):
- No cookies, no browser storage, no tracking pixel, no analytics and no external requests for visitors.
  (Until 13.10.2026 the Turkish site had a Meta Pixel behind a cookie banner; see Git history.)
- Hosting: Hostinger International Ltd. (Cyprus, party of Hostinger's DPA), server in Frankfurt.
  Domain registrar: HOSTINGER operations, UAB (Vilnius).
- Font Instrument Sans is served from the site itself. WordPress emoji script switched off (mu-plugin).
- Comments are closed on all posts (no comment data).
- The signup form asks only for the email address. It posts to a Brevo signup form (Sendinblue SAS, Paris)
  with double opt-in. Brevo measures opens and clicks of the emails (tracking pixel, redirected links).
- Blog posts may contain affiliate links; a disclosure line is added to every post automatically.
- The privacy policy follows the structure of the e-recht24 template the operator supplied (translated and
  adapted, source note at the end).
"""

UPDATED = "October 14, 2026"

CONTACT = (
    "<p>{{lmp:name}}<br>{{lmp:street}}<br>{{lmp:city}}<br>Germany</p>"
    '<p>Email: <a href="mailto:{{lmp:email}}">{{lmp:email}}</a>'
    "<!--lmp:phone--><br>Phone: {{lmp:phone}}<!--/lmp:phone--></p>"
)

HOSTER = "Hostinger International Ltd.<br>61 Lordou Vironos str.<br>6023 Larnaca, Cyprus"
REGISTRAR = "HOSTINGER operations, UAB<br>Švitrigailos str. 34<br>03230 Vilnius, Lithuania"
BREVO = "Sendinblue SAS (Brevo), 9–17 rue Salneuve, 75017 Paris, France"
META = "Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, Ireland"
PINTEREST = "Pinterest Europe Ltd., Palmerston House, 2nd Floor, Fenian Street, Dublin 2, Ireland"
TIKTOK = "TikTok Technology Limited, 10 Earlsfort Terrace, Dublin, D02 T380, Ireland"
GOOGLE = "Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland"

AMAZON_STATEMENT = "As an Amazon Associate I earn from qualifying purchases."


def _updated(date=UPDATED):
    return f'<p class="lmp-updated">Last updated: {date}</p>'


def _if(flag, html):
    return f"<!--lmp:{flag}-->{html}<!--/lmp:{flag}-->"


def _link(url, label):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


# ------------------------------------------------------------------------------------------ Legal Notice
def imprint_html():
    return "".join([
        "<p>Information pursuant to Section 5 of the German Digital Services Act (Digitale-Dienste-Gesetz, DDG).</p>",
        "<h2>Service provider and contact</h2>",
        CONTACT,
        _if("vat", "<h2>VAT identification number</h2>"
                   "<p>VAT identification number pursuant to Section 27a of the German VAT Act (UStG): {{lmp:vat}}</p>"),
        "<h2>Important health notice</h2>",
        "<p>The information on this website, in our emails and in the free e-book is for general information only and "
        "does not replace medical advice, diagnosis or treatment. Please read our "
        '<a href="/disclaimer/">Disclaimer</a> before you start.</p>',
        "<h2>Liability for content</h2>",
        "<p>We create the content of this website with great care. However, we cannot guarantee that it is accurate, "
        "complete or up to date. As a service provider, we are responsible for our own content on these pages under "
        "general law. We are not obliged to monitor third-party information that is transmitted or stored, or to "
        "investigate circumstances that indicate illegal activity. If we become aware of any legal violations, we will "
        "remove the content concerned immediately.</p>",
        "<h2>Liability for links</h2>",
        "<p>Our website contains links to external websites of third parties, including affiliate links. We have no "
        "influence on their content and therefore cannot accept any liability for it. The respective provider or "
        "operator is always responsible for the content of linked pages. If we become aware of any legal violations, "
        "we will remove such links immediately.</p>",
        "<h2>Copyright</h2>",
        "<p>The texts, design and the e-book <strong>The 30-Day Weight Loss Plan</strong> are protected by copyright. "
        "You may download and print the e-book for your personal use. Copying, selling or republishing it elsewhere "
        "without permission is not allowed.</p>",
        "<h2>Consumer dispute resolution</h2>",
        "<p>We are neither willing nor obliged to take part in dispute resolution proceedings before a consumer "
        "arbitration board.</p>",
        '<p>You can find out how we process your personal data in our <a href="/privacy-policy/">Privacy Policy</a>.</p>',
    ])


# ------------------------------------------------------------------------------------------ Privacy Policy
def privacy_html():
    return "".join([
        "<p>This privacy policy explains which personal data we process when you visit <strong>leanmodepro.com</strong>, "
        "sign up for the free <strong>30-Day Weight Loss Plan</strong> or contact us, for what purpose and on which legal "
        "basis. We process your data in accordance with the EU General Data Protection Regulation (GDPR), the German "
        "Federal Data Protection Act (BDSG) and the German Telecommunications and Digital Services Data Protection Act "
        "(TDDDG).</p>",

        # 1 -------------------------------------------------------------------------------------------------
        "<h2>1. Privacy at a glance</h2>",
        "<h3>In short</h3><ul>",
        "<li>When you visit the site, the server briefly stores technical access data so it can show you the page.</li>",
        "<li>We don't use cookies, analytics, tracking pixels or advertising tools on this website.</li>",
        "<li>If you sign up, we process your email address with our email service Brevo after you confirm it "
        "(double opt-in), to send you the plan and our newsletter and to measure whether our emails are opened and "
        "clicked. You can withdraw your consent at any time.</li>",
        "<li>The signup form only asks for your email address; we don't ask for any health information.</li>",
        "<li>We don't sell your data.</li></ul>",

        "<h3>General information</h3>",
        "<p>The following information gives you a simple overview of what happens to your personal data when you visit "
        "this website. Personal data is any data that can be used to identify you personally (e.g. your email address "
        "or your IP address). You'll find detailed information in the sections below this overview.</p>",

        "<h3>Data collection on this website</h3>",
        "<p><strong>Who is responsible for data collection on this website?</strong><br>Data on this website is processed "
        "by the website operator. You'll find their contact details in the section “Controller” of this privacy "
        "policy.</p>",
        "<p><strong>How do we collect your data?</strong><br>Some of your data is collected when you give it to us, for "
        "example the email address you enter in the signup form or an email you send us. Other data is collected "
        "automatically by our IT systems when you visit the website. This is mainly technical data (e.g. browser, "
        "operating system or the time you accessed the page). This data is collected automatically as soon as you "
        "enter this website.</p>",
        "<p><strong>What do we use your data for?</strong><br>Some of the data is collected to make sure the website "
        "works without errors. If you sign up, we use your email address to send you the free plan and our "
        "newsletter.</p>",
        "<p><strong>What rights do you have regarding your data?</strong><br>You have the right to receive information "
        "about the origin, recipients and purpose of your stored personal data free of charge at any time. You also "
        "have the right to request that this data be corrected or deleted. If you have given your consent to data "
        "processing, you can withdraw it at any time with effect for the future. Under certain circumstances, you also "
        "have the right to request that the processing of your personal data be restricted. You also have the right to "
        "lodge a complaint with the competent supervisory authority. You can contact us at any time about this and any "
        "other questions about data protection.</p>",

        # 2 -------------------------------------------------------------------------------------------------
        "<h2>2. Hosting</h2>",
        "<p>We host the content of our website with the following provider.</p>",
        "<h3>External hosting</h3>",
        "<p>This website is hosted externally. The personal data collected on this website is stored on the servers of "
        "the hosting provider. This may include IP addresses, contact requests, metadata and communication data, "
        "contact details, website access and other data generated by a website.</p>",
        "<p>Hosting is used to fulfill our obligations to our potential and existing users (Art. 6(1)(b) GDPR) and in "
        "the interest of a secure, fast and efficient provision of our online service by a professional provider "
        "(Art. 6(1)(f) GDPR). Our hosting provider only processes your data to the extent necessary to fulfill its "
        "service obligations and follows our instructions regarding this data.</p>",
        f"<p>Our hosting provider:</p><p>{HOSTER}</p>",
        f"<p>Registrar of our domain (Hostinger group):</p><p>{REGISTRAR}</p>",
        "<p>The website's server is located in Frankfurt (Germany). Hostinger's privacy policy: "
        f"{_link('https://www.hostinger.com/legal/privacy-policy', 'hostinger.com/legal/privacy-policy')}</p>",
        "<h3>Data processing agreement</h3>",
        "<p>We have concluded a data processing agreement (Art. 28 GDPR) for the use of the service named above. This is "
        "a contract required by data protection law that ensures the provider processes the personal data of our "
        "website visitors only according to our instructions and in compliance with the GDPR.</p>",

        # 3 -------------------------------------------------------------------------------------------------
        "<h2>3. General information and mandatory information</h2>",
        "<h3>Data protection</h3>",
        "<p>We take the protection of your personal data very seriously. We treat your personal data confidentially and "
        "in accordance with the statutory data protection regulations and this privacy policy.</p>",
        "<p>When you use this website, various personal data is collected. This privacy policy explains which data we "
        "collect and what we use it for. It also explains how and for what purpose this happens.</p>",
        "<p>Please note that data transmission over the internet (e.g. when communicating by email) can have security "
        "gaps. Complete protection of data against access by third parties is not possible.</p>",

        "<h3>Controller</h3>",
        "<p>The controller responsible for data processing on this website is:</p>",
        CONTACT,
        "<p>The controller is the natural or legal person who alone or jointly with others decides on the purposes and "
        "means of processing personal data (e.g. names, email addresses). We are not legally required to appoint a data "
        "protection officer.</p>",

        "<h3>Storage period</h3>",
        "<p>Unless a more specific storage period is stated in this privacy policy, your personal data will remain with us "
        "until the purpose for processing it no longer applies. If you make a justified request for deletion or "
        "withdraw your consent to data processing, your data will be deleted unless we have other legally permissible "
        "reasons for storing it (e.g. retention periods under tax or commercial law); in that case it will be deleted "
        "once those reasons no longer apply.</p>",

        "<h3>General information on the legal bases for data processing</h3>",
        "<p>If you have consented to data processing, we process your personal data on the basis of Art. 6(1)(a) GDPR. If "
        "you have expressly consented to the transfer of personal data to third countries, the processing is also based "
        "on Art. 49(1)(a) GDPR. If you have consented to the storage of cookies or to access to information on your "
        "device (e.g. via device fingerprinting), the processing is also based on Section 25(1) TDDDG. Consent can be "
        "withdrawn at any time. If your data is required to fulfill a contract or to carry out pre-contractual "
        "measures, we process it on the basis of Art. 6(1)(b) GDPR. If your data is required to fulfill a legal "
        "obligation, we process it on the basis of Art. 6(1)(c) GDPR. Data processing may also be based on our "
        "legitimate interest under Art. 6(1)(f) GDPR. The relevant legal basis in each individual case is explained in "
        "the following sections of this privacy policy.</p>",
        "<p>We don't ask for or process special categories of personal data such as health data (Art. 9 GDPR).</p>",

        "<h3>Recipients of personal data</h3>",
        "<p>In the course of our business, we work with various external parties. In some cases, this requires "
        "personal data to be transferred to them. We only pass on personal data to external parties if this is "
        "necessary to fulfill a contract, if we are legally obliged to do so (e.g. passing on data to tax authorities), "
        "if we have a legitimate interest in the transfer under Art. 6(1)(f) GDPR, or if another legal basis permits "
        "it. When we use processors, we only pass on personal data on the basis of a valid data processing agreement. "
        "In the case of joint processing, a joint controller agreement is concluded.</p>",
        "<p>On this website, your data may be transferred to the following recipients: our hosting provider Hostinger "
        "and our email service Brevo (both as processors). We don't sell your data.</p>",

        "<h3>Transfers to third countries</h3>",
        "<p>Hostinger and Brevo are companies based in the European Union and process your data on servers in the EU. "
        "The social networks named in section 5 may also transfer data to their parent companies in the USA (Meta "
        "Platforms, Inc., Pinterest, Inc., Google LLC) or to other countries (TikTok). Meta Platforms, Inc., "
        "Pinterest, Inc. and Google LLC are certified under the EU-U.S. Data Privacy Framework, for which the European "
        "Commission has adopted an adequacy decision (Art. 45 GDPR). In addition, EU standard contractual clauses "
        "(Art. 46(2)(c) GDPR) are used.</p>",

        "<h3>Automated decision-making</h3>",
        "<p>We don't use automated decision-making within the meaning of Art. 22 GDPR, and we don't create profiles.</p>",

        "<h3>Your rights at a glance</h3>",
        "<p>Under the GDPR you have the right to:</p><ul>",
        "<li>access the data we hold about you (Art. 15)</li>",
        "<li>have incorrect data corrected (Art. 16)</li>",
        "<li>have your data deleted (Art. 17)</li>",
        "<li>have the processing restricted (Art. 18)</li>",
        "<li>receive your data in a common format (data portability, Art. 20)</li>",
        "<li>object to the processing (Art. 21)</li>",
        "<li>withdraw your consent at any time (Art. 7(3))</li>",
        "<li>lodge a complaint with a supervisory authority (Art. 77)</li></ul>",
        "<p>Just send us an email to exercise these rights.</p>",

        "<h3>Withdrawal of your consent to data processing</h3>",
        "<p>Many data processing operations are only possible with your express consent. You can withdraw consent you "
        "have already given at any time. The lawfulness of the data processing carried out until the withdrawal remains "
        "unaffected. You can withdraw your consent to our emails with the unsubscribe link in every email or by writing "
        "to us.</p>",

        "<h3>Right to object to data collection in special cases and to direct marketing (Art. 21 GDPR)</h3>",
        "<p><strong>If data processing is based on Art. 6(1)(e) or (f) GDPR, you have the right to object to the "
        "processing of your personal data at any time on grounds relating to your particular situation; this also "
        "applies to profiling based on these provisions. You'll find the legal basis on which a processing operation is "
        "based in this privacy policy. If you object, we will no longer process your personal data concerned unless we "
        "can demonstrate compelling legitimate grounds for the processing that override your interests, rights and "
        "freedoms, or the processing serves the establishment, exercise or defense of legal claims (objection under "
        "Art. 21(1) GDPR).</strong></p>",
        "<p><strong>If your personal data is processed for direct marketing, you have the right to object at any time to "
        "the processing of personal data concerning you for such marketing; this also applies to profiling to the "
        "extent that it is related to such direct marketing. If you object, your personal data will no longer be used "
        "for direct marketing (objection under Art. 21(2) GDPR).</strong></p>",

        "<h3>Right to lodge a complaint with the competent supervisory authority</h3>",
        "<p>In the event of violations of the GDPR, data subjects have the right to lodge a complaint with a supervisory "
        "authority, in particular in the member state of their habitual residence, their place of work or the place of "
        "the alleged violation. The right to lodge a complaint is without prejudice to any other administrative or "
        "judicial remedies.</p>",
        _if("authority", "<p>The supervisory authority responsible for us: {{lmp:authority}}.</p>"),

        "<h3>Right to data portability</h3>",
        "<p>You have the right to have data that we process automatically on the basis of your consent or in fulfillment "
        "of a contract handed over to you or to a third party in a common, machine-readable format. If you request the "
        "direct transfer of the data to another controller, this will only be done to the extent technically "
        "feasible.</p>",

        "<h3>Access, correction and deletion</h3>",
        "<p>Within the framework of the applicable legal provisions, you have the right at any time to free information "
        "about your stored personal data, its origin and recipients and the purpose of the data processing and, if "
        "applicable, a right to have this data corrected or deleted. You can contact us at any time about this and any "
        "other questions about personal data.</p>",

        "<h3>Right to restriction of processing</h3>",
        "<p>You have the right to request that the processing of your personal data be restricted. You can contact us at "
        "any time about this. The right to restriction of processing applies in the following cases:</p><ul>",
        "<li>If you dispute the accuracy of your personal data stored by us, we usually need time to check this. For the "
        "duration of the check, you have the right to request that the processing of your personal data be "
        "restricted.</li>",
        "<li>If the processing of your personal data was or is unlawful, you can request the restriction of data "
        "processing instead of deletion.</li>",
        "<li>If we no longer need your personal data, but you need it to exercise, defend or assert legal claims, you have "
        "the right to request the restriction of the processing of your personal data instead of deletion.</li>",
        "<li>If you have lodged an objection under Art. 21(1) GDPR, your interests and ours must be weighed against each "
        "other. As long as it has not yet been determined whose interests prevail, you have the right to request that "
        "the processing of your personal data be restricted.</li></ul>",
        "<p>If you have restricted the processing of your personal data, this data may — apart from being stored — only be "
        "processed with your consent or for the establishment, exercise or defense of legal claims or for the protection "
        "of the rights of another natural or legal person or for reasons of important public interest of the European "
        "Union or a member state.</p>",

        "<h3>SSL/TLS encryption</h3>",
        "<p>For security reasons and to protect the transmission of confidential content, such as the data you send us, "
        "this site uses SSL/TLS encryption. You can recognize an encrypted connection by the address bar of your browser "
        "starting with “https://” instead of “http://” and by the lock symbol in the address bar. When SSL/TLS "
        "encryption is active, the data you send us (e.g. the email address you enter in the signup form) cannot be read "
        "by third parties.</p>",

        "<h3>Objection to promotional emails</h3>",
        "<p>We hereby object to the use of the contact details published as part of our legal notice obligation for "
        "sending unsolicited advertising and information material. We expressly reserve the right to take legal action "
        "in the event of unsolicited advertising information being sent, such as spam emails.</p>",

        "<h3>If you live outside the EU</h3>",
        "<p>Because we are based in Germany, the GDPR applies to the processing of your data wherever you live, and you "
        "have the rights described above. We don't sell or share your personal information for targeted advertising, "
        "and we don't use it for profiling.</p>",

        # 4 -------------------------------------------------------------------------------------------------
        "<h2>4. Data collection on this website</h2>",
        "<h3>Cookies and browser storage</h3>",
        "<p>This website doesn't use cookies for visitors and doesn't store information in your browser "
        "(e.g. localStorage). There are no analytics, tracking pixels or advertising tools, and no content (such as "
        "videos or fonts) is loaded from third-party servers. Technically necessary cookies are only set when the site "
        "administrator logs in to WordPress; they don't affect visitors.</p>",

        "<h3>Server log files</h3>",
        "<p>When you open the website, your browser automatically sends certain information to the server. Our hosting "
        "provider stores it in log files:</p>",
        "<ul><li>IP address</li><li>date and time</li><li>page or file requested</li>"
        "<li>previously visited page (referrer)</li><li>browser and operating system</li>"
        "<li>amount of data transferred and the server's response code</li></ul>",
        "<p>We process this data to deliver the website, to keep it secure and to detect errors or attacks. This data is "
        "not combined with other data sources. The legal basis is our legitimate interest in a technically error-free "
        "and secure website (Art. 6(1)(f) GDPR). The log files are deleted automatically after a short time.</p>",

        "<h3>Contact by email</h3>",
        "<p>If you email us, your request, including all personal data it contains (e.g. your name, email address and "
        "message), will be stored and processed by us for the purpose of handling your request. We don't pass this data "
        "on without your consent.</p>",
        "<p>This data is processed on the basis of Art. 6(1)(b) GDPR if your request relates to the fulfillment of a "
        "contract or is necessary for pre-contractual measures; in all other cases, it is based on our legitimate "
        "interest in effectively handling the requests sent to us (Art. 6(1)(f) GDPR).</p>",
        "<p>The data you send us remains with us until you ask us to delete it or the purpose no longer applies (e.g. after "
        "your request has been dealt with). Mandatory statutory provisions, in particular statutory retention periods, "
        "remain unaffected.</p>",

        "<h3>Fonts</h3>",
        "<p>The font used on this site (Instrument Sans) is loaded from our own server. No connection to Google or any "
        "other font provider is made.</p>",

        "<h3>Downloading the e-book</h3>",
        "<p>After you confirm your signup, you can download the e-book directly from our server. Only the server log files "
        "described above are created.</p>",

        "<h3>Affiliate links</h3>",
        "<p>Some articles contain affiliate links. If you click such a link, you go to the merchant's website. We don't "
        "pass any personal data to the merchant. The merchant or its affiliate network may set cookies on its own website "
        "to attribute a purchase to our link; this happens under the merchant's responsibility and privacy policy, not "
        "on our website. We use affiliate links on the basis of our legitimate interest in financing our free content "
        "(Art. 6(1)(f) GDPR). More about this in our <a href=\"/disclaimer/\">Disclaimer</a>.</p>",
        _if("amazon",
            "<p><strong>Amazon Associates:</strong> We participate in the Amazon Associates program, an affiliate "
            "program run by Amazon. " + AMAZON_STATEMENT + " If you click an Amazon link, Amazon may use cookies to track "
            "the origin of orders. Amazon's privacy notice: "
            f"{_link('https://www.amazon.com/privacy', 'amazon.com/privacy')}</p>"),

        # 5 -------------------------------------------------------------------------------------------------
        "<h2>5. Social media</h2>",
        "<h3>No social media plugins</h3>",
        "<p>We don't use social media plugins, share buttons or embedded feeds on this website. Opening our pages doesn't "
        "transfer any data to social networks.</p>",
        "<h3>Our profiles on social networks</h3>",
        "<p>We share content on the following platforms and point to our website from there:</p><ul>",
        f"<li><strong>Pinterest:</strong> {PINTEREST}. Privacy policy: "
        f"{_link('https://policy.pinterest.com/privacy-policy', 'policy.pinterest.com/privacy-policy')}</li>",
        f"<li><strong>Instagram:</strong> {META}. Privacy policy: "
        f"{_link('https://privacycenter.instagram.com/policy/', 'privacycenter.instagram.com/policy')}</li>",
        f"<li><strong>TikTok:</strong> {TIKTOK}. Privacy policy: "
        f"{_link('https://www.tiktok.com/legal/privacy-policy-eea', 'tiktok.com/legal/privacy-policy-eea')}</li>",
        f"<li><strong>YouTube:</strong> {GOOGLE}. Privacy policy: "
        f"{_link('https://policies.google.com/privacy', 'policies.google.com/privacy')}</li></ul>",
        "<p>When you visit our profiles or interact with our content there, the respective provider processes your data "
        "(e.g. IP address, device information, interactions and data linked to your account) for its own purposes and "
        "may use cookies. The providers only give us anonymous statistics about the use of our profiles; we can't "
        "identify individual people from them. Where a provider offers an agreement on joint controllership for these "
        "statistics (Art. 26 GDPR), as Meta does for Instagram "
        f"({_link('https://www.facebook.com/legal/terms/page_controller_addendum', 'Page Insights Addendum')}), "
        "the provider is primarily responsible for informing you and for handling your rights. You can exercise your "
        "rights both with the provider and with us; we will forward requests to the provider if necessary.</p>",
        "<p>The legal basis is our legitimate interest in communicating with users and presenting our content "
        "(Art. 6(1)(f) GDPR). If a provider asks for your consent (e.g. for cookies), the legal basis is that consent "
        "(Art. 6(1)(a) GDPR, Section 25(1) TDDDG). The providers may also transfer data to third countries "
        "(see “Transfers to third countries”).</p>",

        # 6 -------------------------------------------------------------------------------------------------
        "<h2>6. Free plan and email newsletter</h2>",
        "<h3>Newsletter data</h3>",
        "<p>When you enter your email address in the signup form, we process it to send you the free "
        "<strong>30-Day Weight Loss Plan</strong> and then emails from LEAN MODE PRO with helpful content and offers "
        "(newsletter). We offer the free plan together with signing up for our newsletter; this is stated clearly in "
        "the signup form. The form only asks for your email address; we don't ask for your name, weight, height or "
        "health information. We use this data to send the emails and don't pass it on to anyone other than our email "
        "service Brevo.</p>",

        "<h3>How signing up works, step by step (double opt-in)</h3>",
        "<ol>",
        "<li>You enter your email address in the form and click the button. What you are agreeing to is explained right "
        "below the button.</li>",
        "<li>Your email address is sent from your browser over an encrypted connection directly to Brevo's signup form "
        "(sibforms.com). Brevo also technically receives your IP address, the time of signup and browser information. "
        "Our site doesn't load any scripts or cookies from Brevo for this; the connection to Brevo is only made when you "
        "submit the form.</li>",
        "<li>We then take you to an information page, and Brevo sends you a confirmation email.</li>",
        "<li>When you click the link in the confirmation email, your signup is complete and you are taken to the page "
        "where you can download the plan. After that, we may send you our newsletter.</li>",
        "<li>If you don't click the confirmation link, your email address is not added to our list and you won't receive "
        "any further emails.</li>",
        "</ol>",
        "<p>This process prevents someone else from signing up with your email address. To be able to prove your "
        "consent, we record the time of signup and confirmation, the IP addresses used and the signup form used at "
        "Brevo (consent log).</p>",

        "<h3>Legal basis</h3>",
        "<p>Processing your email address and sending the emails is based on the consent you give when signing up "
        "(Art. 6(1)(a) GDPR). Storing the consent log is based on our obligation to prove your consent (Art. 6(1)(c) in "
        "conjunction with Art. 7(1) GDPR) and on our legitimate interest in being able to defend ourselves against legal "
        "claims (Art. 6(1)(f) GDPR).</p>",

        "<h3>Email service: Brevo</h3>",
        f"<p>We send the confirmation email and the newsletter with Brevo. Provider: {BREVO}. Brevo stores the signup "
        "form, the email addresses and the consent log, sends the emails and measures how they are used (see "
        "below).</p>",
        "<p>Brevo processes this data as a processor only on our behalf and according to our instructions; we have "
        "concluded a data processing agreement with Brevo (Art. 28 GDPR). Brevo stores the data on servers in the EU. If "
        "Brevo's sub-processors exceptionally transfer data outside the EU, this is based on an adequacy decision "
        "(Art. 45 GDPR) or EU standard contractual clauses (Art. 46(2)(c) GDPR). The use of Brevo is based on your "
        "consent (Art. 6(1)(a) GDPR) and on our legitimate interest in sending emails securely and efficiently "
        "(Art. 6(1)(f) GDPR). Brevo's privacy policy: "
        f"{_link('https://www.brevo.com/legal/privacypolicy/', 'brevo.com/legal/privacypolicy')}</p>",

        "<h3>Measuring opens and clicks</h3>",
        "<p>To understand how much interest our emails receive and to improve our content, we use Brevo to measure "
        "whether an email is opened and which links in it are clicked. For this, the emails contain a small, invisible "
        "image (tracking pixel) and links redirected via Brevo. The time of opening and clicking, the IP address and "
        "technical information about the email program and device are recorded and linked to your email address.</p>",
        "<p>The legal basis is the consent you gave to receive our emails (Art. 6(1)(a) GDPR). It isn't technically "
        "possible to object to the measurement separately; if you don't want it, you need to unsubscribe. When you "
        "unsubscribe, the measurement ends too.</p>",

        "<h3>Unsubscribing and storage period</h3>",
        "<p>You can withdraw your consent at any time: with the unsubscribe link at the end of every email or by writing "
        "to us. The withdrawal doesn't affect the lawfulness of the processing carried out until then.</p>",
        "<p>We store the data you provide for the newsletter with us or Brevo until you unsubscribe and delete it from the "
        "mailing list after you unsubscribe or once the purpose no longer applies. We reserve the right to delete or "
        "block email addresses from our mailing list at our own discretion within the scope of our legitimate interest "
        "(Art. 6(1)(f) GDPR). Data stored by us for other purposes remains unaffected.</p>",
        "<p>After you unsubscribe, your email address may be stored on a blocklist with us or Brevo if this is necessary "
        "to prevent future emails to you. The data on the blocklist is only used for this purpose and is not combined "
        "with other data. This serves both your interest and our interest in complying with the legal requirements "
        "for sending emails (Art. 6(1)(f) GDPR). Storage on the blocklist is not limited in time. You can object to "
        "this storage if your interests outweigh our legitimate interest.</p>",
        "<p>We keep the consent log after your subscription ends for as long as legal claims could be made "
        "(usually three years), so that we can prove your consent.</p>",

        # 7 -------------------------------------------------------------------------------------------------
        "<h2>7. Changes</h2>",
        "<p>If we change the website or the services we use, we will update this privacy policy. The current version on "
        "this page always applies.</p>",
        f'<p class="lmp-updated">Last updated: {UPDATED}<br>Parts of this privacy policy are based on a template by '
        f"e-recht24.de, translated and adapted. Source: {_link('https://www.e-recht24.de', 'e-recht24.de')}</p>",
    ])


# ------------------------------------------------------------------------------------------ Disclaimer
def disclaimer_html():
    return "".join([
        "<h2>Medical disclaimer</h2>",
        "<p>The content on this website, in our emails, on our social media profiles and in the free e-book "
        "<strong>The 30-Day Weight Loss Plan</strong> is for general information and education only. It is not medical "
        "advice and does not replace advice, diagnosis or treatment from a doctor, registered dietitian or other "
        "qualified health professional.</p>",
        "<p>Talk to your doctor before you change how you eat or exercise, especially if you have a chronic condition, "
        "take medication regularly, are pregnant or breastfeeding, or have a history of eating disorders. Stop exercising "
        "right away if you feel pain, dizziness, chest pain or shortness of breath. Our content is intended for healthy "
        "adults aged 18 and over.</p>",
        "<p>Everyone starts from a different place, so results vary from person to person. We don't promise or guarantee "
        "any particular result, such as a specific amount of weight loss. You use the information at your own "
        "responsibility.</p>",

        "<h2>Affiliate disclosure</h2>",
        "<p>Some links on this website, in our emails and in our social media posts are affiliate links. If you buy "
        "something through such a link, we may earn a small commission. This doesn't cost you anything extra; the price "
        "is the same for you. Commissions help us keep our content free.</p>",
        _if("amazon", f"<p><strong>{AMAZON_STATEMENT}</strong></p>"),
        "<p>We only recommend products we consider useful, and a commission never influences what we write. We don't sell "
        "the products ourselves: your purchase contract is with the respective merchant, and prices and availability can "
        "change. Articles that contain affiliate links say so at the top, and in social media posts we mark them as "
        "advertising.</p>",

        "<h2>External links</h2>",
        "<p>Our content contains links to websites of third parties. We have no influence on their content and accept no "
        "liability for it; the respective provider is responsible. More in our "
        '<a href="/legal-notice/">Legal Notice</a>.</p>',

        "<h2>Contact</h2>",
        CONTACT,
        _updated(),
    ])


BODIES = {
    "legal-notice": imprint_html,
    "privacy-policy": privacy_html,
    "disclaimer": disclaimer_html,
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
    while True:                                   # blocks can be nested
        new = pattern.sub(block, html)
        if new == html:
            break
        html = new
    for key, val in operator.items():
        html = html.replace("{{lmp:" + key + "}}", escape(str(val)))
    return html
