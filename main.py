from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))

@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bath'))
    sqft = float(request.form.get('sq_feet'))  # Convert to float for numerical input

    # Ensure the input is in the format the model expects
    input_data = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])

    # If your pipeline already includes transformers like OneHotEncoder or StandardScaler, the following will work
    try:
        prediction = pipe.predict(input_data)[0] * 1e5
    except AttributeError as e:
        return f"Error: {str(e)}. Make sure your pipeline includes preprocessing steps like OneHotEncoder or StandardScaler."

    return str(np.round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
