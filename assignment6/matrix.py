# WAP to print matrix containg a group of similar by giving the input randomely in another matrix.
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        element=int(input("Enter the element: "))
        row.append(element)
    matrix.append(row)
print("The matrix is: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
flat=[]
for row in matrix:
    for element in row:
        flat.append(element)
print("Matrix containing a group of similar elements: ")
for element in flat:
    if flat.count(element) > 1:
        print(element, end=" ")
print()