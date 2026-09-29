#!/usr/bin/env python3
"""Generates the static pages of bytunasoft.com (EN at the root, DE under /de/, TR under /tr/).

Run `python3 build.py` after editing any text below; the generated HTML files are committed
and served as-is by GitHub Pages. No runtime JavaScript, no cookies, no third-party requests.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://bytunasoft.com"
UPDATED = "2026-09-29"

COMPANY = {
    "legal": "BYTUNASOFT TEKNOLOJİ VE YAZILIM HİZMETLERİ LİMİTED ŞİRKETİ",
    "street": "Fikirtepe Mah. Hızırbey Cad. No:115-A Kapı No:137",
    "city": "34720 Kadıköy / İstanbul",
    "country": {"en": "Türkiye", "de": "Türkei", "tr": "Türkiye"},
    "tax_office": "Göztepe Vergi Dairesi",
    "vkn": "1950867948",
    "email": "yusuf.bozkurt@bytunasoft.com",
    "director": "Yusuf Bozkurt",
}
APP = "Plapperland – Ilos Wortreise"

LANGS = ["en", "de", "tr"]
PREFIX = {"en": "/", "de": "/de/", "tr": "/tr/"}
PAGES = {"home": "", "imprint": "imprint/", "privacy": "plapperland/privacy/", "support": "plapperland/support/"}


def url(lang, page):
    return PREFIX[lang] + PAGES[page]


def address_html(lang):
    return f'{COMPANY["legal"]}<br>{COMPANY["street"]}<br>{COMPANY["city"]}<br>{COMPANY["country"][lang]}'


MAIL = f'<a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a>'

# ---------------------------------------------------------------------------
# Shared UI strings
# ---------------------------------------------------------------------------
UI = {
    "en": {
        "skip": "Skip to content", "brand_sub": "Istanbul", "nav_services": "Services", "nav_apps": "Apps",
        "nav_contact": "Contact", "nav_imprint": "Imprint", "lang_label": "Language",
        "footer_note": "Software development and consulting. Registered in Istanbul, Türkiye.",
        "privacy": "Privacy (Plapperland)", "support": "Support (Plapperland)",
        "updated": "Last updated", "back_app": "Plapperland",
    },
    "de": {
        "skip": "Zum Inhalt springen", "brand_sub": "Istanbul", "nav_services": "Leistungen", "nav_apps": "Apps",
        "nav_contact": "Kontakt", "nav_imprint": "Impressum", "lang_label": "Sprache",
        "footer_note": "Softwareentwicklung und Beratung. Eingetragen in Istanbul, Türkei.",
        "privacy": "Datenschutz (Plapperland)", "support": "Support (Plapperland)",
        "updated": "Stand", "back_app": "Plapperland",
    },
    "tr": {
        "skip": "İçeriğe geç", "brand_sub": "İstanbul", "nav_services": "Hizmetler", "nav_apps": "Uygulamalar",
        "nav_contact": "İletişim", "nav_imprint": "Künye", "lang_label": "Dil",
        "footer_note": "Yazılım geliştirme ve danışmanlık. İstanbul, Türkiye'de kayıtlıdır.",
        "privacy": "Gizlilik (Plapperland)", "support": "Destek (Plapperland)",
        "updated": "Son güncelleme", "back_app": "Plapperland",
    },
}

# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
HOME = {
    "en": {
        "title": "Bytunasoft – Software development & consulting",
        "desc": "Bytunasoft is a software company in Istanbul: enterprise Java and Spring, BPM with Camunda, "
                "system integration, telecom OSS/BSS consulting, and our own apps such as Plapperland.",
        "eyebrow": "Software development · Istanbul",
        "h1": "Backend systems that run the business, and apps we build ourselves.",
        "lede": "<strong>Bytunasoft</strong> designs and builds enterprise software: Java and Spring services, "
                "business process automation, and the integrations that tie them together. Alongside client work we "
                "make our own products.",
        "reg_label": "Company record",
        "reg": [("Legal name", COMPANY["legal"]), ("Registered office", "Kadıköy / İstanbul, Türkiye"),
                ("Tax office", COMPANY["tax_office"]), ("Tax ID (VKN)", COMPANY["vkn"]),
                ("Managing director", COMPANY["director"])],
        "services_h": "What we do",
        "services_p": "Hands-on engineering and consulting, delivered by the people who write the code.",
        "services": [
            ("Enterprise Java & Spring", "Java · Spring Boot",
             "Design and development of backend services and APIs, from greenfield services to the long-lived "
             "systems that need careful change."),
            ("Business process automation", "BPMN · DMN · Camunda",
             "Process models, decision tables and process-engine applications with Camunda, including testing and "
             "operation of long-running workflows."),
            ("System integration", "REST · messaging · TM Forum Open APIs",
             "Connecting systems through well-defined APIs and events: adapters, contracts, error handling and "
             "the tests that keep interfaces honest."),
            ("Telecom OSS/BSS consulting", "Order · service · resource",
             "Consulting on order management, fulfilment and inventory processes for telecom operators, from "
             "design through implementation."),
        ],
        "apps_h": "Our apps",
        "apps_p": "Products we design, build and publish ourselves.",
        "app_kicker": "iPad app for children",
        "app_text": "Ilo the hedgehog takes young children on a journey through their first German words. Every "
                    "object is spoken in German with its article, so children learn by playing. Parent settings "
                    "are available in German, English and Turkish.",
        "app_facts": ["No data collected", "No ads", "No tracking", "No account", "One-time purchase unlocks all worlds"],
        "app_privacy": "Privacy policy", "app_support": "Support",
        "shot1_alt": "Plapperland map: an island with play worlds for colours, farm, vehicles, garden, numbers, shapes, zoo and kitchen",
        "shot2_alt": "Plapperland farm world: Ilo the hedgehog with a cow, sheep, pig, duck and rooster",
        "icon_alt": "Plapperland app icon",
        "contact_h": "Contact",
        "contact_p": "For project enquiries, app support or anything else, write to us by email.",
        "contact_mail_label": "Email", "contact_addr_label": "Address",
    },
    "de": {
        "title": "Bytunasoft – Softwareentwicklung & Beratung",
        "desc": "Bytunasoft ist ein Softwareunternehmen in Istanbul: Enterprise Java und Spring, BPM mit Camunda, "
                "Systemintegration, Telekom-OSS/BSS-Beratung und eigene Apps wie Plapperland.",
        "eyebrow": "Softwareentwicklung · Istanbul",
        "h1": "Backend-Systeme, die das Geschäft tragen, und Apps, die wir selbst bauen.",
        "lede": "<strong>Bytunasoft</strong> entwirft und entwickelt Unternehmenssoftware: Java- und Spring-Services, "
                "Prozessautomatisierung und die Integrationen, die alles verbinden. Neben Kundenprojekten "
                "entwickeln wir eigene Produkte.",
        "reg_label": "Unternehmensdaten",
        "reg": [("Firma", COMPANY["legal"]), ("Sitz", "Kadıköy / İstanbul, Türkei"),
                ("Finanzamt", COMPANY["tax_office"]), ("Steuernummer (VKN)", COMPANY["vkn"]),
                ("Geschäftsführer", COMPANY["director"])],
        "services_h": "Was wir tun",
        "services_p": "Engineering und Beratung aus einer Hand – von den Leuten, die den Code schreiben.",
        "services": [
            ("Enterprise Java & Spring", "Java · Spring Boot",
             "Entwurf und Entwicklung von Backend-Services und APIs – vom neuen Service bis zum langlebigen "
             "System, das sorgfältig weiterentwickelt werden muss."),
            ("Prozessautomatisierung", "BPMN · DMN · Camunda",
             "Prozessmodelle, Entscheidungstabellen und Process-Engine-Anwendungen mit Camunda, inklusive Tests "
             "und Betrieb langlaufender Workflows."),
            ("Systemintegration", "REST · Messaging · TM Forum Open APIs",
             "Systeme über klar definierte APIs und Events verbinden: Adapter, Schnittstellenverträge, "
             "Fehlerbehandlung und Tests, die Schnittstellen verlässlich halten."),
            ("Telekom-OSS/BSS-Beratung", "Order · Service · Resource",
             "Beratung zu Auftragsmanagement, Fulfillment- und Inventarprozessen für Telekommunikationsanbieter – "
             "vom Entwurf bis zur Umsetzung."),
        ],
        "apps_h": "Unsere Apps",
        "apps_p": "Produkte, die wir selbst entwerfen, entwickeln und veröffentlichen.",
        "app_kicker": "iPad-App für Kinder",
        "app_text": "Ilo der Igel nimmt kleine Kinder mit auf eine Reise durch ihre ersten deutschen Wörter. Jeder "
                    "Gegenstand wird auf Deutsch mit Artikel gesprochen – so lernen Kinder spielend. Der "
                    "Elternbereich ist auf Deutsch, Englisch und Türkisch verfügbar.",
        "app_facts": ["Keine Datenerhebung", "Keine Werbung", "Kein Tracking", "Kein Konto", "Einmalkauf öffnet alle Welten"],
        "app_privacy": "Datenschutzerklärung", "app_support": "Support",
        "shot1_alt": "Plapperland-Karte: eine Insel mit Spielwelten für Farben, Bauernhof, Fahrzeuge, Garten, Zahlen, Formen, Zoo und Küche",
        "shot2_alt": "Plapperland-Bauernhof: Ilo der Igel mit Kuh, Schaf, Schwein, Ente und Hahn",
        "icon_alt": "App-Symbol von Plapperland",
        "contact_h": "Kontakt",
        "contact_p": "Für Projektanfragen, App-Support oder alles andere schreiben Sie uns eine E-Mail.",
        "contact_mail_label": "E-Mail", "contact_addr_label": "Anschrift",
    },
    "tr": {
        "title": "Bytunasoft – Yazılım geliştirme ve danışmanlık",
        "desc": "Bytunasoft, İstanbul'da bir yazılım şirketidir: kurumsal Java ve Spring, Camunda ile BPM, "
                "sistem entegrasyonu, telekom OSS/BSS danışmanlığı ve Plapperland gibi kendi uygulamalarımız.",
        "eyebrow": "Yazılım geliştirme · İstanbul",
        "h1": "İşi taşıyan backend sistemleri ve kendi geliştirdiğimiz uygulamalar.",
        "lede": "<strong>Bytunasoft</strong> kurumsal yazılım tasarlar ve geliştirir: Java ve Spring servisleri, "
                "iş süreci otomasyonu ve bunları birbirine bağlayan entegrasyonlar. Müşteri projelerinin yanında "
                "kendi ürünlerimizi de geliştiriyoruz.",
        "reg_label": "Şirket bilgileri",
        "reg": [("Ticaret unvanı", COMPANY["legal"]), ("Merkez", "Kadıköy / İstanbul, Türkiye"),
                ("Vergi dairesi", COMPANY["tax_office"]), ("VKN", COMPANY["vkn"]),
                ("Şirket müdürü", COMPANY["director"])],
        "services_h": "Neler yapıyoruz",
        "services_p": "Kodu yazan ekipten, uygulamalı mühendislik ve danışmanlık.",
        "services": [
            ("Kurumsal Java & Spring", "Java · Spring Boot",
             "Backend servisleri ve API'lerin tasarımı ve geliştirilmesi – sıfırdan servislerden, dikkatle "
             "değiştirilmesi gereken uzun ömürlü sistemlere kadar."),
            ("İş süreci otomasyonu", "BPMN · DMN · Camunda",
             "Camunda ile süreç modelleri, karar tabloları ve process-engine uygulamaları; uzun süren iş "
             "akışlarının test edilmesi ve işletilmesi dahil."),
            ("Sistem entegrasyonu", "REST · mesajlaşma · TM Forum Open API'leri",
             "Sistemleri iyi tanımlanmış API'ler ve olaylar üzerinden bağlamak: adaptörler, arayüz sözleşmeleri, "
             "hata yönetimi ve arayüzleri güvenilir tutan testler."),
            ("Telekom OSS/BSS danışmanlığı", "Sipariş · servis · kaynak",
             "Telekom operatörleri için sipariş yönetimi, fulfillment ve envanter süreçlerinde tasarımdan "
             "uygulamaya danışmanlık."),
        ],
        "apps_h": "Uygulamalarımız",
        "apps_p": "Kendimiz tasarlayıp geliştirdiğimiz ve yayınladığımız ürünler.",
        "app_kicker": "Çocuklar için iPad uygulaması",
        "app_text": "Kirpi Ilo, küçük çocukları ilk Almanca kelimelerine doğru bir yolculuğa çıkarır. Her nesne "
                    "artikeliyle birlikte Almanca seslendirilir; çocuklar oynayarak öğrenir. Ebeveyn ayarları "
                    "Almanca, İngilizce ve Türkçe olarak sunulur.",
        "app_facts": ["Veri toplanmaz", "Reklam yok", "Takip yok", "Hesap yok", "Tek seferlik satın alma tüm dünyaları açar"],
        "app_privacy": "Gizlilik politikası", "app_support": "Destek",
        "shot1_alt": "Plapperland haritası: renkler, çiftlik, araçlar, bahçe, sayılar, şekiller, hayvanat bahçesi ve mutfak dünyalarının olduğu bir ada",
        "shot2_alt": "Plapperland çiftlik dünyası: kirpi Ilo ile inek, koyun, domuz, ördek ve horoz",
        "icon_alt": "Plapperland uygulama simgesi",
        "contact_h": "İletişim",
        "contact_p": "Proje talepleri, uygulama desteği veya diğer her konu için bize e-posta ile yazın.",
        "contact_mail_label": "E-posta", "contact_addr_label": "Adres",
    },
}

# ---------------------------------------------------------------------------
# Imprint
# ---------------------------------------------------------------------------
IMPRINT = {
    "en": {
        "title": "Imprint – Bytunasoft", "h1": "Imprint",
        "desc": "Legal information about BYTUNASOFT TEKNOLOJİ VE YAZILIM HİZMETLERİ LİMİTED ŞİRKETİ.",
        "intro": "Information about the provider of this website.",
        "rows": [("Company", COMPANY["legal"]), ("Legal form", "Limited liability company (Limited Şirketi) under Turkish law"),
                 ("Address", None), ("Managing director", COMPANY["director"]), ("Tax office", COMPANY["tax_office"]),
                 ("Tax ID (VKN)", COMPANY["vkn"]), ("Email", MAIL)],
        "resp_h": "Responsible for content", "resp": f'{COMPANY["director"]}, address as above.',
        "site_h": "Privacy on this website",
        "site": [
            "This website sets no cookies and uses no analytics, tracking or advertising services. Fonts and images "
            "are served from this website itself; no content is loaded from third parties.",
            "The site is hosted on GitHub Pages (GitHub, Inc.). When you visit it, GitHub processes technical data "
            "such as your IP address to deliver the pages and keep the service secure; see the "
            '<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub '
            "General Privacy Statement</a>. We do not receive or evaluate visitor logs.",
            f"If you write to us by email, we use your message and address only to answer you. Questions: {MAIL}.",
        ],
        "apps_h": "Apps", "apps": "Privacy policy and support for our app Plapperland:",
    },
    "de": {
        "title": "Impressum – Bytunasoft", "h1": "Impressum",
        "desc": "Impressum der BYTUNASOFT TEKNOLOJİ VE YAZILIM HİZMETLERİ LİMİTED ŞİRKETİ.",
        "intro": "Angaben zum Anbieter dieser Website.",
        "rows": [("Firma", COMPANY["legal"]), ("Rechtsform", "Gesellschaft mit beschränkter Haftung nach türkischem Recht (Limited Şirketi)"),
                 ("Anschrift", None), ("Geschäftsführer", COMPANY["director"]), ("Finanzamt", COMPANY["tax_office"]),
                 ("Steuernummer (VKN)", COMPANY["vkn"]), ("E-Mail", MAIL)],
        "resp_h": "Verantwortlich für den Inhalt", "resp": f'{COMPANY["director"]}, Anschrift wie oben.',
        "site_h": "Datenschutz auf dieser Website",
        "site": [
            "Diese Website setzt keine Cookies und nutzt keine Analyse-, Tracking- oder Werbedienste. Schriften und "
            "Bilder werden von dieser Website selbst ausgeliefert; es werden keine Inhalte von Dritten geladen.",
            "Die Website wird bei GitHub Pages (GitHub, Inc.) gehostet. Beim Aufruf verarbeitet GitHub technische "
            "Daten wie Ihre IP-Adresse, um die Seiten auszuliefern und den Dienst abzusichern; siehe das "
            '<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub '
            "General Privacy Statement</a>. Besucherprotokolle erhalten wir nicht und werten sie nicht aus.",
            f"Wenn Sie uns per E-Mail schreiben, nutzen wir Ihre Nachricht und Adresse nur zur Beantwortung. Fragen: {MAIL}.",
        ],
        "apps_h": "Apps", "apps": "Datenschutz und Support für unsere App Plapperland:",
    },
    "tr": {
        "title": "Künye – Bytunasoft", "h1": "Künye",
        "desc": "BYTUNASOFT TEKNOLOJİ VE YAZILIM HİZMETLERİ LİMİTED ŞİRKETİ yasal bilgileri.",
        "intro": "Bu web sitesinin sağlayıcısına ilişkin bilgiler.",
        "rows": [("Ticaret unvanı", COMPANY["legal"]), ("Şirket türü", "Limited şirket (Türk hukukuna tabi)"),
                 ("Adres", None), ("Şirket müdürü", COMPANY["director"]), ("Vergi dairesi", COMPANY["tax_office"]),
                 ("VKN", COMPANY["vkn"]), ("E-posta", MAIL)],
        "resp_h": "İçerikten sorumlu", "resp": f'{COMPANY["director"]}, adres yukarıdaki gibidir.',
        "site_h": "Bu web sitesinde gizlilik",
        "site": [
            "Bu web sitesi çerez kullanmaz; analiz, takip veya reklam hizmeti kullanmaz. Yazı tipleri ve görseller "
            "doğrudan bu siteden sunulur; üçüncü taraflardan içerik yüklenmez.",
            "Site GitHub Pages (GitHub, Inc.) üzerinde barındırılır. Siteyi ziyaret ettiğinizde GitHub, sayfaları "
            "sunmak ve hizmeti güvende tutmak için IP adresiniz gibi teknik verileri işler; bkz. "
            '<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub '
            "General Privacy Statement</a>. Ziyaretçi kayıtlarını almıyor ve değerlendirmiyoruz.",
            f"Bize e-posta ile yazarsanız mesajınızı ve adresinizi yalnızca size yanıt vermek için kullanırız. Sorular: {MAIL}.",
        ],
        "apps_h": "Uygulamalar", "apps": "Plapperland uygulamamız için gizlilik ve destek:",
    },
}

# ---------------------------------------------------------------------------
# Plapperland privacy policy (adapted from ilo-und-die-woerter/docs/store/privacy.html)
# ---------------------------------------------------------------------------
PRIVACY = {
    "en": {
        "title": "Plapperland Privacy Policy", "h1": "Privacy Policy",
        "desc": f"Privacy policy for the iPad app {APP}: the app collects no data.",
        "summary": "In short: this app collects no data.",
        "sections": [
            ("What the app does not do", [
                "No personal data is collected, stored or transmitted.",
                "No ads, no sign-in, no account.",
                "No tracking, no analytics or statistics services, no third-party SDKs.",
                "The app works offline and makes no network connections of its own (apart from the purchase via Apple, see below).",
                "The app does not use the camera, microphone, location or contacts.",
            ]),
            ("In-app purchase", [
                "The only exception to offline use is the optional one-time unlock of all worlds (in-app purchase). "
                "Purchase and “Restore purchases” are handled entirely by Apple through the App Store; we receive "
                "no payment or personal data.",
                "The purchase is only reachable in the parent area behind a parental gate.",
            ]),
            ("Data stored on the device", [
                "Game progress (for example collected stickers, music and voice settings, play-time setting) is stored "
                "only locally on the device and is never shared.",
                "Deleting the app removes this data. Progress and stickers can also be reset in the parent area.",
            ]),
        ],
        "children_h": "Children",
        "children": "The app is made for young children. Because it collects no personal data at all, no data about "
                    "children is collected either. Parent settings and the purchase are protected by a parental gate.",
        "rights_h": "Your rights",
        "rights": "Under the GDPR and the Turkish Personal Data Protection Law (KVKK) you have rights of access, "
                  "rectification, erasure and objection, and the right to lodge a complaint with a supervisory "
                  "authority. As the app processes no personal data, there is normally nothing we hold about you; "
                  "if you contact us by email, we use your message only to answer it.",
        "changes_h": "Changes",
        "changes": "If the app's handling of data ever changes, this page will be updated before the change is released.",
        "controller_h": "Controller",
    },
    "de": {
        "title": "Plapperland Datenschutz", "h1": "Datenschutzerklärung",
        "desc": f"Datenschutzerklärung für die iPad-App {APP}: Die App erhebt keine Daten.",
        "summary": "Kurz gesagt: Diese App erhebt keine Daten.",
        "sections": [
            ("Was die App nicht tut", [
                "Keine personenbezogenen Daten werden erhoben, gespeichert oder übertragen.",
                "Keine Werbung, keine Anmeldung, kein Konto.",
                "Kein Tracking, keine Analyse- oder Statistikdienste, keine Drittanbieter-SDKs.",
                "Die App funktioniert offline und baut selbst keine Internetverbindung auf (bis auf den Kauf über Apple, siehe unten).",
                "Die App verwendet weder Kamera, Mikrofon, Standort noch Kontakte.",
            ]),
            ("In-App-Kauf", [
                "Einzige Ausnahme vom Offline-Betrieb ist die optionale, einmalige Freischaltung aller Welten "
                "(In-App-Kauf). Kauf und „Käufe wiederherstellen“ wickelt ausschließlich Apple über den App Store "
                "ab; wir erhalten dabei keine Zahlungs- oder personenbezogenen Daten.",
                "Der Kauf ist nur im Elternbereich hinter einer Elternabfrage erreichbar.",
            ]),
            ("Auf dem Gerät gespeicherte Daten", [
                "Der Spielfortschritt (z. B. gesammelte Sticker, Einstellungen für Musik, Stimme und Spielzeit) wird "
                "nur lokal auf dem Gerät gespeichert und nie weitergegeben.",
                "Beim Löschen der App wird er entfernt. Fortschritt und Sticker lassen sich außerdem im Elternbereich zurücksetzen.",
            ]),
        ],
        "children_h": "Kinder",
        "children": "Die App ist für kleine Kinder gemacht. Da sie überhaupt keine personenbezogenen Daten erhebt, "
                    "werden auch keine Daten über Kinder erhoben. Elterneinstellungen und Kauf sind durch eine "
                    "Elternabfrage geschützt.",
        "rights_h": "Ihre Rechte",
        "rights": "Nach der DSGVO und dem türkischen Datenschutzgesetz (KVKK) haben Sie Rechte auf Auskunft, "
                  "Berichtigung, Löschung und Widerspruch sowie das Recht, sich bei einer Aufsichtsbehörde zu "
                  "beschweren. Da die App keine personenbezogenen Daten verarbeitet, liegen uns in der Regel keine "
                  "Daten über Sie vor; schreiben Sie uns eine E-Mail, nutzen wir sie nur zur Beantwortung.",
        "changes_h": "Änderungen",
        "changes": "Sollte sich der Umgang der App mit Daten jemals ändern, wird diese Seite vor der Veröffentlichung der Änderung aktualisiert.",
        "controller_h": "Verantwortlicher",
    },
    "tr": {
        "title": "Plapperland Gizlilik", "h1": "Gizlilik Politikası",
        "desc": f"{APP} iPad uygulaması için gizlilik politikası: uygulama hiçbir veri toplamaz.",
        "summary": "Kısacası: Bu uygulama hiçbir veri toplamaz.",
        "sections": [
            ("Uygulamanın yapmadıkları", [
                "Hiçbir kişisel veri toplanmaz, saklanmaz veya aktarılmaz.",
                "Reklam yok, giriş yok, hesap yok.",
                "Takip yok, analiz veya istatistik hizmeti yok, üçüncü taraf SDK yok.",
                "Uygulama çevrimdışı çalışır ve kendi başına internet bağlantısı kurmaz (aşağıdaki Apple üzerinden satın alma hariç).",
                "Uygulama kamera, mikrofon, konum veya kişiler verilerini kullanmaz.",
            ]),
            ("Uygulama içi satın alma", [
                "Çevrimdışı kullanımın tek istisnası, tüm dünyaların isteğe bağlı, tek seferlik kilidinin açılmasıdır "
                "(uygulama içi satın alma). Satın alma ve “Satın alımları geri yükle” işlemleri tamamen Apple "
                "tarafından App Store üzerinden yürütülür; bize hiçbir ödeme veya kişisel veri ulaşmaz.",
                "Satın almaya yalnızca ebeveyn kontrolünün arkasındaki ebeveyn alanından ulaşılabilir.",
            ]),
            ("Cihazda saklanan veriler", [
                "Oyun ilerlemesi (ör. toplanan çıkartmalar, müzik, ses ve oyun süresi ayarları) yalnızca cihazda yerel "
                "olarak saklanır ve asla paylaşılmaz.",
                "Uygulama silindiğinde bu veriler de silinir. İlerleme ve çıkartmalar ebeveyn alanından da sıfırlanabilir.",
            ]),
        ],
        "children_h": "Çocuklar",
        "children": "Uygulama küçük çocuklar için yapılmıştır. Hiçbir kişisel veri toplamadığı için çocuklara ait veri de "
                    "toplanmaz. Ebeveyn ayarları ve satın alma bir ebeveyn kontrolüyle korunur.",
        "rights_h": "Haklarınız",
        "rights": "GDPR ve 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) kapsamında bilgi talep etme, "
                  "düzeltme, silme ve itiraz haklarına ve bir denetim makamına şikâyette bulunma hakkına sahipsiniz. "
                  "Uygulama kişisel veri işlemediği için normalde hakkınızda tuttuğumuz bir veri yoktur; bize e-posta "
                  "gönderirseniz mesajınızı yalnızca yanıt vermek için kullanırız.",
        "changes_h": "Değişiklikler",
        "changes": "Uygulamanın veri kullanımı bir gün değişirse, bu sayfa değişiklik yayınlanmadan önce güncellenir.",
        "controller_h": "Veri sorumlusu",
    },
}

# ---------------------------------------------------------------------------
# Plapperland support (facts taken from the app: ios/Ilo/Parent/ParentViews.swift, Core/Store.swift)
# ---------------------------------------------------------------------------
SUPPORT = {
    "en": {
        "title": "Plapperland Support", "h1": "Support",
        "desc": f"Help and frequently asked questions for the iPad app {APP}.",
        "intro": "Answers to common questions. If yours is not here, write to us and we will help.",
        "faq": [
            ("How do I open the parent area?", [
                "Press and hold the gear icon in the top-right corner for about two seconds.",
                "The parental gate shows a number written as a word. Tap the matching number to continue.",
            ], True),
            ("How do I restore my purchase?", [
                "Open the parent area (see above).",
                "Tap “Restore purchases”. Make sure you are signed in to the App Store with the Apple ID used for the purchase.",
            ], True),
            ("How does the session timer work?", [
                "In the parent area, set “Playtime per session” between 10 and 60 minutes (default: 20). When the "
                "time is up, Ilo finishes the current level and then falls asleep. The app stays quiet until a grown-up "
                "starts a new session in the parent area.",
            ], False),
            ("Which worlds are free?", [
                "Colours and Shapes are free to play. A single in-app purchase (“All Worlds”) unlocks the other six "
                "worlds – no subscription. Refunds are handled by Apple via reportaproblem.apple.com.",
            ], False),
            ("Why does Ilo only speak German?", [
                "Plapperland is made for learning German, so everything the child hears and sees stays German. The parent "
                "area follows the iPad's language: German, English or Turkish (other languages show English).",
            ], False),
            ("How do I keep my child inside the app?", [
                "Use Guided Access (Settings › Accessibility › Guided Access). The iPad then stays in Plapperland until you end it.",
            ], False),
        ],
        "contact_h": "Contact",
        "contact": f"Email: {MAIL}. Please tell us your iPad model and iPadOS version if something does not work.",
    },
    "de": {
        "title": "Plapperland Support", "h1": "Support",
        "desc": f"Hilfe und häufige Fragen zur iPad-App {APP}.",
        "intro": "Antworten auf häufige Fragen. Ist Ihre nicht dabei, schreiben Sie uns – wir helfen gern.",
        "faq": [
            ("Wie öffne ich den Elternbereich?", [
                "Halten Sie das Zahnrad oben rechts etwa zwei Sekunden lang gedrückt.",
                "Die Elternabfrage zeigt eine als Wort geschriebene Zahl. Tippen Sie auf die passende Zahl.",
            ], True),
            ("Wie stelle ich meinen Kauf wieder her?", [
                "Öffnen Sie den Elternbereich (siehe oben).",
                "Tippen Sie auf „Käufe wiederherstellen“. Sie müssen im App Store mit der Apple-ID angemeldet sein, mit der gekauft wurde.",
            ], True),
            ("Wie funktioniert die Spielzeit pro Sitzung?", [
                "Im Elternbereich stellen Sie die „Spielzeit pro Sitzung“ zwischen 10 und 60 Minuten ein "
                "(Standard: 20). Ist die Zeit um, spielt Ilo das aktuelle Level zu Ende und schläft dann ein. Die App "
                "bleibt ruhig, bis ein Erwachsener im Elternbereich eine neue Sitzung startet.",
            ], False),
            ("Welche Welten sind kostenlos?", [
                "Farben und Formen sind kostenlos spielbar. Ein einmaliger In-App-Kauf („Alle Welten“) öffnet die "
                "anderen sechs Welten – ohne Abo. Erstattungen laufen über Apple (reportaproblem.apple.com).",
            ], False),
            ("Warum spricht Ilo nur Deutsch?", [
                "Plapperland ist zum Deutschlernen gemacht; alles, was das Kind hört und sieht, bleibt Deutsch. Der "
                "Elternbereich folgt der iPad-Sprache: Deutsch, Englisch oder Türkisch (andere Sprachen zeigen Englisch).",
            ], False),
            ("Wie bleibt mein Kind in der App?", [
                "Nutzen Sie „Geführter Zugriff“ (Einstellungen › Bedienungshilfen › Geführter Zugriff). Das iPad "
                "bleibt dann in Plapperland, bis Sie ihn beenden.",
            ], False),
        ],
        "contact_h": "Kontakt",
        "contact": f"E-Mail: {MAIL}. Wenn etwas nicht funktioniert, nennen Sie uns bitte Ihr iPad-Modell und die iPadOS-Version.",
    },
    "tr": {
        "title": "Plapperland Destek", "h1": "Destek",
        "desc": f"{APP} iPad uygulaması için yardım ve sık sorulan sorular.",
        "intro": "Sık sorulan soruların yanıtları. Sorunuz burada yoksa bize yazın, yardımcı olalım.",
        "faq": [
            ("Ebeveyn alanını nasıl açarım?", [
                "Sağ üst köşedeki dişli simgesine yaklaşık iki saniye basılı tutun.",
                "Ebeveyn kontrolü, yazıyla yazılmış bir sayı gösterir. Devam etmek için doğru sayıya dokunun.",
            ], True),
            ("Satın alımımı nasıl geri yüklerim?", [
                "Ebeveyn alanını açın (yukarıya bakın).",
                "“Satın alımları geri yükle” düğmesine dokunun. App Store'da satın alma için kullanılan Apple ID ile oturum açmış olmanız gerekir.",
            ], True),
            ("Oturum süresi nasıl çalışır?", [
                "Ebeveyn alanında “Oturum başına oyun süresi“ni 10 ile 60 dakika arasında ayarlayın (varsayılan: 20). "
                "Süre dolunca Ilo o anki bölümü bitirir ve uykuya dalar. Bir yetişkin ebeveyn alanından yeni bir oturum "
                "başlatana kadar uygulama sessiz kalır.",
            ], False),
            ("Hangi dünyalar ücretsiz?", [
                "Renkler ve Şekiller ücretsiz oynanabilir. Tek seferlik bir uygulama içi satın alma (“Tüm Dünyalar”) "
                "diğer altı dünyayı açar – abonelik yoktur. İadeler Apple üzerinden yapılır (reportaproblem.apple.com).",
            ], False),
            ("Ilo neden sadece Almanca konuşuyor?", [
                "Plapperland Almanca öğrenmek için yapılmıştır; çocuğun duyduğu ve gördüğü her şey Almancadır. Ebeveyn "
                "alanı iPad'in diline göre Almanca, İngilizce veya Türkçe gösterilir (diğer dillerde İngilizce).",
            ], False),
            ("Çocuğumun uygulamada kalmasını nasıl sağlarım?", [
                "Rehberli Erişim'i kullanın (Ayarlar › Erişilebilirlik › Rehberli Erişim). iPad, siz sonlandırana kadar Plapperland'de kalır.",
            ], False),
        ],
        "contact_h": "İletişim",
        "contact": f"E-posta: {MAIL}. Bir şey çalışmıyorsa lütfen iPad modelinizi ve iPadOS sürümünüzü belirtin.",
    },
}

NUM_CLASS = ' class="num"'
LANG_NAME = {"en": "English", "de": "Deutsch", "tr": "Türkçe"}


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def head(lang, page, title, desc):
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{url(l, page)}">' for l in LANGS)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{url(lang, page)}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}{url('en', page)}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#f2f4f1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0d1412" media="(prefers-color-scheme: dark)">
<link rel="preload" href="/assets/fonts/familjen-grotesk-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
</head>"""


