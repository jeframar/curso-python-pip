# MÓDULO 08 — Listas y Tuplas
# Ejercicios guiados

# ── 1. Crear y acceder ───────────────────────────────────────
frutas = ["manzana", "banana", "naranja", "uva", "mango"]
print(frutas[0])     # manzana
print(frutas[-1])    # mango
print(frutas[1:4])   # ['banana', 'naranja', 'uva']

# ── 2. Modificar ─────────────────────────────────────────────
numeros = [10, 20, 30, 40, 50]
numeros[2] = 99
print(numeros)   # [10, 20, 99, 40, 50]

# ── 3. append, insert, extend ───────────────────────────────
colores = ["rojo", "verde"]
colores.append("azul")
print(colores)   # ['rojo', 'verde', 'azul']

colores.insert(1, "amarillo")
print(colores)   # ['rojo', 'amarillo', 'verde', 'azul']

colores.extend(["morado", "naranja"])
print(colores)

# ── 4. remove, pop ──────────────────────────────────────────
lista = [1, 2, 3, 4, 5]
lista.remove(3)       # elimina el valor 3
print(lista)          # [1, 2, 4, 5]

ultimo = lista.pop()  # elimina y devuelve el último
print(ultimo)         # 5
print(lista)          # [1, 2, 4]

segundo = lista.pop(0)  # elimina el primero
print(segundo)          # 1

# ── 5. sort y sorted ────────────────────────────────────────
notas = [85, 42, 97, 73, 61]
ordenadas = sorted(notas)         # nueva lista, no modifica
print(ordenadas)
print(notas)                      # original intacta

notas.sort()                      # modifica en su lugar
print(notas)

notas.sort(reverse=True)          # descendente
print(notas)

# ── 6. Funciones integradas ──────────────────────────────────
ventas = [1500, 3200, 800, 4100, 2700]
print(f"Total:    {sum(ventas):,}")
print(f"Promedio: {sum(ventas)/len(ventas):,.2f}")
print(f"Mínima:   {min(ventas):,}")
print(f"Máxima:   {max(ventas):,}")

# ── 7. List comprehension ────────────────────────────────────
cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)

pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)

nombres = ["  Ana  ", "  Luis  ", " María "]
limpios = [n.strip().title() for n in nombres]
print(limpios)

# ── 8. Iterar con enumerate ──────────────────────────────────
lenguajes = ["Python", "JavaScript", "Rust", "Go"]
for posicion, lang in enumerate(lenguajes, start=1):
    print(f"{posicion}. {lang}")

# ── 9. Listas anidadas (matriz) ──────────────────────────────
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])   # 6 (fila 1, columna 2)

for fila in matriz:
    print(fila)

# ── 10. Tuplas ───────────────────────────────────────────────
punto = (3.0, 4.0)
print(punto[0], punto[1])

# Desempaquetado
x, y = punto
print(f"x={x}, y={y}")

distancia_al_origen = (x**2 + y**2) ** 0.5
print(f"Distancia al origen: {distancia_al_origen}")

# ── 11. Tuplas con múltiples valores ─────────────────────────
persona = ("Ana García", 28, "Bogotá", "Python")
nombre, edad, ciudad, lenguaje = persona
print(f"{nombre} tiene {edad} años, vive en {ciudad} y programa en {lenguaje}.")

# ── 12. zip() ────────────────────────────────────────────────
productos = ["Laptop", "Mouse", "Teclado"]
precios = [2_500_000, 80_000, 150_000]
cantidades = [1, 2, 1]

print("\n--- Carrito de compras ---")
total_general = 0
for producto, precio, cantidad in zip(productos, precios, cantidades):
    subtotal = precio * cantidad
    total_general += subtotal
    print(f"{producto:10} x{cantidad} = ${subtotal:>12,}")
print(f"{'TOTAL':>20} = ${total_general:>12,}")
