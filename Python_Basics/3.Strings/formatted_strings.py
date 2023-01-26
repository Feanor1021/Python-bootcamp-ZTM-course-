
arr = "hello"
arr2 = "hello2"

#You can format strings as same as in C with % operator.
#https://www.tutorialspoint.com/python3/python_strings.htm you can find all formatting characters in this link.(%x %i %g ....)
print("Usage of % \n")
print("%d %d %s" % (12,13,arr+arr2))
#...........................................................

#usage of .format
val1,val2 = "Cindy",50
print("\n\nUsage of .format")
print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {1}, your balance is {0}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50)) #if you use a local variable it will give error with indexes (0,1,2...) 

print("Hello {1}, your balance is {0}.".format(val1, val2)) #if you use variable that declared outside of the format, you cant use {arr} it will give error. you have to use indexes

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
#...........................................................

#usage of f""

print("\n\nUsage of f\"\"")

print(f"Hello {val1}, your balance is {val2}.") #you can add python expression between the curly brackets

print(f"Hello {val2}, your balance is {val1}.")
#...........................................................