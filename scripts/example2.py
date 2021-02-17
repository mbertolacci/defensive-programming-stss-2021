import numpy as np

def cov_exponential(x, length_scale):
    assert length_scale > 0, 'length_scale must be positive'
    return np.exp(-np.linalg.norm(x) / length_scale)

cov_exponential(np.random.normal(size = 10), -1)
