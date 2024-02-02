import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
data = pd.read_csv('data.csv')
print (data)

print ("-------------------Mean-------------------------")
print (data.mean())

print ("------------------Median------------------------")
print (data.median())

print ("------------------Mode--------------------------")
print (data.mode())

print ("--------------------Std-------------------------")
print (data.std())

print ("--------------------Var--------------------------")
print (data.var())

print ("---------------------Sum--------------------------")
print (data.isnull().sum())

data['Calories'] = data['Calories'].fillna(data['Calories'].mean())

print ("----------------------Sum2-----------------------")
print (data.isnull().sum())

print ("---------------------Min, Max, Count, Mean----------------")
result = data[['Duration','Maxpulse']].agg(['min','max','count','mean'])
print (result)

print ("--------------------Calories Data1---------------------------")
d1 = data[data['Calories'].between(500,1000)]
print (d1)

print ("-----------------------Calories Data2--------------------------")
d2 = data[(data['Calories']>500) & (data['Pulse']<100)]
print (d2)

print ("--------------------Maxpulse Modified-----------------------------")
data_modified=data.drop('Maxpulse',axis=1)
print (data_modified)

print ("----------------------Maxpulse---------------------------")
data.drop('Maxpulse',axis=1)
data["Calories"]=data["Calories"].astype(float).astype(int)
print (data)

print ("-------------------Scatter Plot------------------------------")
plot = data.plot.scatter(x="Duration", y="Calories", title="Scatter Plot: Duration vs Calories")
plt.show()
print ("plot: ", plot)