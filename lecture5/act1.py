#logical oparator
a = 100
b = 150
c = 200


#and
if(a == 100) and (b == 100):
    print("Alls Well that ends wells")
else:
    print("All that glitters is not gold")

#or
if(b == 150) and (c == 100):
    print("One apple a day keeps the doctor away")
else:
    print("Only hardwork matters")

#not
fruits = ['apple','banana','cherry']

if 'kiwi'not in fruits:
    print("Kiwi is not in the list")
else:
    print("Kiwi is in the list")