import flask
from flask import request, render_template, url_for
from flask_cors import CORS
import joblib

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def homePage():
    return render_template('home.html')
    

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/tips', methods=['GET'])
def tips():
    return render_template('tips.html')


@app.route('/predict', methods=['POST'])
def predict():
    a = int(request.form['age'])
    g = int(request.form['gen'])
    tb = float(request.form['tbil'])
    db = float(request.form['dbil'])
    ap = int(request.form['alk'])
    ala = int(request.form['ala'])
    asa = int(request.form['asp'])
    tp = float(request.form['tpro'])
    alb = float(request.form['alb'])
    ag = float(request.form['albglo'])
    X = [[a, g, tb, db, ap, ala, asa, tp, alb, ag]]
    model = joblib.load('disease.pkl')
    disease = model.predict(X)[0]
    return render_template('predict.html',res=disease)

if __name__ == '__main__':
    app.debug = True
    app.run()
