from ipywidgets import interactive
from IPython.display import SVG,display, Image 
from graphviz import Source
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from six import StringIO
import pydotplus
from subprocess import call
import os
import pydot


def create_graph(dot_path, png_path):
    print('Creating .png tree.')
    (graph,) = pydot.graph_from_dot_file(dot_path)
    graph.write_png(png_path)  


def create_decision_tree(output_path, X, y, features_label, class_label, crit, split, depth, min_samples_split, min_samples_leaf=0.2):
    print ('Creating decision tree.')
    estimator = DecisionTreeClassifier(
            random_state = 0,
            criterion = crit,
            splitter = split,
            max_depth = depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf
        )

    estimator.fit(X, y)

    dot_path = '{output_path}\\binary-tree-{crit}.dot'.format(output_path=output_path, crit=crit)
    png_path = '{output_path}\\binary-tree-{crit}.png'.format(output_path=output_path, crit=crit)
    
    os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

    print('Creating .dot tree.')
    dotfile = StringIO()
    dotfile = open(dot_path, 'w')
    export_graphviz(estimator,
        feature_names=features_label,
        class_names=class_label,
        impurity=True,
        filled = True,
        out_file=dotfile)
    dotfile.close()

    create_graph(dot_path, png_path)


def generate(table, base, output_path, crit, split):
    print ('\nGenerating binary tree.')

    X, y = table, base['scorelmup']
    features_label = table.columns
    class_label = ['0','1']

    create_decision_tree(output_path, X, y, 
        features_label, class_label, 
        crit = crit,
        split = split,
        depth=30,
        min_samples_split=5,
        min_samples_leaf=5)
    







