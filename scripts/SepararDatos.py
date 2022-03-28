
from random import random, uniform
from tabnanny import check
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("C://Users//Enrique/Documents/GitHub/python-ml-course/datasets/customer-churn-model/Customer Churn Model.txt")
print(len(data))

vector = np.random.randn(len(data))


check = (vector < 0.8)
print(check)
training = data[check]
testing = data[~check]

plt.hist(check.astype(int))
plt.show()