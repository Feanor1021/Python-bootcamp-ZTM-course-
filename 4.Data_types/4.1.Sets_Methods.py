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

# intersection_update method : The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
# Syntax : set.intersection_update(set1, set2, ....)
# parameter : set1 is "Required". The set to search for equal items in. set2 and more are "Optional"

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
# ............................................................

# Isdisjoint method : The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False. In short if they don't have common item it return True otherwise false.
# Syntax : set.isdisjoint(set)
# parameter : "Required". The set to search for equal items in

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.isdisjoint(x)

print(z)
# ............................................................

# Issubset method : The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
# Syntax : set.issubset(set).
# parameter : "Required". The set to search for equal items in

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)  # It looks that wether the x is sub set of y

print(z)
# ............................................................

# Issuperset method : The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
# Syntax : set.issuperset(set)
# parameter : "Required". The set to search for equal items in

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = y.issuperset(x)  # It looks that wether the x is sub set of y

print(z)
# ............................................................

# Pop method : The pop() method removes a random item from the set. This method returns the removed item. It is exactly like stack's pop function.
# It is actually not random. Sets are implementation of hash tables. pop method is pops the firs hash entry in hashtable.
# Syntax : set.pop()
# parameter : No parameter values.

fruits = {"apple", "banana", "cherry"}

# Unlike the lists you can't give argument to pop method. Because sets are unordered and can't be reachable with index nums.
fruits.pop()
print(fruits)
# ............................................................

# Symmetric_difference method :
# Syntax : set.symetric_difference(set)
# parameter : "Required". The set to check for matches in

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)  # it returns not common items.
print(z)
# ............................................................

# symmetric_difference_update method : The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
# Syntax : set.symmetric_difference_update(set)
# parameter : 	"Required". The set to check for matches in

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)
# ............................................................

# UNION method : Definition and Usage The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
# You can specify as many sets you want, separated by commas.It does not have to be a set, it can be any iterable object. If an item is present in more than one set, the result will contain only one appearance of this item.
# Syntax : set.union(iterable1, iterable, iterable3, iterable4....)
# parameter : iterable1 is 	"Required". The iterable to unify with. iterable2 and others are "Optional"

x = {"apple", "banana", "cherry"}
y = ["google", "microsoft", "apple"]

z = x.union(y)  # since it is a set, common items are not coppied twice ofc.
print(z)
# ............................................................

# Update method : The update() method updates the current set, by adding items from another set (or any other iterable). If an item is present in both sets, only one appearance of this item will be present in the updated set.
# Syntax : set.update(iterable)
# parameter : Required. The iterable insert into the current se

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)
print(x)
# ............................................................
