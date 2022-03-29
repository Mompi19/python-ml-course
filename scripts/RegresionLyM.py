import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

data = pd.read_csv("C://Users//Enrique/Documents/GitHub/python-ml-course/datasets/ads/Advertising.csv")
lm = smf.ols(formula = "Sales~TV",data = data).fit()


print(lm.params)
print("El modelo seria : Sales = %f + %f * TV" %(lm.params.Intercept, lm.params.TV))

print(lm.pvalues) #Parametros que validan el modelo cuanto mas pequeños estos sean

print(lm.rsquared) #Correlacion de las variables estudiadas
print(lm.rsquared_adj)

print(lm.summary()) # Resumen del modelo de regresion

sales_pred = lm.predict(pd.DataFrame(data["TV"]))
print(sales_pred)

plt.plot(data['TV'],data['Sales'],'b.', data['TV'], sales_pred,'r')
plt.show()