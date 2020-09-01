def parser(formula):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    operators = ['+','-','*','/',' ','(',')']
    goniometrische = ['sin(', 'cos(', 'tan(', 'cot(','csc(','sec(']
    hyperbolische=['sinh(','cosh(','tanh(','coth(','sech(','csch(']
    grieks_2 = ['pi','xi','mu','nu']
    grieks_3 = ['eta','rho','tau','phi','chi','psi']
    grieks_4 = ['beta','zeta','iota']
    grieks_5 = ['alpha','gamma','delta','theta','kappa','sigma','omega']
    grieks_6=['lambda']
    grieks_7 = ['epsilon','omicron','upsilon']
    areaal_1 = ['arsinh(','arcosh(','artanh(','arcoth(','arcsch(','arsech(']
    areaal_2 = ['arcsinh(','arccosh(','arctanh(','arccoth(','arccsch(','arcsech(']
    inv_hyper = ['arcsin(','arccos(','arctan(','arccot(','arccsc(','arcsec(']

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
                elif elem < len(formula) - 1 and formula[elem:elem+2] in grieks_2:
                    elem += 1
                elif elem < len(formula) - 2 and formula[elem:elem+3] in grieks_3:
                    elem += 2
                elif elem < len(formula) - 3 and formula[elem:elem+4] in grieks_4:
                    elem += 3
                elif elem < len(formula) - 4 and formula[elem:elem+5] in grieks_5:
                    elem += 4
                elif elem < len(formula) - 5 and formula[elem:elem+6] in grieks_6:
                    elem += 5
                elif elem < len(formula) - 6 and formula[elem:elem+7] in grieks_7:
                    elem += 6
                elif elem < len(formula) - 7 and formula[elem:elem+4] in areaal_1:
                    new_formula = formula[:elem+1] + formula[elem+2:]
                    formula = new_formula
                    elem += 6
                elif elem < len(formula) - 8 and formula[elem:elem+8] in areaal_2:
                    new_formula = formula[:elem+1] + formula[elem+3:]
                    formula = new_formula
                    elem += 6
                elif elem < len(formula) - 7 and formula[elem:elem+7] in inv_hyper:
                    new_formula = formula[:elem+1] + formula[elem+3:]
                    formula = new_formula
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


if __name__ == "__main__":
    test_cases = [
        ('2^5', '2**5'),
        ('2x', '2*x'),
        ('sin(x)', 'sin(x)'),
        ('sin(2x)', 'sin(2*x)'),
        ('sinh(x)', 'sinh(x)'),
        ('22', '22'),
        ('x2', 'x*2'),
        ('2*pi^2 + theta', "2*pi**2 + theta"),
        ('arcsin(x)', "asin(x)"),
        ('arcsinh(x)', "asinh(x)"),
        ('x^2', 'x**2'),
        ('2x_1', '2*x_1'),
        ('2theta_1^2', '2*theta_1**2'),
        ('log(x)', 'log(x)'),
        ('ln(x)', 'log(x)'),
        ('srqt(x)', 'sqrt(x)')
    ]
    correct = 0
    i = 1
    for test_case in test_cases:
        if parser(test_case[0]) == test_case[1]:
            correct +=1
            print('✅ passed test case ' + str(i))
        else:
            print('❌ failed test case ' + str(i))
            print('    returned {0} ipv {1}'.format(parser(test_case[0]), test_case[1]))
        i += 1
