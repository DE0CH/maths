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
y = Function('y')(t)
ee = diff(y, t, t) + y - epsilon * (diff(y, t)**3 - diff(y, t))
ee

# %%
dsolve(ee)

# %%
import sympy as sp
from scipy.integrate import solve_ivp
import numpy as np

# Define symbols
t = sp.symbols('t')
y1, y2, epsilon = sp.symbols('y1 y2 epsilon')

# Define the system of first-order ODEs
dy1_dt = y2
dy2_dt = -y1 + epsilon * (y2 - y2**3)

# Convert the system to numerical functions using lambdify
f_dy1_dt = sp.lambdify((t, y1, y2, epsilon), dy1_dt, 'numpy')
f_dy2_dt = sp.lambdify((t, y1, y2, epsilon), dy2_dt, 'numpy')

# Define the function for solve_ivp
def system(t, Y, epsilon):
    y1, y2 = Y
    return [f_dy1_dt(t, y1, y2, epsilon), f_dy2_dt(t, y1, y2, epsilon)]

# Initial conditions
y1_0 = 4  # Initial value of y
y2_0 = 0  # Initial value of dy/dt
epsilon_value = 0.1  # Set epsilon to a specific value
t0 = 0
t_target = 2

# Solve the system numerically
solution = solve_ivp(system, [t0, t_target], [y1_0, y2_0], args=(epsilon_value,), t_eval=[t_target])

# Get the solution at t = 2
y1_at_target = solution.y[0][0]
y2_at_target = solution.y[1][0]
print(f"y(2) = {y1_at_target}, dy/dt(2) = {y2_at_target}")

# %%
