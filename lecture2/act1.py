name = "penguin"
age = 15
is_student = True
weight = 70.5

print("name:",name)
print("data type of name:",type(name))

print("age:",age)
print("data type of age:",type(age))

print("is student", is_student)
print("data type of student:",type(is_student))

print("weight:",weight)
print("data type of weight:",type(weight))

print("some type casting")
age = str(age)
print(age)

weight = int(weight)
print(weight)

print(f"datatype of weightafter type casting:{type(weight)}")
