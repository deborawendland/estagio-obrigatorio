from matplotlib.pyplot import table
import numpy as np
from sklearn.model_selection import train_test_split


def split_train_test(x, y):
    print('Spliting train-test samples.')
    X_train, X_val, y_train, y_val = train_test_split(x, y, test_size = 0.4, random_state = 0)
    print(f"Training set has {X_train.shape[0]} samples.")
    print(f"Testing set has {X_val.shape[0]} samples.")
    return X_train, X_val, y_train, y_val


def drop_column(base, attributes):
    if len(attributes['drop_cols']) > 0:
        print('Dropping {cols} colums'.format(cols=attributes['drop_cols']))
        return base.drop(columns=attributes['drop_cols'])
    elif len(attributes['select_cols']) > 0:
        print('Keeping {cols} columns'.format(cols=[attributes['select_cols']]))
        return base.loc[:,attributes['select_cols']]
        

def map_columns(base, attributes):
    for map_col in attributes['map_cols']:
        name = map_col['name']
        print('Formating column {col}.'. format(col=name))
        values = map_col['value']
        if '1' in values:
            values = {int(k) if k.isdigit() else k: v for k, v in values.items()}
            base[name] = base[name].map(values)
        else: 
            base[name] = base[name].map(values)
    return base


def replace_na_values(base):
    print('Replacing nan values.')
    base.replace(np.nan, 0, inplace = True)
    return base

def drop_na_values(base):
    print('Dropping nan values.')
    return base.dropna(how='any')

def target_attribute(base, attribute):
    print('Selecting target attribute {attr}.'.format(attr=attribute))
    y = base[attribute]
    x = base.drop([attribute], axis=1)
    return x, y
