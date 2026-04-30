name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the binary to decimal converter.")
binary = input("Enter the binary number: ")
decimal = 0
power = 0
for digit in binary[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1
print(f"The decimal equivalent of {binary} is: {decimal}")
print("thank you for using the binary to decimal convertor!")
