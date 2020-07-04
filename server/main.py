from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def test():
   return jsonify(request.args.get('integral', default="test", type= str))
