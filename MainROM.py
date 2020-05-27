"""

Stefania Fresca, MOX Laboratory, Politecnico di Milano
April 2019

"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
sys.stdout = open('*.out', 'w')

import utils
from ROMNet import ROMNet

if __name__ == '__main__':
    config = dict()
    config['n'] = 3                                                                # n
    config['n_params'] = 3                                                         # n_{\mu} + 1
    config['lr'] = 0.0001                                                          # starting learning rate
    config['omega_h'] = 0.5
    config['omega_n'] = 0.5
    config['batch_size'] = 40
    config['n_data'] = 49000                                                       # N_{train} * N_t
    config['N_h'] = 4096                                                           # N
    config['n_h'] = 8                                                              # N = [n_h, n_h, 64]
    config['N_t'] = 1000                                                           # N_t
    config['train_mat'] = 'data/scar/S_train.mat'                                  # training snapshot matrix
    config['test_mat'] = 'data/scar/S_test.mat'                                    # testing snapshot matrix
    config['train_params'] = 'data/scar/params_train.mat'                          # training parameter matrix
    config['test_params'] = 'data/scar/params_test.mat'                            # testing parameter matrix
    config['checkpoints_folder'] = 'checkpoints'
    config['graph_folder'] = 'graphs'
    config['large'] = False                                                        # True if data are saved in .h5 format
    config['zero_padding'] = False                                                 # True if you must use zero padding
    config['p'] = 0                                                                # size of zero padding
    config['restart'] = False                                                      # True if you want to restart training

    model = ROMNet(config)
    model.build()
    model.train_all(10000)                                                         # number of epochs
