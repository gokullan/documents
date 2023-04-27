import pickle
from flask import Flask, render_template, request
from xgboost import XGBClassifier
import numpy as np

app = Flask(__name__)

cols_selected = [
    'tidal_volume_observed', 'pao2fio2ratio', 'platelet', 'rbc', 'wbc',
    'temperature', 'glucose', 'age', 'vaso_amount', 'minute_volume',
    'heart_rate', 'mbp', 'tidal_volume_set', 'lactate', 'vaso_rate',
    'resp_rate', 'potassium', 'calcium', 'pco2', 'ph', 'peep',
]

def load_model(X):
    filename = 'xg_boost_18h_3l.sav'
    model = pickle.load(open(filename, 'rb'))
    result = model.predict_proba(np.array([X]))
    return round(result[0][1] * 100, 2)

@app.route('/submit', methods=['POST'])
def submit():
    X = []
    for col in cols_selected:
        X.append(request.form.get(col))
    result = load_model(X)
    return render_template('result.html', result=result)

@app.route('/')
def hello():
    return render_template('ards.html')
    # return '<h1>Hello, World!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
