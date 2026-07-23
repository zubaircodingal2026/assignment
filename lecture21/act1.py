#set of prime number 
set_prime = {1,2,3,5,5,11,7,11}
print (set_prime)

#copy set
#shallow copy
set_number_copy = set_prime.copy()
print(f"orginal set : {set_prime}")
print(f"copied set : {set_number_copy}")

#equality and identity
print(set_prime == set_number_copy)
print(set_prime is set_number_copy)

#set from list
list = [1,2,2,3,4,4,5,6,6,6,7,7,7]
set1 = set(list)
print(set1)
#set from tuple
t1 = (1,2,2,2,3,4,5,6)
set2 = set(t1)
print(set1)

#set from dict
fruits = {
    '1' :"apple",
    '2' :"banana",
    '3' :"mango"
    }

set3 = set(fruits.keys())
set4 = set(fruits.values())
print(set3)
print(set4)

#adding members to a set (set_prime)
print("\nadding element to the set...")
print('\nbefore adding...')
print(set_prime)

#remove members from
#1.discard()
set_prime.discard(13)
set_prime.discard(20)
print("\nAfter removing...")
print(set_prime)

#2.remove
set_prime.remove(11)
try:
    print("trying to remove...")
    set_prime.remove(100)
    print("removed successfully")
except KeyError:
    print("element not present..")
finally:
    print("end of program")
    
print("after removal....")
print(set_prime)


#3.pop()
popped_val = set_prime.pop()
print(f"\nitem removed : {popped_val}")
print(f"after removal : {set_prime}")