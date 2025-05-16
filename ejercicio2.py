# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
notas = []
cantidad = int(input("¿Cuántas notas vas a agregar?: "))

for i in range(cantidad):
    nota = float(input(f"Nota {i+1}: "))
    while nota < 1.0 or nota > 7.0:
        nota = float(input(f"Nota {i+1} (entre 1.0 y 7.0): "))
    notas.append(nota)

promedio = float(f"{sum(notas) / cantidad:.2f}")
print(f"Promedio: {promedio}")

if promedio >= 4.0:
    print("Aprobaste")
else:
    print("No aprobaste.")
