# Using the | operator, we can merge two dictionaries together.

d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}
merged_dict = d1 | d2
print(merged_dict)


# Using enumerate() to iterate over a list and return the index and value of each item in the list.
data = [1,2,3,4]

for idx, num in enumerate(data):
    print(idx, num)

# Using List Comprehension to create a list of tuples.

squares = []

for i in range(1,11):
    squares.append(i*i)

squares = [i*i for i in range(10)]
print(squares)


# Sort complex iterables with sorted()

data = (1,2,3,4,5,6,7,8,9,10)
sorted_data = sorted(data, reverse=True)

print(sorted_data)

data = [
{"name": "Alex", "age": 25}, 
{"name": "John", "age": 30}, 
{"name": "Steve", "age": 26}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

# Save memory with generators

import sys

my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")

# Define default values in Dictionaries with .get() and .setdefault()

my_dict = {"name": "Alex", "age": 25}
count = my_dict.get("count", 0)
print(count)


count = my_dict.setdefault("count", 0)
print(count)
print(my_dict)

# Concat string with .join()

list_of_strings = ["Hello", "my", "name", "is", "Alex"]
my_string = " ".join(list_of_strings)
print(my_string)

# Simplify if statements for multiple checks

colors = ["red", "green", "blue"]

c = "green"
if c in colors:
    print("Found")



condition = False
x = 1 if condition else 2
print(x)

num1 = 10_000_000
num2 = 10_000_000_000

total = num1 + num2
print(f'{total:,}')


names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heores = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for name, hero in zip(names, heores):
    print(f'{name} is actually {hero}')


a, b, *c = [1, 2, 3, 4, 5]
print(a, b, c)

a, b, *_, d = [1, 2, 3, 4, 5]
print(a, b, d)