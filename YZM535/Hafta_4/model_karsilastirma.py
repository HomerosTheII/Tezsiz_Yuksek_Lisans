import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

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

# 4. Scale the features for KNN and Logistic Regression
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Create the models
models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )
}

# 6. Train and evaluate each model
results = []

for name, model in models.items():

    if name in ["KNN", "Logistic Regression"]:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(
            y_test, y_pred,
            pos_label="gecti",
            zero_division=0
        ),
        "Recall": recall_score(
            y_test, y_pred,
            pos_label="gecti",
            zero_division=0
        ),
        "F1-score": f1_score(
            y_test, y_pred,
            pos_label="gecti",
            zero_division=0
        )
    })

    print(f"\n{name}")
    print("Confusion Matrix:")
    print(confusion_matrix(
        y_test, y_pred,
        labels=["kaldi", "gecti"]
    ))

# 7. Display the comparison table
results_df = pd.DataFrame(results)

print("\nModel Comparison:")
print(results_df.round(3).to_string(index=False))