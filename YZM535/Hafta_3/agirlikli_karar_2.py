import numpy as np

# Kullanıcıdan notları alma
not_ortalamasi = float(input("Not ortalamasını girin: "))
proje_puani = float(input("Proje puanını girin: "))

# Özellik vektörü
ogrenci = np.array([not_ortalamasi, proje_puani])

# Ağırlıklar
agirliklar = np.array([0.6, 0.4])

# Doğrusal skor hesaplama
skor = np.dot(ogrenci, agirliklar)
print("\nToplam skor:", skor)

# Durum değerlendirme
if skor > 75:
    print("Durum: Başarılı")
else:
    print("Durum: Geliştirilmeli")
