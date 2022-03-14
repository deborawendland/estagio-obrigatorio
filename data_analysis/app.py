import pandas as pd
import sys
import os
from data import filter, graph
from data.analysis import mean_absolute_error, binary_tree, logistic_regression
from files import config, database


def main():
    config_file = config.read()
    os.mkdir('..\\{filepath}'.format(filepath=config_file['output_path']))

    for file in config_file['files']:
        print ('\nAnalysing data from: {base}'.format(base=file['basename']))

        output_path = '..\\{filepath}\\{base}'.format(filepath=config_file['output_path'], base=file['basename'])
        os.mkdir(output_path)

        base = database.read(file['filepath'])

        base = filter.drop_column(base, file['attributes'])
        base = filter.map_columns(base, file['attributes'])

        if 'dropna' in file['attributes']['filter']:
                base = filter.drop_na_values(base)
        elif 'replacena' in file['attributes']['filter']:
            base = filter.replace_na_values(base)

        x, y = filter.target_attribute(base, file['attributes']['target_attribute'])

        X_train, X_val, y_train, y_val = filter.split_train_test(x, y)
        selector = mean_absolute_error.calculate(X_train, y_train, X_val, output_path)

        x = logistic_regression.generate_table(base)
        X_train, X_val, y_train, y_val = filter.split_train_test(x, y)
        logistic_regression.calculate(X_train,y_train, X_val, y_val)

        binary_tree.generate(x, base, output_path, 
                            crit=config_file['binary-tree']['crit'], 
                            split=config_file['binary-tree']['split'], 
                            target=file['attributes']['target_attribute'])

        cols = base.columns

        for name in cols:        
            graph.plot_graph(base, name, output_path)

if __name__ == "__main__":
    main()