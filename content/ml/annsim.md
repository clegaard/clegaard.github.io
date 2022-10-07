+++
title = "Notebooks for Differentiable Programming Tutorial"
date = 2022-10-07
+++

Over the summer I was employed as a PhD Intern at *Pacific Northwest National Laboratory* in Washington.
They were kind enough to sponsor my attendance to [Annual Modeling and Simulation Conference 2022](https://scs.org/annsim/) where I delivered a tutorial on differentiable programming.

As part of the tutorial I wrote a couple of workbooks as an introduction to differentiable programming.
Specifically the notebooks cover:
* Basic use of `jax.grad`, `jax.vmap`, and how to implement a simple gradient descent optimization scheme to solve a linear regression problem.
* An exercise in how to use differentiable programming to solve geometric constraints. 
* How to define ordinary differential equations in Python, how to implement a solver in Jax, how to tune the parameters of an ODE using gradient descent, and how to implement and train a neural ODEs model in pure Jax.

The notebooks can be opened in Google Colaboratory through the links:
* [1_intro_to_jax](https://githubtocolab.com/clegaard/clegaard.github.io/blob/main/content/ml/notebooks/1_intro_to_jax.ipynb)
* [1a_exercise.ipynb](https://githubtocolab.com/clegaard/clegaard.github.io/blob/main/content/ml/notebooks/1a_exercise.ipynb)
* [1a_exercise_solution.ipynb](https://githubtocolab.com/clegaard/clegaard.github.io/blob/main/content/ml/notebooks/1a_exercise_solution.ipynb)
* [2_lotka_volterra.ipynb](https://githubtocolab.com/clegaard/clegaard.github.io/blob/main/content/ml/notebooks/2_lotka_volterra.ipynb)

![prediction](../notebooks/prediction.svg)
![loss](../notebooks/loss.svg)
