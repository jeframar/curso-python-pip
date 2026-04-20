# MÓDULO 03 — Operadores y Expresiones
# Ejercicios guiados

# ── 1. Aritméticos ──────────────────────────────────────────
a = 17
b = 5

print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4
print(a // b)   # 3  (cociente entero)
print(a % b)    # 2  (resto)
print(a ** b)   # 1419857

# ── 2. División siempre da float ────────────────────────────
print(10 / 2)       # 5.0 (no 5)
print(type(10 / 2)) # <class 'float'>

# ── 3. Módulo — usos prácticos ──────────────────────────────
numero = 27
print(numero % 2 == 0)   # False → no es par
print(numero % 3 == 0)   # True  → es divisible por 3

# ── 4. Operadores de comparación ────────────────────────────
print(10 == 10)   # True
print(10 != 5)    # True
print(10 > 5)     # True
print(10 < 5)     # False
print(10 >= 10)   # True
print(10 <= 9)    # False

# ── 5. Comparaciones con variables ──────────────────────────
edad = 20
print(edad >= 18)         # True → es mayor de edad
print(edad >= 18 and edad <= 65)  # True → en rango laboral

# ── 6. Operadores lógicos ────────────────────────────────────
tiene_dni = True
es_mayor = True
print(tiene_dni and es_mayor)    # True
print(tiene_dni and not es_mayor) # False

llueve = False
hace_frio = True
print(llueve or hace_frio)       # True → al menos uno

# ── 7. Operadores de asignación ─────────────────────────────
puntaje = 100
puntaje += 50
print(puntaje)   # 150

puntaje -= 30
print(puntaje)   # 120

puntaje *= 2
print(puntaje)   # 240

puntaje //= 10
print(puntaje)   # 24

# ── 8. Precedencia ──────────────────────────────────────────
print(2 + 3 * 4)      # 14 (multiplica antes)
print((2 + 3) * 4)    # 20 (paréntesis primero)
print(2 ** 3 + 1)     # 9  (potencia antes de suma)
print(2 ** (3 + 1))   # 16 (paréntesis primero)

# ── 9. Operador in ──────────────────────────────────────────
vocales = "aeiou"
print("a" in vocales)    # True
print("b" in vocales)    # False
print("e" not in vocales) # False

# ── 10. Expresiones complejas ────────────────────────────────
base = 10
altura = 5
area_triangulo = (base * altura) / 2
print("Área:", area_triangulo)

celsius = 100
fahrenheit = celsius * 9 / 5 + 32
print("100°C en Fahrenheit:", fahrenheit)
