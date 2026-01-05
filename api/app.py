import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import os
from sklearn.preprocessing import MinMaxScaler
app = Flask(__name__, template_folder="../templates")
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "..", "model.pkl")
model = pickle.load(open(model_path, "rb"))
data_path = os.path.join(BASE_DIR, "..", "diabetes.csv")
dataset = pd.read_csv(data_path)
dataset_X = dataset.iloc[:, [1, 2, 5, 7]].values
sc = MinMaxScaler(feature_range=(0, 1))
sc.fit(dataset_X)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    final_features = np.array([float_features])
    prediction = model.predict(sc.transform(final_features))
    return render_template("index.html", prediction_text=str(prediction.tolist()))
def handler(event, context):
    return app(event, context)
