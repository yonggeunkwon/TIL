import numpy as np

def vector_size_check(*vector_variables):
    vector_size = [len(vector_variable) for vector_variable in vector_variables]
    return True if len(set(vector_size)) == 1 else False


def vector_addition(*vector_variables):
    if len(set([len(vector_variable) for vector_variable in vector_variables])) != 1:
        raise ArithmeticError("ArithmeticError")
    return [sum(vector_variable) for vector_variable in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return None


def scalar_vector_product(alpha, vector_variable):
    return [alpha * num for num in vector_variable]


def matrix_size_check(*matrix_variables):
    matrix_size = [len(matrix_variable) for matrix_variable in matrix_variables]
    return True if len(set(matrix_size)) == 1 else False


def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return None
