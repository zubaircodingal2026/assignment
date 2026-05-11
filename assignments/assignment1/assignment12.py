# Number Counter Program

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("\nCounting numbers...\n")

for number in range(start, end + 1):
    print("Number =", number)

print("\nCounting Finished!")