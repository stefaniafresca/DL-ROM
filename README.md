# DL-ROM

Source code for deep learning-based reduced order models in cardiac electrophysiology.

### Abstract. 
Predicting the electrical behavior of the heart, from the cellular scale to the tissue level, relies on the numerical approximation of coupled nonlinear dynamical systems. These systems describe the cardiac action potential, that is the polarization/depolarization cycle occurring at every heart beat that models the time evolution of the electrical potential across the cell membrane, as well as a set of ionic variables. Multiple solutions of these systems, corresponding to different model inputs, are required to evaluate outputs of clinical interest, such as activation maps and action potential duration. More importantly, these models feature coherent structures that propagate over time, such as wavefronts. These systems can hardly be reduced to lower dimensional problems by conventional reduced order models (ROMs) such as, e.g., the reduced basis method. This is primarily due to the low regularity of the solution manifold (with respect to the problem parameters), as well as to the nonlinear nature of the input-output maps that we intend to reconstruct numerically. To overcome this difficulty, in this paper we propose a new, nonlinear approach relying on deep learning (DL) algorithms—such as deep feedforward neural networks and convolutional autoencoders—to obtain accurate and efficient ROMs, whose dimensionality matches the number of system parameters. We show that the proposed DL-ROM framework can efficiently provide solutions to parametrized electrophysiology problems, thus enabling multi-scenario analysis in pathological cases. We investigate four challenging test cases in cardiac electrophysiology, thus demonstrating that DL-ROM outperforms classical projection-based ROMs.

### Citation
```
Fresca S, Manzoni A, Dedè L, Quarteroni A (2020) Deep learning-based reduced order models in cardiac electrophysiology. PLoS ONE 15(10): e0239416. https://doi.org/10.1371/journal.pone.0239416
```

For the full implementation of the DL-ROM neural network, please write to stefania.fresca@polimi.it.
