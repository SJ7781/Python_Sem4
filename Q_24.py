'''
24. WAP to add two matrices.
'''

def input_matrix(rows,cols):
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            element = int(input(f"Enter element at position ({i + 1},{j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(mat1,mat2,rows,cols):
    Sum_matrix=[[0 for i in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            Sum_matrix[i][j]=mat1[i][j]+mat2[i][j]
    return Sum_matrix

rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
print()

print("Enter Elements of Matrix 1: ")
Mat1=input_matrix(rows,cols)
print()

print("Enter Elements of Matrix 2: ")
Mat2=input_matrix(rows,cols)
print()

Sum_matrix=add_matrices(Mat1,Mat2,rows,cols)

print("Resultant matrix after addition:")
for i in Sum_matrix:
    print(i)
