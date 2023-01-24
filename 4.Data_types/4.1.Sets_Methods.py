# Add method : The add() method adds an element to the set.If the element already exists, the add() method does not add the element since it is tupple it won't allow a duplicate value.
# Syntax : set.add(elmnt)
# Parameter : elmnt = "Required". The element to add to set.

fruit = set(("apple", "banana", "grape"))
# will add the item to set if item is not present in the set. # it can be tuple but not list.
fruit.add(tuple((1, 32, 4)))
print(fruit)  # Order may be different since it is nor ordered
# ............................................................

# Copy method : The copy() method copies the set.
# Syntax : set.copy()
# parameter : None

x = fruit.copy()
print(x)
# ............................................................

# Clear method : The clear() method removes all elements in a set.
# Syntax : set.clear()
# parameter : None

x.clear()
print(x)
x = set((1, 23, 4))
print(x)
# You can use del keyword too. But it will erase the x from the memory so you cant reach it anymore you have to declare again.
del x
# print(x) # will give error because we erase x from the memory it self
# ............................................................

# Remove method : The remove() method removes the specified element from the set.
# This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
# Syntax : set.remove(item)
# parameter : "Required". The item to search for, and remove

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")  # if it not present it will give an error
print(fruits)  # Order may be different since it is nor ordered
# ............................................................

# Difference method :  The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.
# Syntax : set.difference(set)
# parameter : "Required". The set for check diff in

# Order may be different since it is nor ordered
x = {"apple", "banana", "cherry"}
y = ("google", "microsoft", "apple")  # it can be tuple and list
# it will return the values that in x but not in y
z = x.difference(y)  # if x and y is equal then it will return empty set.
print(z, x)  # Order may be different since it is nor ordered

# ............................................................

# Difference_update() method : The difference_update() method removes the items that exist in both sets. It is different from .diffrence method because .difference
# return a set that don't contain common values. On the other hand difference_update() method is removes common item from original set.
# without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
# Syntax : set.difference_update(set)
# parameter : "Required". The set to check difference in.

x = {"apple", "banana", "cherry"}
y = ["google", "microsoft", "apple"]  # it can be tuple and list
x.difference_update(y)  # it returns none
print(x)


# ............................................................

# Discard method : The discard() method removes the specified item from the set. This method is different from the remove() method,
# because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
# Syntax : set.discard(item)
# parameter : "Required". The item to search for, and remove

fruits = {"apple", "banana", "cherry"}
fruits.discard("banan2a")  # it won't throw an error.
print(fruits)
# ............................................................

# Intersection method : The intersection() method returns a set that contains the similarity between two or more sets.
# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
# Syntax : set.intersection(set1, set2, ...)
# parameter : set1 is "Required". others are optional

x = {"apple", "banana", "cherry"}
y = list(("google", "banana", "apple"))  # it can be tuple or list
z = x.intersection(y)
print(z)
# ............................................................


# intersection_update method : 
# Syntax : set.clear()
# parameter : None

# ............................................................


# Clear method :
# Syntax : set.clear()
# parameter : None

# ............................................................

# Difference method :
# Syntax : set.clear()
# parameter : None

# ............................................................


# Clear method :
# Syntax : set.clear()
# parameter : None

# ............................................................
