import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
salary_data = pd.read_csv('Salary_Data.csv')
print (salary_data)


X = salary_data["YearsExperience"]
Y = salary_data["Salary"]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.33,random_state=0)

regressor = LinearRegression()
model = regressor.fit(X_train.values.reshape(-1, 1),Y_train.values.reshape(-1, 1))

print(model.coef_)
print(model.intercept_)

Y_predict = model.predict(X_test.values.reshape(-1,1))
plt.title("Salary/Years of XP")
plt.ylabel("Salary $")
plt.xlabel("Years")
plt.scatter(X_test,Y_test,color="blue",label="real data")
plt.plot(X_test,Y_predict,color="red",label="linear model")
plt.legend()
plt.show()

mean_squared_error(Y_test, Y_predict)