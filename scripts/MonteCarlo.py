import numpy as np
import matplotlib.pyplot as plt

n = 10000
n_exp = 1000
nFavorable = 0
pi_avg = 0
pi_value_list = []
for i in range(n_exp):
    value = 0
    x = np.random.uniform(0,1,n).tolist()
    y = np.random.uniform(0,1,n).tolist()
    for j in range(n):
        z = x[j]**2 + y[j]**2
        if(z<=1):
            value +=1
    float_value = float(value)
    pi_value = float_value * 4 /n
    pi_value_list.append(pi_value)
    pi_avg += pi_value
pi = pi_avg/n_exp
print(pi)
plt.plot(pi_value_list)
plt.show()
