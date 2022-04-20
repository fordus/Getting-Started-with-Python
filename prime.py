# from distutils.command.build_scripts import first_line_re
from os import system
system("cls")

# Show the greatest element in list

list = [1,-2,4,6,8,9,1,7,11,12,13,15]

# greater_number = 0
# number = 0

# for num in list:
#     if num > greater_number:
#         greater_number = num

# print('The greatest number is: ', greater_number)


# Show the first prime number in the list

first_prime_number = 0
print('''
*-------* LISTA *-------* 
''')
print(list)
print('''
*-------* OBTENER EL PRIMER NUMERO PRIMO DE LA LISTA *-------* 
''')

for num in list:

    if num <= 1:
        first_prime_number = 0
        print(num, ' AQUI ES MENOR O IGUAL A 1')
    elif num == 2:
        print('┌───────')
        print(f'│ {num} AQUI ES IGUAL A DOS')
        first_prime_number = num
        break
    elif num % 2 == 0:
        first_prime_number = 0
        print(num, ' AQUI ES PAR MAYOR A DOS')
    else:
        print('┌───────')
        print(f'│ {num} AQUI SE DIVIDE {num} DESDE 2 HASTA {num-1}')
        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                print(f'│ {num} -> SE PUEDE DIVIDIR POR {i}: NO ES PRIMO')
                break
            else:
                is_prime = True
                print(f'│ {num} -> NO SE PUEDE DIVIDIR POR {i}')

        if is_prime:
            first_prime_number = num
            print(f'│ {num}  ENTONCES ES PRIMO')
            break

        print('└───────')

print('└───────')
if first_prime_number == 0:
    print('NO HAY PRIMO')
else:   
    print('PRIMER NÚMERO PRIMO:', first_prime_number)
