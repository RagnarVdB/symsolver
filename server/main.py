from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from subprocess import call
from modules.parser import parser

app = Flask(__name__)
CORS(app)
@app.route("/v1/integral", methods=["POST"])
def test():
  if request.method == "POST":
    data = request.json
    integrand = parse_expr( parser(data["integrand"]) )
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

# Github deployment
@app.route("/webhooks/github", methods=["POST"])
def reload():
  print("received push")
  data = request.json
  try:
    repo = data["repository"]["id"]
  except:
    return jsonify(401)
  if (repo == 276705563):
    call("./reload_server.sh", shell=True)
  else:
    return jsonify(401)
  return jsonify(200)
