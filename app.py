import pandas as pd
import json
from flask import Flask, request, render_template


app = Flask(__name__)

# Load The Model

# Load The File
data = pd.read_csv("C:/Users/Inspiron/Desktop/APP/Kaggke_LGBM_3r_March.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    dict1 = request.form.to_dict()
    product_id = dict1["Store_Product_Id"]
    t1 = data[data['id']==product_id]
    json_list = json.loads(json.dumps(list(t1.T.to_dict().values()))) 
    jsonString = json.dumps(json_list)
    return jsonString



if __name__ == "__main__":
    app.run()