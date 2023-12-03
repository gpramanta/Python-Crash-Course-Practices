# A Simple Example
cars = []
cars.insert(0, 'audi')
cars.insert(1, 'bmw')
cars.insert(2, 'subaru')
cars.insert(3, 'toyota')

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")

vocalists_names = []
vocalists_names.insert(0, 'james')
vocalists_names.insert(1, 'paul')
vocalists_names.insert(2, 'mccartney')

for vocalists_name in vocalists_names:
    if vocalists_name == 'mccartney':
        print("McCartney")
    else:
        print(vocalists_name.title())
print("\n")

# Conditional Tests
# Checking for Equality
# 1 >>> car = 'audi'
# 2 >>> car == 'bmw'
# False
# A single equal sign is really a statement; you might read the code at 1 as 
# “Set the value of car equal to 'audi'.” On the other hand, a double equal 
# sign, like the one at 2, asks a question: “Is the value of car equal to 
# 'bmw'?” Most programming languages use equal signs in this way.

# Practice:
car1 = 'audi'
car2 = 'bmw'
cars = [car1, car2]

for car in cars:
    if car1 == car2:
        print("True")
    else:
        print("False")
print("\n")

# Ignoring Case When Checking for Equality
#1 >>> car = 'Audi'
#2 >>> car.lower() == 'audi'
# True
#3 >>> car
# 'Audi'
# At u we store the capitalized string 'Audi' in the variable car. At v we 
# convert the value of car to lowercase and compare the lowercase value to the 
# string 'audi'. The two strings match, so Python returns True. At w we can see 
# that the value stored in car has not been affected by the conditional test.

# Checking for Inequality
# When you want to determine whether two values are not equal, you can combine 
# an exclamation point and an equal sign (!=). The exclamation point represents 
# not, as it does in many programming languages.

requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the Anchovies")
print("\n")

# Numerical Comparisons
answer = 17

if answer != 42:    #1
    print("This is not the correct answer. Please try again.")

# The conditional test at 1 passes, because the value of answer (17) is not 
# equal to 42. Because the test passes, the indented code block is executed:
# That is not the correct answer. Please try again!

# Practice
answer1 = 9
correct_answer = 9

message_wrong = "Your answer is wrong. Please try again."
message_right = "Your answer is correct."

if answer1 != correct_answer:    
    print(message_wrong)
else:
    print(message_right)
print("\n")

age = 19

if age < 21:
    print(True)
else:
    print(False)

if age <= 21:
    print(True)
else:
    print(False)

if age > 21:
    print(True)
else:
    print(False)

if age >= 21:
    print(True)
else:
    print(False)

# Each mathematical comparison can be used as part of an if statement, 
# which can help you detect the exact conditions of interest.

# Practice:
age_0 = 19
age_1 = 21
ages = []
ages.append(age_0)
ages.append(age_1)

for age in ages:
    if age_0 <= age_1:
        print("Correct")
    else:
        print("False")
print("\n")

# Checking Multiple Conditions
# You might need two conditions to be True to take an action. Other times 
# you might be satisfied with just one condition being True. The keywords 
# and and or can help you in these situations.

# Using and to Check Multiple Conditions
# To check whether two conditions are both True simultaneously, use the keyword 
# and to combine the two conditional tests; if each test passes, the overall 
# expression evaluates to True. If either test fails or if both tests fail, 
# the expression evaluates to False.

age_0 = 22
age_1 = 18 

if age_0 >= 21 and age_1 >= 21:
    print(True)
else:
    print(False)

age_1 = 22

if age_0 >= 21 and age_1 >= 21:
    print(True)
else:
    print(False)

# At 1 we define two ages, age_0 and age_1. At 2 we check whether both ages 
# are 21 or older. The test on the left passes, but the test on the right 
# fails, so the overall conditional expression evaluates to False. At 3 we 
# change age_1 to 22. The value of age_1 is now greater than 21, so both 
# individual tests pass, causing the overall conditional expression to 
# evaluate as True.

# Practice:
my_age = 25
her_age = 18
our_age = []
our_age.append(my_age)
our_age.append(her_age)

