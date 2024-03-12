'''
25. WAP to implement matrix multiplication in python.
'''

def input_matrix(rows,cols):
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            element=int(input(f"Enter element at position ({i + 1},{j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def multiply_matrices(mat1,mat2,rows1,cols1,rows2,cols2):
    if cols1!=rows2:
        print("Matrix multiplication is not possible. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

    product_matrix=[[0 for i in range(cols2)] for i in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                product_matrix[i][j]+=mat1[i][k] * mat2[k][j]
    return product_matrix

rows1=int(input("Enter number of rows for Matrix 1: "))
cols1=int(input("Enter number of columns for Matrix 1: "))

rows2=int(input("Enter number of rows for Matrix 2: "))
cols2=int(input("Enter number of columns for Matrix 2: "))
print()

if cols1!=rows2:
    print("Matrix multiplication is not possible.\nNumber of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    print("Enter Elements of Matrix 1: ")
    Mat1=input_matrix(rows1, cols1)
    print()

    print("Enter Elements of Matrix 2: ")
    Mat2=input_matrix(rows2, cols2)
    print()

    product_matrix=multiply_matrices(Mat1,Mat2,rows1,cols1,rows2,cols2)

    if product_matrix:
        print("Product matrix :")
        for i in product_matrix:
            print(i)