def header(lang, page):
    u = UI[lang]
    home = url(lang, "home")
    switch = []
    for l in LANGS:
        if l == lang:
            switch.append(f'<span aria-current="true" lang="{l}" title="{LANG_NAME[l]}">{l.upper()}</span>')
        else:
            switch.append(f'<a href="{url(l, page)}" hreflang="{l}" lang="{l}" title="{LANG_NAME[l]}">{l.upper()}</a>')
    cur = ' aria-current="page"' if page == "imprint" else ""
    return f"""<body>
<a class="skip" href="#main">{u['skip']}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{home}"><span class="brand-word">by<b>tuna</b>soft</span><span class="brand-sub">{u['brand_sub']}</span></a>
    <nav class="nav" aria-label="Main">
      <a href="{home}#services">{u['nav_services']}</a>
      <a href="{home}#apps">{u['nav_apps']}</a>
      <a href="{home}#contact">{u['nav_contact']}</a>
      <a href="{url(lang, 'imprint')}"{cur}>{u['nav_imprint']}</a>
      <span class="lang" role="group" aria-label="{u['lang_label']}">{''.join(switch)}</span>
    </nav>
  </div>
</header>"""


def footer(lang):
    u = UI[lang]
    return f"""<footer class="site-footer">
  <div class="wrap">
    <p>© 2026 {COMPANY['legal']} · VKN {COMPANY['vkn']}<br>{u['footer_note']}</p>
    <nav aria-label="Legal">
      <a href="{url(lang, 'imprint')}">{u['nav_imprint']}</a>
      <a href="{url(lang, 'privacy')}">{u['privacy']}</a>
      <a href="{url(lang, 'support')}">{u['support']}</a>
    </nav>
  </div>
</footer>
</body>
</html>
"""


