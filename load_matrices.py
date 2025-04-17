import numpy as np
from scipy.sparse import coo_matrix

# --- 1: Dense Matrices ---

# Load two matrices from CSV files. These should just be standard comma-separated grids of numbers.
matrix1 = np.loadtxt('matrix1.csv', delimiter=',')
matrix2 = np.loadtxt('matrix2.csv', delimiter=',')

print("Here's Matrix 1:")
print(matrix1)

print("\nAnd here's Matrix 2:")
print(matrix2)

# math operations
added = matrix1 + matrix2
print("\nMatrix 1 + Matrix 2:")
print(added)

subtracted = matrix1 - matrix2
print("\nMatrix 1 - Matrix 2:")
print(subtracted)

multiplied = matrix1 @ matrix2  
print("\nMatrix 1 multiplied by Matrix 2:")
print(multiplied)


# --- Part 2: Sparse Matrices ---

def load_sparse_matrix(file_path, rows, cols):
    """
    Loads a sparse matrix from a CSV file where each row looks like:
    row_index, column_index, value

    This approach is handy for large matrices where most values are zero.
    """
    try:
        raw_data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    except Exception as e:
        print(f"Could not load file {file_path}: {e}")
        return None

    row_idx = raw_data[:, 0].astype(int)
    col_idx = raw_data[:, 1].astype(int)
    values = raw_data[:, 2]

    # Build the sparse matrix in COO format
    return coo_matrix((values, (row_idx, col_idx)), shape=(rows, cols))


# Load example sparse matrices 
sparse1 = load_sparse_matrix('matrix1.csv', 5, 5)
sparse2 = load_sparse_matrix('matrix2.csv', 5, 5)

print("\nSparse Matrix 1:")
print(sparse1)

print("\nSparse Matrix 2:")
print(sparse2)

