mode = input(
    "enter the mode you want to use \n (binary to decimal, decimal to binary, octal to decimal): ")


def binary_decimal():
    binary = input("Enter your binary number:")
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    print(f"The decimal equivalent of {binary} is: {decimal}")


def decimal_binary():
    decimal_input = input("Enter your decimal number:")
    decimal = int(decimal_input)
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    print(f"The binary equivalent of {decimal_input} is: {binary}")


def octal_decimal():
    octal = input("Enter your octal number:")
    decimal = 0
    power = 0
    for digit in octal[::-1]:
        decimal += int(digit) * (8 ** power)
        power += 1
    print(f"The decimal equivalent of {octal} is: {decimal}")


if mode == "binary to decimal":
    binary_decimal()
elif mode == "decimal to binary":
    decimal_binary()
elif mode == "octal to decimal":
    octal_decimal()
else:
    print("Invalid mode selected. Please choose 'binary to decimal', 'decimal to binary', or 'octal to decimal'.")
