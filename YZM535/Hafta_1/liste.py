#list
studentA = ["Gozde",  "Cay", 2010, [70, 60, 70]]
studentB = ["Mustafa",  "Cay", 1999, [80, 80, 70]]
studentC = ["Gizem",  "Cay", 1998, [80, 70, 90]]

print(f"{studentA[0]} {studentA[1]} {2025-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}")
print(f"{studentB[0]} {studentB[1]} {2025-studentB[2]} yasinda ve not ortalamasi {(studentB[3][0]+studentB[3][1]+studentB[3][2])/3}")
print(f"{studentC[0]} {studentC[1]} {2025-studentC[2]} yasinda ve not ortalamasi {(studentC[3][0]+studentC[3][1]+studentC[3][2])/3}")

#dictionary
ogrenciler = {}

ad = input("Ogrenci adi:")
soyad = input("Ogrenci soyadi:")
dogum = input("Ogrenci dogum yili:")
ortalama = input("Ogrenci ortalamasi:")

ogrenciler.update({
    soyad: {
        'isim': ad,
        'yas': dogum,
        'not': ortalama
    }
})

ad = input("Ogrenci adi:")
soyad = input("Ogrenci soyadi:")
dogum = input("Ogrenci dogum yili:")
ortalama = input("Ogrenci ortalamasi:")

ogrenciler.update({
    soyad: {
        'isim': ad,
        'yas': dogum,
        'not': ortalama
    }
})

ad = input("Ogrenci adi:")
soyad = input("Ogrenci soyadi:")
dogum = input("Ogrenci dogum yili:")
ortalama = input("Ogrenci ortalamasi:")

ogrenciler.update({
    soyad: {
        'isim': ad,
        'yas': dogum,
        'not': ortalama
    }
})


ogrSoyad = input('öğrenci soyadi: ')
ogrenci = ogrenciler[ogrSoyad]
print(ogrenci)

print(f"Aradığınız {ogrSoyad} soyadli öğrencinin adı: {ogrenci['isim']}, dogum yili: {ogrenci['yas']} ve ortalamasi ise {ogrenci['not']}")