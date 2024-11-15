#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with  a try...except 
# block so that the user will allow them to enter an integer,
# or display an error message if they enter in something else.

number = input("Please enter in an integer value")
try:
    print("Now going to try to convert to an integer")
    number = int(number)
    print("We have successfully converted to an integer")
    print(f"You have entered {number}")
except Exception as e:
    print(f"There was an error {e}")

