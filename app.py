from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model (pickle file)
model = pickle.load(open('C:/Users/HP/PycharmProjects/bank loan credit prediction project/model/model4.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        gender = request.form['gender']
        married = request.form['married']
        income = float(request.form['income'])
        credit_history = int(request.form['credit_history'])

        # Convert categorical values to numerical for prediction
        gender = 1 if gender == 'Male' else 0
        married = 1 if married == 'Yes' else 0

        # Prepare the input for the model
        data = np.array([[gender, married, income,credit_history]])

        # Make the prediction
        prediction = model.predict(data)[0]

        # Return result to the user
        return render_template('index.html',
                               prediction_text=f'Loan Status: {"Approved" if prediction == 1 else "Rejected"}')

if __name__ == '__main__':
    app.run(debug=True)