# MÓDULO 04 — Strings y Entrada del Usuario
# Ejercicios guiados

# ── 1. f-strings básicos ────────────────────────────────────
nombre = "Carlos"
edad = 30
ciudad = "Bogotá"
print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

# ── 2. Expresiones dentro de f-strings ─────────────────────
precio = 80_000
iva = 0.19
print(f"Precio sin IVA: {precio:,}")
print(f"Precio con IVA: {precio * (1 + iva):,.2f}")

# ── 3. Métodos de texto ─────────────────────────────────────
frase = "  El aprendizaje nunca se detiene  "
print(frase.strip())             # sin espacios extremos
print(frase.strip().upper())     # en mayúsculas
print(frase.strip().lower())     # en minúsculas
print(frase.strip().title())     # Cada Palabra En Mayúscula

# ── 4. replace() y count() ──────────────────────────────────
email = "usuario@dominio.com"
print(email.replace("@", " [at] "))
print(email.count("."))          # 1

# ── 5. split() — dividir en partes ──────────────────────────
csv = "Ana,30,Bogotá,Python"
partes = csv.split(",")
print(partes)
print(partes[0])   # Ana
print(partes[3])   # Python

# ── 6. Indexado ─────────────────────────────────────────────
lenguaje = "Python"
print(lenguaje[0])    # P
print(lenguaje[-1])   # n
print(lenguaje[1:4])  # yth

# ── 7. Slicing avanzado ──────────────────────────────────────
texto = "abcdefghij"
print(texto[::2])    # acegi (cada 2)
print(texto[::-1])   # jihgfedcba (invertido)
print(texto[2:8:2])  # ceg

# ── 8. len() ────────────────────────────────────────────────
palabra = "extraordinario"
print(len(palabra))
print(f"La palabra '{palabra}' tiene {len(palabra)} letras.")

# ── 9. find() y startswith() / endswith() ───────────────────
url = "https://www.python.org"
print(url.startswith("https"))   # True
print(url.endswith(".org"))       # True
print(url.find("python"))         # posición donde empieza

# ── 10. Concatenación y repetición ──────────────────────────
separador = "=" * 40
print(separador)
print("=" * 15 + " RESULTADO " + "=" * 15)
saludo = "Hola" + ", " + nombre + "!"
print(saludo)

# ── 11. Caracteres especiales ────────────────────────────────
print("Línea 1\nLínea 2\nLínea 3")
print("Columna1\tColumna2\tColumna3")
print("Ella dijo: \"Python es genial\"")

# ── 12. input() — descomenta para usar interactivamente ──────
# nombre_usuario = input("¿Cuál es tu nombre? ")
# anio_nacimiento = int(input("¿En qué año naciste? "))
# edad_aprox = 2024 - anio_nacimiento
# print(f"Hola {nombre_usuario}, tienes aproximadamente {edad_aprox} años.")
