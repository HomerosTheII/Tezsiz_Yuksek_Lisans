urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price': '7000' }
]

toplam = 0
for urun in urunler:
   fiyat = int(urun['price'])
   toplam += fiyat
print('toplam ürün fiyatı: ', toplam)
