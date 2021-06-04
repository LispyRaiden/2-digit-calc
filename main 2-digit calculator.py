print("Welcome to the 2 digit calculator. Type Start to being")  # Welcome message
multiply_action = ["Multiply", "Multiplication", "multiply", "multiplication"]  # Possible ways someone will spell the action
add_action = ["Add", "add", "Addition", "addition"]
sub_action = ["subtract", "Subtract", "subtraction", "Subtraction"]
divide_action = ["divide", "division", "Divide", "Division"]
exponent_action = ["exponent", "Exponent"]
x = input()  # This is where the program gets initiated
start_input = ["start", "Start"]
if x in start_input:  # This checks if x is any of the ways to say start
    print("Insert first number")
    x = int(input())  # the first number, for example in 3-1, 3 would go here
    print("Insert second number")
    y = int(input())  # the second number, for example 3-1, 1 would go here
    print("Insert action : We have multiply, addition, division, exponent, and subtraction.")
    z = input()  # this is the specific action the user desires out of the choices provided
    if z in multiply_action:  # this checks if the users input (input z) has any of the values in the data list named multiply_action which is at the very top
        def multiply_1(a):  # this defines a function and that function is (* y)
            return a * y  # when asked to print "multiply_1" it will reply with blank*y


        print(f"The result is {multiply_1(x)}")  # this part multiplies the value of x, which is the first number, with y, f makes the values understandable so they are not registered as text
    elif z in divide_action:  # the same process the multiplication went through repeats here, and 3 more times, but the names and values are different, also the arithmetic operators are also different
        def divide_2(a):
            return a / y


        print(f"The result is {divide_2(x)}")
    elif z in exponent_action:
        def exponent_3(a):
            return a ** y


        print(f"The result is {exponent_3(x)}")
    elif z in add_action:
        def add_4(a):
            return a + y


        print(f"The result is {add_4(x)}")
    elif z in sub_action:
        def sub_5(a):
            return a - y


        print(f"The result is {sub_5(x)}")
    else:
        print("Please give a proper value, reset and try again.")  # this is used to notify the user if something they put is invalid or comes up with an error
else:
    print("Please give a proper value, reset and try again.")  # this is used to notify the user if something they put is invalid or comes up with an error

print("Thank you for using the 2 digit calculator!")
print("Have a good rest of the day!")  # nice goodbye message
