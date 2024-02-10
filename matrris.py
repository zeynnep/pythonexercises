# Kullanıcıdan matrisin boyutlarını al
satir_sayisi = int(input("Matrisin satır sayısını girin: "))
sutun_sayisi = int(input("Matrisin sütun sayısını girin: "))

# Matrisi oluştur ve elemanları kullanıcıdan al
matris = []
for i in range(satir_sayisi):
    satir = []
    elemanlar = input(f"{i+1}. satırı girin (elemanları boşlukla ayırın): ").split()
    for eleman in elemanlar:
        satir.append(int(eleman))  # Kullanıcıdan alınan elemanları int'e dönüştürerek satır listesine ekle
    matris.append(satir)  # Oluşturulan satırı matrise ekle

# Satır ve sütun toplamlarını hesapla
satir_toplamlari = []
for satir in matris:
    toplam = 0
    for eleman in satir:
        toplam += eleman  # Her satırdaki elemanları toplamak için iç içe döngü kullan
    satir_toplamlari.append(toplam)  # Satır toplamlarını listeye ekle

sutun_toplamlari = []
for j in range(sutun_sayisi):
    toplam = 0
    for i in range(satir_sayisi):
        toplam += matris[i][j]  # Sütun toplamlarını hesaplamak için matrisin elemanlarını sütun bazında topla
    sutun_toplamlari.append(toplam)  # Sütun toplamlarını listeye ekle

# Sonuçları göster
print("Matris:")
for satir in matris:
    print(satir)  # Matrisi ekrana yazdır

print("Satır Toplamları:", satir_toplamlari)  # Satır toplamlarını ekrana yazdır
print("Sütun Toplamları:", sutun_toplamlari)  # Sütun toplamlarını ekrana yazdır2
