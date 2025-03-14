import joblib
from flask import Flask, request, jsonify
import pandas as pd

# Load the trained model
model = joblib.load("random_forest_model.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Convert input JSON into a DataFrame
    input_data = pd.DataFrame([data])

    # Ensure feature order matches training data
    expected_features = model.feature_names_in_
    input_data = input_data[expected_features]

    # Make prediction
    prediction = model.predict(input_data)[0]

    return jsonify({"prediction": "Malicious" if prediction == -1 else "Safe"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
