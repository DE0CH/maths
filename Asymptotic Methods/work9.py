# %%
from sympy.abc import *
from sympy import *

# %%
lambda_ = Symbol('lambda')

# %%
Yv = Function('Y')(x)

# %%
yv = exp(lambda_*Y)
yv

# %%
expr = Derivative(y, x, x) - (lambda_**2*x**4 + lambda_*x**3)*y
expr

# %%
def series(terms):
    ans = 0
    for i in range(terms):
        n = Function(f'Y{i}')(x) * lambda_**(-i)
        ans += n
    return ans
series(3)

# %%
exp_subbed = ((expr.subs(Y, Yv).doit().expand())/lambda_**2/exp(lambda_*Yv)).simplify().expand()
exp_subbed

# %%
series_subbed = exp_subbed.subs(Yv, series(2)).doit().expand()
series_subbed

# %%
first = poly(series_subbed, 1/lambda_).coeff_monomial(1)
first

# %%
Y0v = [yy.rhs for yy in dsolve(first)]
display(*Y0v)

# %%
second = poly(series_subbed, 1/lambda_).coeff_monomial(1/lambda_)
second

# %%
second_subbed = [second.subs(Function('Y0')(x), yy).doit() for yy in Y0v]
display(*second_subbed)

# %%
Y1 = [dsolve(yy).rhs for yy in second_subbed]
display(*Y1)

# %%



