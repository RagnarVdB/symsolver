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
    assert parser('2^5') == '2**5'
    assert parser('2x') == '2*x'
    assert parser('sin(x)') == 'sin(x)'
    assert parser('sin(2x)') == 'sin(2*x)'
    assert parser('sinh(x)') == 'sinh(x)'
    assert parser('22') == '22'
    assert parser('x2') == 'x*2'
    assert parser('2*pi^2 + theta') == "2*pi**2 + theta"
    assert parser('arcsin(x)') == "asin(x)"
    assert parser('arcsinh(x)') == "asinh(x)"
