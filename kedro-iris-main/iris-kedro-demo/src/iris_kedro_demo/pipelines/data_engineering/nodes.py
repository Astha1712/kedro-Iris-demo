"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report


def preprocessing(iris):
    features = iris.columns[:-1]
    target = iris.columns[-1]
    X = iris[features]
    y = iris[target]
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y

def split_data(X, y, params:dict):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =params["test_size"], random_state=params["random_state"])
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print("Accuracy Of Model is: ",accuracy)
    print(report)
    return accuracy, report
 