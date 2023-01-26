# Matrixes are just multidimentional lists nothing more

matrix = [[1, 2, 3, 3],
          [4, 5, 6, 5],
          [7, 8, 9, 1],
          [10, 11, 12]]

print(matrix)
print(matrix[:2])  # slicing gives us the rows

# To extract the columns this function can be used.
# Be careful when you use the function. The column which you want to extract, there should be a item on each row of it.
# Otherwise it will give an error.


def column(matrix, i):
    return [row[i] for row in matrix]


print(column(matrix, 2))
