def parse(integrand):
  from sympy.parsing.sympy_parser import parse_expr
  expr = integrand
  return parse_expr(expr)

if __name__ == "__main__":
  print(parse("x^2 + 2x**(x+1)"))