for age in our_age:
    if my_age and her_age >= 18:
        print("Legal")
    else:
        print("Prohibited")
print("\n")

# To improve readability, you can use parentheses around the individual tests, 
# but they are not required. If you use parentheses, your test would look like 
# this:

# (age_0 >= 21) and (age_1 >= 21)

# Practice
sibling_1 = 18
sibling_2 = 17
siblings = []
siblings.append(sibling_1)
siblings.append(sibling_2)

for sibling in siblings:
    if (sibling_1 >= 18) and (sibling_2 >= 18):
        print("Allowed to Enter.")
    else:
        print("Not Allowed to Enter.") 
print("\n")

# Using or to Check Multiple Conditions

# The keyword or allows you to check multiple conditions as well, but it passes 
# when either or both of the individual tests pass. An or expression fails only 
# when both individual tests fail.

age_0 = 22
age_1 = 18

if (age_0 >= 21) or (age_1 >= 21):
    print(True)
else:
    print(False)

age_0 = 18

if (age_0 >= 21) or (age_1 >= 21):
    print(True)
else:
    print(False)

# We start with two age variables again at 1. Because the test for age_0 at 2 
# passes, the overall expression evaluates to True. We then lower age_0 to 18. 
# In the test at w, both tests now fail and the overall expression evaluates to 
# False.

# Practice:
age1 = 21
age2 = 18
their_age = []
their_age.append(age1)
their_age.append(age2)

for age in their_age:
    if (age1 >= 21) or (age2 >= 21):
        print("Legal")
    else:
        print("Illegal")

age1 = 18

for age in their_age:
    if (age1 >= 21) or (age2 >= 21):
        print("Legal")
    else:
        print("Illegal")
print("\n")

# Checking Whether a Value Is in a List
# To find out whether a particular value is already in a list, use the keyword 
# in.

# >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 1 >>> 'mushrooms' in requested_toppings
# True
# 2 >>> 'pepperoni' in requested_toppings
# False

# Practice:
requested_toppings = []
requested_toppings.insert(0, 'mushrooms')
requested_toppings.insert(1, 'onions')
requested_toppings.insert(2, 'pineapple')

for requested_topping in requested_toppings:
    if 'mushrooms' in requested_toppings:
        print("True")
    else:
        print("False")
for requested_topping in requested_toppings:
    if 'pepperoni' in requested_toppings:
        print("True")
    else:
        print("False")
print("\n")

# Checking Whether a Value Is Not in a List
# If a value does not appear in a list. You can use the keyword not in this 
# situation.

# Practice:
banned_users = []
banned_users.insert(0, 'andrew')
banned_users.insert(1, 'carolina')
banned_users.insert(2, 'david')

user = 'marie'
message = ", you can post a response if you wish."

if user not in banned_users:
    print(user.title() + message)
print("\n")

# Boolean Expressions
# A Boolean expression is just another name for a conditional test. A Boolean 
# value is either True or False, just like the value of a conditional 
# expression after it has been evaluated.

# game_active = True 
# can_edit = False

# Try It Yourself
# 5-1. Conditional Tests:
city = "London"
print("Is capital city of Britain == 'London'? I predict it is true.") 
print(city == 'London')

city1 = "Paris"
print("Is capital city of France == 'Milan'? I predict it is false.")
print(city1 == 'Milan')
print("\n")

# 1.Conditional Test (True):
# Red States
answer_red = 'alaska'
question_red = "Is " + answer_red.title() + " one of the red states?"
red_states = []
red_states.insert(0, 'alabama')
red_states.insert(1, 'alaska')
red_states.insert(2, 'arizona')

print(question_red)
if answer_red in red_states:
    print("True")
else:
    print("False")

if (answer_red == red_states[1]):
    print("It is a red state.")
else:
    print("It is a blue state.")
print("\n")

# 2.Conditional Test (False):
# Blue States
answer_blue = "alabama"
question_blue = "Is " + answer_blue.title() + " one of the blue states?"
blue_states = []
blue_states.insert(0, 'california')
blue_states.insert(1, 'connecticut')
blue_states.insert(2, 'delaware')

