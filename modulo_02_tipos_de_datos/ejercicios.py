# MÓDULO 02 — Tipos de Datos
# Ejercicios guiados

# ── 1. Tipos básicos ────────────────────────────────────────
entero = 42
decimal = 3.14
texto = "Python"
booleano = True

print(entero, decimal, texto, booleano)

# ── 2. Verificar tipos con type() ───────────────────────────
print(type(entero))    # <class 'int'>
print(type(decimal))   # <class 'float'>
print(type(texto))     # <class 'str'>
print(type(booleano))  # <class 'bool'>

# ── 3. Enteros grandes con separador visual ─────────────────
poblacion = 50_000_000
distancia = 1_234_567
print(poblacion)
print(distancia)

# ── 4. Operaciones con int ──────────────────────────────────
print(10 + 3)    # suma       → 13
print(10 - 3)    # resta      → 7
print(10 * 3)    # producto   → 30
print(10 / 3)    # división   → 3.333...
print(10 // 3)   # div. entera→ 3
print(10 % 3)    # módulo     → 1
print(2 ** 10)   # potencia   → 1024

# ── 5. Floats y su precisión ────────────────────────────────
print(0.1 + 0.2)           # 0.30000000000000004 (normal)
print(round(0.1 + 0.2, 2)) # 0.3 (redondeado)

# ── 6. Strings con comillas simples y dobles ────────────────
a = "Hola"
b = 'Mundo'
c = """Esto es
un texto
multilínea"""
print(a)
print(b)
print(c)

# ── 7. Booleanos como resultado de comparaciones ────────────
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True
print(5 != 3)   # True

# ── 8. Conversión de tipos ──────────────────────────────────
numero_str = "100"
numero_int = int(numero_str)
print(numero_int + 50)          # 150 (ya es número)

precio_str = "29.99"
precio_float = float(precio_str)
print(precio_float * 2)         # 59.98

numero = 42
numero_como_texto = str(numero)
print("El número es: " + numero_como_texto)

# ── 9. bool() con distintos valores ─────────────────────────
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("hola")) # True
print(bool(None))   # False

# ── 10. None — ausencia de valor ────────────────────────────
resultado = None
print(resultado)
print(type(resultado))   # <class 'NoneType'>
