import numpy as np

def no_numpy_scalar(v1, v2):

    result = sum([v1[i]*v2[i] for i in range(len(v1))])
    return result

def numpy_scalar (v1, v2):

    result = v1.dot(v2)
    return result