print(question_blue)
if answer_blue in blue_states:
    print("True")
else:
    print("False")

blue_state = answer_blue
if(blue_state == blue_state in blue_states[0:3]):
    print("It is a blue state.")
else:
    print("It is a red state.")
print("\n")

# 3.Conditional Test (True):
# Who Wants To Be A Millionaire

n = "national"
h = "health"
s = "service"
NHS = n + " " + h + " " + s

nhs_question = "In the UK, the abbreviation NHS stands for National what Service?"
nhs_options = []
nhs_answer = 'health'
nhs_answer = nhs_answer.title()
nhs_options.insert(0, 'Humanity')
nhs_options.insert(1, 'Health')
nhs_options.insert(2, 'Honour')
nhs_options.insert(3, 'Household')

print(nhs_question)
for nhs_option in nhs_options:
    print("> " + nhs_option)
if nhs_answer in nhs_options:
    print(nhs_answer + ".\n")
else:
    print("I don't know.")

if nhs_answer == nhs_options[1] in nhs_options:
    print(NHS.title() + ".\n")
else:
    print("I don't know.")

# 4.Conditional Test (False):
# Dollar to Rupiah

dollar_symbol = "$"
rupiah_symbol = "Rp. "
dollar_value = 14336
dollar_numbers = list(range(1,6))

dollar_to_rupiahs = []
for dollar_number in dollar_numbers:
    dollar_to_rupiah = dollar_number*dollar_value
    dollar_to_rupiahs.append(dollar_to_rupiah)

rupiahs = dollar_to_rupiahs
indonesian_rupiahs = []
for rupiah in rupiahs:
    indonesian_rupiah = rupiah_symbol + str(rupiah)
    indonesian_rupiahs.append(indonesian_rupiah)

dollars = []
one_dollar = 'Rp. 14336'
two_dollar = 'Rp. 28672'
three_dollar = 'Rp. 43008'
four_dollar = 'Rp. 57344'
five_dollar = 'Rp. 71680'

dollars.append(one_dollar)
dollars.append(two_dollar)
dollars.append(three_dollar)
dollars.append(four_dollar)
dollars.append(five_dollar)

rupiah_question = "How much is $1 in Indonesian Rupiah?"
rupiah_answer = "Rp. 14337"
print(rupiah_question)
print("Is it " + rupiah_answer + "?")

if rupiah_answer in indonesian_rupiahs:
    print("Correct.")
else:
    print("Incorrect.")

if rupiah_answer == indonesian_rupiahs[0] :
    print("$1 is equal to Rp. 14336.")
else:
    print("You miscalculated.")
print("\n")

# 5.Conditional Test (True):
# Additions

numbers = (list(range(1,6)))
addition_answer = 2
addition = numbers[0] + numbers[0]
question_addition = "1 + 1 = ?"
plus_line = "_______ +" 

print(question_addition)
print(str(addition_answer) + "?\n")

print(numbers[0])
print(numbers[0])
print(plus_line)
print(addition)

if addition_answer == addition:
    print("Your addition is correct.")
else:
    print("Your addition is incorrect")
print("\n")

# 6.Conditional Test (False):
# Subtraction
title_practice6 = "Adding & Subtracting Negative Numbers"
question_subtraction = "Evalute 17 + (-8) + (-8)"
question_subtraction1 = 17 + (-8) + (-8)
answer_range = list(range(1,11))
answer_options = ['a. ', 'b. ', 'c. ', 'd. ', 'e. ']
subtraction_answer = answer_range[1]

print(title_practice6 + "\n")
print(question_subtraction + "\n")
for answer_option in answer_options:
    print(str(answer_option) + str(answer_range.pop(0)))

print("Is it b.2?")
if subtraction_answer == question_subtraction1:
    print("Your answer is correct.")
else:
    print("Your answer is incorrect.")
    print("The correct answer is " + str(question_subtraction1) + ".")
print("\n")

# 7.Conditional Test (True):
# Multiplication

