# ===============
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Alonso Quesada
# Fecha: 14/10/2026
# Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión espacial.
# ===============

# --- CONSTANTES ---
CONSUMO_COMBUSTIBLE_DIARIO = 8
RESERVA_COMBUSTIBLE = 10

CONSUMO_OXIGENO_DIARIO = 2
RESERVA_OXIGENO = 5

CONSUMO_ENERGIA_DIARIO = 5
ENERGIA_EXPLORACION = 10

CONSUMO_PROVISIONES_DIARIO = 1
RESERVA_PROVISIONES = 3

VIAJE_IDA_Y_VUELTA = 2

# --- ENTRADA DE DATOS ---
nombre_mision = input("Ingrese el nombre de la misión: ")
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la cantidad de días estimados hasta el destino: "))

# --- PROCESAMIENTO Y CÁLCULOS ---
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

oxigeno_requerido = (dias_viaje * CONSUMO_OXIGENO_DIARIO * VIAJE_IDA_Y_VUELTA * cantidad_tripulantes) + RESERVA_OXIGENO
energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIARIO * VIAJE_IDA_Y_VUELTA) + ENERGIA_EXPLORACION
provisiones_requeridas = (dias_viaje * cantidad_tripulantes * VIAJE_IDA_Y_VUELTA * CONSUMO_PROVISIONES_DIARIO) + RESERVA_PROVISIONES

# --- RESULTADOS ---
print("\n--- RESUMEN DE LA MISIÓN ---")
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")