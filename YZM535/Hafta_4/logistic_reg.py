import pandas as pd

df = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Pass":       [0, 0, 0, 0, 1, 1, 1, 1]
})

print(df)

from sklearn.linear_model import LogisticRegression

X = df[["StudyHours"]]
y = df["Pass"]

model = LogisticRegression()

model.fit(X, y)

# Predict whether a student who studies for 4 hours will pass
prediction = model.predict([[4]])

print("Prediction:", prediction)

# Get input from the user
new_hour = float(input("How many hours did you study today? "))

prediction = model.predict([[new_hour]])

if prediction[0] == 1:
    print("The model predicts that you will PASS.")
else:
    print("The model predicts that you will FAIL.")