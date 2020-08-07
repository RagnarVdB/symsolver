from sympy.parsing.sympy_parser import parse_expr

def parser(formula):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    operators = ['+','-','*','/',' ','(',')']
    goniometrische = ['sin(', 'cos(', 'tan(', 'cot(']
    hyperbolische=['sinh(','cosh(','tanh(','coth(']
    new_formula = formula.replace('^', '**')
    formula = new_formula
    elem = 0
    while elem < len(formula) - 1:
        if formula[elem] not in operators:
            if formula[elem + 1] not in operators and formula[elem+1] not in numbers:
                if elem < len(formula) - 3 and formula[elem:elem+4] in goniometrische:
                    elem += 3
                elif elem < len(formula) - 4 and formula[elem:elem+5] in hyperbolische:
                    elem += 4
                else:
                    new_formula = formula[:elem+1] + '*' + formula[elem+1:]
                    formula = new_formula
            elif formula[elem+1] in numbers:
                if not formula[elem] in numbers:
                    new_formula = formula[:elem + 1] + '*' + formula[elem + 1:]
                    formula = new_formula
        elem += 1
    return formula


assert parser('2^5') == '2**5'
assert parser('2x') == '2*x'
assert parser('sin(x)') == 'sin(x)'
assert parser('sin(2x)') == 'sin(2*x)'
assert parser('sinh(x)') == 'sinh(x)'
assert parser('22') == '22'
assert parser('x2') == 'x*2'