from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import json
from flask_ngrok import run_with_ngrok
#model = pickle.load(open('model1.pkl', 'rb'))

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def man():
    df = pd.read_csv('https://raw.githubusercontent.com/luisyerbes20/yerbaa/main/statess.csv')
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)




#uStates


"""@app.route('/predict', methods=['POST'])
def home():
    #data = {'chart_data': chart_data}
    return render_template("index.html", data=data)"""


if __name__ == "__main__":
    app.run()
