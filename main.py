import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Import data into x and y
x, y = [], []
with open('Muon_Updated.txt') as f:
    for line in f:
        row = line.split()
        x.append(float(row[0]))
        y.append(float(row[1]))

# Create specialized data
reduced_y = [e - 60 for e in y]
poisson_raw = [math.sqrt(e) for e in y]

fitted_data = [-math.log(e-60)+6.5 for e in y]  # data fitted to a logarithmic function

# Create figure and specific axis
fig, ax = plt.subplots()
ax.scatter(x, reduced_y, s=5, c='black')

# Set Spines
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Set Information
ax.set_xlabel('Lifetime ($\mu$s)')
ax.set_ylabel('Number of Occurrences')

plt.errorbar(x, reduced_y, yerr=poisson_raw, fmt='o', color='black', capsize=5)
plt.show()

#  Create figure and specific axis
fig2, ax = plt.subplots()
ax.scatter(x, fitted_data, s=5, c='r')

#  Set Spines
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xlabel('Lifetime ($\mu$s)')
ax.set_ylabel('$\ln(N - 60) + 6.5$')

plt.show()
