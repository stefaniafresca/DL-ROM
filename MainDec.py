"""

Stefania Fresca, MOX Laboratory, Politecnico di Milano
April 2019

"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
sys.stdout = open('*.out', 'w')

import utils
from DecNet import DecNet

if __name__ == '__main__':
    config = dict()
    config['n'] = 3
    config['n_params'] = 3
    config['lr'] = 0.0001
    config['omega_h'] = 0.5
    config['omega_n'] = 0.5
    config['batch_size'] = 40
    config['n_data'] = 49000
    config['N_h'] = 4096
    config['n_h'] = 8
    config['N_t'] = 1000
    config['train_mat'] = 'data/scar/S_train.mat'
    config['test_mat'] = 'data/scar/S_test.mat'
    config['train_params'] = 'data/scar/params_train.mat'
    config['test_params'] = 'data/scar/params_test.mat'
    config['checkpoints_folder'] = 'checkpoints'
    config['graph_folder'] = 'graphs'
    config['large'] = False
    config['zero_padding'] = False
    config['p'] = 0
    config['restart'] = False                                                      # False with DecNet

    model = DecNet(config)
    model.build()
    model.test_all()
