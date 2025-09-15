# modeling.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def simple_regression(df):
    x = df[['rating_num']]
    y = df['price']
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)
    model = LinearRegression()
    model.fit(x_train, y_train)
    preds = model.predict(x_test)
    return {
        "coef": model.coef_.tolist(),
        "intercept": float(model.intercept_),
        "mse": float(mean_squared_error(y_test, preds))
    }
