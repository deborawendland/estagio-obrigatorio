import pandas as pd

def read(filepath):
    base = pd.read_csv('..\\{filepath}'.format(filepath=filepath), sep=',')
    print ('File {filepath} imported successfully.'.format(filepath=filepath))
    return base
