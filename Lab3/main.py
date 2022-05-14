import numpy as np
from tools.luDecomposition import lu_decomposition
from tools.inverseMatrix import inverse_matrix

n = 5
a = np.array([[10., -3., 5.], [-7., 6., -1.], [0., 2., 5.]])

l, u = lu_decomposition(a)
inverse_a = inverse_matrix(a)

print("A:")
print(a)

print("L:")
print(l)

print("U:")
print(u)

print("L * U:")
print(l.dot(u))

print("Inverse A:")
print(inverse_a)

print("(Inverse A) * A:")
print(inverse_a.dot(a))
