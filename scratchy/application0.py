from flask import Flask, request
from flask_restful import Resource, Api
from script import predict
application = app = Flask(__name__)
api = Api(app)

@app.route("/", methods=['POST'])      #<ligid>/<seqid>", methods=['POST'])
class GetPredict(Resource):

    def get(self):
        lines = request.get_json(force=True)
        ligid = lines[int1]
        seqid = lines[int2]
        
        # TODO parse out 2 ints from json

        s = f"prediction at ({ligid},{seqid}): {predict(ligid, seqid)}"
        #s = str(predict(5,5))
        x = predict(ligid, seqid)
        print(s)
        return {'RESULT': str(x), 
                'report': s,
                'show_inp': str(ligid) + str(seqid)}
                #"games": "Hello freakin world"}#'Hello World! jfkldsajfkldajfkldajfkadjfdaklfjlk'}

api.add_resource(GetPredict, '/')

if __name__=='__main__': 
    app.run(debug=True)


