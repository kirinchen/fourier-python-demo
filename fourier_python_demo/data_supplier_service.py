import json
import math
import os

import numpy as np
from numpy import ndarray, float64


def gen_x_pow() -> ndarray:
    y_array = []

    for i in range(2000):
        x = (i - 1000) * 0.001
        v = pow(float(x), 2.0) * 10
        y_array.append(v)
    return np.array(y_array, dtype=float64)


def gen_close_sample() -> ndarray:
    y_array = []
    wd_path = os.path.dirname(__file__)
    filepath = wd_path + '/close_data.json'
    with open(filepath, 'r') as f:
        jstr = f.read()
        qobj: dict = json.loads(jstr)
        for k, v in qobj.items():
            y_array.append((v-20000)/1000)
        y_array = y_array[:2000]
        return np.array(y_array, dtype=float64)
