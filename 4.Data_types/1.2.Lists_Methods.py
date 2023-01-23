#Append : The .append() method appends an element to the end of the list.
#syntax : list.append(elmnt)
#parameter : "Required". An element of any type (string, number, object etc.)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.append(["orange","morange","lorange"])#it is append list to end of the list (so the fruits list become matrix)
print(fruits)
#............................................................

#Clear : The clear() method removes all the elements from a list.
#syntax : list.clear()
#parameter : No parameters

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)
#............................................................

#Copy : The copy() method returns a copy of the specified list.
#syntax : list.copy() No parameters
#parameter : No parameters

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy() # you can copy it with slicing too fruits[:]
print(x)
#............................................................

#Count : The count() method returns the number of elements with the specified value.
#syntax : list.count(value)
#parameter : "Required". Any type (string, number, list, tuple, etc.). The value to search for.

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
#............................................................

#Extend : The extend() method adds the specified list elements (or any iterable) to the end of the current list.
#syntax : list.extend(iterable)
#parameter : "Required". Any iterable (list, set, tuple, etc.)

fruits = ['apple', 'banana', 'cherry']
points = {'1':"k",'2':"kel", '3':"kel" , '4':"kel"}
points2=("2","42")
fruits.extend(points)#it will take dictionary's keys by default use .values() to get values of dict. All type of parameters are turn into list element.
print(fruits)
#............................................................

#Index : The index() method returns the position at the first occurrence of the specified value.  The index() method only returns the first occurrence of the value.
#syntax : list.index(elmnt)
#parameter : "Required". Any type (string, number, list, etc.). The element to search for

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32, 0,-1)#val, start, end
print(x)
#............................................................

#Insert : The insert() method inserts the specified value at the specified position.
#syntax : list.insert(index, elmnt)
#parameter : index = "Required". A number specifying in which position to insert the value, elmnt = "Required". An element of any type (string, number, object etc.)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(3, "orange") # it can append too
print(fruits)
#............................................................

#Pop : The pop() method removes the element at the specified position. It is as same as pop function in stacks by default. It pops the last element(like top of the stack). If you give spesific 
#index it can pop this index too
#syntax : list.pop(index)
#parameter : index =	"Optional". A number specifying the position of the element you want to remove, default value is -1, which returns the last item

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop() # The pop() method returns removed value.
print(x)
#............................................................

#Remove: The remove() method removes the first occurrence of the element with the specified value.
#syntax : list.remove(elmnt)
#parameter: "Required". Any type (string, number, list etc.) The element you want to remove

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
#............................................................

#Reverse: The reverse() method reverses the sorting order of the elements.
#syntax: list.reverse()
#parameter: No param

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
#............................................................

#Sort : The sort() method sorts the list ascending by default. You can also make a function to decide the sorting criteria(s).
#syntax : list.sort(reverse=True|False, key = myfnc)
#parameter : reverse "Optional". reverse=True will sort the list descending. Default is reverse=False. key	"Optional". A function to specify the sorting criteria(s)

def myFunc(e):
    return len(e)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc) # it will sort the list by returned values.
print(cars)

#Sort a list of dictionaries based on the "year" value of the dictionaries:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc) 
print(cars)

# Sort the list by the length of the values and reversed:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print(cars)
cars.sort(reverse=True)# alphebetical reverse sorth
print(cars)
cars.sort(key = myFunc) # by length of elements
print(cars)
cars.sort(reverse=True, key=myFunc) # boyuta göre tersten sıraladık
print(cars)
#............................................................










