import numpy as np
nums = [1,2,3,4,5]
arr = np.array(nums)
print(arr)
print("Type of array:",type(arr))
print("Data type of elements:",arr.dtype)

print("first element:",arr[0])
print("Slicing first 3 :",arr[0:3])



#main activity
data_type = [('name','S15'),('class',int),('height',float)]
students_details = [('james',5,48.5), ('nail',6,52.5),('paul',5,42.10),('pit',5,40.11)]
#create a structure array
students = np.array(students_details,dtype=data_type)
print("Orginal Array:")
print(students)
print("sort by height")
print(np.sort(students,order='height'))