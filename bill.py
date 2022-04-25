from os import system
system("cls")
print("")

suscriptores = [
    [1, 0, 0, 0, 0],
    [2, 0, 0, 0, 0],
    [3, 0, 0, 0, 0],
    [4, 0, 0, 0, 0],
    [5, 0, 0, 0, 0],
]

res = 's'
while res != "n":

    if res == 's':

        print("")
        suscriptor = int(input("INGRESE NÙMERO DE SUSCRIPTOR: "))
        lectura_actual = int(input("INGRESE LECTURA ACTUAL: "))
        lectura_anterior = 0
        estrato = int(input("INGRESE ESTRATO: "))

        if lectura_actual > 0 and estrato == 1 or estrato == 2 or estrato == 3 or estrato == 4 and suscriptor <=5 and suscriptor >= 1:

            # AÑADIENDO LECTURA ACTUAL
            suscriptores[suscriptor - 1][0] = suscriptor
            suscriptores[suscriptor - 1][4] = estrato

            # AÑADIENDO LECTURA ANTERIOR
            if suscriptores[suscriptor - 1][1] != 0:
                lectura_anterior = suscriptores[suscriptor - 1][2]
                suscriptores[suscriptor - 1][3] = lectura_anterior

            suscriptores[suscriptor - 1][2] = lectura_actual

            # AÑADIENDO VALOR A PAGAR
            if estrato == 1:
                suscriptores[suscriptor -1][1] = lectura_actual * 200
            elif estrato == 2:
                suscriptores[suscriptor -1][1] = lectura_actual * 500
            elif estrato == 3:
                suscriptores[suscriptor -1][1] = lectura_actual * 700
            else:
                suscriptores[suscriptor -1][1] = lectura_actual * 2000

            system("cls")
            print("")
            print("VALOR KW: ESTRATO 1 -> 200, 2 -> 500, 3 -> 700, 4 -> 2000")
            print('┌───────────')

            for suscriptor in range(len(suscriptores)):
                print(f"│ SUSCRIPTOR {suscriptores[suscriptor][0]}")
                print(f"│ LECTURA ACTUAL {suscriptores[suscriptor][2]}")
                print(f"│ LECTURA ANTERIOR {suscriptores[suscriptor][3]}")
                print(f"│ VALOR A PAGAR {suscriptores[suscriptor][1]}")
                print(f"│ ESTRATO {suscriptores[suscriptor][4]}")
                print("│")
            print('└──────────')
        else:
            system("cls")
            print('┌───────────')
            if lectura_actual < 0:
                print("│ ERROR: LA LECTURA ACTUAL DEBE SER MAYOR A CERO")

            if estrato != 1 or estrato != 2 or estrato != 3 or estrato != 4:
                print("│ ERROR: EL ESTRATO DEBE SER 1, 2, 3, 4")
            
            if suscriptor != 1 or suscriptor != 2 or suscriptor != 3 or suscriptor != 4 or suscriptor != 5:
                print("│ ERROR: EL SUSCRIPTOR DEBE SER 1, 2, 3, 4 o 5")
            
            print('└──────────')

        res = input("DESEA INGRESAR OTRO SUSCRIPTOR SÍ O NO (s/n): ")
        system("cls")
    else:
        system("cls")
        print('┌───────────')
        print("│ RESPUESTA INCORRECTA")
        print('└──────────')
        res = input("DESEA INGRESAR OTRO SUSCRIPTOR SÍ O NO (s/n): ")
