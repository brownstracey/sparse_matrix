import numpy as np

# Load matrices from the CSV files
matrix_1 = np.loadtxt('matrix1.csv', delimiter=',')
matrix_2 = np.loadtxt('matrix2.csv', delimiter=',')

print("Matrix 1:")
print(matrix_1)

print("Matrix 2:")
print(matrix_2)

matrix_add = matrix_1 + matrix_2
print("Matrix Addition:")
print(matrix_add)

matrix_sub = matrix_1 - matrix_2
print("Matrix Subtraction:")
print(matrix_sub)

matrix_mul = matrix_1 @ matrix_2  # Or you can use np.dot(matrix_1, matrix_2)
print("Matrix Multiplication:")
print(matrix_mul)

from scipy.sparse import coo_matrix

def load_sparse_matrix(file_path, num_rows, num_cols):
    """
    Load a sparse matrix from a CSV file (row, col, value).
    """
    # Load data from the file (like reading a list of numbers)
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)  # Read the file
    
    # Extract the rows, columns, and values from the data
    row_indices = data[:, 0].astype(int)  # The rows where the numbers are
    col_indices = data[:, 1].astype(int)  # The columns where the numbers are
    values = data[:, 2]  # The actual numbers that are in the grid
    
    # Create a sparse matrix (like making a grid with only the numbers we care about)
    sparse_matrix = coo_matrix((values, (row_indices, col_indices)), shape=(num_rows, num_cols))
    
    return sparse_matrix

# Example: Load two matrices from files
matrix_1 = load_sparse_matrix("matrix1.csv", 5, 5)  # Load the first matrix (5x5 grid)
matrix_2 = load_sparse_matrix("matrix2.csv", 5, 5)  # Load the second matrix (5x5 grid)

# Print the matrices (to see what they look like)
print(matrix_1)
print(matrix_2)
