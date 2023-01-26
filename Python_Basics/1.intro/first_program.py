#Before the begining to coding with pyton lets talk about how python interprets code in to machine language.
#Beside this language ı've only know c and c like languages. And those languages use compiler to turn source code to machine language.
#But python uses interpreter, different from compiler. 
# The interpreter does not take the source code (eg .c) like a compiler and directly generate a machine code file (eg .o). 
# The interpreter first compiles the python code and creates an intermediate form we call byte code, 
# then inserts the byte code into Cpythonvm (c python virtual machine) and unlike the compiler, 
# it interprets each line separately and translates it into machine language line by line. 
# This process is repeated in each run. Therefore, it is a slower language compared to other languages.
#you may find more detailed information at this link =  https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html#:~:text=The%20Python%20interpreter%20is%20a,reads%20from%20particular%20memory%20locations).
#first program that i've write in python

print("Hello world")

a = "Furkan"

print(a + " Yardımcı", type(a), "\n")

b = 23

print("Age", int(23 / b ** 4 // 44 + 23),type(b))

list_t = [1, 2, "bir", "iki"]

print("\n\n" + str(len(list_t)) + ("\n"))

for n in list_t:
    print(n, type(n))


# Python Data Types
# Data Types	        Classes	Description
# Numeric	    int, float, complex     	holds numeric values
# String	    str	                        holds sequence of characters
# Sequence	    list, tuple, range	        holds collection of items
# Mapping	    dict	                    holds data in key-value pair form
# Boolean	    bool	                    holds either True or False
# Set	        set, frozeenset	            hold collection of unique items