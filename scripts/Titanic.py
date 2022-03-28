import pandas as pd
data = pd.read_csv("C://Users//Enrique/Documents/GitHub/python-ml-course/datasets/titanic/titanic3.csv")
a = 3
b = 2
print("a vale %d y b vale %d" %(a,b))
print(pd.isnull(data['body']))