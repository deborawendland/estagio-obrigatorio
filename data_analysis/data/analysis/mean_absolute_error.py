from sklearn.feature_selection import  SelectKBest, f_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import pandas as pd


def verify(X_train, y_train, X_val):
    print('Verifying lowest mean absolute error.')
    k_vs_score = []

    for k in range(2,16):
        selector = SelectKBest(score_func=f_regression, k=k)
        X_train2 = selector.fit_transform(X_train,y_train)

        xtest2 = selector.transform(X_val)

        mdl = RandomForestRegressor(n_estimators=100, n_jobs=-1, random_state=0)
        mdl.fit(X_train2, y_train)
        p = mdl.predict(X_train2)
        
        score = mean_absolute_error(y_train, p)
        print("K={} - MAE = {:.10f}".format(k, score))
        k_vs_score.append(score)

    return k_vs_score


def graph(k_vs_score, output_path):
    print('Generating graph lowest_mean_absolute_error.jpg')
    fig = pd.Series(k_vs_score, index=range(2,16)).plot(figsize=(10,7)).get_figure()
    fig.savefig('{output}\\lowest_mean_absolute_error.jpg'.format(output=output_path))


def get_attributes(X_train, y_train, X_val):
    print ('Getting atributes with lowest mean absolute error.')
    selector = SelectKBest(score_func=f_regression, k=8)
    selector.fit(X_train,y_train)
    # mask = selector.get_support()
    # print(X_val.columns[mask]) 

    #score das variaveis 
    # print(pd.Series(selector.scores_,index=X_train.columns))
    #p-value das variaveis
    # print(pd.Series(selector.pvalues_,index=X_train.columns))

    return selector


def calculate(X_train, y_train, X_val, output_path):
    print ('\nCalculating lowest mean absolute error')
    k_vs_score = verify(X_train, y_train, X_val)
    graph(k_vs_score, output_path)
    selector = get_attributes(X_train, y_train, X_val)
    return selector