import numpy as np
import scipy.sparse as sp
from multiprocessing import Pool, cpu_count
import time


def multiply_row(args):
    row, matrix1, matrix2 = args
    result_row = matrix1[row, :] @ matrix2
    return result_row

def parallel_multiply(matrix1, matrix2):
    num_procs = cpu_count()
    rows = matrix1.shape[0]

    args = [(row, matrix1, matrix2) for row in range(rows)]

    with Pool(num_procs) as pool:
        result_rows = pool.map(multiply_row, args)
    
    result_matrix = sp.vstack(result_rows, format='csr')
    
    return result_matrix


rows = 1000
cols = 1000

sparse_matrix1 = sp.random(rows, cols, density=0.01, format='csr')
sparse_matrix2 = sp.random(cols, rows, density=0.01, format='csr')


if __name__ == '__main__':
    start_time = time.time()
    result_sparse_matrix = parallel_multiply(sparse_matrix1, sparse_matrix2)
    end_time = time.time()

    print(f"Multiplicación completada en {end_time - start_time} segundos.")
    print(f"Matriz resultante tiene forma: {result_sparse_matrix.shape}")
    print(result_sparse_matrix.toarray())
    print("\n\nMultiplicacion de matriz en paralelo\n")
    print(result_sparse_matrix)
