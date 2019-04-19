''' attempting to do it not as RESTful ''' 
from __future__ import division

import itertools
import numbers
import numpy as np# type: ignore
from warnings import warn
from abc import ABCMeta, abstractmethod

from sklearn.base import ClassifierMixin, RegressorMixin # type: ignore
from sklearn.externals.joblib import Parallel, delayed# type: ignore
from sklearn.externals.six import with_metaclass# type: ignore
from sklearn.externals.six.moves import zip# type: ignore
from sklearn.metrics import r2_score, accuracy_score# type: ignore
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor# type: ignore
from sklearn.utils import check_random_state, check_X_y, check_array, column_or_1d# type: ignore
from sklearn.utils.random import sample_without_replacement# type: ignore
from sklearn.utils.validation import has_fit_parameter, check_is_fitted# type: ignore
from sklearn.utils import indices_to_mask, check_consistent_length# type: ignore
from sklearn.utils.metaestimators import if_delegate_has_method# type: ignore
from sklearn.utils.multiclass import check_classification_targets# type: ignore

from sklearn.ensemble.base import BaseEnsemble, _partition_estimators# type: ignore


from flask import Flask, request, jsonify#, response_class
import json
import dill
#import numpy as np

with open("predict.pk", "rb") as p: 
    model = dill.load(p)

application = app = Flask(__name__)

@app.route("/", methods=['POST'])      #<ligid>/<seqid>", methods=['POST']
def get():
    lines = request.get_json(force=True)
    smile = lines['smile'] # keys in file test_json_get.py 
    sequ = lines['sequ']

    model.set_params(PUC__n_jobs=1)

    p = model.predict_proba(np.array([[smile, sequ]]))[0,1]

    print(f"the ligand {smile} and the protein {sequ} binds with probability {p}. ")

    outdat = {'prediction': p}
   
    response = app.response_class(
            response=json.dumps(outdat), 
            status=200, 
            mimetype='application/json', 
            #header
            )
    
    #output = [('RESULT', smile),('report', sequ),('show_inp', 700)] 
    #return jsonify(output)
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
