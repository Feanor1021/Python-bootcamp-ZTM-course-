#Find highest even value in a list.

#first method:
#fist sort then reverse it. First even value is highest value among all even numbers.

def highest_even1(list_par):
    list_par=list(list_par) #Function can work with tuple etc.
    list_par.sort()
    list_par.reverse()
    for i in list_par:
        if (i % 2 == 0):
            return i

#second method
#Fisrt we will choose a value that smallest among all list values(which is -inf, none of the list value can't be smaller than in our case). After that we'll iterate on list.
#if any even value is has higher value than our highest_val then it'll be the highest.

def highest_even2(list_par):
    list_par=list(list_par) #Function can work with tuple etc.
    i, highest_val = 0, float('-inf') #min possible value to highest_val
    
    while i<len(list_par):
        if ((list_par[i] % 2 == 0) and (list_par[i] > highest_val)):
            highest_val = list_par[i]
        i += 1
    return highest_val


#third method

def highest_even3(list_par):
    even = []
    for i in list_par:
        if (i % 2 == 0):
            even.append(i)
    return max(even)

#fourth method

def highest_even4(liste):
    return max(value for value in liste if value % 2 == 0 )
