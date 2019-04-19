''' attempting to do it not as RESTful ''' 
from flask import Flask, request, jsonify#, response_class
import json
import dill
import numpy as np

with open("predict.pk", "rb") as p: 
    model = dill.load(p)

application = app = Flask(__name__)

@app.route("/", methods=['POST'])      #<ligid>/<seqid>", methods=['POST']
def get():
    lines = request.get_json(force=True)
    smile = lines['smile'] # keys in file test_json_get.py 
    sequ = lines['sequ']

    p = model.predict_proba(np.array([[smile, sequ]]))[0,1]

    print(f"the ligand {smile} and the protein {sequ} binds with probability {p}. ")

    outdat = {'prediction': p}
   
    response = app.response_class(
            response=json.dumps(outdat), 
            status=200, 
            mimetype='application/json', 
            #header
            )

    #response = Response(outdat, stat
    return response

if __name__=='__main__': 
    app.run(debug=True)

''' from flask import json

@app.route('/summary')
def summary():
    data = make_summary()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response ''' 
