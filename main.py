from file_parser import read_matrix

def print_menu():
    print("\nChoose what to do:")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Transpose a matrix")
    print("5. Show CSR of a matrix")
    print("6. Print matrices")
    print("0. Exit")

def show_csr(csr):
    values, cols, row_ptr = csr
    print("Values:", values)
    print("Columns:", cols)
    print("Row Pointer:", row_ptr)

def main():
    print("Welcome to my Matrix Calculator!\n")

    mat1 = read_matrix("matrix1.txt")
    mat2 = read_matrix("matrix2.txt")

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\nYour results:")
            result = mat1.add(mat2)
            result.print_matrix()

        elif choice == '2':
            print("\nYour results:")
            result = mat1.subtract(mat2)
            result.print_matrix()

        elif choice == '3':
            print("\nYour results:")
            result = mat1.multiply(mat2)
            if result:
                result.print_matrix()
            else:
                print("Can't multiply these matrices.")

        elif choice == '4':
            matrix_choice = input("Transpose which matrix? (1 or 2): ").strip()
            if matrix_choice == '1':
                print("\nTranspose of Matrix 1:")
                mat1.transpose().print_matrix()
            elif matrix_choice == '2':
                print("\nTranspose of Matrix 2:")
                mat2.transpose().print_matrix()
            else:
                print("Invalid choice.")

        elif choice == '5':
            matrix_choice = input("Show CSR of which matrix? (1 or 2): ").strip()
            if matrix_choice == '1':
                print("\nCSR of Matrix 1:")
                show_csr(mat1.to_csr())
            elif matrix_choice == '2':
                print("\nCSR of Matrix 2:")
                show_csr(mat2.to_csr())
            else:
                print("Invalid choice.")

        elif choice == '6':
            print("\nMatrix 1:")
            mat1.print_matrix()
            print("\nMatrix 2:")
            mat2.print_matrix()

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("That’s not a valid option. Pick one of the options above to get results!.")

if __name__ == "__main__":
    main()
