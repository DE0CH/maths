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
T0, T1 = symbols('T_0 T_1')

# %%
T0v = t
T1v = epsilon * t

# %%
y = Function('y')(T0, T1)

# %%
yd = Derivative(y.subs(T0, T0v).subs(T1, T1v), t).doit().subs(T1v, T1).subs(T0v, T0).simplify()
yd

# %%
ydd = Derivative(y.subs(T0, T0v).subs(T1, T1v), t, t).doit().subs(T1v, T1).subs(T0v, T0).simplify()
ydd

# %%
og = ydd + y - epsilon * yd ** 2 * y
og


# %%
def series(terms):
    ans = 0
    for i in range(terms):
        nn = Function(f'y_{i}')(T0, T1)*epsilon**i
        ans += nn
    return ans


# %%
series(3)

# %%
sss = og.subs(Function('y')(T0, T1), series(3)).doit()
sss

# %%
zeroth = poly(expand(sss), epsilon).all_coeffs()[-1]
zeroth

# %%
dsolve(zeroth.subs(Function('y_0')(T0, T1), Function('y_0')(T0)))

# %%
y0v = Function('a')(T1)*cos(T0+Function('b')(T1))
y0v

# %%
first = poly(expand(sss), epsilon).all_coeffs()[-2]
first

# %%
simplify(Eq(sin(t), 1/(2*I)*(exp(I*t)-exp(-I*t))))

# %%
trig_id = Eq(sin(x)**2*cos(x), -Fraction(1, 4)*cos(3*x) + Fraction(1, 4)*cos(x))
assert simplify(trig_id)
trig_id

# %%
subbed = first.subs(Function('y_0')(T0, T1), y0v).doit()
subbed

# %%
xv = T0 + Function('b')(T1)
trig_subbed = subbed.subs(trig_id.lhs.subs(x, xv), trig_id.rhs.subs(x, xv)).expand()
assert simplify(Eq(subbed, trig_subbed))
trig_subbed

# %%
poly(trig_subbed, cos(xv)).coeff_monomial(cos(xv)) * -1

# %%
poly(trig_subbed, sin(xv)).coeff_monomial(sin(xv))

# %%
a0 = Symbol('a0')
dsolve(poly(trig_subbed, cos(xv)).coeff_monomial(cos(xv)) * -1).subs(Function('a')(T1), a0).doit()

# %%
eee = ydd + Function('y')(T0, T1) - epsilon*(yd**3-yd)
eee

# %%
sss = eee.subs(Function('y')(T0, T1), series(3)).doit().expand()
sss

# %%
zeroth = poly(sss, epsilon).coeff_monomial(1)
zeroth

# %%
first = poly(sss, epsilon).coeff_monomial(epsilon)
first

# %%
trig_id2 = Eq(sin(x)**3, Fraction(1/4)*(3*sin(x)-sin(3*x)))
simplify(trig_id2)

# %%
simplify(Eq(sin(x)**3, -1/(8*I)*(exp(3*i*x)-3*exp(I*x)+3*exp(-I*x)-exp(-3*i*x))))

# %%
((1/(2*I)*(exp(I*x) - exp(-I*x)))**3).expand()

# %%
xx = T0 + Function('B')(T1)
y0v = Function('A')(T1)*cos(xx)
subbed = first.subs(Function('y_0')(T0, T1), y0v).doit()
subbed

# %%
subbed_trig = subbed.subs(trig_id2.lhs.subs(x, xx), trig_id2.rhs.subs(x, xx))
subbed_trig

# %%
pp2 = poly(subbed_trig.expand(), cos(xx)).coeff_monomial(cos(xx))
pp2

# %%
pp = poly(subbed_trig.expand(), sin(xx)).coeff_monomial(sin(xx))
Av = dsolve(pp)[1].rhs
Av

# %%
Av.subs(T1, epsilon*t).diff(t).subs(t,0)

# %%
Bv = dsolve(pp2.subs(Function('A')(T1), Av)).rhs
Bv

# %%
Bv = Symbol('C2')
# Because this is different from C1 used in Av

# %%
z = y0v.subs(Function('A')(T1), Av).subs(Function('B')(T1), Bv).subs(T0, T0v).subs(T1, T1v)
z

# %%
zz = y0v.subs(Function('A')(T1), Av).subs(Function('B')(T1), Bv).subs(T0, T0v).subs(T1, T1v).diff(t)
zz

# %%
sim_eq = (Eq(z.subs(t, 0), a), Eq(zz.subs(t, 0), 0))

# %%
sim_eq[0]

# %%
sim_eq[1]

# %%
sols = solve(sim_eq, (Symbol('C1'), Symbol('C2')))
sols

# %%
