print("=== Text to Binary Converter ===")

text = input("Enter any word or sentence: ")

print("\nBinary:")

for letter in text:
    binary = format(ord(letter), "08b")
    print(letter, "=", binary)