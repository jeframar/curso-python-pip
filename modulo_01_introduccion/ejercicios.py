# MÓDULO 01 — Introducción a Python
# Ejercicios guiados — lee y ejecuta línea por línea

# ── 1. Hola mundo ──────────────────────────────────────────
print("Hola, mundo!")

# ── 2. Comentarios ─────────────────────────────────────────
# Esta línea no hace nada, es solo una nota para el programador
print("Los comentarios no se ejecutan")

# ── 3. Variables con texto ──────────────────────────────────
nombre = "Ana"
print(nombre)

# ── 4. Variables con números ────────────────────────────────
edad = 25
altura = 1.68
print(edad)
print(altura)

# ── 5. Imprimir varias cosas juntas ─────────────────────────
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)

# ── 6. Reasignar una variable ───────────────────────────────
ciudad = "Bogotá"
print(ciudad)
ciudad = "Medellín"     # la variable cambia de valor
print(ciudad)

# ── 7. Múltiples variables en una línea ─────────────────────
x = 10
y = 20
z = 30
print(x, y, z)

# ── 8. Nombres válidos e inválidos ──────────────────────────
mi_variable = "válido"
_privado = "también válido"
dato2 = "válido con número al final"
print(mi_variable, _privado, dato2)

# ── 9. Python distingue mayúsculas ──────────────────────────
Nombre = "Carlos"
nombre = "Ana"
print(Nombre)   # Carlos
print(nombre)   # Ana  (son variables distintas)

# ── 10. print() con separador personalizado ─────────────────
print("Python", "es", "genial", sep="-")
print("Línea 1", end=" | ")
print("Línea 2")
