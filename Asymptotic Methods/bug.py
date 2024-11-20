from sympy import parse_latex

s = r'\sin^3(x) - \frac{3}{4}\sin(x) + \frac{1}{4}\sin(3x)'
print(s)
parse_latex(s)
