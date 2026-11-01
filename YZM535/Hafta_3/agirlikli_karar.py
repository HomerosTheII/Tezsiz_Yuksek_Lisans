import numpy as np

# Özellikler: [not ortalaması, proje puanı]
ogrenci = np.array([80, 70])
agirliklar = np.array([0.6, 0.4])

# Basit doğrusal skor
skor = np.dot(ogrenci, agirliklar)
print("Toplam skor:", skor)

if skor > 75:
    print("Durum: Başarılı")
else:
    print("Durum: Geliştirilmeli")
