print("enter marks obtain in 4 subjects... ")
math = int(input("math : "))
english = int(input("english : "))
science = int(input("science : "))
bangali = int(input("bangali : "))


sum = math + english + science + bangali
print(f"total marks : {sum}")

average = sum / 400

percentage_mark = average * 100
print(f"percentage mark : {percentage_mark}")