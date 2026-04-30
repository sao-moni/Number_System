"""name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the binary to decimal converter.")
binary = input("Enter the binary number: ")
decimal = 0
power = 0
for digit in binary [::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1
print(f"The decimal equivalent of {binary} is: {decimal}")
print("thank you for using the binary to decimal convertor!")"""

mode = input("enter the mode")


def binary_decimal():
    binary = input("Enter your binary number:")
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    print(f"The decimal equivalent of {binary} is: {decimal}")


if mode == "binary to decimal":
    binary_decimal()
else:
    print("Invalid mode selected. Please choose 'binary to decimal'.")
