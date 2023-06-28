# Q1. How do you comment code in Python? What are the different types of comments?
#Ans:-  we are use a '#' for the comment code in python.It is used for store a information about a code.
# Example :- 
# # This is a comment
# print("Hello World")
# print("This is a comment")

# Type of Comment
# Single Line Comment :-  # This is a comment
# Multi Line Comment :- """This is a comment"""
# Doc Comment :- """This is a comment"""

# Q2. What are variables in Python? How do you declare and assign values to variables?
# Ans:- A Python Variables is a symbolic name that is refrence or pointer to an Object is assigned to a variable ,you can refer to the Object by that name.
# Variables are assigned a value by using the assignment operator (=).
# Variables are declared by using the keyword var.
# Example :-
# var = 5
# var = 5 + 2
# var = 5 + 2 * 3
# var = 5 + 2 * 3 / 2

# Q3.How do you convert one data type to another in Python?
# Ans:- We are used a convertion for convert one data type to another data type.
# Example :-
# int(x [base])
# Converts x to an integer. base specifies the base if x is a string.
# float(x)
# Converts x to a floating-point number.
# str(x)
# Converts x to a string.
# repr(x)
# Converts x to a string representation.
# hex(x)
# Converts x to a hexadecimal string.
# oct(x)
# Converts x to an octal string.
# bin(x)
# Converts x to a binary string.
# dict(x)
# Converts x to a dictionary.
# list(x)
# Converts x to a list.
# set(x)
# Converts x to a set.
# tuple(x)
# Converts x to a tuple.
# x.isalnum()
# Returns True if x is a string and contains only alphanumeric characters.
# abs(x)
# Returns the absolute value of x.
# pow(x, y)
# Returns x raised to the power y.
# min(x, y)
# Returns the smaller of x and y.
# max(x, y)
# Returns the larger of x and y.
# dir(x)
# Prints the list of attributes of x.
# id(x)
# Returns the identity of x.
# x.__class__
# Returns the class of x.

# Q4. How do you write and execute a Python script from the command line?
# Ans:- The most basic and easy way to run a Python script is by using the python command.
# You need to open a command line and type the word python followed by the path to your script file like this.
# To run a script, you must add the script name to the end of the command.
# Example :-
# python script.py
# To run a script, you must add the script name to the end of the command.

# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
# Ans:- To slice a list, you can use the slice() function.
# slice(start, end, step)
my_list = [1,2,3,4,5]
print(my_list[1:3])
# Output - sub-list is [2,3]


# Q6. What is a complex number in mathematics, and how is it represented in Python?
# Ans:- Complex number is combination of real and imaginary part.
# Complex number is represented in Python as a tuple.
# x + yj
# x - yj
# x is the real part
# y is the imaginary part
# j is the imaginary unit


# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
#Ans:-
age = 25
print(age)
# Output - 25
# it is a carrent way to declare a variable named age and assign the value 25 to it.

# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
# Ans:-
price = 9.99
print(type(price))
# Output - <class 'float'>
# Float is a numerical data type.

# Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable ?
# Ans:-
name = "Aman Kumar Sharma"
print(name)
# Output - Aman Kumar Sharma

# Q10. Given the string "Hello, World!", extract the substring "World"
# Ans:-
# substring(start, end)
# substring(start, end) is a function that returns a substring of the string.
# Example:-
# print(string[start:end])
str = "Hello, World!"
print(str[7:12])
# Output - World

# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.
# Print the value of this variable.
# Ans:-
is_student = True
if is_student == True:
   print(is_student)
   # Output - True
else:
   print(is_student)
   # Output - False



