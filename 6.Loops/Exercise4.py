
my_list = list(('a','b','c','b','d','m','n','n','a'))
buf_list =list(())

#('a','b','c','b','d','m','n','n','a')
# i will iterate over the list and j is iterate with i+1.th index. If it is find similar value then it'll append the value to the buf_list.

k = 1
for i in my_list:
    for j in my_list[k:]:
        if(i == j):
            buf_list.append(j)
    k += 1

print(buf_list)

#with while
buf_list2 = list(())
i, j = 0, 0
while i<len(my_list):
    j = i + 1
    while j<len(my_list):
        if (my_list[i]==my_list[j]):
            buf_list2.append(my_list[j])
        j += 1
    i += 1

print(buf_list2)

#Another ways

dublicate = []
for i in my_list:
    if my_list.count(i) > 1:
        if(i not in dublicate):
            dublicate.append(i)
print(dublicate)