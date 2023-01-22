# Tuple :
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable. They are like constant lists. You can reach values in them like lists but you can't change them.
# Tuples are written with round brackets.

my_tuple = (1,2,3,4,5)
my_tuple2 =tuple((1,2,3,4))
new_tuple = my_tuple2+my_tuple
print(new_tuple*2)
print(my_tuple, my_tuple2[::-1]) #slicing etc works like lists
#As you see lot of feature of the lists are usable with tuple too slicing, concatenation etc.
#............................................................

# Tuple Items ?
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc. (last one [-1] like lists or strings)
#............................................................

# Ordered?
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#............................................................

# Unchangeable?
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#............................................................

# Allow Duplicates?
# Since tuples are indexed, they can have items with the same value. It is don't sounds like feature but on of the data types is don't allow that, which is sets.
#............................................................

# Tupple length:
# You can use len function with tuples too

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#............................................................

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#............................................................

# Tuple Items - Data Types
# Tuple items can be of any data type like lists.
#............................................................

# Most of the tuple features are as same as list's features. Please look at them. "TUPLES ARE BASICALLY UNCHANGEABLE LISTS"
# Note: since they are unchangeable you cant use item assignment. tuple[0]=2,tuple[1:2]=(1,2,3) not allowed