multiplication = 10 * 10
multiplication_options = list(range(97,102))
option_chars = ['a. ', 'b. ', 'c. ', 'd. ', 'e. ']
multiplication_answer = 100

print("Multiplication:\n")
print("\t" + str(int(10)))
print("\t" + str(int(10)))
print("\t____ x")
print("\t00")
print("   10")
print("   ______ +")
print("   " + str(multiplication) + "\n")

for option_char in option_chars:
    print(str(option_char) + str(multiplication_options.pop(0)))

if multiplication_answer == multiplication:
    print(str(multiplication_answer == multiplication) + ". The answer is d.")
else:
    print("False")
print("\n")

# 8.Conditional Test (False):
# Division
question_currency = "How much is Rp. 14335 to a dollar? Is it $ 2?"
dollar1 = "$ "
indo_rupiahs = []
indo_rupiahs.insert(0, 14335)
indo_rupiahs.insert(1, 28670)
indo_rupiahs.insert(2, 43005)
indo_rupiahs.insert(3, 57340)
indo_rupiahs.insert(4, 71675)

rupiah_to_dollars = []
for indo_rupiah in indo_rupiahs:
    rupiah_to_dollar = indo_rupiah / 14335
    rupiah_to_dollars.append(rupiah_to_dollar)

converted_dollars = []
for rupiah_to_dollar in rupiah_to_dollars:
    converted_dollar = str(dollar1) + str(rupiah_to_dollar)
    converted_dollars.append(converted_dollar)

print(question_currency)
if 2 == rupiah_to_dollars[0]:
    print(1 == rupiah_to_dollars[0])
else:
    print(False)
    print("It is " + converted_dollars[0] + ".")
print("\n")

# 9.Conditional Test (True):
# Squares
square_question = "Is 100 the square of 10?"
square_answer = 10**2
square_numbers = list(range(1,11))
squares = []
for square_number in square_numbers:
    square = square_number**2
    squares.append(square)
print(square_question)
if square_answer in squares:
    print(square_answer == squares[9])
else:
    print(False)
print("\n")

# 10.Conditional Test (False):
# Even numbers
even_question = "Mention even numbers from 2 to 10."
even_numbers = list(range(2,11,2))
even_answer = []
even_answer.insert(0, 1)
even_answer.insert(1, 4)
even_answer.insert(2, 6)
even_answer.insert(3, 8)
even_answer.insert(4, 10)

print(even_question)
print(even_answer)
if even_answer == even_numbers:
    print(even_answer == even_numbers)
else:
    print(False)
print("\n")

# 5-2. More Conditional Tests:
# Tests for equality and inequality with strings
my_saving = 'Rp. 20.000.000'
his_saving = 'Rp. 64.000.000'
print("my_saving == his_saving?")
if my_saving == his_saving:
    print("Equal")
else:
    print("Inequal")
print("\n")

# Tests using the lower() function
my_name = "komang pramanta gerinata"
my_name2 = "KOMANG PRAMANTA GERINATA"
lower_name = my_name2.lower()

if my_name == lower_name:
    print(my_name == lower_name)
else:
    print(False)

# Numerical tests involving equality and inequality, greater than and less than, 
# greater than or equal to, and less than or equal to
dollar_rupiah = 14313
euro_rupiah = 16190

print("equality and inequality")
if dollar_rupiah == euro_rupiah:
    print(str(dollar_rupiah) + " == " + str(euro_rupiah))
else:
    print(str(dollar_rupiah) + " =/= " + str(euro_rupiah))
print("\n")

print("greater than and less than")
if dollar_rupiah > euro_rupiah:
    print(str(dollar_rupiah) + " > " + str(euro_rupiah))
else:
    print(str(dollar_rupiah) + " < " + str(euro_rupiah))
print("\n")

print("greater than or equal to, and less than or equal to")
if dollar_rupiah >= euro_rupiah:
    print(str(dollar_rupiah) + " >= " + str(euro_rupiah))
else:
    print(str(dollar_rupiah) + " <= " + str(euro_rupiah))
print("\n")

# if Statements
# Simple if Statements

# if conditional_test:
#     do something

