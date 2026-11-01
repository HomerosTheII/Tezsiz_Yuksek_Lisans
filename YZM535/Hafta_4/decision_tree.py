import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("100_kisilik_sinif.csv")

# 2. Select features and target
X = df[["Ortalama", "Devamsizlik"]]
y = df["Durum"]

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4. Create and train the model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

# 5. Evaluate the model
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# 6. Visualize the decision tree
plt.figure(figsize=(12, 7))

plot_tree(
    model,
    feature_names=["Ortalama", "Devamsizlik"],
    class_names=model.classes_,
    filled=True,
    rounded=True
)

plt.show()

# 7. Predict for a new student
average = float(input("Ogrencinin not ortalamasi: "))
absence = float(input("Ogrencinin devamsizlik sayisi: "))

new_student = pd.DataFrame({
    "Ortalama": [average],
    "Devamsizlik": [absence]
})

prediction = model.predict(new_student)

print("Tahmin edilen durum:", prediction[0])