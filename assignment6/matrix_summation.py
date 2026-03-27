# WAP to print a matrix along with the summation of row amd column elements after entering a 3x3 matrix.
rows=3
cols=3
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
print("Row waise summation: ")
for i in range(rows):
    row_sum=0
    for j in range(cols):
        row_sum+=matrix[i][j]
    print("Sum of row",i+1,"is:",row_sum)
print("Column waise summation: ")
for j in range(cols):
    col_sum=0
    for i in range(rows):
        col_sum+=matrix[i][j]
    print("Sum of column",j+1,"is:",col_sum)
    