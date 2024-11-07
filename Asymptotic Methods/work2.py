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
from sympy.abc import alpha, t, m, s
from sympy import Integral, exp, oo, symbols, assuming, Q, I, gamma, cos, sin, arg, Abs, re, im

# %%
f = t**m*exp(-alpha*t**2)

# %%
f

# %%
expr = Integral(f, (t, 0, oo))

# %%
with assuming(Q.real(m), Q.complex(alpha)):
    v = expr.doit()

# %%
v

# %%
v.subs(m, -1/2).subs(alpha, -I)

# %%
expr = Integral(exp(I*s**2)*s**(-1/2), (s, 0, oo))

# %%
expr.doit()

# %%
mine = 1/2*1/(-I)**(1/4)*gamma(1/4).simplify()

# %%
mine


# %%
