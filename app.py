from flask import Flask, render_template, request
import pickle
import numpy as np
model=pickle.load(open("model.pkl", "rb"))
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def basic():
    if request.method == 'POST':
        sepal_length = request.form['sepallength']
        sepal_width = request.form['petalwidth']
        petal_length = request.form['petallength']
        petal_width = request.form['petalwidth']
        petal_width = request.form['petalwidth']
        petal_width = request.form['petalwidth']
        petal_width = request.form['petalwidth']
        petal_width = request.form['petalwidth']
        y_pred = [[sepal_length, sepal_width, petal_length, petal_width, petal_width, petal_width, petal_width, petal_width]]
        

        input_data = np.asarray(y_pred)
        input_data_reshaped = input_data.reshape(1,-1)
        result=model.predict(input_data_reshaped)
        result= result[0]


        setosa = 'Plant Condition is Good'
        versicolor = 'Plant Condition is Bad'

        if result == 0:
            return render_template('index.html', setosa=setosa)
        else:
            return render_template('index.html', versicolor=versicolor) 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)