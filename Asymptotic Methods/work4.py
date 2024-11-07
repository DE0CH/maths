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
from fractions import Fraction

# %%
T0, T1 = symbols('T0 T1')

# %%
u = Function('u', real=True)(T0, T1)

# %%
T0v = t
T1v = epsilon * t

# %%
ud = Derivative(u.subs(T0, T0v).subs(T1, T1v), t).doit().subs(T1v, T1).subs(T0v, T0).simplify()
ud

# %%
udd = Derivative(ud.subs(T0, T0v).subs(T1, T1v), t).doit().subs(T1v, T1).subs(T0v, T0).simplify()
udd

# %%
left = udd + u
left

# %%
right = epsilon * (ud - Fraction('1/3')*(ud)**3)
right

# %%
expr = left - right
expr


# %%
def series(terms):
    ans = 0
    for i in range(terms):
        n = Function(f'u_{i}')(T0, T1)*epsilon ** i
        ans += n
    return ans


# %%
series(3)

# %%
u

# %%
pp = poly(expr.subs(u, series(3)).doit(), epsilon)
pp

# %%
zeroth = Eq(pp.coeff_monomial(1), 0)
zeroth

# %%
u_0v = Function('a')(T1)*cos(T0+Function('b')(T1))
u_0v

# %%
first = Eq(pp.coeff_monomial(epsilon), 0)
first

# %%
first_order = first.subs(Function('u_0')(T0, T1), u_0v).simplify()
first_order

# %%
trig_iden = Eq(sin(x)**3, -Fraction('1/4')*sin(3*x) + Fraction('3/4')*sin(x))
simplify(trig_iden)

# %%
(sin(x)**3).rewrite(sin(x))

# %%
first_order_with_trig = first_order.subs(sin(T0 + Function('b')(T1))**3, trig_iden.rhs.subs(x, T0 + Function('b')(T1)))
assert simplify(Eq(first_order.rhs - first_order.lhs, first_order_with_trig.rhs - first_order_with_trig.lhs))
first_order_with_trig

# %%
nnnn = collect(collect(expand(first_order_with_trig.lhs - first_order_with_trig.rhs), sin(T0 + Function('b')(T1))), cos(T0 + Function('b')(T1)))
nnnn

# %%
a_intc = nnnn.coeff(sin(T0 + Function('b')(T1)))
a_intc

# %%
dsolve(a_intc)[1]

# %%
non_secular = first_order_with_trig.subs(sin(T0 + Function('b')(T1)), 0).subs(cos(T0 + Function('b')(T1)), 0)
non_secular

# %%

# %%
eq = Derivative(f, x, x) + f
eq

# %%
dsolve(eq)

# %%