# You can put any conditional test in the first line and just about any action 
# in the indented block following the test. If the conditional test evaluates 
# to True, Python executes the code following the if statement. If the test 
# evaluates to False, Python ignores the code following the if statement.

# voting.py

#  age = 19 
#1 if age >= 18: 
#2     print("You are old enough to vote!")
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print("\n")

# if-else Statements
# An if-else block is similar to a simple if statement, but the else statement 
# allows you to define an action or set of actions that are executed when the 
# conditional test fails.

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are to young to vote.")
    print("Please register to vote as soon as you turn 18!")
print("\n")

# The if-elif-else Chain
# To test more than two possible situations, and to evaluate these you can use 
# Python’s if-elif-else syntax. Python executes only one block in an 
# if-elif-else chain. It runs each conditional test in order until one passes. 
# When a test passes, the code following that test is executed and Python skips 
# the rest of the tests.

# Amusement Park
# • Admission for anyone under age 4 is free. 
# • Admission for anyone between the ages of 4 and 18 is $5. 
# • Admission for anyone age 18 or older is $10.
age = 5
if age < 4: # 1
    print("Your admission is free.")
elif age < 18: # 2
    print("Your admission is $ 5.")
else: # 3
    print("Your admission is $ 10.")

candidate = 36
if candidate < 18:
    print("You are not allowed to submit your CV.")
elif candidate < 35:
    print("You are allowed to submit your CV.")
else:
    print("Only experienced workers are choosen.")

age1 = 3
if age1 < 4:
    price = 0  # 1
elif age1 < 18:
    price = 5  # 2
else:
    price = 10  # 3
print("Your admission is $" + str(price) + ".\n")  # 4

# The lines at 1, 2, and 3 set the value of price according to the person’s age,
# as in the previous example. After the price is set by the if-elif-else chain, 
# a separate unindented print statement 1 uses this value to display a message 
# reporting the person’s admission price.
# not enough 0 - 4, Bronze 5 - 10, Silver 11 - 15, Gold 16 - 20

# Using Multiple elif Blocks
age2 = 65
if age2 < 4:
    price = 0
elif age2 < 18:
    price = 5
elif age2 < 65:
    price = 10
else:
    price = 5
print("Your admission is $" + str(price) + ".\n") 

# Omitting the else Block
age3 = 65
if age3 < 5:
    price = 0
elif age3 < 18:
    price = 5
elif age3 < 65:
    price = 10
elif age3 >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".\n")

# Practice if-elif-else chain
print("if-elif-else chain\n")

age = 20

if age < 4:
    price = 0
elif (age >= 4) and (age < 18):
    price = 5
elif age >= 18:
    price = 10

print("Your entry price is $" + str(price) + ".")

age = 65

if age < 4:         # Baby
    price = 0
elif age < 18:      # Teenager
    price = 5
elif age < 65:      # Adult
    price = 10
else:               # Elderly
    price = 5

print("Your entry price is $" + str(price) + ".")

age = 17

if age < 4:
    price = 0
elif (age >= 4) and (age < 18):
    price = 5
elif (age >= 18) and (age < 65):
    price = 10
elif age >= 65:
    price = 5

print("Your entry price is $" + str(price) + ".")

# The else block is a catchall statement. It matches any condition that wasn’t 
# matched by a specific if or elif test, and that can sometimes include invalid 
# or even malicious data. If you have a specific final condition you are 
# testing for, consider using a final elif block and omit the else block. As a 
# result, you’ll gain extra confidence that your code will run only under the 
# correct conditions.

# Testing Multiple Conditions
# Toppings
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding Mushrooms")
if 'macaroni' in requested_toppings:
    print("Adding Macaroni")
if 'extra cheese' in requested_toppings:
    print("Adding Extra Cheese")

print("\nFinish making your Pizza!\n")

# Paul & John
# Paul
names = ['james', 'paul', 'mccartney']
names = [name.title() for name in names]
last_name = names[2]
if last_name in names:
    del names[2]
    names.insert(2, 'McCartney')

