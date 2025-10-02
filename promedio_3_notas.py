# promedio.py
# Programa que suma 3 notas y calcula el promedio

# Pedir las 3 notas al usuario
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# Calcular la suma y el promedio
suma = nota1 + nota2 + nota3
promedio = suma / 3

# Mostrar los resultados
print("La suma de las notas es:", suma)
print("El promedio de las notas es:", promedio)