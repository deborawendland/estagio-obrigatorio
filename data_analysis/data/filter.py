import numpy as np

def drop_column(base, attributes):
    if len(attributes['drop_cols']) > 0:
        print('Dropping {cols} colums'.format(cols=attributes['drop_cols']))
        return base.drop(columns=attributes['drop_cols'])
    elif len(attributes['select_cols']) > 0:
        print('Keeping {cols} columns'.format(cols=[attributes['select_cols']]))
        return base.loc[:,[attributes['select_cols']]]
        

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


def nan_values(base):
    print('Replacing nan values.')
    base.replace(np.nan, 0, inplace = True)
    return base


def target_attribute(base, attribute):
    print('Selecting target attribute {attr}.'.format(attr=attribute))
    y = base[attribute]
    x = base.drop([attribute], axis=1)
    return x, y