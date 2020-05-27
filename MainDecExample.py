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
    config['n'] =
    config['n_params'] =
    config['lr'] =
    config['omega_h'] =
    config['omega_n'] =
    config['batch_size'] =
    config['n_data'] =
    config['N_h'] =
    config['n_h'] =
    config['N_t'] =
    config['train_mat'] = ''
    config['test_mat'] = ''
    config['train_params'] = ''
    config['test_params'] = ''
    config['checkpoints_folder'] = ''
    config['graph_folder'] = ''
    config['large'] =
    config['zero_padding'] =
    config['p'] =
    config['restart'] =

    model = DecNet(config)
    model.build()
    model.test_all()
