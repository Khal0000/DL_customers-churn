from flask import Flask, jsonify, request
import pickle
import pandas as pd
import tensorflow as tf
import numpy as np

app = Flask(__name__)

CLASS = ['Retain', 'Churn']
columns = ["SeniorCitizen", "Partner", "Dependents", "tenure", "OnlineSecurity", "TechSupport", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"]


# import pipelines
with open("preprocessing.pkl", "rb") as f:
    model_prep = pickle.load(f)

my_model = tf.keras.models.load_model('my_model.h5')

@app.route("/")
def hello_world():
    return "<p>Hello, This is my Backend Data!</p>"


@app.route("/predict", methods=['GET', 'POST'])
def body_inference():
    if request.method == 'POST':
        data = request.json
        new_data =[data["SeniorCitizen"],
                    data["Partner"],
                    data["Dependents"],
                    data["tenure"], 
                    data["OnlineSecurity"],
                    data["TechSupport"],
                    data["Contract"],
                    data["PaperlessBilling"],
                    data["PaymentMethod"],
                    data["MonthlyCharges"],
                    data["TotalCharges"]]

        new_data = pd.DataFrame([new_data], columns = columns)
        prep = model_prep.transform(new_data)
        res = my_model.predict(prep)
        res = np.where(res >= 0.5, 1, 0)

        response = {'code':200, 'status':'OK',
                    'result':{'prediction': str(res[0]),
                              'classes': CLASS[res[0].item()]}}
        
        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model Churn Prediction"

# app.run(debug=True)
