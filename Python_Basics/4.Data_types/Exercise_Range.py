#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# You can usa range function to create iterable of integer.
# Syntax:
# range(start, stop, step)
# Parameter Values
# Parameter	Description
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Required. An integer number specifying at which position to stop (not included).
# step	Optional. An integer number specifying the incrementation. Default is 1

#Some important usages.

print(*range(10))

for i in range(-1,0,1): #if we give nonsense arguments to function it returns -1
    print(i)

