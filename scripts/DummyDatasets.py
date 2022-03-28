from hashlib import new
from random import random, uniform
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
n = 1000000
datos = pd.DataFrame(
    {
        'A': np.random.randn(n),
        'B': 1.5 + 2.5 * np.random.randn(n), 
        'C': np.random.uniform(5,32,n)
    }
)
print(datos.describe())

data = pd.read_csv("C://Users//Enrique/Documents/GitHub/python-ml-course/datasets/customer-churn-model/Customer Churn Model.txt")

column_names = data.columns.values.tolist()
a = len(column_names)
new_data = pd.DataFrame(
    {
        'Column Name':column_names,
        'A' : np.random.randn(a),
        'B' : np.random.uniform(0,1,a)
    }
)
print(new_data)
