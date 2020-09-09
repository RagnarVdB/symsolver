from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from subprocess import call
from modules.parser import parser

app = Flask(__name__)
CORS(app)

def solveIntegral(data):
  try:
    integrand = parse_expr( parser(data["integrand"]) )
  except:
    return {"solution": "", "status": "error", "message": "Didn't understand integrand."}
  bounds = data["bounds"]
  I = integrand
  all_bounds = True
  for bound in bounds[::-1]:
    x = sp.symbols(bound[0])
    if bound[1] == "" or bound[2] == "":
      all_bounds = False
      I = sp.Integral(I, x)
    else:
      try:
        I = sp.Integral(I, (x, parser(bound[1]), parser(bound[2])))
      except:
        return {"solution": "", "status": "error", "message": "Didn't understand bounds."}
  try:
    res = I.doit()
    if res != I:
      solution = sp.latex(res)
      return {"solution": solution, "status": "success", "message": ""}
    else:
      raise "no solution"
  except:
    if all_bounds:
      try:
        res = I.as_sum(100, "midpoint").evalf()
        solution = sp.latex(sp.N(res))
        return {"solution": solution, "status": "numerical", "message": "No exact solution could be found. Integral was approximated numerically."}
      except:
        return {"solution": "", "status": "error", "message": "No solution could be found, definite integral may be approximated numerically"}
  return {"solution": "", "status": "error", "message": "No solution could be found, definite integral may be approximated numerically"}

@app.route("/v1/integral", methods=["POST"])
def integral():
  data = request.json
  result = solveIntegral(data)
  print(result)
  return jsonify(result)

# Github deployment
@app.route("/webhooks/github", methods=["POST"])
def reload():
  print("received push")
  data = request.json
  print(data)
  try:
    repo = data["repository"]["id"]
  except:
    return jsonify(401)
  if (repo == 276705563):
    call("./reload_server.sh", shell=True)
  else:
    return jsonify(401)
  return jsonify(200)
