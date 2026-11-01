import pandas as pd
import os

print(os.getcwd())

db = pd.read_csv("./Hafta_2/customer_data_practice.csv")

print("Info")
print(db.info())
print("Description")
print(db.describe())
print("Shape")
print(len(db))
print("Head")
print(db.head())


print("--------------------------------")
# Array halinde kaç NaN değerleri True, diğerlerini False olarak veriyor.
print(db.isna())

# Sütunlara göre kaçar tane NaN değeri olduğunu belirtiyor.
print(db.isna().sum())

# NaN değerlerini median değeri ile dolduruyor.
db["Age"] = db["Age"].fillna(db["Age"].median())
print(db)