def render_home(lang):
    t = HOME[lang]
    reg = "\n".join(
        f'        <div><dt>{k}</dt><dd{NUM_CLASS if v == COMPANY["vkn"] else ""}>{v}</dd></div>'
        for k, v in t["reg"])
    services = "\n".join(
        f'        <li><span class="tag">{tag}</span><h3>{name}</h3><p>{text}</p></li>'
        for name, tag, text in t["services"])
    facts = "".join(f"<li>{f}</li>" for f in t["app_facts"])
    return f"""{head(lang, 'home', t['title'], t['desc'])}
{header(lang, 'home')}
<main id="main">
  <section class="hero">
    <div class="wrap">
      <div class="hero-copy">
        <span class="label">{t['eyebrow']}</span>
        <h1>{t['h1']}</h1>
        <p class="hero-lede">{t['lede']}</p>
      </div>
      <aside class="registry" aria-label="{t['reg_label']}">
        <span class="label">{t['reg_label']}</span>
        <dl>
{reg}
        </dl>
      </aside>
    </div>
  </section>

  <section class="section" id="services" aria-labelledby="services-h">
    <div class="wrap">
      <div class="section-head">
        <h2 id="services-h">{t['services_h']}</h2>
        <p>{t['services_p']}</p>
      </div>
      <ul class="services">
{services}
      </ul>
    </div>
  </section>

  <section class="section" id="apps" aria-labelledby="apps-h">
    <div class="wrap">
      <div class="section-head">
        <h2 id="apps-h">{t['apps_h']}</h2>
        <p>{t['apps_p']}</p>
      </div>
      <article class="app-card">
        <div class="app-body">
          <div class="app-id">
            <img src="/assets/img/plapperland-icon-256.png" width="72" height="72" alt="{t['icon_alt']}">
            <div><span class="label">{t['app_kicker']}</span><h3>{APP}</h3></div>
          </div>
          <p>{t['app_text']}</p>
          <ul class="facts">{facts}</ul>
          <p class="app-links"><a href="{url(lang, 'privacy')}">{t['app_privacy']}</a><a href="{url(lang, 'support')}">{t['app_support']}</a></p>
        </div>
        <div class="app-shots">
          <img src="/assets/img/plapperland-02-karte-1200.jpg" srcset="/assets/img/plapperland-02-karte-640.jpg 640w, /assets/img/plapperland-02-karte-1200.jpg 1200w" sizes="(max-width: 860px) 92vw, 560px" width="1200" height="900" alt="{t['shot1_alt']}" loading="lazy">
          <img class="second" src="/assets/img/plapperland-04-bauernhof-640.jpg" width="640" height="480" alt="{t['shot2_alt']}" loading="lazy">
        </div>
      </article>
    </div>
  </section>

  <section class="section" id="contact" aria-labelledby="contact-h">
    <div class="wrap">
      <div class="section-head">
        <h2 id="contact-h">{t['contact_h']}</h2>
        <p>{t['contact_p']}</p>
      </div>
      <div class="contact">
        <div class="block"><span class="label">{t['contact_mail_label']}</span><p class="contact-mail">{MAIL}</p></div>
        <div class="block"><span class="label">{t['contact_addr_label']}</span><address>{address_html(lang)}</address></div>
      </div>
    </div>
  </section>
</main>
{footer(lang)}"""


