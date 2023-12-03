# User Input and while Loops
print("User Input and while Loops\nHow the input() Function Works:\n")

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Practice :

age = input("Please enter your age: ")

if int(age) < 2:
    person = 'baby'
elif int(age) < 4:
    person = 'toddler'
elif int(age) < 13:
    person = 'kid'
elif int(age) < 20:
    person = 'teenager'
elif int(age) < 65:
    person = 'adult'
elif int(age) >= 65:
    person = 'elder'

if (person == 'adult') or (person == 'elder'):
    print("You are an " + person + ".")
else:
    print("You are a " + person + ".")

# Writing Clear Prompts
print("Writing Clear Prompts\n")

message = input("Please enter your name: ")
print("Hello " + message.title() + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello " + message.title() + "!")

# Using int() to Accept Numerical Input

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")

# The Modulo Operator
print("The Modulo Operator\n")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# Try It Yourself
# 7-1. Rental Car:
print("Try It Yourself\n7-1. Rental Car:\n")

car = input("What kind of rental car they would like? ")

print("\nLet me see if I can find you a " + car.title() + ".")

print("7-2. Restaurant Seating:\n")

people = input("How many people are in your group? ")
people = int(people)

if people > 8:
    print("\nSorry, you will have to wait for a table.")
else:
    print("\nYour table is ready.")

print("7-3. Multiples of Ten:\n")

number = input("Enter a number, and I will tell you if it is a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is a multiple of 10.")
else:
    print("\nThe number " + str(number) + " is not a multiple of 10.")

print("Second version:\n")

prompt = "Enter a number and I will tell you if it is a multiple of 10 or not. \n"

number = input(prompt)

if '0' in number:
    print(number + " is multiple of ten.")
else:
    print(number + " is not multiple of ten.")

# Introducing while Loops
# The while Loop in Action

print("Introducing while Loops\nThe while Loop in Action\n")

current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# Practice
print("Practice\n")
# 1st Version
start = input("Do you want to play a guessing game? ")

while start == 'yes':
    question_input = input("How many finger does human have? ")
    question_input = int(question_input)
    if question_input == 10:
        response_input = input("Your answer is correct. Do you want to play again? ")
        while response_input == 'no':
            input("Thanks for playing the game.")
    else:
        response_input = input("Your answer is incorrect. Do you want tp try again? ")
        while response_input == 'no':
            input("Thanks for playing the game.")
while start == 'no':
    input("Have a good day!")

# 2nd Version
start = input("Do you want to play a guessing game? ")

while start == 'yes':
    question_input = input("How many finger does human have? ")
    question_input = int(question_input)
    if question_input == 10:
        response_input = input("Your answer is correct. Do you want to play again? ")
        while response_input == 'no':
            input("Thanks for playing the game")
    else:
        response_input = input("Your answer is incorrect. Do you want tp try again? ")
        if response_input == 'no':
            input("Thanks for playing the game.")
if start == 'no':
    print("Have a good day!")

# Letting the User Choose When to Quit
print("Letting the User Choose When to Quit\n")

prompt = "Tell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

prompt = "Tell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Practice
print("Practice (1st Version)\n")

start_1 = "Do you want to play a quiz?"
start_2 = "\nEnter 'yes' to play the quiz. "
start_3 = "\nEnter 'quit' to end the quiz. "
starts = start_1 + start_2 + start_3

question = "What is the most famous island is Indonesia? "
reply_t = "Your answer is correct. Do you want to play again?"
reply_f = "Your answer is incorrect. Do you want to try again?"
reply_2 = "\nPress any key to play again. "

ending = "Thanks for playing the game."
ending_2 = "Have a good day!"

start = input(starts).lower()
while start != 'quit':
    if start == 'yes':
        question_input = input(question + start_3).lower()
        if question_input == 'quit':
            start = question_input
        elif question_input == 'bali':
            reply_input = input(reply_t + reply_2 + start_3).lower()
            if reply_input == 'quit':
                start = reply_input
                print(ending)
        else:
            reply_input = input(reply_f + reply_2 + start_3).lower()
            if reply_input == 'quit':
                start = reply_input
                print(ending)
if start == 'quit':
    print(ending_2)

print("Practice (2nd Version)\n")

play_1 = "Do you want to play a quiz? "
play_2 = "\nPress any key to play. "

question = "What is the most famous island in Indonesia? "
reply_t = "Your answer is CORRECT. Do you want to play again?"
reply_f = "Your answer is INCORRECT. Do you want to try again?"

enter_quit = "\nEnter 'quit' to end the program. \n"
ending_quit = "Thanks for playing the game."
ending = "Have a nice day!"

play = input(play_1 + play_2 + enter_quit).lower()  #1
while play != 'quit':
    if play != 'quit': #2
        question_in = input(question + enter_quit).lower()
        if question_in == 'bali':   #3
            reply_in = input(reply_t + play_2 + enter_quit).lower()
            if reply_in == 'quit':  #4
                play = reply_in
                print(ending_quit)
        elif question_in == 'quit': #3
            play = question_in
            print(ending_quit)
        else:   #3
            reply_in = input(reply_f + play_2 + enter_quit).lower()
            if reply_in == 'quit':
                play = reply_in
                print(ending_quit)
if play == 'quit':
    print(ending)

# Using a Flag
print("Using a Flag\n")

prompt = "Tell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True
while active == True:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Practice
print("Practice (1st Version)\n")

start_1 = "Do you want to play a quiz?"
start_2 = "\nEnter 'yes' to play. "
quit_end = "\nEnter 'quit' to end the program. "

question = "What is the most famous island in Indonesia? "
response_t = "Your answer is correct. Do you want to play again?"
response_f = "Your answer is incorrect. Do you want to try again?"

ending = "\nThanks for playing the quiz."
ending_start = "\nHave a nice day!"

first = input(start_1 + start_2 + quit_end + " \n").lower()
if first == 'yes':
    start = True
    while start == True:
        question_in = input(question + quit_end + " \n").lower()
        if question_in == 'bali':
            response_in = input(response_t + start_2 + quit_end + " \n").lower()
            if response_in == 'yes':
                start = True
            elif response_in == 'quit':
                print(ending)
                start = False
        elif question_in == 'quit':
            print(ending_start)
            start = False
        else:
            response_in = input(response_f + start_2 + quit_end + " \n").lower()
            if response_in == 'yes':
                start = True
            elif response_in == 'quit':
                print(ending)
                start = False
elif first == 'quit':
    print(ending_start)
    start = False

# Practice
print("Practice (2nd Version)\n")

first_1 = "Do you want to play a Math game?"
enter_play = "\nEnter 'yes' to play."
enter_quit = "\nEnter 'quit' to end the program."

question = "2 + 2 = ...?"
answer = '4'
response_t = "Your answer is correct. Do you want to play again?"
response_f = "Your answer is incorrect. Do you want to try again?"

ending = "\nHave a nice day!"
ending_quit = "\nThanks for playing the game."

first = input(first_1 + enter_play + enter_quit + " \n").lower()
if first == 'yes':
    game = 'active'
    while game == 'active':
        question_input = input(question + enter_quit + " \n").lower()
        if question_input == answer:
            response_input = input(response_t + enter_play + enter_quit + " \n").lower()
            if response_input == 'quit':
                print(ending_quit + ending)
                game = False
        elif question_input == 'quit':
            print(ending)
            game = False
        else:
            response_input = input(response_f + enter_play + enter_quit + " \n").lower()
            if response_input == 'quit':
                print(ending_quit + ending)
                game = False
elif first == 'quit':
    print(ending)
    game = False

# Using break to Exit a Loop
print("Using break to Exit a Loop\n")

prompt = "Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Practice
print("Practice (1st Version)\n")

start_1 = "Do you want to play a quiz?"
enter_yes = "\nEnter 'yes' to play."
enter_quit = "\nEnter 'quit' to end the quiz."

question = "What is the capital city of England?"
response_t = "Your answer is correct. Do you want to play again?"
response_f = "Your answer is incorrect. Do you want to try again?"

ending = "\nHave a nice day!"
ending_quit = "\nThanks for playing the quiz."

start = input(start_1 + enter_yes + enter_quit + " \n").lower()
while start == 'yes':
    question_input = input(question + enter_quit + " \n").lower()
    if question_input == 'london':
        response_input = input(response_t + enter_yes + enter_quit + " \n").lower()
        if response_input == 'quit':
            print(ending_quit + ending)
            break
    elif question_input == 'quit':
        print(ending)
        break
    else:
        response_input = input(response_f + enter_yes + enter_quit + " \n").lower()
        if response_input == 'quit':
            print(ending_quit + ending)
            break
    if start == 'quit':
        break

# Using continue in a Loop
print("Using continue in a Loop\n")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Practice
print("Practice\nEven Numbers:")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue
    else:
        print(current_number)

print("\nPractice 2\n")

even_odd = "Enter 'even' to show even numbers and 'odd' for odd numbers. \n"
start = "Enter a minimum number. \n"
limit = "Enter a maximum number. \n"
enter_quit = "Enter 'quit' to end the program. \n"
ending = "Have a nice day!"

program = 'active'
while program == 'active':
    even_odd_input = input(even_odd + enter_quit)
    if even_odd_input == 'quit':
        print(ending)
        break
    start_input = input(start + enter_quit)
    if start_input == 'quit':
        print(ending)
        break
    else:
        start_input = int(start_input)
    limit_input = input(limit + enter_quit)
    if limit_input == 'quit':
        print(ending)
        break
    else:
        limit_input = int(limit_input)

    if even_odd_input == 'even':
        current_number = start_input
        while current_number < limit_input:
            current_number += 1
            if current_number % 2 == 0:
                print(current_number)
    elif even_odd_input == 'odd':
        current_number = start_input
        while current_number < limit_input:
            current_number += 1
            if current_number % 2 != 0:
                print(current_number)

# Avoiding Infinite Loops
print("Avoiding Infinite Loops\n")

x = 1
while x <= 5:
    print(x)
    x += 1

# But if you accidentally omit the line x += 1 (as shown next), the loop will run forever:
# Now the value of x will start at 1 but never change. As a result, the conditional test x <= 5 will
# always evaluate to True and the while loop will run forever, printing a series of 1s,

# Try It Yourself
print("Try It Yourself\n")

print("7-4. Pizza Toppings:\n")

prompt = "Tell me what you want for pizza toppings."
prompt += "\nEnter 'quit' to end the program. "

pizza_toppings = ''
while pizza_toppings != 'quit':
    pizza_toppings = input(prompt)
    print("I will add " + pizza_toppings + " on your pizza.")

print("7-5. Movie Tickets:\n")

start = "Please enter your age to check the price of your movie ticket."
enter_quit = "\nEnter 'quit' to end the program.\n"
ending = "Have a nice day!"
ticket = ''

program = 'active'
while program == 'active':
    start_input = input(start + enter_quit)
    if start_input == 'quit':
        program = False
        print(ending)
    else:
        age = int(start_input)
        if age < 3:
            ticket = 'free'
        elif age < 12:
            ticket = '$10'
        elif age >= 12:
            ticket = '$15'

        print("Your ticket price is " + ticket + ".")

print("Version 2\n")

greeting = "Welcome to Disneyland!\n"
first = "Do you want to watch a movie? (yes/no)\n"
prompt = "Enter your age to get your ticket price. \n"
enter_quit = "Enter 'quit' to end the program. \n"
ending = "Have a wonderful day in Disneyland!"

program = 'active'
while program == 'active':
    first_input = input(greeting + first)
    if first_input == 'no':
        print(ending)
        program = False
    while first_input == 'yes':
        age = input(prompt + enter_quit)
        if age == 'quit':
            print(ending)
            break
        else:
            age = int(age)
            if age < 3:
                print("Your ticket price is free.\n")
            elif age < 12:
                print("Your ticket price is $10.\n")
            else:
                print("Your ticket price is $15.\n")
    break

print("7-6. Three Exits:\n")

serve_1 = "Tell me what you want for pizza toppings.\n"
enter_quit = "Enter 'quit' to end the program. \n"
enter_yes = "Enter 'yes' to request another pizza toppings. \n"
ending_order = "Thanks for your request. Your pizza will be ready in 15 minutes. \n"
ending = "Have a nice day!"
request = "\nDo you have any other request? \n"

program = 'active'
while program == 'active':
    first_input = input(serve_1 + enter_quit)
    if first_input == 'quit':
        print(ending)
        break
    elif first_input != 'quit':
        print("\nWe will put " + first_input + " on your pizza.")
        request_input = input(request + enter_yes + enter_quit)
        if request_input == 'quit':
            print("\n" + ending_order + ending)
            program = False

print("Version 2\n")

greeting = "Welcome to Pizza Hut!\nDo you want to order a pizza? (yes/no). \n"
topping = "Enter your requested topping. \n"
stop = "Enter 'quit' to end the program. \n"
other = "Do you have another order? (yes/no) \n"
thanks = "Thank you for ordering our pizza. Your order will be served soon."
ending = "Have a nice day!"

program = 'active'
while program == 'active':
    greeting_input = input(greeting)    # 1
    if greeting_input == 'no':
        print(ending)
        program = False
    else:
        topping_input = input(topping + stop)       # 2
        if topping_input == 'quit':
            print(ending)
            break
        while topping_input != 'quit':
            print("I will put " + topping_input.title() + " on your pizza.\n")
            other_input = input(other)  # 3
            if other_input != 'no':
                topping_input = input(topping + stop)
                if topping_input == 'quit':
                    print(ending)
                    break
            elif other_input == 'no':
                print(thanks)
                break
    program = False

print("7-7. Infinity:\n")

x = 0
while x < 1:
    print(x)

# Using a while Loop with Lists and Dictionaries
print("Using a while Loop with Lists and Dictionaries\n")
print("Moving Items from One List to Another\n")

# Start with the users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['candace', 'brian', 'alice']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print("Verifying user: " + current_users.title())
    confirmed_users.append(current_users)

print("\nThese users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
print("Removing All Instances of Specific Values from a List\n")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input
print("Filling a Dictionary with User Input\n")

name = "What is your name. \n"
mountain = "Which mountain would you like to climb someday? \n"
respond = "Would you like to let another person respond? (yes/no) \n"
dictionary = {}

program = 'active'
while program == 'active':
    name_input = input(name)
    mountain_input = input(mountain)
    dictionary[name_input] = mountain_input

    respond_input = input(respond)

    if respond_input == 'no':
        program = False

print("--- Poll Results ---")
for name, mountain in dictionary.items():
    print(name.title() + " would like to climb " + mountain.title())

# Practice
print("Practice\n")

greeting = ". Welcome to McDonald! \n"
name = "Enter your name here. \n"
order = "Enter your order here. \n"
other = "Do you want to order anything else? Enter 'yes' to order. \n"
confirm = "Enter 'confirm' to confirm your order. \n"
enter_quit = "Enter 'quit' to end the program. \n"
ending = "Have a nice day!"
ending_2 = "Your order will be served soon."

orders = {}
program = 'active'
while program == 'active':
    name_input = input(name + enter_quit)       #1
    if name_input == 'quit':
        print(ending)
        program = False
    else:
        order_input = input("Hello " + name_input.title() + greeting + order + enter_quit)      #2
        if order_input == 'quit':
            print(ending)
            program = False
        while order_input != 'quit':
            other_input = input(other + confirm + enter_quit)       #3
            if other_input == 'quit':
                print(ending)
                program = False
            elif other_input == 'confirm':
                print("Thank you " + name_input.title() + " for ordering our food. Your " +
                      order_input.title() + " will be served soon.")
                program = False
            elif other_input == 'yes':
                order_2 = input(order + enter_quit)     #4
                if order_2 == 'quit':
                    print("Thank you " + name_input.title() + " for ordering our food. Your " +
                          order_input.title() + " will be served soon.")
                    program = False
                elif order_2 != 'quit':
                    orders[name_input] = [order_input, order_2,]
                    print("You ordered: ")
                    for foods in orders.values():
                        print(foods)
                elif order_2 == 'confirm':
                    print("Thank you " + name_input.title() +
                          " for ordering our food. Your orders will be served soon.")
                    program = False

# Try It Yourself
print("Try It Yourself\n")
print("7-8. Deli:\n")

sandwich_orders = ['seafood sandwich', 'egg sandwich', 'chicken sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print("I made your " + sandwiches.title() + ".")
    finished_sandwiches.append(sandwiches)
print("\nHere are sandwiches that have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

print("7-9. No Pastrami:\n")

sandwich_orders = ['seafood sandwich', 'egg sandwich', 'chicken sandwich', 'pastrami', 'pastrami', 'pastrami']
print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# Version 2
print("Version 2")

order = "Enter your order. \n"
stop = "Enter 'quit' to end the program. \n"
pastrami = "We have run out of Pastrami."
ending = "Here are sandwiches that have been made:"

sandwich_orders = []
finished_sandwiches = []

program = 'active'
while program == 'active':
    order_input = input(order + stop)
    if order_input == 'quit':
        while 'pastrami' in finished_sandwiches:
            print(pastrami)
            finished_sandwiches.remove('pastrami')
        print(ending)
        for sandwich in finished_sandwiches:
            print(sandwich.title() + " sandwich.")
        break
    else:
        sandwich_orders = [order_input]
        orders = sandwich_orders.pop()
        finished_sandwiches.append(orders)
        print(finished_sandwiches)

print("7-10. Dream Vacation:\n")

name = "Enter your name. \n"
place = "If you could visit one place in the world, where would you go? \n"
respond = "Would you like to let another person respond? (yes/no) \n"

polls = {}
program = 'active'
while program == 'active':
    name_input = input(name)
    place_input = input(place)
    respond_input = input(respond)
    polls[name_input] = place_input
    if respond_input == 'no':
        break
print("--- Survey Results ---")
for key, value in polls.items():
    print(key.title() + " would like to visit " + value.title() + ".")
