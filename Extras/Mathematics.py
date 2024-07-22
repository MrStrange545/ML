import numpy as np

def menu():
    print("1. Get Matrix")
    print("2. Get Inverse")
    print("3. Get Determinant")
    print("4. Get RREF")
    print("5. Get Solution")
    print("6. Check Similar")
    print("7. Check Equivalent")
    print("8. Matrix Multiplication")
    choice = input("Enter your choice: ")
    if choice == "1":
        get_matrix()
    elif choice == "2":
        get_inverse()
    elif choice == "3":
        get_determinant()
    elif choice == "4":
        get_rref()
    elif choice == "5":
        get_solution()
    elif choice == "6":
        check_similar()
    elif choice == "7":
        check_equivalent()
    elif choice == "8":
        matrix_multiplication()
    else:
        print("Invalid choice")

def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter element ({i},{j}): ")))
        matrix.append(row)
    return np.array(matrix)

def get_inverse():
    matrix = get_matrix()
    if np.linalg.det(matrix) != 0:
        inverse = np.linalg.inv(matrix)
        print("Inverse: ")
        print(inverse)
    else:
        print("Matrix is singular")

def get_determinant():
    matrix = get_matrix()
    det = np.linalg.det(matrix)
    print("Determinant: ", det)

def get_rref():
    matrix = get_matrix()
    rref = np.array(matrix)
    lead = 0
    rowCount = rref.shape[0]
    columnCount = rref.shape[1]
    for r in range(rowCount):
        if lead >= columnCount:
            return rref
        i = r
        while rref[i, lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return rref
        rref[[i, r]] = rref[[r, i]]
        lv = rref[r, lead]
        rref[r] = rref[r] / lv
        for i in range(rowCount):
            if i != r:
                lv = rref[i, lead]
                rref[i] = rref[i] - lv * rref[r]
        lead += 1
    print(rref)

def get_solution():
    matrix = get_matrix()
    b = get_matrix()
    solution = np.linalg.solve(matrix, b)
    print("Solution: ")
    print(solution)

def check_similar():
    matrix1 = get_matrix()
    matrix2 = get_matrix()
    if matrix1.shape != matrix2.shape:
        print("Matrices are not similar")
    else:
        p = np.linalg.inv(matrix1) @ matrix2
        if np.allclose(np.linalg.det(p), 1):
            print("Matrices are similar")
        else:
            print("Matrices are not similar")

def check_equivalent():
    matrix1 = get_matrix()
    matrix2 = get_matrix()
    if matrix1.shape != matrix2.shape:
        print("Matrices are not equivalent")
    else:
        p = np.linalg.inv(matrix1) @ matrix2
        if np.allclose(np.linalg.det(p), 1):
            print("Matrices are equivalent")
        else:
            print("Matrices are not equivalent")

def matrix_multiplication():
    matrix1 = get_matrix()
    matrix2 = get_matrix()
    if matrix1.shape[1] != matrix2.shape[0]:
        print("Matrices cannot be multiplied")
    else:
        result = np.matmul(matrix1, matrix2)
        print("Result: ")
        print(result)

if __name__ == "__main__":
    menu()