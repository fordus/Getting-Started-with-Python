from os import system
system("cls")
# Programa que calcule promedio de estudiantes, promedio del curso, cuántos aprobaron
# y cuántos reprobaron
res = 's'
promedio_estudiantes = []
total_estudiantes = 0
notas_correctas = False
suma_promedios = 0
total_promedio_estudiantes = 0
id_estudiantes = []

while res != "n":
    
    if res == 's':
        
        # DATOS DE ENTRADA
        print('┌───────────')
        print('│INGRESE LOS DATOS DEL ESTUDIANTE')
        id_estudiante = input("│ ID DE ESTUDIANTE: ")
        nota_primer_examen = float(input(f"│ NOTA PRIMER EXAMEN ESTUDIANTE CON ID {id_estudiante}: "))
        nota_segundo_examen = float(input(f"│ NOTA SEGUNDO EXAMEN ESTUDIANTE CON ID {id_estudiante}: "))
        nota_tercer_examen = float(input(f"│ NOTA TERCER EXAMEN ESTUDIANTE CON ID {id_estudiante}: "))
        
        # COMPROBAR QUE LAS NOTAS SON MAYORES O IGUALES A 0 Y MENORES O IGUALES A 5
        if nota_primer_examen < 0 or nota_primer_examen > 5:
            notas_correctas = False
        elif nota_segundo_examen < 0 or nota_segundo_examen > 5:
            notas_correctas = False
        elif nota_tercer_examen < 0 or nota_tercer_examen > 5:
            notas_correctas = False
        else:
            notas_correctas = True
        
        # SI LOS VALORES INTRODUCCIDOS SON CORRECTOS
        if notas_correctas:

            id_estudiantes.append(id_estudiante)

            #CALCULAR SI APROBO O REPROBO
            # 30% DE 5 ES 1,5
            # 40% DE 5 ES 2,0
            nota_primer_examen = nota_primer_examen * 1.5 # PRIMERA NOTA VALE EL 30%
            nota_segundo_examen = nota_segundo_examen * 1.5 # SEGUNDA NOTA VALE EL 30%
            nota_tercer_examen = nota_tercer_examen * 2.0 # TERCERA NOTA VALE EL 40%
            
            # SE CALCULA EL PROMEDIO DIVIDIENDO LAS NOTAS POR 5
            promedio = round(((nota_primer_examen + nota_segundo_examen + nota_tercer_examen)/5), 1)
            promedio_estudiantes.append((promedio))
        
        else:
            system("cls")
            print('┌───────────')
            print('│ ERROR EN LOS VALORES INTRODUCIDOS, DEBEN SER NOTAS DEL 0 - 5.') 
        print('└──────────')    
        res = input("DESEA INGRESAR OTRO ESTUDIANTE SÍ O NO (s/n): ")
        system("cls")
    else:
        system("cls")
        print('┌───────────')
        print("│ RESPUESTA INCORRECTA")
        print('└──────────')  
        res = input("DESEA INGRESAR OTRO ESTUDIANTE SÍ O NO (s/n): ")
else:
    print('RESULTADOS')


total_estudiantes = len(promedio_estudiantes)
# PROMEDIO DE CADA ESTUDIANTE
print('┌───────────')
print('│ PROMEDIO DE CADA ESTUDIANTE')
print(f'│ ID \t NOTA')
for i in range(total_estudiantes):
    print(f'│ {id_estudiantes[i]} \t {promedio_estudiantes[i]}') 

print('├─────────')
            
# PROMEDIO DEL CURSO   
print('│ PROMEDIO DEL CURSO')
for promedio in promedio_estudiantes:
    suma_promedios = suma_promedios + promedio


total_promedio_estudiantes = (suma_promedios/total_estudiantes)
print('│ ',round(total_promedio_estudiantes,1))

# CUANTOS REPROBARON
cuantos_reprobaron = 0
for promedio in promedio_estudiantes:
    if promedio < 3.0:
        cuantos_reprobaron = cuantos_reprobaron + 1
print('├─────────')
print('│ CUANTOS REPROBARON')
print('│ ',cuantos_reprobaron)
print('├─────────')

# CUANTOS APROBARON
cuantos_aprobaron = 0
for promedio in promedio_estudiantes:
    if promedio >= 3.0:
        cuantos_aprobaron = cuantos_aprobaron + 1
print('│ CUANTOS APROBARON')
print('│ ',cuantos_aprobaron)
print('└──────────')
