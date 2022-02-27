

from ntpath import join


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Data Types

# Numbers and Floats
print(f'''{bcolors.OKBLUE}
----------Arithmetic Operators----------''')
a = 5
b = 2
# Operators precedence: () ** // / * % + - 
add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
exp = a ** b
flo = a // b
ope = 7 + 7 % 5 - 2 * 3 / 2 ** 2

print(f'''add a + b: {add}
sub a - b: {sub}
mul a * b: {mul}
div a / b: {div}
mod a % b: {mod}
exp a ** b: {exp}
flo a // b: {flo}
ope a operation b: {ope}'''
)

# ----------Strings and Text----------
print(f'''{bcolors.OKGREEN}
----------Strings----------''')
# We can use single or double quotes: ' or "
print('String: Hello World')
string = "Hello World"
# Each string has a index starting at 0
print(f'First index: {string[1]}') # H
print(f'Inverse indexing: {string[-1]}') # d

# Slice allows us to select a substring of a string
slice_string = string[0:8:2]
print(f'Sliced string 0:8:2: {slice_string}') # Hello

# Show length of string
print(f'String lenght: {str(len(string))}') # 11

# Strings does not support item assignment
name = 'John'
last_letter = name[-1]
print(f'Name: John')
print(f'Last letter: {last_letter}') # n
print(f'Concat J + name[1:]: J{name[1:]}') # John
print(f'Multiply string: {name * 3}') # JohnJohnJohn
print(f'String to uppercase: {name.upper()}') # JOHN
print(f'String to lowercase: {name.lower()}') # john
print(f"Split string (Text-to-split): {'Text-to-split'.split('-')}") # ['Text', 'to', 'split']

# String formatting can be done with f-strings or format()
# It can be done with index or variables
print('Formatting with format(): {r} {r}'.format(q = 'Hello', r = 'World')) # Hello World

result = 1000/8
print(f'Formatting with f-string and float: {result:10.3f}') # 0.113


print(f'''{bcolors.FAIL}
----------List----------''')

first_list = [1, 5]
second_list = ['six', 'ten']
combined_list = first_list + second_list
print(f'First list: {first_list}') # [1, 5]
print(f'Concat lists: {combined_list}') # [1, 2, 3, 4, 5, 'six', 'ten']

combined_list[0] = 'one'
print(f"change list: {combined_list}") # one...
combined_list.append(11)
print(f'Add new element to list with append: {combined_list}') # ...eleven
combined_list.pop(2)
print(f'Remove element from list with pop: {combined_list}') # eleven

