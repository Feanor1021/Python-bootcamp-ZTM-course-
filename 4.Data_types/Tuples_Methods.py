#Since tuples are immutable tuples don't have much methods. We will look all of them.

#1.Count() : The count() method returns the number of times a specified value appears in the tuple.
#syntax : tuples.count(elmnt)
#parameter : value	"Required". The item to search for

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
#............................................................

#2.index() : The index() method finds the first occurrence of the specified value. The index() method raises an exception if the value is not found.
#syntax : tuples.index(value, start, end)
#parameters : "Required" Value is the item that we search for. Start and end are "Optional"

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8,0,-1)
print(x)
#............................................................