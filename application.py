''' attempting to do it not as RESTful ''' 
from flask import Flask, request, jsonify
import json
from script import predict, lig_tfidf
application = app = Flask(__name__)

@app.route("/", methods=['POST'])      #<ligid>/<seqid>", methods=['POST']
def get():
    lines = request.get_json(force=True)
    ligid = lines['int1'] # keys in file test_json_get.py 
    seqid = lines['int2']

    thing = lig_tfidf.transform(["hey peyton how's austin"])

    return json.dumps({'ligid': ligid, 'seqid': seqid, 'prediction': predict(ligid, seqid)})#'thing': thing})#, 'predict': predict(ligid, seqid)})# json.dumps(output)

if __name__=='__main__': 
    app.run(debug=True)


