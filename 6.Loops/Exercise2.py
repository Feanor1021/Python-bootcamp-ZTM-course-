#What is the index of 50 in list of 0 to 100

for i,j in enumerate(list(range(100))): #i, j is unpacking.
    if j == 50:
        print("index of 50 is = {0}".format(i))
