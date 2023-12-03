# TEST
# Loop Triangle
def loop_triangle(character, loop):
    count = 0
    char = ""
    while count < loop:
        char += character
        print(char)
        count += 1


while True:
    charIn = input("Enter your chosen character:\n")
    if charIn == "quit":
        print("Quit!")
        break
    loopIn = input("Enter the exponent number:\n")
    if loopIn == "quit":
        print("Quit!")
        break
    loop_triangle(charIn, int(loopIn))


# FizzBuzz
def fizzbuzz(limit1, limit2, num1, num2):
    fizz = "Fizz"
    buzz = "Buzz"
    numbers = range(limit1, limit2 + 1)
    for number in numbers:
        if (number % num1 == 0) and (number % num2 == 0):
            number = fizz + buzz
            print(number)
        elif number % num1 == 0:
            number = fizz
            print(number)
        elif number % num2 == 0:
            number = buzz
            print(number)
        else:
            print(number)


while True:
    startNum = input("Enter the starting number:\n")
    if startNum == "quit":
        print("Quit!")
        break
    endNum = input("Enter the end number:\n")
    if endNum == "quit":
        print("Quit!")
        break
    num1In = input("Enter the first divisible number:\n")
    if num1In == "quit":
        print("Quit!")
        break
    num2In = input("Enter the second divisible number:\n")
    if num2In == "quit":
        print("Quit!")
        break
    fizzbuzz(int(startNum), int(endNum), int(num1In), int(num2In))


# Chessboard
def create_chessboard(char1, char2, size):
    pattern = ""
    y = 0
    while y < size:
        y += 1
        x = 0
        while x < size:
            x += 1
            if (x + y) % 2 == 0:
                pattern += char1
            else:
                pattern += char2
        pattern += "\n"
    print(pattern)


create_chessboard("#", "^", 5)


# Power
def power(base, exponent):
    count = 0
    result = 1
    while count < exponent:
        count += 1
        result *= base
    return result


while True:
    baseIn = input("Enter the base number:\n")
    if baseIn == "quit":
        print("Quit!")
        break
    exponentIn = input("Enter the exponent number:\n")
    if exponentIn == "quit":
        print("Quit!")
        break
    print(power(int(baseIn), int(exponentIn)))