titles = ['sir ', 'cbe.', 'mbe.']
titles = [title.upper() for title in titles]
sir = titles[0]
if sir in titles:
    del titles[0]
    titles.insert(0, 'Sir ')

paul = titles[0] + " " + names[0] + " " + names[1] + " " + names[2] + " " + titles[1] + titles[2]
print(paul + "\n")

# John
names1 = ['john', 'joseph', 'mcgowan']
names1 = [name1.title() for name1 in names1]
last_name1 = names1[2]
if last_name1 in names1:
    del names1[2]
    names1.insert(2, 'McGowan')
john = names1[0] + " " +  names1[1] + " " + names1[2]
print(john + "\n")

# This code would not work properly if we used an if-elif-else block, because 
# the code would stop running after only one test passes.

requested_toppings = ['mushrooms', 'extra cheese'] 
if 'mushrooms' in requested_toppings: 
   print("Adding mushrooms.") 
elif 'pepperoni' in requested_toppings: 
   print("Adding pepperoni.") 
elif 'extra cheese' in requested_toppings: 
   print("Adding extra cheese.") 

print("\nFinished making your pizza!")

# The test for 'mushrooms' is the first test to pass, so mushrooms are added to 
# the pizza. However, the values 'extra cheese' and 'pepperoni' are never 
# checked, because Python doesn’t run any tests beyond the first test that 
# passes in an if-elif-else chain. The customer’s first topping will be added, 
# but all of their other toppings will be missed.

# In summary, if you want only one block of code to run, use an if-elifelse 
# chain. If more than one block of code needs to run, use a series of 
# independent if statements.

# Try It Yourself
# 5-3. Alien Colors #1a:
print("5-3. Alien Colors #1a:")
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You have just earned 5 points!")
if 'yellow' in alien_color:
    print("You have just earned 9 points!")
if 'blue' in alien_color:
    print("You have just earned 1 points!")

alien_color = 'yellow'

if alien_color == 'green':
    point = 5
else:
    point = 0

if point > 1:
    print("You have just earned " + str(point) + " points!")
else:
    print("You have just earned " + str(point) + " point!")

alien_color = 'red'

if alien_color == 'blue':
    point = 0
elif alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 15

if point > 1:
    print("You have just earned " + str(point) + " points!")
else:
    print("You have just earned " + str(point) + " point!")

# 5-3. Alien Colors #1b:
print("5-3. Alien Colors #1b:")

alien_color = "blue"

if alien_color == 'green':
    print("You have just earned 5 points!")
elif alien_color == 'yellow':
    print("You have just earned 10 points!")
elif alien_color == 'red':
    print("You have just earned 15 points!")

# 5-4. Alien Colors #2:
print("\n5-4. Alien Colors #2:")
alien_color1 = 'yellow'
if 'green' == alien_color1:
    print("You have just earned 5 points for shooting the alien.")
else:
    print("You have just earned 10 points for shooting the alien.")

alien_color2 = 'red'
if 'red' == alien_color2:
    print("You have just earned 5 points for shooting the alien.")
else:
    print("You have just earned 10 points for shooting the alien.")
if 'yellow' == alien_color2:
    print("You have just earned 5 points for shooting the alien.")
else:
    print("You have just earned 10 points for shooting the alien.")

# 5-5. Alien Colors #3:
print("\n5-5. Alien Colors #3:")
alien_colors = ['green', 'yellow', 'red']
alien = alien_colors[0]
if alien_colors[0] == alien:
    print("You have just earned 5 points!")
elif alien_colors[1] == alien:
    print("You have just earned 10 points!")
else:
    print("You have just earned 15 points!")
print("\n")
alien = alien_colors[1]
if alien_colors[0] == alien:
    print("You have just earned 5 points!")
elif alien_colors[1] == alien:
    print("You have just earned 10 points!")
else:
    print("You have just earned 15 points!")
print("\n")
alien = alien_colors[2]
if alien_colors[0] == alien:
    print("You have just earned 5 points!")
elif alien_colors[1] == alien:
    print("You have just earned 10 points!")
else:
    print("You have just earned 15 points!")
print("\n")

