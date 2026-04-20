# Módulo 06 — Bucles

Los bucles permiten ejecutar un bloque de código varias veces.

## Bucle `while`

Se ejecuta **mientras** una condición sea verdadera.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Cuidado:** si la condición nunca se vuelve False, el bucle es infinito.

```python
# Bucle infinito (no hagas esto sin un break):
while True:
    respuesta = input("¿Continuar? (s/n): ")
    if respuesta == "n":
        break
```

## Bucle `for`

Itera sobre una secuencia (lista, string, range, etc.):

```python
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)
```

```python
for letra in "Python":
    print(letra)
```

## La función `range()`

Genera una secuencia de números:

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 8)       # 2, 3, 4, 5, 6, 7
range(0, 10, 2)   # 0, 2, 4, 6, 8  (paso de 2)
range(10, 0, -1)  # 10, 9, 8, ..., 1 (cuenta regresiva)
```

```python
for i in range(5):
    print(i)
```

## `break` — salir del bucle

Termina el bucle inmediatamente:

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)   # imprime 0, 1, 2, 3, 4
```

## `continue` — saltar iteración

Salta al inicio de la siguiente iteración:

```python
for numero in range(10):
    if numero % 2 == 0:
        continue        # salta los pares
    print(numero)       # imprime 1, 3, 5, 7, 9
```

## `else` en bucles

El bloque `else` se ejecuta cuando el bucle termina normalmente (sin `break`):

```python
for i in range(5):
    print(i)
else:
    print("Bucle terminado normalmente")
```

```python
numeros = [1, 3, 5, 7]
for n in numeros:
    if n % 2 == 0:
        print("Encontré un par")
        break
else:
    print("No hay números pares")
```

## `enumerate()` — índice y valor

Cuando necesitas el índice mientras iteras:

```python
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"{indice}: {color}")
```

## Bucles anidados

Un bucle dentro de otro:

```python
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"({fila},{columna})", end=" ")
    print()   # nueva línea al final de cada fila
```

## Patrones comunes

```python
# Acumulador
total = 0
for i in range(1, 11):
    total += i
print(total)   # 55

# Buscar en una lista
objetivo = 7
encontrado = False
for n in [3, 1, 7, 2, 9]:
    if n == objetivo:
        encontrado = True
        break

# Contar ocurrencias
frase = "programacion en python es genial"
conteo = 0
for palabra in frase.split():
    if "on" in palabra:
        conteo += 1
print(conteo)
```
