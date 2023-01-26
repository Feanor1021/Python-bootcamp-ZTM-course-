import math

#some of the builtin functions
#detailed explanations are in below link
#https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch04s04.html

#Built-In Math Functions
print(round(3.4))
print(abs(-23))
print(pow(2,3))

#conversion functions
print("\n\n"+hex(24)) #Create a hexadecimal string representation of number . A leading '0x' is placed on the string as a reminder that this is hexadecimal. hex(684) yields the string '0x2ac'.
print(bin(9)) #Create a bin string representation of number . A leading '0b' is placed on the string as a reminder that this is binary not decimal. bin(9) yields the string '0b1001'.
print(oct(24))#Create a octal string representation of number . A leading '0' is placed on the string as a reminder that this is octal not decimal. oct(509) yields the string '0775'.
print(str(24))
print(repr(24))
#The str( x ) and repr( x ) functions convert any Python object to a string. 
# The str( x ) version is typically more readable, where the repr( x ) version is an internalized representation. 
# For most garden-variety numeric values, there is no difference. For the more complex data types, however, the resultsof repr and str can be very different.
#  For classes you write , your class definition must provide these string representation functions.

print(int(12))
print(int("1001",2))
#The int function has two forms. The int ( x ) form converts a decimal string, x , 
# to an integer. For example int('25') is 25. The int ( x , b ) form converts a string, x , 
# in base b to an integer. For example int('010101',2) yields 21. int('321',4) is 57, int('2ac',16) is 684.

#collection functions
print("\n",max(2,4,62))
print(min(1,252,1,-323,124))

#math module's functions
#https://www.programiz.com/python-programming/modules/math
print("\n\n",math.ceil(15.5))
print(math.copysign(1,-24))
print(math.floor(24.9))
print(math.e)
print(math.pi)
print(math.exp(1))
print(math.expm1(1))
#...
#..
#.