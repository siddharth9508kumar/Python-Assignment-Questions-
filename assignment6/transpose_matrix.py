# WAP to print a transpose of a matrix of nxn order.
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        element=int(input("Enter the element: "))
        row.append(element)
    matrix.append(row)
print("The Original matrix is: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
print("The Transpose of the matrix is: ")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()