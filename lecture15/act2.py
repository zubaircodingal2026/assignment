#function keyword (break)
word = input("Enter a word : ").strip().lower()
vowels = ('a','e','i','o','u')

for letter in word:
    if letter in vowels:
        print("this word contain vowels")
        break
else:
    print("no vowels found")
 
print("\n")   
#break example
for i in range(1,11):
    if i == 6:
        break
    print(i)
    
print("\n")
#function keyword (continue)
for i in range(1,11):
    if i == 6:
        continue
    print(i)
    