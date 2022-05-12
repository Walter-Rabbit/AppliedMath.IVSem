import numpy as np


def lu_decomposition(a: np.array):

    n = len(a)
    u = np.array(a)
    list_l = []

    for i in range(0, n):
        temp_l = []
        for j in range(0, n):
            temp_l.append(0.)

        temp_l[i] = 1
        list_l.append(temp_l)

    l = np.array(list_l)

    for i in range(0, n):
        for j in range(i, n):
            l[j][i] = u[j][i] / u[i][i]

    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                l[j][i] = u[j][i] / u[i][i]

        for i in range(k, n):
            for j in range(k - 1, n):
                u[i][j] = u[i][j] - l[i][k-1] * u[k - 1][j]

    return u, l
