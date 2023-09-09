# Seminar 1
# Numpy fundamentals

import numpy as np

def random_matrix(n: int) -> np.array:
    return np.random.randint(0, 256, size=(n, n, 3), dtype=np.uint8)


def broadcast_array(a: np.array, n: int) -> np.array:
    if len(a.shape) != 1:
        raise ValueError("Input array 'a' must be 1D.")

    return np.tile(a, (n, 1))

def inplace_operation(a: np.array, b: np.array) -> None:
    a[:] = ((a + b) * (-a / 2))
def get_elements(a: np.array, indices: np.array) -> np.array:
    return a[np.arange(len(a)), indices]
def self_inners(a: np.array) -> np.array:
    return np.dot(a, a.T)