# 5-6. Stages of Life:
print("5-6. Stages of Life:")
person = 65
if person < 2:
    print("You are a baby.")
elif person < 4:
    print("You are a toddler.")
elif person < 13:
    print("You are a kid.")
elif person < 20:
    print("You are a teenager.")
elif person < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

age = 65

if age < 2:
    person = "baby"
elif age < 4:
    person = "toddler"
elif age < 13:
    person = "kid"
elif age < 20:
    person = "teenager"
elif age < 65:
    person = "adult"
elif age >= 65:
    person = "elder"

if person == "adult" or person == "elder":
    print("You are an " + person + ".")
else:
    print("You are a " + person + ".")

# 5-7. Favorite Fruit:
print("5-7. Favorite Fruit:")
fav_fruits = ['avocados', 'coconuts', 'durians', 'mangosteens', 'rambutans'] 
if 'avocado' in fav_fruits:
    print("You really like avocados!")
if 'coconuts' in fav_fruits:
    print("You really like coconuts!")
if 'durians' in fav_fruits:
    print("You really like durians!")
if 'mangosteens' in fav_fruits:
    print("You really like mangosteens!")
if 'rambutans' in fav_fruits:
    print("You really like rambutans!\n")

# Using if Statements with Lists
print("Using if Statements with Lists\nChecking for Special Items\n")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("Finish making your Pizza!\n")

# But what if the pizzeria runs out of green peppers? An if statement inside 
# the for loop can handle this situation appropriately:
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinish making your Pizza!\n")

# Practice
requested_indofoods = ['nasi goreng', 'mie goreng', 'bakso', 'nasi campur']
for requested_indofood in requested_indofoods:
    if requested_indofood == 'nasi goreng':
        print("Nasi Goreng is not available today.")
    else:
        print("Making " + requested_indofood.title() + ".")
print("Finish making Indonesian foods.\n")

paul_titles = ['sir', 'ch', 'mbe']
for paul_title in paul_titles:
    if paul_title == 'sir':
        print("Sir")
    else:
        print(paul_title.upper())
print("\n")

# Checking That a List Is Not Empty
requested_toppings = [] # 1
if requested_toppings: # 2
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping)
    print("Finish making Pizza!")
else: # 3
    print("Are you sure you want plain Pizza?\n")
# When the name of a list is used in an if statement, Python returns True if 
# the list contains at least one item; an empty list evaluates to False. If 
# requested_toppings passes the conditional test, we run the same for loop we 
# used in the previous example. If the conditional test fails, we print a 
# message asking the customer if they really want a plain pizza with no 
# toppings 4.

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                        'pepperoni', 'pinneaple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinish making Pizza!\n")

# Try It Yourself
# 5-8. Hello Admin:
print("5-8. Hello Admin:")
name_lists = ['john', 'morrissey', 'thom', 'paul', 'george', 'admin']
for name in name_lists:
    if name == 'admin':
        print("Hello admin, would you like to see status report?")
    else:
        print("Hello " + name.title() + ", thank you for logging again.")

# 5-9. No Users:
print("\n5-9. No Users:")
name_lists = []
if name_lists:
    for name in name_lists:
        print("Hello " + name + ", thank you for logging again.")
else:
    print("We need to find some users!\n")

# 5-10. Checking Usernames:
print("5-10. Checking Usernames:")
current_users = ['joseph', 'harrison', 'mccartney', 'patrick', 'yorke']
new_users = ['joseph', 'harrison', 'michael', 'kanye', 'chris']
for new_user in new_users:
    if new_user in current_users:
        print("User name " + "'" + new_user + "'" + " has already been used. Please enter a new user name.")
    else:
        print("User name " + "'" + new_user + "'" + " is available.")
print("\n")

# 5-11. Ordinal Numbers:
print("5-11. Ordinal Numbers:")
my_numbers = list(range(1,10))
for my_number in my_numbers:
    if my_number == 1:
        print(str(my_numbers[0]) + "st")
    elif my_number == 2:
        print(str(my_numbers[1]) + "nd")
    else:
        print(str(my_number) + "th")

# Styling Your if Statements
