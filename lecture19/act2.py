# All about Tuple
# Create tuples "pasta" and "biriyani"
pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biriyani = ("CHicken Biriyani", "Indian", 45, "Hard")

# Display values
print("Recipe 1 : ", pasta)
print("Name of Recipe 1 : ", pasta[0])
print("Cuisine of Recipe 1 : ", pasta[1])
print(f"Prep Time of Recipe 1 :{pasta[2]} minutes")
print("Difficulty level of Recipe 1 : ", pasta[-1])

print("\n")
print("*"*30)
print("\n")

# tuple slicing
# combine two tuples ==> nested tuple
all_tuples = (pasta, biriyani)
print(f"First Recipe Name : {all_tuples[0][0]}")
print(f"Second Recipe Name : {all_tuples[1][0]}")
print(f"Second Recipe Prep Time : {all_tuples[1][2]} mins")
print(f"Second Recipe Difficulty level {all_tuples[1][3]}")

print("\n")
print("*"*30)
print("\n")

# iterate thorugh a tuple
print("Iterate/Loop through a Tuple")
for detail in pasta:
    print("-", detail)

print("\n")
print("*"*30)
print("\n")

# Enumerate
print("Enumerate through a Tuple")
for idx, detail in enumerate(biriyani, start=1):
    print(f"{idx} : {detail}")

# Tuple Unpacking
print("\n Tuple Unpacking")
print("*"*30)
print("\n")

fruits = ("apple", "banana", "kiwi", "orange","guava")
f1,f2,f3,f4,f5 = fruits
print(f1)
print(f2)
print(f3)
print(f4)

# Advanced tuple unpacking
x , *y = fruits
print(x)
print(y)

# index()
print(fruits.index("apple"))

# count()
print(fruits.count("apple"))

# in 
print("apple" in fruits)
print("apple" not in fruits)

# Zip
t1 = (1,2,3)
t2 = ("John", "David", "Mayank")

t3 = dict(zip(t1,t2))

print("\n")
print("*"*30)
print("\n")
for id, name in t3.items():
    print(f"{id} : {name}")


def process_report_card(subject, *marks):
    # 'marks' automatically collects the numbers into a tuple
    total = sum(marks)
    average = total / len(marks)
    
    # Determine grade based on average score
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"
        
    print(f"Report Card For: {subject}")
    print(f"Tuple received: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Score: {average:.2f}")
    print(f"Final Grade: {grade}")

# Calling the function with individual marks
process_report_card("Marks", 85, 90, 78, 82)

