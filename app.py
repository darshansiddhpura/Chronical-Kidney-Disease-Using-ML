import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('finalized_model.pkl','rb'))

@app.route('/')
def home ():
    return render_template('form.html')


@app.route('/predict',methods=['POST'])

def predict():
    
    int_fetures = [float(x) for x in request.form.values()]
    print(int_fetures)
    final_features = [np.array(int_fetures)]
    print(int_fetures)
    print(final_features)
    prediction =  model.predict(final_features)
    output=round(prediction[0],2)
    # result is displayed on the 'from.html' file
    if  output == 1:
        return render_template('form.html', prediction_text='This patient is in Risk')
    else:
        return render_template('form.html', prediction_text='This patient is at No Risk')
    
if __name__ == "__main__":
    app.run(debug=True)
    