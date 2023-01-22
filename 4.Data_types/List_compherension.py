# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# The Syntax : newlist = [(expression) for (item) in (iterable) if (condition == True)]

# Condition ?
# The condition is like a filter that only accepts the items that valuate to True.

# Iterable ?
# The iterable can be any iterable object, like a list, tuple, set etc.

# Expression ?
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

#rather than writing simple list codes we can do it like below. Example is copies the elements, which has leght of 4 into new_lists

fruits = ["apple", "banana", "cher", "kiwi", "mango"]
new_list = [x for x in fruits if len(x) == 4]# x shows values thrown into new_list. It is item and expression in here but it does not have to be like that.
print(new_list)

new_list = [x.upper() for x in fruits if len(x) == 4]# the expression is current item of new_list(if condition is true ofc), and expression is can be different than item it self you can manipulate it.
print(new_list)

#You can use ternary operator in expression too
#Syntax : [on_true] if [expression] else [on_false]
newlist = [x if x != "banana" else "orange" for x in fruits] # it has ternary in expression. It means that if the compherensions's condition is True than expression's condition should be true too to put
#the value of current item into new_list 
