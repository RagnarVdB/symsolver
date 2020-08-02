def parse(integrand):
  from sympy.parsing.sympy_parser import parse_expr
  expr = integrand
  return parse_expr(expr)
