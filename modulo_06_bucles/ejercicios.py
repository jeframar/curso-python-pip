# MÓDULO 06 — Bucles
# Ejercicios guiados

# ── 1. while básico ─────────────────────────────────────────
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# ── 2. for con lista ────────────────────────────────────────
planetas = ["Mercurio", "Venus", "Tierra", "Marte"]
for planeta in planetas:
    print(planeta)

# ── 3. for con string ────────────────────────────────────────
for letra in "Python":
    print(letra, end=" ")
print()   # salto de línea al final

# ── 4. range() — variantes ──────────────────────────────────
print("Del 0 al 4:")
for i in range(5):
    print(i, end=" ")
print()

print("Del 1 al 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

print("Pares del 0 al 20:")
for i in range(0, 21, 2):
    print(i, end=" ")
print()

print("Cuenta regresiva:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("¡Despegue!")

# ── 5. break ────────────────────────────────────────────────
print("\nBuscar el primer múltiplo de 7:")
for n in range(1, 100):
    if n % 7 == 0:
        print(f"Primer múltiplo de 7: {n}")
        break

# ── 6. continue ─────────────────────────────────────────────
print("\nNúmeros del 1 al 10, saltando los divisibles por 3:")
for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n, end=" ")
print()

# ── 7. while con break ──────────────────────────────────────
# (simulado para no requerir input real)
respuestas = ["s", "s", "n"]   # simula respuestas del usuario
idx = 0
while True:
    respuesta = respuestas[idx]
    idx += 1
    print(f"Respuesta: {respuesta}")
    if respuesta == "n":
        print("Saliendo del bucle")
        break

# ── 8. enumerate() ──────────────────────────────────────────
lenguajes = ["Python", "JavaScript", "Rust", "Go"]
for i, lang in enumerate(lenguajes, start=1):
    print(f"{i}. {lang}")

# ── 9. Acumulador ────────────────────────────────────────────
suma = 0
for i in range(1, 101):
    suma += i
print(f"\nSuma del 1 al 100: {suma}")

# ── 10. Bucles anidados — tabla de multiplicar ──────────────
print("\nTabla de multiplicar (1-5):")
for fila in range(1, 6):
    for col in range(1, 6):
        print(f"{fila * col:3}", end="")
    print()

# ── 11. for / else ──────────────────────────────────────────
lista = [1, 3, 5, 7, 9]
objetivo = 4
for n in lista:
    if n == objetivo:
        print(f"Encontré {objetivo}")
        break
else:
    print(f"{objetivo} no está en la lista")

# ── 12. Contar vocales en una frase ─────────────────────────
frase = "el cielo es azul"
vocales = "aeiouáéíóú"
conteo = 0
for letra in frase:
    if letra in vocales:
        conteo += 1
print(f"\nVocales en '{frase}': {conteo}")
