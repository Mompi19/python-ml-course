import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("C://Users//Enrique/Documents/GitHub/python-ml-course/datasets/customer-churn-model/Customer Churn Model.txt")

k = int(np.ceil(1+np.log2(3333)))
print(k)
# figure,axs = plt.subplots(2,2, sharey = True, sharex= True)

# data.plot(kind = 'scatter',x="Day Mins", y="Day Charge",ax=axs[0][0])
# data.plot(kind = 'scatter',x="Night Mins", y="Night Charge",ax=axs[0][1])
# data.plot(kind = 'scatter',x="Day Calls", y="Night Charge",ax=axs[1][0])
# data.plot(kind = 'scatter',x="Night Calls", y="Day Charge",ax=axs[1][1])
plt.hist(data["Day Calls"],bins= k)

plt.show()



