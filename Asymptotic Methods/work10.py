# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
from sympy.abc import *
from sympy import *


# %%
y = Function('y')(x)
og = epsilon*diff(y, x, x) -y*diff(y, x) - y
expr = -y*diff(y, x) - y
display(expr)
display(dsolve(expr)[0])
dsolve(expr, ics={Function('y')(0):2})

# %%
Xv = (1-x)/(epsilon**nu)

# %%
yd = diff(Function('Y')(Xv), x).subs(Xv, X).simplify()
yd

# %%
ydd = diff(Function('Y')(Xv), x, x).subs(Xv, X).simplify()
ydd

# %%
transformed = og.subs(Derivative(y, x, x), ydd).subs(Derivative(y, x), yd).subs(Function('y')(x), Function('Y')(X))
transformed

# %%
ppp = (transformed.subs(nu, 1).simplify().expand()*epsilon).expand()
ppp

# %%
poly(ppp.subs(Function('Y')(X), Function('Y0')(X)), epsilon).coeff_monomial(1)

# %%
Y0 = Symbol('Y0')
eq = Eq((a + sqrt(Rational('1/2'))*Y0)/(a-sqrt(Rational('1/2'))*Y0), exp(sqrt(2)*a*X))
display(eq)
solve(eq, Y0)[0]

# %%
dsolve(diff(Symbol()))
