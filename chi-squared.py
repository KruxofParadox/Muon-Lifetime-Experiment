import math
import numpy as np

a = 737.955
b = 0.468633
c = 63.5479

# Import data into x and y
x, y = [], []
with open('Muon_Updated.txt') as f:
    for line in f:
        row = line.split()
        x.append(float(row[0]))
        y.append(float(row[1]))


def model(x):
    return a * np.exp(-b * x) + c


def chi_squared(x, y):
    chi = 0
    for i in range(0, len(x)):
        chi += ((y[i] - model(x[i])) / math.sqrt(y[i])) ** 2
    return chi


print(chi_squared(x, y)/179)
