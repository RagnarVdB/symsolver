from sympy.parsing.sympy_parser import parse_expr

def parser(integrand):
  # expr = integrand.replace
  return parse_expr(expr)

# test cases
print(parse('x^2'))
print(parse('2x'))