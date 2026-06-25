def square_filter(start, end):
    even_squares = []
    odd_squares = []

    print("Square Values:")

    for num in range(start, end + 1):
        square = num ** 2
        print(f"{num}^2 = {square}")

        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("\nEven Square Values:")
    for value in even_squares:
        print(value)

    print("\nOdd Square Values:")
    for value in odd_squares:
        print(value)

# Taking input from the user
begin = int(input("Enter the beginning number: "))
end = int(input("Enter the ending number: "))

# Calling the function
square_filter(begin, end)