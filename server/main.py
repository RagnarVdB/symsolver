from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sympy as sp

from modules.parser import parse

app = Flask(__name__)
CORS(app)
@app.route("/v1/integral", methods=["POST"])
def test():
  if request.method == "POST":
    data = request.json
    integrand = parse(data["integrand"])
    bounds = data["bounds"]
    I = integrand
    for bound in bounds[::-1]:
      x = sp.symbols(bound[0])
      if bound[1] == "" or bound[2] == "":
        I = sp.Integral(I, x)
      else:
        I = sp.Integral(I, (x, bound[1], bound[1]))
    solution = sp.latex(I.doit())
    return jsonify(solution)
