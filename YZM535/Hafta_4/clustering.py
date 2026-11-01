import pandas as pd

df = pd.DataFrame({
    "StudyHours": [1, 2, 1.5, 6, 7, 6.5],
    "ScreenTime": [6, 5.5, 6, 2, 1.5, 2]
})

print(df)

import matplotlib.pyplot as plt

plt.scatter(
    df["StudyHours"],
    df["ScreenTime"]
)

plt.xlabel("Study Hours")
plt.ylabel("Screen Time")

plt.show()

