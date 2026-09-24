"""Phases, workouts and the 30 daily pages (Turkish copy)."""

PHASES = [
    {
        "n": 1, "days": (1, 7), "name": "TEMELLERİ OLUŞTUR",
        "lead": "İlk hafta her şeyi değiştirme haftası değil. Temeli kuruyorsun: düzenli öğünler, "
                "su, daha fazla hareket ve ilk antrenmanlar.",
        "goals": ["Başlangıç noktanı anla", "Öğünlerine düzen ver", "Su rutini kur",
                  "Günlük hareketi artır", "İlk basit alışkanlıkları başlat", "İlk antrenmanları yap"],
        "habits": ["Hareket hedefi", "Su", "Protein", "Sebze", "Tabak modeli"],
        "note": "İlk günlerde kaslarında hafif bir ağrı olabilir. Bu normaldir ve genelde "
                "birkaç gün içinde azalır.",
    },
    {
        "n": 2, "days": (8, 14), "name": "RUTİNİ GÜÇLENDİR",
        "lead": "Temel hazır. Şimdi yapıyı sağlamlaştırıyorsun: porsiyonlar, planlama ve "
                "düzenli antrenman.",
        "goals": ["Beslenmeni daha iyi yapılandır", "Porsiyonlarını kontrol et",
                  "Protein ve sebzeyi her öğüne yerleştir", "Hareketi artır",
                  "Antrenmanı düzenli yap", "İlk ilerlemeleri gözlemle"],
        "habits": ["El ölçüsü", "Sıvı kaloriler", "Yavaş yemek", "Alışveriş listesi", "Hazırlık"],
        "note": "Antrenmanlarda set sayısı 3'e çıkıyor. Zor gelirse 2 sette kal; "
                "düzenli yapmak, fazla yapmaktan daha önemli.",
    },
    {
        "n": 3, "days": (15, 21), "name": "SÜREKLİLİĞİ ARTIR",
        "lead": "Plan artık tanıdık. Bu hafta, gerçek hayatın zor anlarına hazırlanıyorsun: "
                "ani yeme istekleri, davetler, yorgun günler.",
        "goals": ["Ani yeme isteklerini anla", "Günlük hayattaki zor durumları yönet",
                  "Dışarıda yemek için plan yap", "Motivasyon düşüşlerine hazırlan",
                  "Disiplini sisteme bağla", "Hareket ve antrenmanı sürdür"],
        "habits": ["10 dakika kuralı", "Uyku rutini", "Dışarıda yemek planı", "En kötü gün planı"],
        "note": "Bu fazda squat, şınav ve lunge hareketlerinde iniş 3 saniye sürüyor. "
                "Daha yavaş, daha kontrollü.",
    },
    {
        "n": 4, "days": (22, 30), "name": "SİSTEMİ OTURT",
        "lead": "Son faz. Öğrendiklerini kalıcı hale getiriyor ve 30. günden sonrası için "
                "kendi sistemini kuruyorsun.",
        "goals": ["Alışkanlıklarını sabitle", "İlerlemeni değerlendir",
                  "Geri adımları doğru yorumla", "Uzun vadeli beslenme planı",
                  "Uzun vadeli hareket planı", "Uzun vadeli antrenman rutini",
                  "30. günden sonrasına hazırlan"],
        "habits": ["Alışkanlık zinciri", "Hafta sonu planı", "Tokluk ölçeği", "Devam planı"],
        "note": "Bu fazda 4 set yapabilirsin. Zor gelirse 3 sette kal; ilerleme yine devam eder.",
    },
]

# Workouts per phase. rows: (exercise, prescription)
WORKOUTS = {
    ("A", 1): {"rest": "60–90 sn", "rows": [("Squat", "2 × 10"), ("Şınav (kolay versiyon)", "2 × 8"),
                                            ("Çekiş", "2 × 10"), ("Kalça köprüsü", "2 × 12"),
                                            ("Plank", "2 × 20 sn")]},
    ("B", 1): {"rest": "60–90 sn", "rows": [("Geriye adım lunge", "2 × 8 her bacak"), ("Çekiş", "2 × 10"),
                                            ("Şınav (kolay versiyon)", "2 × 8"), ("Dead bug", "2 × 6 her taraf"),
                                            ("Duvar oturuşu", "2 × 20 sn")]},
    ("A", 2): {"rest": "60–75 sn", "rows": [("Squat", "3 × 12"), ("Şınav", "3 × 8–10"),
                                            ("Çekiş", "3 × 12"), ("Kalça köprüsü", "3 × 15"),
                                            ("Plank", "3 × 25 sn")]},
    ("B", 2): {"rest": "60–75 sn", "rows": [("Geriye adım lunge", "3 × 10 her bacak"), ("Çekiş", "3 × 12"),
                                            ("Şınav", "3 × 8–10"), ("Dead bug", "3 × 8 her taraf"),
                                            ("Duvar oturuşu", "3 × 30 sn")]},
    ("A", 3): {"rest": "60 sn", "rows": [("Squat (3 sn iniş)", "3 × 12"), ("Şınav (3 sn iniş)", "3 × 10"),
                                         ("Çekiş (üstte 1 sn sık)", "3 × 12"), ("Kalça köprüsü (üstte 2 sn)", "3 × 15"),
                                         ("Plank", "3 × 30 sn")]},
    ("B", 3): {"rest": "60 sn", "rows": [("Geriye adım lunge (3 sn iniş)", "3 × 12 her bacak"),
                                         ("Çekiş (üstte 1 sn sık)", "3 × 12"), ("Şınav (3 sn iniş)", "3 × 10"),
                                         ("Dead bug", "3 × 10 her taraf"), ("Duvar oturuşu", "3 × 40 sn")]},
    ("A", 4): {"rest": "60 sn", "rows": [("Squat", "4 × 12"), ("Şınav", "4 × 10"),
                                         ("Çekiş", "4 × 12"), ("Kalça köprüsü", "3 × 15"),
                                         ("Plank", "3 × 40 sn")]},
    ("B", 4): {"rest": "60 sn", "rows": [("Geriye adım lunge", "3 × 12 her bacak"), ("Çekiş", "4 × 12"),
                                         ("Şınav", "3 × 10–12"), ("Dead bug", "3 × 10 her taraf"),
                                         ("Duvar oturuşu", "3 × 45 sn")]},
}


def workout(letter, phase, note=None, extra=None):
    w = WORKOUTS[(letter, phase)]
    return {"kind": "strength", "name": f"Antrenman {letter}", "type": "Tüm vücut kuvvet",
            "rest": w["rest"], "rows": w["rows"], "note": note, "extra": extra}


def recovery(label, text):
    return {"kind": "recovery", "name": label, "text": text}


