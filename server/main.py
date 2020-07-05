from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

app = Flask(__name__)
CORS(app)

@app.route("/integral/<string:integral>")
@cross_origin()
def test(integral):
  x = sp.symbols('x')
  expr = parse_expr(integral)
  I = sp.Integral(expr, x)
  return jsonify(sp.latex(I.doit()))
