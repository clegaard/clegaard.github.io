+++
title = "Automatic Differentiation in Python"
date = 2022-10-04
tags = ["Python", "ML", "Jax", "PyTorch"]
draft = true
+++

*Automatic Differentiation* (AD) refers to a set of techniques for differentiating computer programs with respect to their inputs.
The concept of differentiating a program deserve an explanation.
Consider the function $f(x) = \sin x$. Looking the function up in table of trig function derivatives we find that the derivative of $f$ with respect to $x$ is: $f'(x) = \cos x$

<!-- ![Some image](../diff.png) -->
<figure>
    <img src="../diff.png"
         alt="Elephant at sunset">
    <figcaption>TODO give credits</figcaption>
</figure>


In the context of ML this provides the basis for implementing gradient descent based optimization of a models parameters.

[Automatic Differentiation in Machine Learning](https://arxiv.org/abs/1502.05767)

What AD is not:
* Symbolic differentation
* Numerical Differentiation

# Jax

``` Python
import jax.numpy as jnp
from jax import grad, jit, vmap


def f(x):
    v = x
    for i in range(4):
        v = 4*v*(1-v)
    return v

df = grad(f, argnums=(0,))
```

Compared to 
* [diffrax](https://github.com/patrick-kidger/diffrax)

# PyTorch

Recently a new module [functorch](https://pytorch.org/functorch/stable/#functorch) was added to PyTorch that allows models to be implenented in a similar style to Jax.
At the time of writing there are still limitations

Notable solvers out there are:
* [torchdyn](https://github.com/DiffEqML/torchdyn)
* [torchdiffeq](https://github.com/rtqichen/torchdiffeq)


# TensorFlow

# Performance
