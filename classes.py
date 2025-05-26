class Matrix:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        self.values = values if values else {}

    def print_matrix(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(str(self.values.get((i, j), 0)))
            print(" ".join(row))

    def add(self, other):
        result = {}
        for key in self.values:
            result[key] = self.values[key]
        for key in other.values:
            if key in result:
                result[key] += other.values[key]
            else:
                result[key] = other.values[key]
        return Matrix(self.rows, self.cols, result)

    def subtract(self, other):
        result = {}
        for key in self.values:
            result[key] = self.values[key]
        for key in other.values:
            if key in result:
                result[key] -= other.values[key]
            else:
                result[key] = -other.values[key]
        return Matrix(self.rows, self.cols, result)

    def multiply(self, other):
        if self.cols != other.rows:
            print("Matrix sizes don't work for multiplication")
            return None
        result = {}
        for (i, j), val in self.values.items():
            for k in range(other.cols):
                if (j, k) in other.values:
                    if (i, k) not in result:
                        result[(i, k)] = 0
                    result[(i, k)] += val * other.values[(j, k)]
        return Matrix(self.rows, other.cols, result)

    def transpose(self):
        new_data = {}
        for (i, j), val in self.values.items():
            new_data[(j, i)] = val
        return Matrix(self.cols, self.rows, new_data)

    def to_csr(self):
        values = []
        columns = []
        row_ptr = [0]
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.values:
                    values.append(self.values[(i, j)])
                    columns.append(j)
                    count += 1
            row_ptr.append(count)
        return values, columns, row_ptr