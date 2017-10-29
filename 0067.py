INFINITY = 999999999999999999

mat = []

file = open('0067_triangle.txt', 'r')
i = 0
for line in file.readlines():
    currentLine = line.split(' ')
    mat.append([])
    j = 0
    for number in currentLine:
        mat[i].append(int(number))
        j += 1
    i += 1

matlen = len(mat)

for i in range(matlen - 2, -1, -1):
  for j in range(matlen - (matlen - i - 1)):
    if (j + 1 < matlen):
      mat[i][j] = max(mat[i][j] + mat[i+1][j], mat[i][j] + mat[i+1][j + 1])
    else:
      mat[i][j] = mat[i][j] + mat[i+1][j]

print mat[i][j]
