# List:
# Lists are used to store multiple items in a single variable. 
# Lists are one of 4 built-in data structures in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered ?
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Basically it means that it has succesive memory like 100 101 102 (depend on what the data type is 100+(data type byt))

# Changeable ?
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# You can create mutable strings with lists.

# Allow Duplicates ?
# Since lists are indexed, lists can have items with the same value:

# You can find length of a list with len function like strings

thislist = list(["hi",2,2.9,"BYE!"])
print(len(thislist))

#List are like arrays in C but not the same thing. All the arrays should be exactly one type in C but here we can create
#list that containing first element of int and second string third float... They are different in this respect.
#But both of them have sequential memory (ordered).

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

print(type(list1))

# You can use slicing with list and slicing will create COPY of the list as same as the immutable strings.

list_test = [1,31,"Hi",69,59,49,95,"Bye"]
print(list_test[::-1]) #Slicing is exactly as same as with strings and it will create "COPY!"

