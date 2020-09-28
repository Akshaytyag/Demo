rows,columns = input().split()
rows=int(rows)
columns=int(columns)
matrix = []
print("Enter the %s x %s matrix: "% (rows, columns))
for i in range(rows):
    matrix.append(list(map(int, input().rstrip().split())))
