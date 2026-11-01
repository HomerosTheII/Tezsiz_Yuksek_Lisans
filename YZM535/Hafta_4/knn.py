import pandas as pd

# 1. Load the dataset
df = pd.read_csv("./YZM535/Hafta_4/100_kisilik_sinif.csv")

print(df.head())

# 2. Select input features and target
X = df[["Ortalama", "Devamsizlik"]]
y = df["Durum"]

# 3. Split the data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4. Scale the features
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Create and train the KNN model
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train_scaled, y_train)

# 6. Make predictions
y_pred = model.predict(X_test_scaled)

# 7. Evaluate the model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=["kaldi", "gecti"]))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 8. Predict the result for a new student
average = float(input("Ogrencinin not ortalamasi: "))
absence = float(input("Ogrencinin devamsizlik sayisi: "))

new_student = pd.DataFrame({
    "Ortalama": [average],
    "Devamsizlik": [absence]
})

new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)

print("Tahmin edilen durum:", prediction[0])

# 9. Show prediction probabilities
probabilities = model.predict_proba(new_student_scaled)

print("\nTahmin olasiliklari:")

for class_name, probability in zip(model.classes_, probabilities[0]):
    print(f"{class_name}: {probability:.2%}")