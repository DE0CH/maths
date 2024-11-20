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
from sympy.parsing.latex import parse_latex

# %%
T0, T1 = symbols('T0 T1')
T0v = t
T1v = epsilon * t

# %%
y = Function('y')(T0, T1)
y

# %%
yd = diff(y.subs(T0, T0v).subs(T1, T1v), t).subs(T1v, T1).subs(T0v, T0).simplify()
yd

# %%
ydd = diff(yd.subs(T0, T0v).subs(T1, T1v), t).subs(T1v, T1).subs(T0v, T0).simplify()
ydd

# %%
def series(terms):
    ans = 0
    for i in range(terms):
        n = Function(f'y_{i}')(T0, T1)*epsilon**i
        ans += n
    return ans
series(3)

# %%
expression = ydd+y-epsilon*(yd**3-yd)
expression

# %%
s = r'\sin^3(x) = \frac{3}{4}\sin(x) - \frac{1}{4}\sin(3x)'

trig_id = parse_latex(s)
assert(simplify(trig_id))
trig_id

# %%
xx = T0 + Function('B')(T1)

first = expression.subs(y, series(3)).expand().doit().expand().coeff(epsilon, 1).subs(Function('y_0')(T0, T1), Function('A')(T1)*cos(T0 + Function('B')(T1))).doit().subs(trig_id.lhs.subs(x, xx), trig_id.rhs.subs(x, xx)).simplify()
first

# %%
dsolve(first.coeff(sin(xx)))



# %%
first.coeff(cos(xx))

# %%