def doc_page(lang, page, title, desc, h1, body, aside):
    return f"""{head(lang, page, title, desc)}
{header(lang, page)}
<main id="main" class="doc">
  <div class="wrap doc-grid">
    <aside class="doc-aside">{aside}</aside>
    <article class="doc-main">
      <header>
        <h1>{h1}</h1>
        <p class="meta">{UI[lang]['updated']}: {UPDATED}</p>
      </header>
{body}
    </article>
  </div>
</main>
{footer(lang)}"""


def app_aside(lang):
    alt = HOME[lang]["icon_alt"]
    return (f'<img src="/assets/img/plapperland-icon-128.png" width="64" height="64" alt="{alt}">'
            f'<p><strong>{APP}</strong><br>{HOME[lang]["app_kicker"]}</p>')


def render_imprint(lang):
    t = IMPRINT[lang]
    rows = "\n".join(
        f'        <div><dt>{k}</dt><dd>{address_html(lang) if v is None else v}</dd></div>' for k, v in t["rows"])
    site = "\n".join(f"        <p>{p}</p>" for p in t["site"])
    body = f"""      <p>{t['intro']}</p>
      <dl class="record">
{rows}
      </dl>
      <section><h2>{t['resp_h']}</h2><p>{t['resp']}</p></section>
      <section>
        <h2>{t['site_h']}</h2>
{site}
      </section>
      <section><h2>{t['apps_h']}</h2><p>{t['apps']} <a href="{url(lang, 'privacy')}">{UI[lang]['privacy']}</a> · <a href="{url(lang, 'support')}">{UI[lang]['support']}</a></p></section>"""
    aside = f'<span class="label">{COMPANY["legal"].split()[0]}</span>'
    return doc_page(lang, "imprint", t["title"], t["desc"], t["h1"], body, aside)


