# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# All items are not stored successively like list or tuples !!! OS store them random on the ram.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set items are unchangeable, but you can remove items and add new items.
# ............................................................

# Set Items ?
# Set items are unordered, unchangeable, and do not allow "DUPLICATE!!!" values. (THIS IS THE MAIN FEATURE !!)

# Unordered?
# Unordered means that the items in a set do not have a defined order and they can not be indexed.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable?
# Set items are unchangeable, meaning that we cannot change the items after the set has been created. Because you can not reach them you can just look what it is in them with "in" keyword
# Once a set is created, you cannot change its items, but you can remove items and add new items.
# ............................................................

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

thisset = {"apple", "banana", "cherry", "apple"}
print("banana" in thisset)
# ............................................................

# Get the Length of a Set
# To determine how many items a set has, use the len() function.

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# ............................................................

# Set Items - Data Types
# Set items can be of any data type:

set1 = {"abc", 34, True, 40, "male"}
# ............................................................

# type()
# From Python's perspective, sets are defined as objects with the data type 'set':

# <class 'set'>

myset = {"apple", "banana", "cherry"}
print(type(myset))
# ............................................................

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
# ............................................................

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:  # You can't indexed them but you can reach values of it with for just like in list or Tuples
    print(x)

# You can use "in" keyword in print or another functions too to check an element is present in a Set.
# ............................................................

# concatenate and Repedition of sets:

thisset = {"1", "2", "3"}
thisset2 = {12, 5, 3}
#print(thisset*2 + thisset2)
# You can do this operation with list and tuples but since sets are unordered you can not do that with sets
# ............................................................

# Adding item to sets.
# Since sets don't have indexing, you can't reach their values directly, or you can not change any item in a set. But you can add, or remove items of the set via methods, which we will cover on next.
# ............................................................
