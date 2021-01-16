from flask import Flask, render_template, request
import joblib,pickle
import numpy as np


from flask import Flask,render_template

app=Flask(__name__,template_folder='template')

app = Flask(__name__)

model = joblib.load('model.pkl')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    Revenue = (request.form['Revenue'])
    Frequency = (request.form['Frequency'])
    Recency = (request.form['Recency'])


    data = [[Revenue, Frequency, Recency]]
    print(data)
    prediction = model.predict(data)
    print(prediction)
    if float(prediction) == 0:
        return render_template('index.html', prediction_text='High value customer')
    elif float(prediction) == 1:
        return render_template('index.html', prediction_text='Medium value customer')
    elif float(prediction) == 2:
        return render_template('index.html', prediction_text='Low value customer ')
    else:
        return render_template('index.html', prediction_text='please give another input')

            
if __name__ == "__main__":
    app.run(debug=Flask) # use debug = False for jupyter notebook