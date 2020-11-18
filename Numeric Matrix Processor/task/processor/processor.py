from copy import deepcopy


def matrix_create(a1):
    mat = []
    for a in range(a1):
        mat.append(input().split())
    return mat


def adding():
    n1, m1 = input("Enter size of first matrix: ").split()
    n1, m1 = int(n1), int(m1)
    print("Enter first matrix:")
    mat = matrix_create(n1)

    n2, m2 = input("Enter size of second matrix: ").split()
    n2, m2 = int(n2), int(m2)
    print("Enter second matrix:")
    mat2 = matrix_create(n2)

    if int(n1) == int(n2) and int(m1) == int(m2):
        print("The result is:")
        for x in range(n1):
            for y in range(m1):
                print(float(mat[x][y]) + float(mat2[x][y]), end=" ")
            print()
    else:
        print("The operation cannot be performed.\n")


def multiply_const():
    n, m = input("Enter size of matrix: ").split()
    n, m = int(n), int(m)
    print("Enter matrix:")
    mat3 = matrix_create(int(n))

    number = float(input("Enter constant: "))
    print("The result is:")
    for i in mat3:
        for j in i:
            print(number * float(j), end=" ")
        print()
    print()


def multiply_mat():
    n11, m11 = input("Enter size of first matrix: ").split()
    n11, m11 = int(n11), int(m11)
    print("Enter first matrix:")
    mat6 = matrix_create(n11)

    n22, m22 = input("Enter size of second matrix: ").split()
    n22, m22 = int(n22), int(m22)
    print("Enter second matrix:")
    mat7 = matrix_create(n22)

    if int(m11) == int(n22):
        print("The result is:")
        for x in range(n11):
            for y in range(m22):
                number = 0
                for z in range(m11):
                    number += float(mat6[x][z]) * float(mat7[z][y])
                print(number, end=" ")
            print()
        print()
    else:
        print("The operation cannot be performed.\n")


def transpose():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    option1 = int(input("Your choice: "))
    n5, m5 = input("Enter size of matrix: ").split()
    n5, m5 = int(n5), int(m5)
    print("Enter matrix:")
    mat9 = matrix_create(int(n5))
    print("The result is:")
    if option1 == 1:
        for x9 in range(n5):
            for y9 in range(m5):
                print(mat9[y9][x9], end=" ")
            print()
    elif option1 == 2:
        for x1 in range(n5):
            for y1 in range(m5):
                print(mat9[n5 - 1 - y1][m5 - 1 - x1], end=" ")
            print()
    elif option1 == 3:
        for x2 in range(n5):
            for y2 in range(m5):
                print(mat9[x2][m5 - 1 - y2], end=" ")
            print()
    elif option1 == 4:
        for x3 in range(n5):
            for y3 in range(m5):
                print(mat9[n5 - 1 - x3][y3], end=" ")
            print()
    print()


def matrix_three(mat):
    deter1 = (float(mat[0][0]) * float(mat[1][1]) * float(mat[2][2])
              + float(mat[0][1]) * float(mat[1][2]) * float(mat[2][0])
              + float(mat[0][2]) * float(mat[1][0]) * float(mat[2][1])
              - float(mat[0][2]) * float(mat[1][1]) * float(mat[2][0])
              - float(mat[0][0]) * float(mat[1][2]) * float(mat[2][1])
              - float(mat[0][1]) * float(mat[1][0]) * float(mat[2][2]))
    return deter1


def matrix_recursive(matt):
    degree = len(matt)
    # print(f"degree: {degree}")
    if degree == 3:
        # print(f"deter:  {matrix_three(matt)}")
        return matrix_three(matt)
    else:
        total = 0
        for i in range(0, degree):
            matt1 = [row[:i] + row[i + 1:] for row in matt[1:degree]]
            # print(i)
            # print(matt1)
            total += float(matt[0][i]) * (-1) ** (1 + i + 1) * matrix_recursive(matt1)
            # print(total)
        return total


def determinant_calculate():
    n, m = input("Enter size of matrix: ").split()
    n, m = int(n), int(m)
    print("Enter matrix:")
    mat5 = matrix_create(int(n))
    global new_mat
    new_mat = deepcopy(mat5)
    determinant = 0
    if n == 1:
        determinant = float(mat5[0][0])
    elif n == 2:
        determinant = float(mat5[0][0]) * float(mat5[1][1]) - float(mat5[0][1]) * float(mat5[1][0])
    elif n == 3:
        determinant = matrix_three(mat5)
    elif n > 3:
        determinant = matrix_recursive(mat5)
    return determinant


def det_print():
    deter = determinant_calculate()
    print("The result is:")
    print(deter)
    print()


def matrix_inverse():
    determinant1 = determinant_calculate()
    # print(determinant1)
    # print(new_mat)
    degree = len(new_mat)
    new_matt = deepcopy(new_mat)
    new_matt_trans = deepcopy(new_mat)
    for i in range(0, degree):
        for j in range(0, degree):
            new_matt1 = deepcopy(new_mat)
            # print(new_mat)
            matt1 = [new_matt1[k][:j] + new_matt1[k][j + 1:] for k in range(degree) if int(k) != i]
            # print(f"i = {i} {type(i)}, j = {j} {type(j)}")
            # print(matt1)
            # print(new_matt1)
            n1 = degree - 1
            # print(n1)
            determinant11 = 0
            if n1 == 1:
                determinant11 = float(matt1[0][0])
            elif n1 == 2:
                determinant11 = float(matt1[0][0]) * float(matt1[1][1]) - float(matt1[0][1]) * float(matt1[1][0])
            elif n1 == 3:
                determinant11 = matrix_three(matt1)
            elif n1 > 3:
                determinant11 = matrix_recursive(matt1)
            # print((-1) ** (1 + i + 1 + j) * determinant11)
            new_matt[i][j] = (-1) ** (1 + i + 1 + j) * determinant11
    # print(new_matt)
    for x91 in range(degree):
        for y91 in range(degree):
            new_matt_trans[x91][y91] = new_matt[y91][x91]
    print("The result is:")
    for i in new_matt_trans:
        for j in i:
            print(1 / determinant1 * float(j), end=" ")
        print()
    print()


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    option = int(input("Your choice: "))
    print()
    if option == 1:
        adding()
    elif option == 2:
        multiply_const()
    elif option == 3:
        multiply_mat()
    elif option == 4:
        transpose()
    elif option == 5:
        det_print()
    elif option == 6:
        global new_mat
        matrix_inverse()
    elif option == 0:
        exit()
