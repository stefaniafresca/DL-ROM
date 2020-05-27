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
    config['n'] =                                                                  # reduced dimension
    config['n_params'] =                                                           # number of parameters (time excluded)
    config['lr'] =                                                                 # starting learning rate
    config['omega_h'] =
    config['omega_n'] =
    config['batch_size'] =
    config['n_data'] =                                                             # N_{train} * N_t
    config['N_h'] =                                                                # FOM dimension
    config['n_h'] =                                                                # N_h = [n_h, n_h, 64]
    config['N_t'] =                                                                # N_t
    config['train_mat'] = ''                                                       # training snapshot matrix
    config['test_mat'] = ''                                                        # testing snapshot matrix
    config['train_params'] = ''                                                    # training parameter matrix
    config['test_params'] = ''                                                     # testing parameter matrix
    config['checkpoints_folder'] = ''
    config['graph_folder'] = ''
    config['large'] =                                                              # True if data are saved in .h5 format
    config['zero_padding'] =                                                       # True if you must use zero padding
    config['p'] =                                                                  # size of zero padding
    config['restart'] =

    model = ROMNet(config)
    model.build()
    model.train_all(10000)                                                         # number of epochs
