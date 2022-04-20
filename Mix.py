
print('1. Read the side of a square and print the area')
input_str = input("Enter the side of a square: ")
side = int(input_str)
area = side * side
print("The area of the square is: ", area)

print('2. Read the base and height of a triangle and print the area')
input_str = input("Enter the base and height of a triangle together (a b): ")
base, height = input_str.split()
base = int(base)
height = int(height)
area = base * height / 2
print("The area of the triangle is: ", area)


print('3. Read the values of the sides of a rectangle and print the area')
input_str = input("Enter the values of the sides of a rectangle (a b): ")
side1, side2 = input_str.split()
side1 = int(side1)
side2 = int(side2)
area = side1 * side2
print("The area of the rectangle is: ", area)

print('4. Read the data needed to calculate the data of a trapezoid')
input_str = input("Enter the values of the sides of a trapezoid (b B h): ")
base1, base2, height = input_str.split()
base1 = int(base1)
base2 = int(base2)
height = int(height)
area = (base1 + base2) * height / 2
print("The area of the trapezoid is: ", area)

print('5. Read the data needed to calculate the area of a cube')
input_str = input("Enter the side of a cube: ")
side = int(input_str)
area = side * side * 6
print('The area of the cube is: ', area)


# The While loops are used to repeat the same code until a condition is met

# The cicle is used to repeat the same code until a condition is met

# The for loops are used to repeat the same code for a specific number of times

# The diference between the while and the for loops is that the while loop
# executes the code inside the while loop until the condition is met
# The for loop executes the code inside the for loop for a specific number of times


# WHILE LOOPS

print('1. Show the number from 10 to 20 using a while loop')
i = 10
while i <= 20:
    print(i)
    i += 1

print('2. Show the number from 20 to 10 using a while loop')
i = 20
while i >= 10:
    print(i)
    i -= 1

print('3. show the table of 5 using a while loop')
i = 1
while i <= 10:
    print(5 * i)
    i += 1

print('4. show the multiplication tables from the table of 1 to 10 using a while loop')
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j)
        j += 1
    i += 1

print('5. show the first 20 odd numbers using a while loop')
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

# FOR LOOPS

print('1. Show the number from 10 to 20 using a for loop')
for i in range(10, 21):
    print(i)

print('2. Show the number from 20 to 10 using a for loop')
for i in range(20, 9, -1):
    print(i)

print('3. show the table of 5 using a for loop')
for i in range(1, 11):
    print(5 * i)

print('4. show the multiplication tables from the table of 1 to 10 using a for loop')
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j)

print('5. show the first 20 odd numbers using a for loop')
for i in range(1, 21, 2):
    print(i)

print('6. show the first 20 even numbers using a for loop')
for i in range(2, 22, 2):
    print(i)
