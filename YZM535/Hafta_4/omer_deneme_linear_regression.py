import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# db_supervised = pd.read_csv("./Hafta_4/supervised.csv")
db_unsupervised = pd.read_csv("./Hafta_4/unsupervised.csv")

# x_sup = db_supervised[["StudyHours"]] # Öğrenmesini istediğimiz değişken
# y_sup = db_supervised["ExamScore"] # Etiket

# model = LinearRegression()
# model.fit(x_sup, y_sup)

# for i in range(6):
#     prediction = model.predict([[i]])
#     print(f"{i} saat calistiysan, tahmini skorun: {prediction[0]}")

cats = db_unsupervised[["StudyHours", "ScreenTime", "iQ"]]

model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(cats)

plt.scatter(
    db_unsupervised["StudyHours"],
    db_unsupervised["ScreenTime"],
    c = model.labels_
)
plt.xlabel("Study Hours")
plt.ylabel("Screen Time")

plt.show()