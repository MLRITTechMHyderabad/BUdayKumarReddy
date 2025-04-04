matrix=[[1,2,3],[4,5,6],[7,8,9]]

transpose=[]

rows=len(matrix)
cols=len(matrix[0])

for i in range(cols):
    row=[]
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)



for row in transpose:
  print(row)