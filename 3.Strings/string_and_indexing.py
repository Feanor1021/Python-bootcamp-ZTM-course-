#you can directly create a string

string = str(4214)
string = "Hello world"
string = 'Hello world'
string = hex(324)
string = "Hello world2"

#... There are many ways to do that. In python "" '' are same unlike c. There are no char type
#There are only strings and it's substrings.
#...........................................................

#string immutability:
#You can't change sub value of a string as like as in C. You have to replace it with new string. Old string is deleted.
#...........................................................

#Accessing values in Strings

print(string)
print(string[0])
print(string[-1])
#...........................................................

#usage = string[start : stop : stepover(default = 1)]

print(string[0:5])#from 0 to 4 is printed and at 5 it is stopped

print(string[0:5:1])#it is as same as above. Default value of stepover is 1

print(string[4:0:-1])#you can give negative stepover too. it will write "olle" in this case

print(string[4::-1])#if you don't give any value to stop it will continue to the end of the string(in opposite case start of the string).
#if start > stop and stepver is negative then 0th index is last value otherwise last index is last value


print(string[5:10:-1])#if you give any non-logical any value to start, stop and stepover it will print nothing to the stdin
print(string[:5:-1])# if you don't give any value, it will give it logical value
#normally start index is 0 but if we give 0 to start in last example it will be like this
#start with 0 to 5 and decrement by 1 each step. It is nonsense. Python sees it and gives start to max value that
# value > than 5 because it is the only logical case in here.
#If we leave the column blank, python assigns a value there to get the maximum string it can write. for example "5::1". It will give value of last index to stop.

print(string[::1]) #stepover is 1 and other values are blank. Python gives 0 to start and last index value to stop becase stepover is 1.
print(string[::-1])#stepover is -1 and othher values are blank. Python gives last index value to start and fisrt index value to stop because stepover is -1.
#it would be nonsense to 0 to last index with -1 stepover.
#If you give a value like that [0:last index] it will start with 0th index and stop at lasth index. It wont write last. index it is stop right there. You have to give + 1.
# But if don't give any value to'a colon [0:] like this python gives to stop value that it can write every thing.
#[0:last index:-1] it would not include first letter. But if you don't give any value to it, python gives it right value to write every thing.
#...........................................................

#string="Hello world2"
#index = 01234567891011
#nindex= -12-11-10-9-8-7-6-5-4-3-2-1
print(string[-1])
print(string[-2])
print(string[-12])
