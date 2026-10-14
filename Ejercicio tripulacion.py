
# Archivo: ejercicio3_soporte_tripulacion.py

# Integrantes: Alonso Quesada
# Fecha: 14/10/2026
# Versión: 1.0
# Descripción: Verifica si la nave posee oxígeno y provisiones suficientes para la tripulación.


# --- ENTRADA DE DATOS ---
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))

provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# --- DECISIN CON CONDICIONAL DOBLE ---
# Se evalúan ambas condiciones de manera simultánea usando el operador lógico 'and'
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")