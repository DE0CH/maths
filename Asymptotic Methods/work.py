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
import sympy
from sympy.abc import x, t, s
from sympy import exp, cos, sin, Integral, pi, sqrt, oo
from math import isclose

# %%
f = exp(x*(cos(t) - 1 + t**2/2))

# %%
f

# %%
f.series(t, 0, 10)

# %%
i_ground = Integral(exp(x*sin(t)), (t, 0, pi/2))

# %%
i_ground


# %%
def check_ground(i_ground, i):
    for x0 in range(1, 1000, 100):
        a_ground = i_ground.subs(x, x0).evalf()
        a = i.subs(x, x0).evalf()
        assert isclose(a_ground, a)


# %%
i = Integral(exp(x*(1-t**2/2))*f, (t, 0, pi/2))

# %%
i

# %%
i = Integral(exp(x*(1-t**2/2))*f.series(t, 0, 10).removeO(), (t, 0, pi/2))

# %%
i

# %%
it = Integral(i.transform(t, (sqrt(2*s/x), s)).function, (s, 0, oo))

# %%
it

# %%
it.doit(simplify=True)

# %%
check_ground(i_ground, i)

# %%

# %%