MOBILITY_TEXT = "10 dakikalık mobilite rutini (s. {p:isinma})."

DAYS = [
    # ------------------------------------------------------------------ FAZ 1
    {
        "n": 1, "title": "Başlangıç noktanı belirle",
        "focus": "Bugün hiçbir şeyi mükemmel yapmaya çalışmıyorsun. Sadece nerede olduğunu görüyorsun: "
                 "ölçülerini alıyor ve normal bir gününü gözlemliyorsun.",
        "nutrition": "3 ana öğün düzeni kur ve yediklerini not et ya da fotoğrafla. Yargılamadan, sadece gözlemle.",
        "meals": [
            ("Kahvaltı", "2 haşlanmış yumurta, 1 dilim tam buğday ekmeği, domates, salatalık, 5 zeytin"),
            ("Öğle", "1 kase mercimek çorbası, 1 avuç içi ızgara tavuk, bol yeşil salata"),
            ("Ara öğün", "1 elma ve 10 çiğ badem (acıkırsan)"),
            ("Akşam", "Tavuk sote (1 avuç içi tavuk, biber, domates, soğan), 1 yumruk bulgur pilavı, 1 kase yoğurt"),
        ],
        "movement": ("20 dakika yürüyüş",
                     "Telefonun veya saatin adım sayıyorsa bugünkü adım sayını not et. Bu senin başlangıç değerin."),
        "training": recovery("Antrenman yok",
                             "İstersen s. {p:isinma:deki} ısınma hareketlerini bir kez dene ve hareketleri tanı."),
        "tip": "İlk gün her şeyi değiştirmeye çalışma. Büyük başlangıçlar genelde çabuk biter, "
               "küçük başlangıçlar devam eder.",
        "task": "İlerleme Tablosu'nda (s. {p:ilerleme}) Gün 1 sütununu doldur: kilo, bel çevresi ve bugünkü adım sayısı.",
    },
    {
        "n": 2, "title": "Su rutinini kur",
        "focus": "Bugünün odağı su. Gün boyunca düzenli su içmek, en basit ama en sık unutulan alışkanlıklardan biri.",
        "nutrition": "Her öğünle birlikte 1 bardak su iç. Şekerli içecekleri bugün suyla değiştirmeyi dene.",
        "meals": [
            ("Kahvaltı", "Yulaf kasesi: 4 yemek kaşığı yulaf (40 g), 1 kase yoğurt, yarım muz, tarçın"),
            ("Öğle", "Ton balıklı salata: 1 kutu süzülmüş ton balığı, yarım su bardağı haşlanmış nohut, "
                     "marul, domates, salatalık, limon, 1 tatlı kaşığı zeytinyağı"),
            ("Ara öğün", "1 bardak ayran ve 1 mandalina"),
            ("Akşam", "Fırında derisiz tavuk but (1 avuç içi), fırın sebze (kabak, biber, havuç), 1 orta boy haşlanmış patates"),
        ],
        "movement": ("20 dakika yürüyüş", "Antrenmandan ayrı bir zamanda, örneğin öğle arasında."),
        "training": workout("A", 1, note="İlk antrenman: Tekniği öğrenmeye odaklan. Hareketleri s. {p:egzersiz:den} kontrol et."),
        "tip": "Suyu görebileceğin bir yere koy. Masandaki bir şişe, çoğu zaman en iyi hatırlatıcıdır.",
        "task": "Bir su şişesi hazırla ve gün boyunca yaklaşık 8 bardak su içmeyi hedefle.",
    },
    {
        "n": 3, "title": "Her ana öğünde protein",
        "focus": "Protein uzun süre tok kalmana yardımcı olabilir ve kaslarının korunmasını destekler. Bugün her ana öğüne bir protein kaynağı ekliyorsun.",
        "nutrition": "Kahvaltı, öğle ve akşam: Her tabakta yumurta, yoğurt, peynir, tavuk, balık, et veya baklagil olsun.",
        "meals": [
            ("Kahvaltı", "Peynirli omlet: 2 yumurta, 1 kibrit kutusu beyaz peynir, 1 avuç ıspanak; 1 dilim tam buğday ekmeği"),
            ("Öğle", "1 kase kuru fasulye, yarım yumruk pirinç pilavı veya 1 dilim ekmek, cacık"),
            ("Ara öğün", "1 kase süzme yoğurt veya skyr, birkaç çilek"),
            ("Akşam", "Izgara köfte (1 avuç içi, 4–5 adet), piyaz veya çoban salata"),
        ],
        "movement": ("25 dakika yürüyüş", "Ardından 10 dakika mobilite."),
        "training": recovery("Aktif toparlanma", MOBILITY_TEXT),
        "tip": "Protein kaynakları: yumurta, yoğurt, kefir, beyaz peynir, lor, tavuk, hindi, balık, "
               "ton balığı, kırmızı et, mercimek, nohut, fasulye. Her ana öğünde bu listeden en az birini seç.",
        "task": "Yarınki üç ana öğün için protein kaynaklarını şimdiden seç ve not et.",
    },
    {
        "n": 4, "title": "Günlük hareketi artır",
        "focus": "Antrenman dışındaki hareket de önemlidir. Bugün gününe küçük hareket molaları ekliyorsun.",
        "nutrition": "Her ana öğünde protein devam ediyor. Tatlı isteğinde önce bir meyve dene.",
        "meals": [
            ("Kahvaltı", "Kahvaltı tabağı: 2 yumurta, 1 kibrit kutusu beyaz peynir, domates, salatalık, yeşillik, 1 dilim tam buğday ekmeği"),
            ("Öğle", "Tavuk dürüm: 1 tam buğday lavaş, 1 avuç içi tavuk, marul, domates, yoğurtlu sos"),
            ("Ara öğün", "Havuç ve salatalık çubukları, 2 yemek kaşığı humus"),
            ("Akşam", "Fırında somon veya levrek (1 avuç içi), buharda brokoli, 1 yumruk bulgur pilavı"),
        ],
        "movement": ("25 dakika yürüyüş + 3 hareket molası",
                     "Her 1–2 saatte bir 3–5 dakika kalk: merdiven çık, ayakta telefon görüşmesi yap, kısa bir tur at."),
        "training": workout("B", 1),
        "tip": "Asansör yerine merdiven, kısa mesafede araç yerine yürüyüş. Küçük seçimler gün sonunda fark yaratır.",
        "task": "Telefonuna 3 hatırlatıcı kur: 11.00, 15.00 ve 18.00'de kısa bir hareket molası.",
    },
    {
        "n": 5, "title": "Sebzeyi çoğalt",
        "focus": "Sebzeler hacimlidir, lif içerir ve tabağını doyurucu yapar. Bugün en az iki öğünde sebze var.",
        "nutrition": "Öğle ve akşam yemeğinde tabağının yaklaşık yarısını sebzeyle doldur.",
        "meals": [
            ("Kahvaltı", "Menemen (2 yumurta, domates, biber), 1 dilim tam buğday ekmeği, salatalık"),
            ("Öğle", "Büyük bir porsiyon zeytinyağlı taze fasulye, 1 kase yoğurt, 1 dilim tam buğday ekmeği"),
            ("Ara öğün", "1 armut ve 1 kibrit kutusu beyaz peynir"),
            ("Akşam", "Az yağlı kıymalı ıspanak, 1 kase yoğurt, yarım yumruk pirinç pilavı veya 1 dilim ekmek"),
        ],
        "movement": ("30 dakika yürüyüş", "Ardından 10 dakika mobilite."),
        "training": recovery("Aktif toparlanma",
                             "Dünkü antrenmandan sonra kasların hafifçe ağrıyabilir. " + MOBILITY_TEXT),
        "tip": "Hazır sebze, iyi niyetten daha etkilidir. Doğranmış havuç, salatalık ve domates buzdolabının ön rafında dursun.",
        "task": "Buzdolabına 2–3 günlük hazır sebze hazırla: yıka, doğra, bir kaba koy.",
    },
    {
        "n": 6, "title": "Tabağını kur",
        "focus": "Tabak modeli, kalori saymadan porsiyonlarını dengelemenin en kolay yolu: yarısı sebze, "
                 "çeyreği protein, çeyreği karbonhidrat.",
        "nutrition": "Bugün öğle ve akşam yemeğini tabak modeline göre hazırla (s. {p:tabak}).",
        "meals": [
            ("Kahvaltı", "Süzme yoğurt kasesi: 1 kase süzme yoğurt veya skyr, 1 avuç meyve, 1 yemek kaşığı yulaf, 2 ceviz içi"),
            ("Öğle", "1 avuç içi ızgara tavuk, 1 yumruk bulgur pilavı, tabağın yarısı çoban salata"),
            ("Ara öğün", "1 haşlanmış yumurta ve 1 meyve"),
            ("Akşam", "1 kase etli nohut, tabağın yarısı mevsim salatası, 1 kase cacık"),
        ],
        "movement": ("25 dakika yürüyüş", "Rahat bir tempoda; sohbet edebilmelisin."),
        "training": workout("A", 1, note="Hareketler artık daha tanıdık. Aynı set ve tekrarlarla, daha iyi teknikle yap."),
        "tip": "Daha küçük bir tabak kullan. Tabak dolu görünür, porsiyon makul kalır.",
        "task": "Tabak modeline göre hazırladığın bir öğünün fotoğrafını çek. Sonraki günlerde örnek olarak kullan.",
    },
    {
        "n": 7, "title": "İlk haftanı değerlendir",
        "focus": "Bir hafta tamamlandı. Bugün kendine not vermiyorsun; sadece neyin işe yaradığına bakıyorsun.",
        "nutrition": "Hafta sonu da olsa öğün düzenini koru. Dışarıda yiyeceksen bir protein ve bir sebze seç.",
        "meals": [
            ("Kahvaltı", "2 yumurta (haşlanmış veya menemen), 1 kibrit kutusu beyaz peynir, 5 zeytin, bol yeşillik, 1–2 dilim tam buğday ekmeği"),
            ("Öğle", "1 kase mercimek çorbası, 1 kase yoğurt, mevsim salatası, 1 dilim ekmek"),
            ("Ara öğün", "1 bardak kefir ve birkaç dilim meyve"),
            ("Akşam", "Fırında köfte (1 avuç içi) ve sebze (kabak, biber, domates), 1 orta boy patates"),
        ],
        "movement": ("40 dakika uzun yürüyüş", "Parkta, sahilde veya doğada; konuşabileceğin bir tempoda."),
        "training": recovery("Dinlenme günü", "Kasların antrenmanlar arasında toparlanarak güçlenir."),
        "tip": "İlerleme sadece tartıdaki sayı değildir. Enerjin, uykun, merdivende nefesin ve kıyafetlerin de ilerlemenin parçası.",
        "task": "1. Hafta Değerlendirmesi'ni (s. {p:hafta1}) doldur ve İlerleme Tablosu'na Gün 7 değerlerini yaz.",
    },
    # ------------------------------------------------------------------ FAZ 2
    {
        "n": 8, "title": "Porsiyonları elinle ölç",
        "focus": "Terazi ya da uygulama gerekmiyor: Avuç içi, yumruk ve başparmak her zaman yanında. "
                 "Bugün porsiyonlarını elinle ölçüyorsun.",
        "nutrition": "Her ana öğünde: 1 avuç içi protein, 1 yumruk karbonhidrat, 2 avuç sebze, 1 başparmak yağ (s. {p:tabak}).",
        "meals": [
            ("Kahvaltı", "Yulaf kasesi: 40 g yulaf, 1 kase yoğurt, 1 avuç çilek veya yaban mersini, 1 başparmak kadar ceviz"),
            ("Öğle", "Tavuk sote (1 avuç içi), 1 yumruk bulgur pilavı, 2 avuç salata"),
            ("Ara öğün", "1 bardak kefir ve 1 elma"),
            ("Akşam", "Izgara hindi veya tavuk göğsü (1 avuç içi), 1 yumruk fırın patates, 2 avuç buharda sebze, 1 tatlı kaşığı zeytinyağı"),
        ],
        "movement": ("7.000 adım veya 35 dakika yürüyüş", "Başlangıç ortalaman çok düşükse, ona yaklaşık 1.000 adım ekle."),
        "training": workout("A", 2, note="Yeni faz: Set sayısı 3'e çıkıyor."),
        "tip": "Porsiyonunu yemeğe başlamadan tabağına koy. Tencere veya servis tabağı masada durmasın.",
        "task": "Bugün üç ana öğünü el ölçüsüyle hazırla. Hangi porsiyonun alıştığından farklı olduğunu not et.",
    },
    {
        "n": 9, "title": "İçtiklerine dikkat et",
        "focus": "Şekerli içecekler, meyve suları ve şekerli kahveler fark ettirmeden çok enerji ekleyebilir. "
                 "Bugün ne içtiğine bakıyorsun.",
        "nutrition": "Bugünün içecekleri: su, maden suyu, sade çay, sade kahve ve ayran. Çaya şeker atıyorsan yarıya indir.",
        "meals": [
            ("Kahvaltı", "Menemen (2 yumurta), 1 kibrit kutusu beyaz peynir, 1 dilim tam buğday ekmeği, salatalık"),
            ("Öğle", "6 adet mercimek köftesi, bol yeşillik ve limon, 1 kase yoğurt"),
            ("Ara öğün", "1 avuç sade leblebi ve 1 bardak ayran"),
            ("Akşam", "Fırında somon (1 avuç içi), 1 yumruk bulgur veya pirinç pilavı, roka salatası"),
        ],
        "movement": ("35 dakika tempolu yürüyüş",
                     "10 dk rahat + 5 × (2 dk tempolu, 2 dk rahat) + 5 dk rahat. Tempolu kısımda konuşabilirsin ama şarkı söyleyemezsin."),
        "training": recovery("Kardiyo günü", "Bugün kuvvet antrenmanı yok; tempolu yürüyüş senin kardiyo antrenmanın."),
        "tip": "Meyve suyu yerine meyvenin kendisini ye. İçindeki lif sayesinde daha tok tutar.",
        "task": "Bugün içtiğin her şeyi yaz. Akşam şekerli olanları işaretle ve yarın birini değiştir.",
    },
    {
        "n": 10, "title": "Yavaş ye",
        "focus": "Tokluk sinyalinin beynine ulaşması biraz zaman alır. Bugün en az bir öğünü 20 dakikaya yayıyorsun.",
        "nutrition": "Lokmalar arasında çatalını bırak. Yemek sırasında telefon ve ekran yok.",
        "meals": [
            ("Kahvaltı", "2 haşlanmış yumurta, 2 yemek kaşığı lor peyniri, domates, salatalık, yeşillik, 1 dilim tam buğday ekmeği"),
            ("Öğle", "Tavuklu bulgur salatası: 1 avuç içi tavuk, 1 yumruk bulgur, domates, salatalık, maydanoz, limon"),
            ("Ara öğün", "1 kase süzme yoğurt, tarçın"),
            ("Akşam", "Etli kabak veya etli bamya (1 avuç içi et), 1 kase yoğurt, 1 dilim ekmek"),
        ],
        "movement": ("7.000 adım veya 35 dakika yürüyüş", "Yemekten sonra 10 dakikalık kısa bir yürüyüş de sayılır."),
        "training": workout("B", 2),
        "tip": "Öğüne salata veya çorbayla başla. Böylece ana yemeği daha sakin yersin.",
        "task": "Akşam yemeğinde bir zamanlayıcı kur ve yemeği en az 20 dakikaya yay.",
    },
    {
        "n": 11, "title": "Alışverişini planla",
        "focus": "Evde ne varsa onu yersin. Bugün plana uygun bir alışveriş listesi hazırlıyorsun.",
        "nutrition": "Alışverişe tok git ve listeye sadık kal. Temel liste s. {p:alisveris:de}.",
        "meals": [
            ("Kahvaltı", "Yulaf lapası: 40 g yulafı 1 su bardağı sütle pişir, yarım muz ve tarçın ekle; yanında 1 haşlanmış yumurta"),
            ("Öğle", "Dünden kalan akşam yemeği veya ton balıklı salata, bol yeşillik"),
            ("Ara öğün", "Havuç çubukları ve 2 yemek kaşığı humus"),
            ("Akşam", "1 kase kırmızı mercimek yemeği, 1 yumruk bulgur pilavı, 1 kase yoğurt, salata"),
        ],
        "movement": ("7.000 adım", "Ardından 10 dakika mobilite."),
        "training": recovery("Aktif toparlanma", MOBILITY_TEXT),
        "tip": "Markette önce sebze, meyve, et ve süt ürünleri reyonlarına git. Paketli atıştırmalıklar listende yoksa sepetine de girmesin.",
        "task": "Önümüzdeki 3–4 gün için bir alışveriş listesi yaz ve alışverişi yap.",
    },
    {
        "n": 12, "title": "Önceden hazırla",
        "focus": "Yorgun akşamlar en zor anlardır. Bugün 2–3 öğünlük yemeği önceden hazırlıyorsun.",
        "nutrition": "Bir tencere protein, bir tencere tahıl ve bir tepsi fırın sebze: Birkaç günün temeli hazır.",
        "meals": [
            ("Kahvaltı", "Peynirli omlet (2 yumurta, 1 kibrit kutusu peynir, biber), domates, 1 dilim tam buğday ekmeği"),
            ("Öğle", "Hazırladığın tavuk (1 avuç içi), 1 yumruk bulgur, fırın sebze"),
            ("Ara öğün", "1 bardak kefir ve 1 avuç çilek"),
            ("Akşam", "Fırında köfte (1 avuç içi), fırın sebze ve patates, cacık"),
        ],
        "movement": ("7.000 adım veya 35 dakika yürüyüş", "Adımlarını gün içine yay: sabah, öğle ve akşam."),
        "training": workout("A", 2),
        "tip": "Hazırlığı sabit bir zamana bağla: örneğin her pazar ve çarşamba akşamı 45 dakika.",
        "task": "En az 2 öğünlük protein ve tahıl pişir, porsiyonlara ayır ve buzdolabına koy.",
    },
    {
        "n": 13, "title": "Atıştırmalıkları bilinçli seç",
        "focus": "Atıştırmak yasak değil. Amaç, ne zaman ve ne atıştırdığını bilinçli seçmek.",
        "nutrition": "Gerçekten acıktığında ara öğün: protein ve lif birlikte. Paketli atıştırmalıklar yerine hazır alternatifler.",
        "meals": [
            ("Kahvaltı", "1 kase süzme yoğurt, 1 avuç meyve, 1 yemek kaşığı yulaf, isteğe bağlı 1 tatlı kaşığı bal"),
            ("Öğle", "1 kase mercimek çorbası, 1 avuç içi ızgara tavuk, çoban salata"),
            ("Ara öğün", "1 elma ve 10 badem veya 1 haşlanmış yumurta ve salatalık"),
            ("Akşam", "Ton balıklı tam buğday makarna (1 yumruk makarna, yarım kutu ton balığı, domates sosu), bol yeşil salata"),
        ],
        "movement": ("45 dakika uzun yürüyüş", "Parkta, sahilde veya doğada; istersen biriyle birlikte."),
        "training": recovery("Dinlenme günü", "Uzun yürüyüş bugünkü aktif toparlanman."),
        "tip": "Atıştırmalıkları görünmeyen bir yere, meyveyi göz hizasına koy. Çevren, iradenden daha güçlüdür.",
        "task": "Evde 3 hazır, sağlıklı atıştırmalık hazırla (ör. yoğurt, meyve, haşlanmış yumurta) ve paketli olanları dolaba kaldır.",
    },
    {
        "n": 14, "title": "İlk ilerlemeleri gör",
        "focus": "İki hafta tamamlandı. Bugün ölçülerini alıyor ve neyin değiştiğine bakıyorsun.",
        "nutrition": "Normal bir plan günü. Hafta sonu yemeklerinde tabak modelini hatırla.",
        "meals": [
            ("Kahvaltı", "Menemen (2 yumurta), 1 kibrit kutusu beyaz peynir, 5 zeytin, bol yeşillik, 1 dilim ekmek"),
            ("Öğle", "1 kase etli kuru fasulye, yarım yumruk pirinç pilavı, cacık"),
            ("Ara öğün", "1 bardak ayran ve 1 mandalina"),
            ("Akşam", "Fırında tavuk ve sebze, 1 orta boy patates"),
        ],
        "movement": ("20–30 dakika hafif yürüyüş", "Ardından 10 dakika mobilite."),
        "training": recovery("Dinlenme günü", MOBILITY_TEXT),
        "tip": "Değişim her hafta aynı hızda olmaz. Tartı bir hafta yerinden oynamazken bel ölçün azalabilir. Birkaç ölçüye birlikte bak.",
        "task": "2. Hafta Değerlendirmesi'ni (s. {p:hafta2}) doldur ve İlerleme Tablosu'na Gün 14 değerlerini yaz.",
    },
    # ------------------------------------------------------------------ FAZ 3
    {
        "n": 15, "title": "Açlık mı, istek mi?",
        "focus": "Her yeme isteği açlık değildir. Bugün fiziksel açlığı ani yeme isteğinden ayırt etmeyi öğreniyorsun.",
        "nutrition": "10 dakika kuralı: Ani bir istek geldiğinde 10 dakika bekle ve bir bardak su iç. "
                     "İstek hâlâ oradaysa küçük bir porsiyonu bilerek seç.",
        "meals": [
            ("Kahvaltı", "Yulaf kasesi: 40 g yulaf, 1 kase yoğurt, 1 avuç meyve, 1 yemek kaşığı fındık"),
            ("Öğle", "Tavuk dürüm (tam buğday lavaş, 1 avuç içi tavuk, sebze, yoğurtlu sos), 1 bardak ayran"),
            ("Ara öğün", "1 kase süzme yoğurt veya 1 haşlanmış yumurta ve 1 meyve"),
            ("Akşam", "Izgara balık (1 avuç içi), 1 yumruk bulgur pilavı, roka ve domates salatası"),
        ],
        "movement": ("8.000 adım veya 40 dakika yürüyüş", "Başlangıç ortalaman düşükse, önceki haftana yaklaşık 1.000 adım ekle."),
        "training": workout("A", 3, note="Yeni faz: İnişi 3 saniyede yap. Daha yavaş olunca daha zor, ama daha kontrollü."),
        "tip": "Fiziksel açlık yavaş gelir ve birçok yiyecek onu giderir. Ani istek aniden gelir ve genelde belirli bir yiyecek ister.",
        "task": "Bugün ani bir yeme isteği yaşarsan saatini, ne istediğini ve o an nasıl hissettiğini (sıkılmış, yorgun, stresli) not et.",
    },
    {
        "n": 16, "title": "Uyku ve iştah",
        "focus": "Kötü uyuduğun gecelerin ertesinde daha çok acıktığını fark ettin mi? Bugün bir uyku rutini başlatıyorsun.",
        "nutrition": "Akşam yemeğini yatmadan 2–3 saat önce bitir. Öğleden sonra kahve ve enerji içeceği yok.",
        "meals": [
            ("Kahvaltı", "2 yumurta, 1 kibrit kutusu beyaz peynir, domates, salatalık, 1 dilim tam buğday ekmeği"),
            ("Öğle", "1 kase nohut yemeği veya nohutlu ıspanak, 1 kase yoğurt, 1 dilim ekmek"),
            ("Ara öğün", "1 elma ve 10 badem"),
            ("Akşam", "Tavuk sote (1 avuç içi), buharda sebze, yarım yumruk pirinç pilavı"),
        ],
        "movement": ("40 dakika tempolu yürüyüş", "10 dk rahat + 6 × (2 dk tempolu, 2 dk rahat) + 6 dk rahat."),
        "training": recovery("Kardiyo günü", "Bugün kuvvet antrenmanı yok; tempolu yürüyüş senin kardiyo antrenmanın."),
        "tip": "Her gün aynı saatte yatıp kalkmak, uykunu desteklemenin en basit yolu. Hafta sonu bile fark 1 saati geçmesin.",
        "task": "Bu akşam için bir yatma saati belirle ve yatmadan 30 dakika önce ekranları kapat.",
    },
    {
        "n": 17, "title": "Dışarıda yemek",
        "focus": "Restoran, lokanta ya da iş yemeği: Planın dışarıda da işe yarar. Bugün dışarıda yemek için basit bir strateji kuruyorsun.",
        "nutrition": "Menüde önce proteini seç (ızgara, fırın, haşlama), sonra sebzeyi. Ekmek ve pilavdan birini seç.",
        "meals": [
            ("Kahvaltı", "Menemen (2 yumurta), 1 dilim tam buğday ekmeği, salatalık"),
            ("Öğle", "Lokantada: ızgara köfte veya tavuk şiş, çoban salata, yarım porsiyon pilav; yanında ayran"),
            ("Ara öğün", "1 bardak kefir"),
            ("Akşam", "Fırında sebzeli tavuk (1 avuç içi), 1 kase yoğurt"),
        ],
        "movement": ("8.000 adım veya 40 dakika yürüyüş", "Dışarıda yiyorsan dönüşte bir durak önce in ve yürü."),
        "training": workout("B", 3),
        "tip": "Porsiyon büyükse yarısını en başta ayır ve paket yaptır. Yemeğe başlamadan karar vermek, açken karar vermekten kolaydır.",
        "task": "Sık gittiğin 2 yer için “benim siparişim”i belirle ve not et.",
    },
    {
        "n": 18, "title": "Davetler ve misafirlik",
        "focus": "Aile yemekleri, çay saatleri, bayram ziyaretleri: Sosyal ortamlar hayatın bir parçası. "
                 "Bugün onlara nasıl hazırlanacağını planlıyorsun.",
        "nutrition": "Davete çok aç gitme; öncesinde proteinli küçük bir ara öğün ye. Sofrada önce salata ve protein al, "
                     "tatlıdan küçük bir porsiyon seç.",
        "meals": [
            ("Kahvaltı", "1 kase süzme yoğurt, 1 avuç meyve, 1 yemek kaşığı yulaf"),
            ("Öğle", "Hazırladığın tavuk ve bulgur, bol salata"),
            ("Ara öğün", "Davetten önce: 1 haşlanmış yumurta ve salatalık"),
            ("Akşam", "Davette: tabağın yarısı salata ve sebze, bir protein (et, tavuk, köfte), 1–2 kaşık pilav veya börek; tatlıdan küçük bir porsiyon"),
        ],
        "movement": ("8.000 adım", "Ardından 10 dakika mobilite."),
        "training": recovery("Aktif toparlanma", MOBILITY_TEXT),
        "tip": "“Çok lezzetliydi, gerçekten doydum” demek kaba değildir. İkinci tabak ısrarında bir çay istemek de bir seçenek.",
        "task": "Önümüzdeki hafta bir davet veya buluşman varsa, planını 2 cümleyle yaz.",
    },
    {
        "n": 19, "title": "Motivasyon düştüğünde",
        "focus": "Motivasyon her gün aynı değildir ve bu normal. Bu yüzden bugün “en kötü gün planı”nı hazırlıyorsun.",
        "nutrition": "Yorgunsan en basit öğünü seç: yumurta, yoğurt, hazır salata. Basit bir öğün de planın bir parçası.",
        "meals": [
            ("Kahvaltı", "2 haşlanmış yumurta, 1 dilim tam buğday ekmeği, domates ve salatalık"),
            ("Öğle", "1 kase mercimek çorbası, ton balıklı salata"),
            ("Ara öğün", "1 kase yoğurt ve 1 meyve"),
            ("Akşam", "Sebzeli omlet (2–3 yumurta), bol salata, 1 dilim ekmek"),
        ],
        "movement": ("8.000 adım veya 40 dakika yürüyüş", "Canın istemiyorsa 10 dakikayla başla; çoğu zaman devamı gelir."),
        "training": workout("A", 3, extra="Bitiriş (isteğe bağlı): 3 tur × 30 sn tempolu yerinde yürüyüş, 30 sn dinlenme."),
        "tip": "Motivasyonu bekleme, başlamayı kolaylaştır. Spor kıyafetini akşamdan hazırlamak, sabahki “yapayım mı?” tartışmasını kısaltır.",
        "task": "En kötü gün planını yaz: Çok yorgun olduğun bir günde yapacağın en küçük 3 adım "
                "(ör. 10 dk yürüyüş, proteinli bir öğün, 8 bardak su).",
    },
    {
        "n": 20, "title": "Bir öğün planı bozmaz",
        "focus": "Bir öğün planın dışında kalabilir. Önemli olan, bir sonraki öğünde normale dönmek. "
                 "Bugün “ya hep ya hiç” düşüncesini bırakıyorsun.",
        "nutrition": "Plan dışı bir şey yediysen telafi etmek için öğün atlama. Bir sonraki öğünü normal planına göre ye.",
        "meals": [
            ("Kahvaltı", "Peynirli omlet (2 yumurta), domates, 1 dilim tam buğday ekmeği"),
            ("Öğle", "1 kase etli nohut, yarım yumruk pirinç pilavı, cacık"),
            ("Ara öğün", "1 avuç sade leblebi ve 1 mandalina"),
            ("Akşam", "Fırında somon veya levrek (1 avuç içi), 1 yumruk fırın patates, yeşil salata"),
        ],
        "movement": ("45–60 dakika uzun yürüyüş", "Yeni bir güzergâh dene: farklı bir park ya da mahalle."),
        "training": recovery("Dinlenme günü", "Uzun yürüyüş bugünkü aktif toparlanman."),
        "tip": "Bir dilim pasta planı bozmaz. “Zaten bozuldu” deyip bütün günü bırakmak bozar. Tek bir öğün, 30 günün çok küçük bir parçası.",
        "task": "Şu cümleyi yaz ve görebileceğin bir yere koy: “Bir öğün kötü gitse de bir sonraki öğünde devam ederim.”",
    },
    {
        "n": 21, "title": "Üçüncü haftayı değerlendir",
        "focus": "Üç hafta geride kaldı. Bugün neyin artık alışkanlığa dönüştüğüne bakıyorsun.",
        "nutrition": "Normal bir plan günü. Bu hafta en çok zorlandığın öğünü bugün önceden planla.",
        "meals": [
            ("Kahvaltı", "Yulaf lapası (40 g yulaf, süt), 1 avuç meyve, 1 haşlanmış yumurta"),
            ("Öğle", "Tavuklu salata: 1 avuç içi tavuk, yeşillik, nohut, zeytinyağı ve limon"),
            ("Ara öğün", "1 bardak ayran ve 1 elma"),
            ("Akşam", "Kıymalı sebze yemeği, 1 kase yoğurt, 1 dilim ekmek"),
        ],
        "movement": ("20–30 dakika hafif yürüyüş", "Ardından 10 dakika mobilite."),
        "training": recovery("Dinlenme günü", MOBILITY_TEXT),
        "tip": "Artık düşünmeden yaptığın şeyler senin yeni temelin. Yeni bir şey eklemeden önce bu temeli koru.",
        "task": "3. Hafta Değerlendirmesi'ni (s. {p:hafta3}) doldur ve İlerleme Tablosu'na Gün 21 değerlerini yaz.",
    },
    # ------------------------------------------------------------------ FAZ 4
    {
        "n": 22, "title": "Alışkanlıklarını sabitle",
        "focus": "Son faza hoş geldin. Bugün 30 günden sonra da devam edeceğin 3 temel alışkanlığı seçiyorsun.",
        "nutrition": "Beslenme artık tanıdık: tabak modeli, her ana öğünde protein, tabağın yarısı sebze.",
        "meals": [
            ("Kahvaltı", "2 yumurta, 1 kibrit kutusu beyaz peynir, 5 zeytin, domates, salatalık, 1 dilim tam buğday ekmeği"),
            ("Öğle", "1 kase kuru fasulye, yarım yumruk pirinç pilavı, salata"),
            ("Ara öğün", "1 kase süzme yoğurt ve 2 ceviz içi"),
            ("Akşam", "Izgara tavuk (1 avuç içi), fırın sebze, 1 yumruk bulgur pilavı"),
        ],
        "movement": ("8.000–10.000 adım veya 45 dakika yürüyüş", "Bu senin uzun vadeli hareket hedefin olabilir."),
        "training": workout("B", 4, note="Son faz: 4 set yapabilirsin. Zor gelirse 3 sette kal."),
        "tip": "Yeni bir alışkanlığı var olan bir alışkanlığa bağla: “Sabah çayımı koyduktan sonra 1 bardak su içerim.”",
        "task": "Devam ettireceğin 3 alışkanlığı seç ve her birini mevcut bir rutinine bağlayarak yaz.",
    },
    {
        "n": 23, "title": "Hafta sonu stratejisi",
        "focus": "Hafta içi düzenli giden plan, hafta sonu kolayca dağılabilir. Bugün hafta sonları için basit bir plan kuruyorsun.",
        "nutrition": "Hafta sonu da 3 ana öğün. Geç ve büyük bir kahvaltı yaptıysan öğle yemeğini hafif tut.",
        "meals": [
            ("Kahvaltı", "Menemen (2 yumurta), 1 kibrit kutusu beyaz peynir, bol yeşillik, 1–2 dilim tam buğday ekmeği"),
            ("Öğle", "Hafif öğle: 1 kase mercimek çorbası ve 1 kase yoğurt"),
            ("Ara öğün", "1 meyve ve 10 badem"),
            ("Akşam", "Izgara köfte (1 avuç içi), piyaz, bol salata"),
        ],
        "movement": ("40 dakika tempolu yürüyüş", "Veya sevdiğin bir aktivite: bisiklet, yüzme, dans."),
        "training": recovery("Kardiyo günü", "Bugün kuvvet antrenmanı yok. Hareketi keyifli bir aktiviteyle yap."),
        "tip": "Hafta sonu hareketini sosyal yap: arkadaşınla yürüyüş, ailenle bisiklet, pazarda uzun bir tur.",
        "task": "Bu hafta sonu için 1 aktivite ve dışarıda yiyeceksen 1 yemek planı belirle.",
    },
    {
        "n": 24, "title": "Açlık-tokluk ölçeği",
        "focus": "Doymak ile tıka basa dolmak arasında fark var. Bugün 1'den 10'a kadar bir ölçekle tokluğunu fark ediyorsun.",
        "nutrition": "1 = çok aç, 5 = nötr, 10 = aşırı tok. Öğüne 3–4 civarında başla, 6–7 civarında (rahat tok) bitir.",
        "meals": [
            ("Kahvaltı", "Yulaf kasesi: 40 g yulaf, 1 kase yoğurt, 1 avuç meyve, 1 yemek kaşığı fındık"),
            ("Öğle", "Ton balıklı sandviç: 2 dilim tam buğday ekmeği, yarım kutu ton balığı, marul, domates; yanında ayran"),
            ("Ara öğün", "Havuç çubukları ve 2 yemek kaşığı humus"),
            ("Akşam", "Fırında balık (1 avuç içi), buharda brokoli ve havuç, 1 orta boy patates"),
        ],
        "movement": ("8.000–10.000 adım", "Öğle arasında 15 dakikalık bir yürüyüş eklemeyi dene."),
        "training": workout("A", 4),
        "tip": "Tabağında yemek kalabilir. “Tabağı bitirme” alışkanlığı yerine “tokluğumu dinleme” alışkanlığı kur.",
        "task": "Her ana öğünden önce ve sonra açlık-tokluk puanını (1–10) not et.",
    },
    {
        "n": 25, "title": "İlerlemeni ölç",
        "focus": "Son günlere girmeden ölçülerini alıyorsun. Amaç tek bir sayıya değil, genel eğilime bakmak.",
        "nutrition": "Normal bir plan günü. Ölçümü sabah, kahvaltıdan önce yap.",
        "meals": [
            ("Kahvaltı", "2 haşlanmış yumurta, 2 yemek kaşığı lor peyniri, domates, salatalık, 1 dilim tam buğday ekmeği"),
            ("Öğle", "6 adet mercimek köftesi, bol yeşillik, 1 kase yoğurt"),
            ("Ara öğün", "1 bardak kefir ve 1 armut"),
            ("Akşam", "Tavuk sote (1 avuç içi), 1 yumruk bulgur pilavı, cacık"),
        ],
        "movement": ("9.000 adım", "Ardından 10 dakika mobilite."),
        "training": recovery("Aktif toparlanma", MOBILITY_TEXT),
        "tip": "Ölçümleri kendini yargılamak için değil, planı ayarlamak için kullan. Beklediğin gibi gitmeyen bir şey, başarısızlık değil; yeni bir bilgi.",
        "task": "Kilo ve bel ölçünü al, Gün 1 ile karşılaştır. İlerleme Tablosu'nun altına en az 1 olumlu değişiklik yaz (enerji, uyku, güç, kıyafet).",
    },
    {
        "n": 26, "title": "Uzun vadeli beslenme",
        "focus": "Kalıcı beslenme, mükemmel beslenme değildir. Bugün 30 günden sonrası için esnek bir yapı kuruyorsun.",
        "nutrition": "Basit kural: Öğünlerinin büyük çoğunluğu plana uygun olsun; sevdiğin yiyeceklere de planlı olarak yer aç.",
        "meals": [
            ("Kahvaltı", "Peynirli omlet (2 yumurta), ıspanak, 1 dilim tam buğday ekmeği"),
            ("Öğle", "Etli sebze yemeği, 1 kase yoğurt, 1 dilim ekmek"),
            ("Ara öğün", "1 kase süzme yoğurt ve 1 avuç meyve"),
            ("Akşam", "Izgara köfte (1 avuç içi), yarım yumruk pirinç pilavı, bol salata"),
        ],
        "movement": ("8.000–10.000 adım", "Uzun oturduğun günlerde saatte bir kalkmayı unutma."),
        "training": workout("B", 4),
        "tip": "Sevdiğin bir tatlıyı tamamen yasaklamak yerine haftalık planına küçük bir porsiyon olarak ekle. Planlanan şey suçluluk yaratmaz.",
        "task": "30 günden sonra her hafta tekrarlayabileceğin 5 kolay öğünün listesini yaz (ör. menemen, tavuk sote, mercimek çorbası).",
    },
    {
        "n": 27, "title": "Uzun vadeli hareket",
        "focus": "Yürümeyi günlük hayatına ekledin. Bugün bunu uzun vadede nasıl sürdüreceğini planlıyorsun.",
        "nutrition": "Normal bir plan günü. Uzun aktiviteden önce hafif bir ara öğün: meyve ve yoğurt.",
        "meals": [
            ("Kahvaltı", "1 kase süzme yoğurt, 1 avuç meyve, 1 yemek kaşığı yulaf"),
            ("Öğle", "Tavuklu salata (1 avuç içi tavuk), 1 dilim tam buğday ekmeği"),
            ("Ara öğün", "1 muz ve 1 bardak ayran"),
            ("Akşam", "Fırında somon (1 avuç içi), 1 yumruk bulgur pilavı, fırın sebze"),
        ],
        "movement": ("60 dakika aktivite", "Uzun bir yürüyüş veya sevdiğin yeni bir aktivite: bisiklet, yüzme, dans, doğa yürüyüşü."),
        "training": recovery("Aktif gün", "Bugün kuvvet antrenmanı yok; uzun aktivite senin antrenmanın."),
        "tip": "En iyi hareket, yapmaktan hoşlandığın ve düzenli yapabildiğin harekettir.",
        "task": "Önümüzdeki 4 hafta için hareket planını yaz: kaç gün yürüyüş, kaç gün antrenman, hangi gün uzun aktivite.",
    },
    {
        "n": 28, "title": "Uzun vadeli antrenman",
        "focus": "Plandaki son antrenman. Bugün 2. gündeki ilk antrenmanınla karşılaştırıyor ve sonrası için rutinini belirliyorsun.",
        "nutrition": "Normal bir plan günü. Antrenmandan sonraki öğünde protein olsun.",
        "meals": [
            ("Kahvaltı", "Menemen (2 yumurta), 1 kibrit kutusu beyaz peynir, 1 dilim tam buğday ekmeği"),
            ("Öğle", "1 kase kuru fasulye veya nohut yemeği, yarım yumruk pirinç pilavı, cacık"),
            ("Ara öğün", "1 bardak kefir ve 1 elma"),
            ("Akşam", "Izgara tavuk (1 avuç içi), 1 yumruk fırın patates, bol salata"),
        ],
        "movement": ("8.000–10.000 adım", "Antrenmandan ayrı bir zamanda."),
        "training": workout("A", 4, extra="Tekrar testi: Son setinde squat ve şınavda doğru teknikle kaç tekrar yapabildiğini say. "
                                            "2. gündeki ilk antrenmanını düşün: Aynı hareketler şimdi nasıl hissettiriyor?"),
        "tip": "Güçlenmeye devam etmek için hareketleri zamanla biraz zorlaştır: daha fazla tekrar, bir set daha, daha zor bir versiyon.",
        "task": "30 günden sonrası için haftada 2–3 antrenman günü seç ve takvimine yaz.",
    },
    {
        "n": 29, "title": "Sonraki 4 haftanı planla",
        "focus": "Yarın 30. gün. Bugün sonraki 4 haftayı planlıyorsun; böylece plan bittiğinde ne yapacağını biliyorsun.",
        "nutrition": "Normal bir plan günü. Gelecek haftanın alışveriş listesini bugün hazırla.",
        "meals": [
            ("Kahvaltı", "Yulaf lapası (40 g yulaf, süt), yarım muz, 1 yemek kaşığı fındık"),
            ("Öğle", "Hazırladığın tavuk ve bulgur, bol salata"),
            ("Ara öğün", "1 haşlanmış yumurta ve 1 mandalina"),
            ("Akşam", "1 kase kırmızı mercimek yemeği, 1 kase yoğurt, salata"),
        ],
        "movement": ("30 dakika yürüyüş", "Ardından 10 dakika mobilite."),
        "training": recovery("Aktif toparlanma", MOBILITY_TEXT),
        "tip": "Plan yapmak karar yorgunluğunu azaltır. Ne yiyeceğini ve ne zaman hareket edeceğini önceden bilmek, günü kolaylaştırır.",
        "task": "“Sonraki 4 hafta” şablonunu (s. {p:devam}) doldur.",
    },
]

