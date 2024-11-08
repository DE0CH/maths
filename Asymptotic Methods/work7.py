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
T0 = Symbol('T0')
T1 = Symbol('T1')

# %%
T0v = t
T1v = epsilon * t

# %%
y = Function('y')(T0, T1)

# %%
yd = y.subs(T0, T0v).subs(T1, T1v).diff(t).subs(T1v, T1).subs(T0v, T0).simplify()
yd

# %%
ydd = yd.subs(T0, T0v).subs(T1, T1v).diff(t).subs(T1v, T1).subs(T0v, T0).simplify()
ydd

# %%
og = ydd + 2*epsilon*yd + y - epsilon * y**3
og


# %%
def series(terms):
    ans = 0
    for i in range(terms):
        n = Function(f'y_{i}')(T0, T1)*epsilon ** i
        ans += n
    return ans


# %%
poly(og.subs(y, series(3)).doit(), epsilon).coeff_monomial(1)

# %%
y0v = Function('A')(T1)*sin(T0 + Function('B')(T1))
y0v

# %%
subbed = poly(og.subs(y, series(3)).doit(), epsilon).coeff_monomial(epsilon).subs(Function('y_0')(T0, T1), y0v)
subbed

# %%
trig_id = Eq(sin(x)**3, Rational('1/4')*(3*sin(x) - sin(3*x)))
assert simplify(trig_id)
trig_id

# %%
xx = T0 + Function('B')(T1)

subbed_trig = subbed.subs(trig_id.lhs.subs(x, xx), trig_id.rhs.subs(x, xx))
subbed_trig

# %%
A_zero = poly(subbed_trig.doit().expand(), cos(xx)).coeff_monomial(cos(xx))
A_zero

# %%
Av = dsolve(A_zero).rhs
Av

# %%
B_zero = poly(subbed_trig.doit().expand(), sin(xx)).coeff_monomial(sin(xx))
B_zero

# %%
Bv = dsolve(B_zero.subs(Function('A')(T1), Av)).doit().rhs
Bv

# %%
u0v = y0v.subs(Function('B')(T1), Bv).subs(Function('A')(T1), Av).subs(T0, T0v).subs(T1, T1v)
u0v

# %%
ttt = solve((Eq(u0v.subs(t, 0), 0), Eq(u0v.diff(t).subs(t, 0), 0)), (Symbol('C1'), Symbol('C2')))
ttt

# %% [markdown]
# Two solutions? Shouldn't there be only one? (it shows four but actually two are the same)

# %%
u0v.diff(t).subs(t, 0)

# %%
u0v.subs(t, 0)

# %%
