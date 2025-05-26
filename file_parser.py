from classes import Matrix

def read_matrix(filename):
    with open(filename, "r") as f:
        first_line = f.readline().strip()
        row_col = first_line.split()
        rows = int(row_col[0])
        cols = int(row_col[1])
        data = {}

        for line in f:
            parts = line.strip().split()
            i = int(parts[0])
            j = int(parts[1])
            val = int(parts[2])
            data[(i, j)] = val

    return Matrix(rows, cols, data)