DAY30 = {
    "title": "30. GÜN – BURADAN SONRA NE OLACAK?",
    "focus": "Planın son günü. Bugün geriye bakıyor, ölçülerini alıyor ve devam planını netleştiriyorsun.",
    "nutrition": "Normal bir plan günü. En sevdiğin plan öğünüyle kutla.",
    "meals": [
        ("Kahvaltı", "2 yumurta, 1 kibrit kutusu beyaz peynir, 5 zeytin, bol yeşillik, 1–2 dilim tam buğday ekmeği"),
        ("Öğle", "1 kase mercimek çorbası, tavuklu salata"),
        ("Ara öğün", "1 kase yoğurt ve 1 meyve"),
        ("Akşam", "En sevdiğin plan öğünü, tabak modeline göre"),
    ],
    "movement": ("30–45 dakika rahat yürüyüş", "30 günün kutlama yürüyüşü."),
    "training": "Antrenman yok. Planda 13 antrenman vardı; kaçını yaptığını say ve not et.",
    "task": "İlerleme Tablosu'na (s. {p:ilerleme}) Gün 30 değerlerini yaz ve sonraki sayfadaki soruları cevapla.",
    "questions": [
        "Bu 30 günde ne öğrendim?",
        "Hangi alışkanlıkları kurdum?",
        "Neler iyi işledi?",
        "Neleri sürdürmek istiyorum?",
        "Neyi geliştirmem gerekiyor?",
    ],
}

