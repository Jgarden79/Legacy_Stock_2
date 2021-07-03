import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier
from lazypredict.Supervised import LazyClassifier
import numpy as np

def feature_prep():
    raw = pd.read_csv("clean_raw.csv")
    X_y_df = raw.drop(['Date', 'Instrument', 'fwd_ret',"Timeframe","GICS Sector Name" ], axis=1)
    X = X_y_df.drop('quartiles', axis = 1).to_numpy()
    y = X_y_df['quartiles'].to_numpy()

    return X, y

def pipeline(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    param_grid = {'n_estimators': [200, 500],
                  'max_depth':[4,5,6,7],
                  "max_features": ['auto', 'sqrt' ,'log2'],
                  "criterion": ['gini', 'entropy'],
                  "bootstrap": [False, True]}
    etc = ExtraTreesClassifier(random_state=42)
    clf = GridSearchCV(etc, param_grid=param_grid, cv=5)
    clf.fit(X_train, y_train)
    t = clf.best_params_
    print(t)
    return t, X_train, X_test, y_train, y_test

def run_model(t, X_train, X_test, y_train, y_test):
    return

if __name__=="__main__":
    X, y = feature_prep()
    t, X_train, X_test, y_train, y_test = pipeline(X,y)
