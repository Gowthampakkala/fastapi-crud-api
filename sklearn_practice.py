import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib
data={
       "experience":[1,2,3,4,5,6,7,8,9,10],
        "salary":[30000, 35000, 40000, 50000, 55000, 65000, 70000, 80000, 85000, 95000]
}
df=pd.DataFrame(data)
print(df)
X = df[["experience"]]
Y = df["salary"]
X_train,X_test,Y_train,Y_test = train_test_split( 
    X,
    Y,                                            
    test_size=0.2 , 
    random_state=42
)
print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))
model = LinearRegression()
model.fit(X_train,Y_train)
print("model trained successfully")
rf_model=RandomForestRegressor(random_state=42)
rf_model.fit(X_train,Y_train)
print("random forest trained successfully")
lr_prediction = model.predict(X_test)
rf_prediction = rf_model.predict(X_test)
print("linear Regression Prediction:")
print(lr_prediction)
print("Random Forest Prediction:")
print(rf_prediction)

joblib.dump(model, "salary_model.pkl")
print("Model Saved Successfully")
new_salary = model.predict([[11]])

print("Predicted Salary for 11 Years Experience:")
model = joblib.load("salary_model.pkl")
new_employee = pd.DataFrame({"experience": [11]})

new_salary = model.predict(new_employee)

print(new_salary)