WEEK_REVIEWS = {
    1: "İlk hafta genelde en zor haftadır, çünkü her şey yeni. Tamamladığın her gün bir adım.",
    2: "Tartıdaki sayı beklediğin kadar değişmediyse endişelenme. Bel ölçüne, enerjine ve uykuna da bak.",
    3: "Artık bir rutinin var. Son faz, bu rutini kalıcı hale getirmekle ilgili.",
}

WEEK_HABITS = ["Su (8–10 bardak)", "Her ana öğünde protein", "Tabağın yarısı sebze", "Hareket hedefi",
               "Antrenman (planlı günlerde)"]

CONTINUE = {
    "title": "30 gün bitti. Ama amaç burada bitmiyor.",
    "lead": "Bu 30 günde bir diyeti bitirmedin; bir sistem kurdun. Şimdi bu sistemi korumak "
            "ve adım adım geliştirmek var.",
    "rules": [
        ("Temeli koru.", "Her ana öğünde protein, tabağın yarısı sebze, günde 8–10 bardak su."),
        ("Hareketi planla.", "Günlük adım hedefin ve haftada 1 uzun aktivite."),
        ("Haftada 2–3 antrenman.", "Aynı hareketlerle devam et ve onları zamanla zorlaştır."),
        ("Haftada 1 kontrol.", "Ölçü, enerji ve uyku. Gerekirse küçük bir ayar yap."),
        ("Geri dönüş kuralı.", "Birkaç gün aksarsa baştan başlama. En kötü gün planınla başla, "
                                "sonra Faz 2'deki herhangi bir günü aç ve oradan devam et."),
    ],
    "progression": [
        ("Hafta 5–6", "Antrenman A ve B: 4 set. Adım hedefin: 8.000–10.000."),
        ("Hafta 7–8", "Daha zor versiyonlar: ör. diz üstü şınavdan klasik şınava, sırt çantasıyla squat."),
    ],
    "template_cols": ["Antrenman günleri", "Günlük adım hedefi", "Tek odak alışkanlığım", "Alışveriş / hazırlık günü"],
}

CLOSING = {
    "title": "Mükemmel olman gerekmiyor.\nDevam etmen gerekiyor.",
    "text": [
        "30 gün boyunca her gün bir adım attın. Bazı günler kolaydı, bazıları değildi. "
        "Önemli olan, bir sonraki adımı atmaya devam etmen.",
        "LEAN MODE PRO olarak basit, uygulanabilir ve sürdürülebilir bir yolun en iyi başlangıç "
        "olduğuna inanıyoruz. Bu rehberi istediğin zaman tekrar açabilir, dilediğin günden yeniden "
        "başlayabilirsin.",
    ],
    "signoff": "Yolun açık olsun.",
}
