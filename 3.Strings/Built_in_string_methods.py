arr = "Hello"

#usage of string methods in python you can find all of them with definition in this link. https://www.w3schools.com/python/ref_string_maketrans.asp

print(arr.capitalize(), arr)

print(arr.center(7,'s'),arr)

print(arr.casefold(),arr)

print(arr.upper(),arr) #all upper

print(arr.lower(),arr) # all lower

print(arr.find('l'),)
print(arr.find('o',-3,99)) #if it cant find the value return -1 otherwise return the index

print(arr.count('l'))

#There are several string decoding methods. Ascii and unicode two of them.
#Ascii has 127 chracter in it and all the characters are represented by 1 byte. Ascii is takes much less byte to store but it can only decode english characters
#and some of the symbols such as {},[],! etc. But there are much more character among the all languages. Unicode is created to solve this problem.
#Unicode theoretically can decode over a million grapheme (the smallest meaningful contrastive unit in a writing system.). 
#We've talked about decoding what about encoding ? 
#ASCII encodes characters into seven bits of binary data each strings characters has 7 bit long value (eg A=d'65 = 0b'1000001)
#Unicode has more than one encoding thecniques one of them UTF-32. In UFT-32 all the graphemes are represented by 4 byte. It is not good way to store strings because
#it takes too much space on memory. UFT-8 on the other hand more convenient in term of memory. UTF-8 assigns byte value to the minimum values that graphemes can fit.
#For example grapheme 'A' is 65 in decimal and it can fit in 1 byte so UTF-8 represent it with 1 byte. I't is more convenient for memory and by default python uses UTF-8

print(arr.encode("UTF-8"),arr)
print(arr.encode("UTF-16"),arr)
print(arr.encode("UTF-32"),arr)

print(arr.endswith('o'))#Returns true if the string ends with the specified value

print(arr.expandtabs(0))

print(arr.index('H'))

#isalnum, isalpha .... are like in C. In Chey work for a single character, here they work for the entire string.
#If all of the character are alphabet in string then isalpha is return True.
print(arr.isalnum())

# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), 
# or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print(arr.isidentifier())

# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
my_list=["Merhaba","Furkan"]
print(" ".join(my_list))

x=arr.ljust(20) #The ljust() method will left align the string, using a specified character (space is default) as the fill character.
print(x)

value = "    hi              "
print("Hello",value.lstrip()," merhaba") #Returns a left trim version of the string

value2=arr.maketrans('H','F')
print(arr.translate(value2)) # The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.


##The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

x = arr.replace('H','F')
print(x,arr)

value = "O araba, bu araba ve su araba"
x=value.rfind("araba") #The rfind() method finds the last occurrence of the specified value. -1 if the value is not found.
print(x)

