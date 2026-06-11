try:
    num1,num2 = eval(input("Enter two numbers,saparated by comma : "))
    result = num1 / num2
    print("result is", result)
#using multiple except block for different tyoe of errror

except ZeroDivisionError:
    print("cant divid by zero!! ")
except SyntaxError:
    print("Enter number saparated by comma like this 1, 2")
except ValueError:
    print("wrong input")
else:
    print("no exception")
finally:
    print("program ends......")
        