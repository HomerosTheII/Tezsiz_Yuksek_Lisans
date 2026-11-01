import pandas as pd

# Basit bir öğrenci verisi
data = {
    "ÇalışmaSaati": [1, 2, 3, 4, 5],
    "Başarı": [40, 50, 60, 70, 85]
}

df = pd.DataFrame(data)

# Temel gözlem
print(df.describe())
print("\nÇalışma saati arttıkça başarı artıyor mu?")
print(df.corr())  # korelasyon
