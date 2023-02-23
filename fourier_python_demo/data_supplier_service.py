import math

import numpy as np
from numpy import ndarray, float64


def gen_x_pow() -> ndarray:
    y_array = []

    for i in range(2000):
        x = (i - 1000) * 0.001
        v = pow(float(x), 2.0)*10
        y_array.append(v)
    return np.array(y_array,dtype=float64)
