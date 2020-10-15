import pandas as pd
import numpy as np

def optimized_elastic_net_linear_categorical_regression(dataframe, predictors, target):
    """
    ElasticNet, Cross-validation, Grid search
    """
    
    from sklearn.linear_model import ElasticNet
    from sklearn.model_selection import GridSearchCV
    
    subset_categorical = dataframe[predictors].applymap(lambda x: str(round(10*x)))
    dummies = pd.get_dummies(subset_categorical, drop_first=True)

    X = dummies.to_numpy()
    y = dataframe[[target]].to_numpy()

    enet = ElasticNet(random_state=42, max_iter=10000)

    params_space = [{'alpha': np.logspace(-4, -0.5, 30)}]

    clf = GridSearchCV(enet, params_space, cv=5, refit=True)
    clf.fit(X, y)
    
    return clf


def optimized_elastic_net_linear_3_levels_categorical_regression(dataframe, predictors, target):
    """
    ElasticNet, Cross-validation, Grid search
    Porém usado para a abordagem de 3 níveis
    """
    
    from sklearn.linear_model import ElasticNet
    from sklearn.model_selection import GridSearchCV
    
    subset_categorical = dataframe[predictors]
    dummies = pd.get_dummies(subset_categorical, drop_first=True)

    X = dummies.to_numpy()
    y = dataframe[[target]].to_numpy()

    enet = ElasticNet(random_state=42, max_iter=10000)

    params_space = [{'alpha': np.logspace(-4, -0.5, 30)}]

    clf = GridSearchCV(enet, params_space, cv=5, refit=True)
    clf.fit(X, y)
    
    return clf