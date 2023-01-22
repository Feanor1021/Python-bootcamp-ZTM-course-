# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# List:
# Lists are used to store multiple items in a single variable. 
# Lists are one of 4 built-in data structures in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)
#............................................................

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
#............................................................

# You can find length of a list with len function like strings

thislist = list(("hi",2,2.9,"BYE!")) # note the double round-brackets
print(len(thislist))
#............................................................

#List are like arrays in C but not the same thing. All the arrays should be exactly one type in C but here we can create
#list that containing first element of int and second string third float... They are different in this respect.
#But both of them have sequential memory (ordered).

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

print(type(list1))
#............................................................

# You can use slicing with list and slicing will create COPY of the list as same as the immutable strings.

list_test = [1,31,"Hi",69,59,49,95,"Bye"]
print(list_test[::-1]) #Slicing is exactly as same as with strings and it will create "COPY!". Indexing is as same as strings. 0,1,2,3... -1,-2,-3...
print(list_test[2][::-1])
#............................................................

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
print("apple" in thislist)
print("appl2e" not in thislist)# or not present
#both of them return bool value

#............................................................

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# if you insert much more element than you replace, new items will be inserted where you specified, and remaining items will move acordingly.
thislist[1:2] = ["blackcurrant", "watermelon"]
#thislist[1:1] = ["blackcurrant", "watermelon"]. in here both element are inserted in list because 1:1 range has actual range of 1:0 (thislist[1:1] = []) 
print(thislist)

#if you insert much less element than range you specified, the new items will be shrinked, and remaining items will move acordingly.
thislist[1:3] = ["watermelon"] #1 and 2 turn into watermelon and list is shrinked
print(thislist)
#............................................................

#concatenate of lists: You can do it with + operator like with strings.

list1=list((1,2,6,5))
list2=list((1,7,2,4))
list_new=list1+list2

print(list_new)
#............................................................

#Repetation. like strings

list1=list((1,2))
new_list = list1*5
print(new_list)
#............................................................

#List unpacking: You can unpack lists into single variables or smaller lists.

a,*b,c,d=[1,2,3,4,5,6,7,8,9] #You can use *name just once. Where ever you want.
print(a,b,c,d)
#............................................................
