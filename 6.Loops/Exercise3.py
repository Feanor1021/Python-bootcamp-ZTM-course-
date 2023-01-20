#Write the matrix to sys.stdout with loops

matrix_gui=[[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]

for i in matrix_gui:
    for j in i:
        if (j == 0):
            print(' ',end = '')
        else:
            print('*',end = '')
    print('\n',end = '')

print("\n")

i, j = 0, 0

while i < len(matrix_gui):
    j = 0
    while j < len(matrix_gui[i]):
        if  matrix_gui[i][j] == 0:
            print(' ', end = '')
        else:
            print('*', end = '')
        j += 1
    print("\n", end = '')
    i += 1

