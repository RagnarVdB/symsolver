from sympy.parsing.sympy_parser import parse_expr

def parser(integrand):
  symbols = ('+','-','*','/')
  for elem in range(len(integrand)):
    if integrand[elem] is '^':
      integrand[elem] == '**'
    elif isinstance(integrand[elem], int) and not isinstance(integrand[elem + 1], int):
      if not isinstance(integrand[elem + 1], symbols) or integrand[elem + 1] is ' ':
        integrand.insert('*',elem + 1)

  # expr = integrand.replace
  return integrand

# test cases
print(parser('x^2'))
print(parser('2x'))