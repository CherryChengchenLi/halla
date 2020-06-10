#TODO: move to the appropriate directory

from tools import HAllA
from os.path import dirname, abspath, join

X_file = join(dirname(abspath(__file__)), 'data', 'X_line1_16_16.txt')
Y_file = join(dirname(abspath(__file__)), 'data', 'Y_line1_16_16.txt')

pdist_metric = 'nmi'

test_halla = HAllA(discretize_func='equal-freq', discretize_num_bins=4,
                  pdist_metric=pdist_metric, seed=123)

test_halla.load(X_file, Y_file)
# test_halla.run()
# print(test_halla.X_hierarchy.distance_matrix)