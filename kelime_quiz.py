import random

# Sözlük tanımla
kelime = {
    "Carry": "taşımak",
    "Passenger": "yolcu",
    "Aware": "farkında",
    "Hope": "umarım",
    "Agent": "etmen",
    "Ever": "hiç"
}

# Quiz testi oluşturan fonksiyon
def quiz_test(kelime, soru_sayisi):
    Liste = list(kelime.items())
    random.shuffle(Liste)
    puan = 0
    yanlis_cevaplar = []

    for i in range(min(soru_sayisi, len(Liste))):
        key, value = Liste[i]
        cevap = input(f"'{key}' kelimesinin anlamı nedir? ")
        if cevap.lower() == value.lower():
            print("Doğru!")
            puan += 1
        else:
            print(f"Üzgünüz, doğru cevap '{value}'")
            yanlis_cevaplar.append((key, value, cevap))

    print(f"\nTest Bitti. Puanınız: {puan}/{soru_sayisi}")

    if yanlis_cevaplar:
        print("\nYanlış Cevaplarınız:")
        for key, value, cevap in yanlis_cevaplar:
            print(f"'{key}' kelimesi için doğru cevap '{value}' idi, siz '{cevap}' dediniz.")

# Kullanıcıya kaç soru sormak istediğini sor
def soru_sayisi_al():
    while True:
        try:
            soru_sayisi = int(input("Kaç soru sormak istersiniz? "))
            if soru_sayisi > 0:
                return soru_sayisi
            else:
                print("Lütfen pozitif bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

# Kullanıcıya yeni kelime ekleme imkanı sun
def kelime_ekle(kelime):
    while True:
        yeni_kelime = input("Eklemek istediğiniz İngilizce kelimeyi girin (çıkmak için 'q'): ")
        if yeni_kelime.lower() == 'q':
            break
        anlam = input(f"'{yeni_kelime}' kelimesinin Türkçe anlamını girin: ")
        kelime[yeni_kelime] = anlam
        print(f"'{yeni_kelime}' kelimesi sözlüğe eklendi.")

# Ana menü
def ana_menu():
    while True:
        print("\n--- Ana Menü ---")
        print("1. Quiz'e Başla")
        print("2. Yeni Kelime Ekle")
        print("3. Çıkış")
        secim = input("Seçiminiz (1/2/3): ")

        if secim == '1':
            soru_sayisi = soru_sayisi_al()
            quiz_test(kelime, soru_sayisi)
        elif secim == '2':
            kelime_ekle(kelime)
        elif secim == '3':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# Ana menüyü başlat
ana_menu()