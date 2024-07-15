#Functions is a block of reusable code

def square(a):  #defining a function
  print(a**2)

a=int(input("Enter the value of a= ")) 
square(a) #calling a function 
#without calling nothing is printed


def square(a):  #defining a function
  return a**2

a=int(input("Enter the value of a= ")) 
c = square(a) #calling a function 
print("c = " ,c)


def add_numbers(a,b):
""" Function to add two numbers"""
return a + b
#Calling the function
print(add_number(3,4))


#Function with Default Arguments
def greet(name, message="Hello"):
  """Function to greet a person with a default message"""
  return f"{message}, {name}!"
#Calling the function
print(greet("Bob"))
print(greet("Alice","Hi"))


#Function with variable-Length Arguments
def sum_all(*args):
"""Function to sum all given arguments"""
return sum(args)

#Calling the function
print(sum_all(1,2,3,4,5))


#Function with Keyword Arguments
def display_info(**kwargs):
  """Function to display information using keyword arguments"""
  for key, value in kwarsg.items():
      print(f"{key}: {value}")

#calling the function
display_info(name="John", age=30, city="New York")


#Highest-Order function
def apply_function(func,x,y):
  """Function to apply another function to give aarguments"""
    return func(x,y)

def multiply(a,b):
  return a * b

#Calling the higher-order function
print(apply_function(multiply,6,7))


#Lambda expression, also known as anonymous function, are small,unnamed function defined using the "lambda" keyword. They are often used for short,throwaway function.

#Simple LAmbda function
square = lambda x: x * x

#Calling the lambda function
print(square(5))


#LAmbda funciton in 'map'
numbers = [1,2,3,4,5]
sqaures = list(map(lambda x: x * x, numbers))

#Displaying the reuslt
print(squares)


#Lambda function in 'filter'
numbers = [1,2,3,4,5,6]
even_numbers = list(filter x: x % 2 == 0, numbers))

#Displaying the result
print(even_numbers)


#Lambda Function in 'sorted'
students = [("Alice",25),("Bob",20),("Charlie",23)]
sorted_students = sorted(students, key=lambda students: student[1])

#Displaying the result
print(sorted_handling)



#Error Handling
#Error HAndling in Python is done using try,except,else and finally blocks. 
#It allows you to handle exception gracefully and ensure that the program continues to run.


#Basic Try-exxcept Block
try:
  #code that may raise an exception
  result = 10/0
except ZeroDivisionError:
  #code to handle the exception
  print("Cannot divide by zero!")


#Try-Except-Else Block
try:
  #Code that may raise an exception
  result = 10/2
except ZeroDivisionError:
  #code to handle the exception
  print("Cannot divide by zero!")
else:
  #Code to run if no exception occurs
  print("Division Successful")


#Try-Except-Finally Block
try:
  #Code that may raise an exception
  result = 10/2
except ZeroDivisionError:
  #Code to handle the exception
  print("Cannot divide by zero!")
finally:
  #Code to run regardless of whether an exception occurs
  print("Exceution completed.")


#Handling Multiple EXceptions
try:
  #Code that say raise an exception
  number = int(input("Enter a number: "))
  result = 10 / number
except ValueError:
  #code to handle the exception
  print("Invalid input! Please enter a number.")
except ZeroDivisionError:
  #Code to handle the exception
  print("Cannot divide by zero!")


#Raising Exception
def check_positive(number):
  if number <= 0:
    raise ValueError("Number must be positive")

try:
  check_positive(-5)
except ValueError as e:
  print(e)
