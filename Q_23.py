'''
23. WAP to transpose a matrix.
'''

def input_matrix(rows,cols):
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

Mat1=input_matrix(rows,cols)

T_mat=[[0 for i in range(rows)] for i in range(cols)]

for i in range(rows):
    for j in range(cols):
        T_mat[j][i]=Mat1[i][j]

print("Transposed matrix :")
for i in T_mat:
    print(i)

