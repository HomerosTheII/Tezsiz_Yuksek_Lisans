import pandas as pd

df = pd.DataFrame({
    "StudyHours": [1, 2, 1.5, 6, 7, 6.5],
    "ScreenTime": [6, 5.5, 6, 2, 1.5, 2]
})

from sklearn.cluster import KMeans

X = df[["StudyHours", "ScreenTime"]]

model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

model.fit(X)

labels = model.labels_

print(labels)

import matplotlib.pyplot as plt

plt.scatter(
    df["StudyHours"],
    df["ScreenTime"],
    c=labels
)

plt.xlabel("Study Hours")
plt.ylabel("Screen Time")

plt.show()