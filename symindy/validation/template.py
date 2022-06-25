"""Simple template pipeline for evaluating the reconstruction of dynamical
system with SymINDy."""

import matplotlib.pyplot as plt
import numpy as np
import pysindy.utils.odes as odes
from sklearn.metrics import r2_score

from symindy.symindy.symindy import SymINDy
from symindy.systems import non_linear_systems as nl
from symindy.systems.dynamical_system import DynamicalSystem
from symindy.systems.non_linear_systems import lorenz
from symindy.validation.utils import plot2d, plot3d, split

### Non linear 2d dynamical system
system = nl.myspring

# time range
time_start = 0
time_end = 10
nsamples = 500
time_span = np.linspace(time_start, time_end, nsamples, endpoint=False)
# initial conditions
x0 = [-2, 2]  # change depending on the dimensionality of the system

# istantiate dynamical system and simulate results
dynsys = DynamicalSystem(system, x0=x0)
x, xdot = dynsys.simulate(time_start, time_end, nsamples)

# Split the simulated data into the train and test sets
ratio = 0.33
x_tr, x_te = split(x, ratio)
xdot_tr, xdot_te = split(xdot, ratio)
time_tr, time_te = split(time_span, ratio)

# istantiate symINDy
symindy = SymINDy(verbose=False, sparsity_coef=0.1, library_name="polynomial", ngen=20)

# fit symINDy on the training data
symindy.fit(x_tr, xdot_tr, time_tr)

# predict NB! x0 == x_te[0]
x_te_pred, xdot_te_pred = symindy.predict(x_te[0], time_te)

# assess predictions via correlation
corr_x = r2_score(x_te, x_te_pred)
corr_xdot = r2_score(xdot_te, xdot_te_pred)

# aggregate the data in a dict
data = {
    "x_te": x_te,
    "x_te_pred": x_te_pred,
    "xdot_te": xdot_te,
    "xdot_te_pred": xdot_te_pred,
    "x_metric": {"name": "r2", "value": corr_x},
    "xdot_metric": {"name": "r2", "value": corr_xdot},
    "time": time_te
}

# plot original and predicted data
fig, ax = plot2d(data, figtitle=system.__class__.__name__)
plt.show()
