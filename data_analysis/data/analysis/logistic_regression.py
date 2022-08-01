from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import metrics

def get_columns():
    print('Enter selected columns: [press 0 to exit]')
    cols = []
    while (True):
        col = input('Column: ')
        if col not in "0":
            if col in "1":
                cols = ['partner', 'age1st_preg','lmup2','lmup1', 'lmup3', 'lmup4', 'lmup5']
                break
            elif col in "2":
                cols = ['ZIdadeM', 'YRF2_REC', 'YRF1_REC', 'RDE5', 'RDE4', 'ISD5_cat','EV5_REC', 'DR28', 'XSS1', 'DE1_REC','Wdesfecho']
                break
            else:
                cols.append(col)
        else:
            break
    print ('Selected columns: {columns}'.format(columns=cols))
    
    return cols

def generate_table(base):
    print('\nGenerating regression table')
    cols = get_columns()
    table = base.loc[:,cols]
    return table

def calculate(X_train,y_train, X_val, y_val):
    print('\nCalculating logistic regression.')
    modelo = LogisticRegression()
    model_fit = modelo.fit(X_train,y_train)
    coef = modelo.coef_
    intercept = modelo.intercept_
    
    modelo2 = modelo.predict(X_val) #prediction
    acc = accuracy_score(y_val, modelo2) #accuracy
    print (acc)
    print(metrics.classification_report(y_val, modelo2))