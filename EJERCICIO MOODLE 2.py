import numpy as np

estudiantesCod = np.arange(200000, 206500)
nombresEst = []

for i in range(6500):
    nombresEst.append("Estudiante_" + str(i))

nombreEst= np.array(nombresEst)
#Condicional menor a 2.0
promedios = np.round(np.random.uniform(2.0, 5.0, 6500), 2)
#Codigos de 1 a 100
carreras = np.random.randint(1, 101, 6500)

añosIngreso = np.random.randint(1960, 2025, 6500)

estadoCondicional = promedios < 2.0  
codigoCarrera = int(input("Digite el código de la carrera a dar: "))

filtroCarrera = []

for i in range(len(carreras)):  
    if carreras[i] == codigoCarrera and promedios[i] >= 4.0:  
        filtroCarrera.append(True)  
    else:
        filtroCarrera.append(False)  


filtroCarrera = np.array(filtroCarrera)

estudiantesCarrera = np.column_stack((estudiantesCod[filtroCarrera], nombreEst[filtroCarrera]))
                                     

print("\nEstudiantes con promedio >= 4.0 en la carrera", codigoCarrera)
print("Código    Nombre")
print("-----------------")
for codigo, nombre in estudiantesCarrera:
    print(f"{int(codigo)} - {nombre}")

print("\nTotal de estudiantes encontrados:", len(estudiantesCarrera))


filtroCondicional = (añosIngreso < 1990) & estadoCondicional
estudiantesCondicionales = np.column_stack((estudiantesCod[filtroCondicional], nombreEst[filtroCondicional]))

print("\nEstudiantes que ingresaron antes de 1990 y están condicionales")
print("Código    Nombre")
print("-----------------")
for codigo, nombre in estudiantesCondicionales:
    print(f"{int(codigo)} - {nombre}")

print("\nTotal de estudiantes encontrados:", len(estudiantesCondicionales))

