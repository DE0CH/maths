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
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

# %%
intersection_area = (
    r**2 * acos((d**2 + r**2 - R**2) / (2 * d * r)) +
    R**2 * acos((d**2 + R**2 - r**2) / (2 * d * R)) -
    Rational('1/2') * sqrt((-d + r + R) * (d - r + R) * (d + r - R) * (d + r + R))
)
intersection_area

# %%
ann = R**2*pi / 4 + r**2*pi / 4 - intersection_area/2
ann

# %%
ans1 = ann.subs(d, 1).simplify()
ans1

# %%
ans1.subs(r, R).simplify()

# %%
Rv = sqrt(x**2 + y**2)
display(Rv)
rv = sqrt((1-x)**2 + y**2)
display(rv)
ans = ans1.subs(R, Rv).subs(r, rv)
ans

# %%
simplify(Eq(ans.subs(1-x, t).subs(x, 1-x).subs(t, x), ans))

# %%

# %%
yval = 0.3
f = lambdify((r, R), ans1, 'numpy')

# Generate x values and evaluate the function
x_vals = np.linspace(yval, 1-yval, 500)
y_vals = f(np.sqrt(yval*yval + x_vals*x_vals), np.sqrt(yval**2 + (1-x_vals)*(1-x_vals)))
plt.plot(x_vals, y_vals)
plt.grid()
plt.legend()
plt.show()

# %%
yval = 0.3
f = lambdify(x, ans.subs(y, yval), 'numpy')

# Generate x values and evaluate the function
x_vals = np.linspace(yval, 1-yval, 500)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals)
plt.grid()
plt.legend()
plt.show()

# %%
yval = 0.4
f = lambdify(x, ans.subs(y, yval), 'numpy')

# Generate x values and evaluate the function
x_vals = np.linspace(yval, 1-yval, 500)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals)
plt.grid()
plt.legend()
plt.show()

# %%
f = lambdify((x, y), ans, 'numpy')

# Define the limits
x_lower = lambda y: y  # x: y -> 1-y
x_upper = lambda y: 1 - y
y_lower = 0            # y: 0 -> 0.5
y_upper = 0.5

# Perform the numerical double integration
result, error = dblquad(
    f, 
    y_lower, y_upper,  # y integration limits
    x_lower, x_upper,  # x integration limits
    epsabs=1e-11, epsrel=1e-11  # Absolute and relative tolerance
)
result * 4

# %%
result = integrate(ans, (x, y, 1-y), (y, 0, 0.5))
result

# %%
final = result.doit()
final

# %%
