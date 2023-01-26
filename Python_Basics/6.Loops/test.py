
# 1-10 a kadar git ama 7yi yazma 
#for ve while için go brrr

for i in range(1,11):
    if i == 7:
        continue
    print(i)

i = 1
while i<=10:
    if (i == 7):
        i+=1
        continue
    print(i)
    i+=1

#100 e kadar gitmeye çalış ama 23 te kır döngüyü

print("\n\n")

for i in range(100):
    if i==23:
        print(i)
        break
    else:
        print(i)

i = 0
while i<100:
    if (i == 23):
        print(i)
        break
    else:
        print(i)
    i += 1

print("\n\n\n")

i = 0

while i<100:
    pass
    print(i)
    i += 1