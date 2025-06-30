import joblib
import numpy as np
from flask import Flask, render_template, request
from config.paths_config import MODEL_OUTPUT_PATH

app = Flask(__name__)

# Load your trained model
loaded_model = joblib.load(MODEL_OUTPUT_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Collect inputs from form
            age = int(request.form['age'])
            education = int(request.form['education'])
            cigsPerDay = int(request.form['cigsPerDay'])
            diabetes = int(request.form['diabetes'])
            totChol = int(request.form['totChol'])
            sysBP = float(request.form['sysBP'])
            diaBP = float(request.form['diaBP'])
            BMI = float(request.form['BMI'])
            heartRate = int(request.form['heartRate'])
            glucose = int(request.form['glucose'])

            # Prepare the feature array
            features = np.array([[ age, education, cigsPerDay,
                                    diabetes,
                                  totChol, sysBP, diaBP, BMI, heartRate, glucose]])

            # Predict
            prediction = loaded_model.predict(features)

            return render_template('index.html', prediction=int(prediction[0]))

        except Exception as e:
            return f"Error: {e}", 400

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
