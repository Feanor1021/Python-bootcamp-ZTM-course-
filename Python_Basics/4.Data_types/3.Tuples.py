# Tuple :
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable. They are like constant lists. You can reach values in them like lists but you can't change them.
# Tuples are written with round brackets.

my_tuple = (1, 2, 3, 4, 5, "hey",tuple((1,23,4)))
print(my_tuple)
# ............................................................
# Tuple Items ?
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc. (last one [-1] like lists or strings)
# ............................................................

# Ordered?
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# ............................................................

# Unchangeable?
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# ............................................................

# Allow Duplicates?
# Since tuples are indexed, they can have items with the same value. It is don't sounds like feature but on of the data types is don't allow that, which is sets.
# ............................................................

# Most of the tuple features are as same as list's features. Please look at them. "TUPLES ARE BASICALLY UNCHANGEABLE LISTS". You can see brief examples below
# Note: since they are unchangeable you cant use item assignment. tuple[0]=2,tuple[1:2]=(1,2,3) not allowed
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
my_tuple2 = tuple((1, 2, 3, 4))
new_tuple = my_tuple2+my_tuple
print(type(tuple))
print(new_tuple*2)
# slicing etc works like lists and create copy of the tuple not change them
print(my_tuple, my_tuple2[::-1])
# As you see lot of feature of the lists are usable with tuple too slicing, concatenation etc.
# Some important features are explained below
# ............................................................

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# ............................................................

# Tuple unpacking:
# It is as same as lists but there is a little differance that i want to show.
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a "LIST".
a, b, c, *d = (1, 2, 3, 4)  # You can use *name just once. Where ever you want.
print(a, b, c, d)
# ............................................................

# del keyword:

list1 = (1, 23, 4, 5, 6, 7)

del list1[1]  # you can also del entire list with "del list1" like .clear() method

print(list1)
# ............................................................

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Example
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
# ............................................................
