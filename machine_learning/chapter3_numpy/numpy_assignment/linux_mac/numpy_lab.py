import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    return np.arange(n**2).reshape(-1,n)


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        return np.zeros(shape=shape, dtype=np.int)
    elif type == 1:
        return np.ones(shape=shape, dtype=np.int)
    elif type == 99:
        return np.empty(shape=shape, dtype=np.int)


def change_shape_of_ndarray(X, n_row):
    if n_row == 1:
        return X.reshape(-1)
    else:
        return X.reshape(n_row, -1)


def concat_ndarray(X_1, X_2, axis):
    try:
        if axis == 0:
            if X_1.shape[1:] == X_2.shape[1:]:
                return np.concatenate((X_1, X_2), axis=0)
            else:
                return False
        elif axis == 1:
            if X_1.shape[1:] == X_2.shape[1:]:
                return np.concatenate((X_1, X_2), axis=1)
            else:
                return False
    except:
        pass


def normalize_ndarray(X, axis, dtype=np.float32):
    n_row, n_column = X.shape
    if axis == 0:
        return (X - X.mean(axis=0).reshape(n_column, -1)) / X.std(axis=0).reshape(n_column, -1)
    elif axis == 1:
        return (X - X.mean(axis=1).reshape(n_row, -1)) / X.std(axis=1).reshape(n_row, -1)
    elif axis == 99:
        return (X - X.mean()) / X.std()


def save_ndarray(X, filename="test.npy"):
    return np.save(filename, X)


def boolean_index(X, condition):
    condition = eval(str("X") + condition)
    return np.where(condition)


def find_nearest_value(X, target_value):
    return X[np.argmin(np.abs(X - target_value))]


def get_n_largest_values(X, n):
    return sorted(X)[:n]
