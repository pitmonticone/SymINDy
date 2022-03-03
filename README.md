# SIND_and_symbolic_regression

## Dependencies

In order to install dependencies, run the following:

```bash
pip install pip-tools
```

and then 

```bash
pip install -r requirements/dev.txt
```

## Commands

```bash
SymINDy propagate -s myspring -t 10
```

## High-level goals
- Passing the Build CI
- Passing the documentation (sphinx recommended, but open to alternatives)
- Have command-line interface (click recommended, but open to alternatives)
- Publish paper on JOSS
- Publish video tutorial on Youtube
- Ask to be mentioned in the related packages [here](https://github.com/dynamicslab/pysindy)

## Notes

This software is based on the one used [here](https://www.researchgate.net/publication/344475621_Orbital_Anomaly_Reconstruction_Using_Deep_Symbolic_Regression?_sg%5B0%5D=0wBU1i2FuNFv7GrI5tBwlNlsXa1lTJSK3rr_wah32-TZA0DthKdFWvdgDnhpa4j9zw4oxvvYCXRlm-dut4Ex33DScJfQ7oLG-5lmh-vk.qBVh3aGjqIRH7w-Nv8p7oDqT05hMsVnx7MgIomyCJsV_xdfT0YrIb-Tjm2I3-AnyS49FuI-t7qR0m5asIPW71g).

It combines [deap](https://deap.readthedocs.io/en/master/) with [PySINDy](https://pysindy.readthedocs.io/en/latest/).

SINDy is nice because it allows one to leverage linear ideas, while deap takes care of nonlinearities (to some extent).
See also works by Brenden (LLNL) and Max Tegmark (MIT). Deep Symbolic Regression, AI Feynman.
See also work by Facebook AI.

Why this and not simply SINDy? Because here we can get functions like the norm, the cross product, the scalar product..functions acting on vectors. In this way we can for example reconstruct the equations of motion of a two-body problem, not sure how straightforward it is for SINDy to do it.

Can we also do something with divergence? Gradient? Do we need measurements in space as well to compute the partials with finite difference? In this way we can have a bigger library.

It makes sense to add a flag for the user stating whether the system is autonomous or non autonomus: if it is not,
time is added as an additional state variable, and so we are then able to obtain \ddot{x} = - k x + sin (sin(\omega t)), for example.