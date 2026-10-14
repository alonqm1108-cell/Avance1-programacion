# Archivo: ejercicio4_autorizacion.py
# Integrantes: Alonso Quesada
# Fecha: 14/10/2026
# Versión: 1.0
# Descripción: Determina la autorización final del lanzamiento evaluando todos los recursos requeridos.


# --- CONSTANTE ---
RESERVA_COMBUSTIBLE = 10

# --- ENTRADA DE DATOS ---
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))

oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))

energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))

provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# --- PROCESAMIENTO ---
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# --- DECISIÓN CONn CONDICIONAL DOBLE COMPUESTA ---
# Evaluación simultánea de los cuatro recursos usando el operador lógico 'and'
if (combustible_disponible >= combustible_total and 
    oxigeno_disponible >= oxigeno_requerido and 
    energia_disponible >= energia_requerida and 
    provisiones_disponibles >= provisiones_requeridas):
    
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
