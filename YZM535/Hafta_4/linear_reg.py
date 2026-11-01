import pandas as pd

df = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5],
    "Score": [45, 52, 61, 70, 78]
})

print(df)

from sklearn.linear_model import LinearRegression

X = df[["StudyHours"]]
y = df["Score"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)

new_hour = float(input("Bugun kac saat calistin? "))

prediction = model.predict([[new_hour]])

print(prediction)