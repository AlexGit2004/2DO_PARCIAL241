import numpy as np
from scipy.sparse import coo_matrix

def multiplicar_matrices_sparse(matrix1, matrix2):
    matrix1_csr = matrix1.tocsr()
    matrix2_csr = matrix2.tocsr()
    
    result_matrix = matrix1_csr @ matrix2_csr
    
    return result_matrix




rows = 1000
cols = 1000
density = 0.01

row_indices_1 = np.random.randint(low=0, high=rows, size=int(rows*cols*density))
col_indices_1 = np.random.randint(low=0, high=cols, size=int(rows*cols*density))
data_1 = np.random.randint(0, 100, size=int(rows*cols*density))

row_indices_2 = np.random.randint(low=0, high=rows, size=int(rows*cols*density))
col_indices_2 = np.random.randint(low=0, high=cols, size=int(rows*cols*density))
data_2 = np.random.randint(1, 100, size=int(rows*cols*density))

sparse_matrix_1 = coo_matrix((data_1, (row_indices_1, col_indices_1)), shape=(rows, cols))
sparse_matrix_2 = coo_matrix((data_2, (row_indices_2, col_indices_2)), shape=(rows, cols))

print("Matriz dispersa 1:")
print(sparse_matrix_1)
print("\nMatriz dispersa 2:")
print(sparse_matrix_2)

matriz_mult = multiplicar_matrices_sparse(sparse_matrix_1, sparse_matrix_2)


print("Resultado de la multiplicación:")
print(matriz_mult)
