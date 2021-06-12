# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
app = Flask(__name__)
# Load the model
model = pickle.load(open('DiabetesPredModel.pkl','rb'))
@app.route('/api',methods=['POST'])
def getPrediction():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    output = predict(data)
    return jsonify(output)

def predict(data):
    # Make prediction using model loaded from disk as per the data.
    print(data['values'])
    prediction = model.predict([np.array(data['values'])])
    # Take the first value of prediction
    output = prediction[0]
    return output


def test_predict():
    data={
        "parameters":["Pregnancies", "Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"],
        #"values":[6,148,72,35,0,33.6,0.627,50]
        "values":[1,85,66,29,0,26.6,0.351,31]
    }
    output = predict(data)
    print(str(output))

if __name__ == '__main__':
    #test_predict()
    app.run(port=5000, debug=True)
