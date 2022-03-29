from matplotlib.pyplot import plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = 1.5 + 2.5 * np.random.randn(100)
res = 0 + 6 * np.random.randn(100)

y_act = 4 + 7 * x + res
y_pred = 4 + 7 * x

data = pd.DataFrame(
    {
        "x" : x,
        "y Real": y_act,
        "y Prediccion": y_pred
    }
)
y_mean = [np.mean(y_act) for i in range(1, len(x) + 1)]

#plt.plot(data['x'],data['y Real'],'b.',data['x'],data['y Prediccion'], 'r')


y_m = np.mean(y_act)
data["SSR"]=(data["y Prediccion"]-y_m)**2 #Distancia de la prediccion a la media en un punto
data["SSD"]=(data["y Prediccion"]-data["y Real"])**2 #Distancia de la prediccion al valor real de y en un punto
data["SST"]=(data["y Real"]-y_m)**2 #Distancia del valor real a la media, independiente de la calidad del modelo

#El objetivo de la regresion lineal es conseguir que la distancia total de nuestro modelo al valor real represente un porcentaje 
#lo menor posible respecto a la distancia total (minimizar SSD, maximizar SSR)

SSR = sum(data["SSR"])
SSD = sum(data["SSD"])
SST = sum(data["SST"])
R2 = SSR/SST

print('SSR: %f ; SSD: %f ; SST: %f ; SST C: %f ; R2: %f' %(SSR,SSD,SST,SSR+SSD,R2))


#plt.hist(res)

 
# Obtenemos la recta de regresion: y = a + b*x
x_m = np.mean(data['x'])
y_m = np.mean(data['y Real'])

b = sum((data['x']-x_m)*(data['y Real']-y_m))/sum((data['x']-x_m)**2)
a = y_m - b * x_m
print('Modelo obtenido: y = %f + %f * x'%(a,b))

data["y_model"] = a + b * data["x"]
print(data.head())
plt.plot(data['x'],data['y Real'],'b.',data['x'],data['y Prediccion'], 'r',data['x'],data['y_model'], 'g')

SSRR = sum((data["y_model"]-y_m)**2)
SSDR = sum((data["y_model"]-data["y Real"])**2)
SSTR = sum((data["y Real"]-y_m)**2)
R2R = SSRR/SSTR
print('SSRR: %f ; SSDR: %f ; SSTR: %f ; SSTR C: %f ; R2R: %f' %(SSRR,SSDR,SSTR,SSRR+SSDR,R2R))
print('Comparacion de modelos R2: %f ; R2R: %f' %(R2,R2R))

plt.show()
