# app.py (Flask application)

import joblib
from flask import Flask, render_template, request, jsonify

# Load the best SVR model
model = joblib.load(open('best_svr_model.joblib', 'rb'))

# Create the Flask application
app = Flask(__name__, static_folder='static')

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input feature values from the form
    CICo = float(request.form['CICo'])
    SM1 = float(request.form['SM1'])
    GATS1i = float(request.form['GATS1i'])
    NdsCH = float(request.form['NdsCH'])
    NdssC = float(request.form['NdssC'])
    MLOGP = float(request.form['MLOGP'])

    # Make predictions using the model
    input_data = [[CICo, SM1, GATS1i, NdsCH, NdssC, MLOGP]]
    LC50_prediction = model.predict(input_data)[0]

    # Return the prediction as a JSON response
    return jsonify({'LC50_prediction': round(LC50_prediction, 3)})

if __name__ == '__main__':
    app.run(debug=True)