def render_privacy(lang):
    t = PRIVACY[lang]
    parts = [f'      <p class="summary">{t["summary"]}</p>']
    for h, items in t["sections"]:
        lis = "".join(f"<li>{i}</li>" for i in items)
        parts.append(f"      <section><h2>{h}</h2><ul>{lis}</ul></section>")
    for key in ("children", "rights", "changes"):
        parts.append(f"      <section><h2>{t[key + '_h']}</h2><p>{t[key]}</p></section>")
    parts.append(f"      <section><h2>{t['controller_h']}</h2><p>{address_html(lang)}</p>"
                 f"<p>{IMPRINT[lang]['rows'][3][0]}: {COMPANY['director']} · {MAIL}</p></section>")
    return doc_page(lang, "privacy", t["title"], t["desc"], f'{t["h1"]}<br><span class="meta">{APP}</span>',
                    "\n".join(parts), app_aside(lang))


def render_support(lang):
    t = SUPPORT[lang]
    parts = [f"      <p>{t['intro']}</p>", '      <div class="faq">']
    for q, steps, ordered in t["faq"]:
        if ordered:
            inner = "<ol>" + "".join(f"<li>{s}</li>" for s in steps) + "</ol>"
        else:
            inner = "".join(f"<p>{s}</p>" for s in steps)
        parts.append(f"        <section><h2>{q}</h2>{inner}</section>")
    parts.append("      </div>")
    parts.append(f"      <section><h2>{t['contact_h']}</h2><p>{t['contact']}</p></section>")
    return doc_page(lang, "support", t["title"], t["desc"], f'{t["h1"]}<br><span class="meta">{APP}</span>',
                    "\n".join(parts), app_aside(lang))


RENDER = {"home": render_home, "imprint": render_imprint, "privacy": render_privacy, "support": render_support}


def main():
    written = []
    for lang in LANGS:
        for page, fn in RENDER.items():
            out = ROOT / url(lang, page).lstrip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fn(lang), encoding="utf-8")
            written.append(out.relative_to(ROOT))
    urls = "".join(f"  <url><loc>{SITE}{url(l, p)}</loc><lastmod>{UPDATED}</lastmod></url>\n" for l in LANGS for p in PAGES)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n',
        encoding="utf-8")
    print("\n".join(str(p) for p in written))


if __name__ == "__main__":
    main()
