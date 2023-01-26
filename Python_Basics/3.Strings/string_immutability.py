#Strings are immutable(literal) in python but what is immutability ??
#It means that you cant change any grapheme in an string you can only re assign new string or some part of the an string
#to a variable. If you try to change content of a string (a grapheme) you'll get error.

String = "I'm ımmutable"
#String[0]="2" #it'll get error
print(String[0])

#This concept is as same as literals in C which you can create with char *(Name) = "Text". If you did'nt give any allocated
#ordered memory block to it, compiler defaulty create literal string and it can not be changed. we know that.

#Why strings are immutable in python ? As we know python is created with C, and all the variables in python are like pointers in C.
#You can just call by referance in here. Because of that all strings are created like literals in python.

#Mutable strings:
#As in c you can create mutable strings with arrays (Lists).

String_mutable=list("Hi I'm mutable")
String_mutable[0]='B'
String_mutable[1]='y'
print(String_mutable)

#There is no char type in here. So all the indexes above are strings, and you can change with strings.

String_mutable[0]="By B"
print(String_mutable)

#Of cource if you create a string with list you can't use most of the string methods (very few of them common).
#But if you want C like experience in python you can create and you can do what ever process you want on them with while for etc.