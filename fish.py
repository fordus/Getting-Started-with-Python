from os import system


class bcolors:
    ALERT = '\033[91m'
    ENDC = '\033[0m'


system("cls")
print("")

regiones = [
    [1, 'region_1', 0, 0, 0],
    [2, 'region_2', 0, 0, 0],
    [3, 'region_3', 0, 0, 0],
]

res = 's'
while res != "n":

    if res == 's':

        print("")
        region = int(input("INGRESE NÙMERO DE REGION (1, 2 ,3): "))
        cantidad_ano_anterior = int(
            input("INGRESE CANTIDAD ATRAPADA AÑO ANTERIOR: "))
        cantidad_ano_actual = int(
            input("INGRESE CANTIDAD ATRAPADA AÑO ACTUAL: "))
        indice = region - 1

        if region <= 3 and region >= 1 and cantidad_ano_actual > 0 and cantidad_ano_anterior > 0:

            regiones[indice][0] = region
            regiones[indice][2] = cantidad_ano_anterior
            regiones[indice][3] = cantidad_ano_actual

            porcentaje = ((cantidad_ano_actual/cantidad_ano_anterior)*100)-100
            porcentaje = round(porcentaje, 0)

            regiones[indice][4] = porcentaje

            system("cls")
            print("")
            print('┌───────────')

            for region in range(len(regiones)):
                print(f"│ REGION {regiones[region][0]}")
                print(
                    f"│ CANTIDAD ATRAPADA AÑO ANTERIOR {regiones[region][2]}")
                print(f"│ CANTIDAD ATRAPADA AÑO ACTUAL {regiones[region][3]}")
                print(f"│ ÍNDICE {regiones[region][4]}%")

                if regiones[region][4] >= 30 and regiones[region][2] != 0 and regiones[region][3] != 0:
                    print(
                    f"│ {bcolors.ALERT}ALERTA, EL AUMENTO ES IGUAL O MAYOR AL 30% EN {regiones[region][1]}{bcolors.ENDC}")
                if regiones[region][4] <= -30 and regiones[region][2] != 0 and regiones[region][3] != 0:
                    print(
                    f"│ {bcolors.ALERT}ALERTA, LA DISMINUCIÓN ES IGUAL O MENOR AL -30% EN {regiones[region][1]}{bcolors.ENDC}")
                print("│")

            print('└──────────')
        else:
            system("cls")
            print('┌───────────')
            if region > 3 or region < 1:
                print("│ ERROR: REGION INVÁLIDA")

            if cantidad_ano_anterior <= 0 or cantidad_ano_actual <= 0:
                print("│ ERROR: CANTIDAD ATRAPADA INVÁLIDA")

            print('└──────────')

        res = input("DESEA INGRESAR OTRA REGIÓN SÍ O NO (s/n): ")
        system("cls")
    else:
        system("cls")
        print('┌───────────')
        print("│ RESPUESTA INCORRECTA")
        print('└──────────')
        res = input("DESEA INGRESAR OTRA REGIÓN SÍ O NO (s/n): ")
else:
    print("TERMINADO")
