import pandas as pd

df = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5],
    "Score": [45, 52, 61, 70, 78]
})

print(df)

import matplotlib.pyplot as plt

plt.scatter(df["StudyHours"], df["Score"])

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.show()

#Tahmin

predicted = 40 + 8 * df["StudyHours"]

print(predicted)

#yeni ögrenci

study_hours = 6

prediction = 40 + 8 * study_hours

print(prediction)
