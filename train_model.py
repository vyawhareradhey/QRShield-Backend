import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("new_extracted.csv")

# Drop the index column if it exists
df = df.drop(columns=['Index'], errors='ignore')

# Define features and target
X = df.drop(columns=['class'])  # All columns except 'class' are features
y = df['class']  # Target variable

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "random_forest_model.pkl")

print("✅ Model training complete and saved!")