unordered_list = [5, 2, 9, 1, 3, 4, 7, 8, 6]
unordered_list.sort()
print(f'Ordered list: {unordered_list}') # [1, 2, 3, 4, 5, 6, 7, 8, 9]
unordered_list.reverse()
print(f'Reverse ordered list: {unordered_list}') # [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f'''{bcolors.WARNING}
----------Dictionaries----------''')

my_dict = {'one': 1, 'two': 2, 'three': 3}
print(f'Dictionary: {my_dict}') # {'one': 1, 'two': 2, 'three': 3}
print(f'Get value from dictionary: {my_dict["one"]}') # 1

my_dict["four"] = 4
print(f'Add new key to dictionary: {my_dict}') # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(f'See all keys, values, or items: {my_dict.items()}') # dict_keys(['one', 'two', 'three', 'four'])

print(f'''{bcolors.OKCYAN}
----------Tuples----------''')

# Tuples are immutable
new_tuple = (a, b, a)
new_list = [1, 2, 3]
print(f'Show type of tuple: {type(new_tuple)}') # <class 'tuple'>

print(f'Count of tuple: {new_tuple.count(a)}') # 3
print(f'Index of tuple: {new_tuple.index(a)}') # 0

print('\n----------Set----------')
# Sets are unordered and unindexed collections of unique elements
my_list_with_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Using Set to remove duplicates: {set(my_list_with_duplicates)}') # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print('\n----------Boolean----------')
# Booleans are either True or False
print(f'Boolean: {True}') # True
print(f'Check if 1 is bigger than 2: {1 > 2}') # False

# Operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Conditional operators: if, elif, else

print('\n----------If Statements----------')
# If statements are used to execute code based on a condition
if True == True and not True:
    print('True')
else:
    print('False')

print(f'''{bcolors.OKGREEN}
----------For----------''')
# For loops are used to execute a block of code a number of times
another_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in another_list:
    if item % 2 == 0:
        print(f'{item} is even')
    else:
        print(f'{item} is odd')

# Sum of all numbers in list
sum = 0
for item in another_list:
    sum += item
print(f'Sum of all numbers in list: {sum}') # 55

# Print each letter in string
for index,letter in enumerate('Hello'):
    print(index,letter)

# Print (a,b) for each item in a tuple
tuple_list = [(1, 2), (3, 4), (5, 6)]
for (a, b) in tuple_list:
    print(f'{a}, {b}')

# Print (a,b) for each item in a dictionary
dict_list = {'a': 1, 'b': 2, 'c': 3}
for a, b in dict_list.items():
    print(f'{a}, {b}')


print(f'''{bcolors.HEADER}
----------While----------''')
# While loops are used to repeat a block of code until a condition is met
i = 0
while i < 10:
    print(f'{i}')
    i += 1
else: 
    print('Done')

# Pass statement is used when a statement is required syntactically but you do not want any command or code to execute
# Continue statement is used to skip the rest of the code in the current iteration of the loop
# Break statement is used to end the loop and skip the rest of the code in the current iteration of the loop

# Range function is used to generate a sequence of numbers
#for i in range(0,10,2):
#   print(i)

#list(range(0,10,2)) # [0, 2, 4, 6, 8]

print(f'\n----------Zip----------')
# Zip function is used to combine sequences into a single sequence
for a, b in zip(range(0,10,2), range(10,30,2)):
    print(a,b)

# Min and max functions are used to find the smallest or largest item in a list
# min(list) and max(list)

# Create a fast list of numbers
fast_list = [x**2 for x in range(0,10)]
print(f'Fast list: {fast_list}') # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Convert Celsius to Fahrenheit
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(f'Celsius to Fahrenheit: {fahrenheit}') # [32.0, 50.6, 68.1, 100.9]


print(bcolors.ENDC) 

print(f'''{bcolors.OKBLUE}
----------Methods and Functions----------''')
# Methods are functions defined inside a class and used to modify the state of an object
# Functions are used to perform a task and return a value (or None)

def add_numbers(a, b):
    return a + b

print(f'Add numbers: {add_numbers(1, 2)}') # 3

# *Args is used to pass a variable number of arguments to a function
def multiply_numbers(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(f'Multiply numbers: {multiply_numbers(1, 2, 3, 4, 5)}') # 120

# **Kwargs is used to pass a variable number of keyword arguments to a function (keyword arguments are given after *args)
def func(**kwargs):
    if 'fruit' in kwargs:
        print(f'My favorite fruit is {kwargs["fruit"]}')
    else:
        print('I do not know my favorite fruit')

func(fruit='apple') 

def func2(a, b, c=0, *args, **kwargs):
    print(f'a = {a}, b = {b}, c = {c}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}') 

func2(1, 2, None, 4, 5, x=6, y=7)

# Lambda functions are used to create small anonymous functions
# Lambda functions can take any number of arguments but can only have one expression
# Lambda functions can be used as an argument to functions like map(), filter(), reduce() and list()
# Map function is used to apply a function to every item in a list and return a list of the results
# Filter function is used to filter out items from a list based on a condition

def square(x):
    return x**2

print(f'Map: {list(map(square, [1, 2, 3, 4, 5]))}') # [1, 4, 9, 16, 25]

print (f'Filter: {list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))}') # [2, 4]

print(f'{list(map(lambda x: x==1, [1, 2, 3, 4, 5]))}') # [True, False, False, False, False]


# Global and local variables are used to store data in a function
# Global variables are variables that are defined outside of a function
# Local variables are variables that are defined inside a function

print(f'''{bcolors.OKBLUE}
----------Classes----------''')
# Classes are used to create objects with custom attributes and methods (functions inside a class)
class Person:
    def __init__(self, name, age, alive):
        self.name = name
        self.age = age
        self.alive = alive

    def myfunc(self):
        return print(f'Hello my name is {self.name} and I am {self.age} years old')

john = Person('John', 36, True)
john.myfunc()

# Inheritance is used to create new classes from existing classes (child class inherits attributes and methods from parent class)
class Student(Person):
    def __init__(self, name, age, alive, grade):
        super().__init__(name, age, alive)
        self.grade = grade

    def myfunc(self):
        super().myfunc()
        print(f'I am in grade {self.grade}')

jessica = Student('Jessica', 25, True, 12)
jessica.myfunc()


# __init__ is a special method that is called when a new object is created from a class
# __init__ is used to assign values to object attributes
# __init__ is also used to perform other setup actions

# __main__ is a special name for the script that is run directly

# Try and except statements are used to catch exceptions and handle errors
# Finally statements are used to execute code, regardless of the result of an exception

try :
    print('Hello')
    print(1/0)
except ZeroDivisionError:
    print('Error')
finally:
    print('Finally')

