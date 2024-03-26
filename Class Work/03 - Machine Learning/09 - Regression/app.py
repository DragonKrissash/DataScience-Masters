import pickle as pkl
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)

ridge=pkl.load(open('models/ridge_regressor.pkl','rb'))
scaler=pkl.load(open('models/scaler2.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host='localhost',port=5000)