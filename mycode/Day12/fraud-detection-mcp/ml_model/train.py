import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib  # To save the model

# Load dataset (example: Kaggle credit card fraud dataset)
data = pd.read_csv("data/creditcard.csv")

# Features (X) and Target (y)
X = data.drop("Class", axis=1)  # All columns except 'Class'
y = data["Class"]  # 1 = Fraud, 0 = Legitimate

# Split into training & testing (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model (good for imbalanced data)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the trained model for API use
joblib.dump(model, "model.joblib")

print("✅ Model trained & saved!")