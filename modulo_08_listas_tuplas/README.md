# Módulo 08 — Listas y Tuplas

## Listas

Una lista es una colección **ordenada y mutable** de elementos.

```python
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True, 3.14]
vacia = []
```

### Acceder a elementos (indexado)

```python
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])    # manzana (primer elemento)
print(frutas[-1])   # naranja (último elemento)
print(frutas[1:3])  # ['banana', 'naranja']
```

### Modificar elementos

```python
frutas[1] = "mango"   # modifica el segundo elemento
print(frutas)         # ['manzana', 'mango', 'naranja']
```

## Métodos de listas

```python
lista = [3, 1, 4, 1, 5, 9]
```

| Método              | Descripción                         |
|---------------------|-------------------------------------|
| `.append(x)`        | Agrega x al final                   |
| `.insert(i, x)`     | Inserta x en la posición i          |
| `.extend([a, b])`   | Agrega varios elementos             |
| `.remove(x)`        | Elimina la primera aparición de x   |
| `.pop()`            | Elimina y devuelve el último        |
| `.pop(i)`           | Elimina y devuelve el de posición i |
| `.sort()`           | Ordena en su lugar (modifica)       |
| `.reverse()`        | Invierte en su lugar                |
| `.count(x)`         | Cuántas veces aparece x             |
| `.index(x)`         | Posición de x                       |
| `.clear()`          | Vacía la lista                      |
| `.copy()`           | Devuelve una copia                  |

## Funciones integradas con listas

```python
numeros = [5, 2, 8, 1, 9]
print(len(numeros))       # 5
print(min(numeros))       # 1
print(max(numeros))       # 9
print(sum(numeros))       # 25
print(sorted(numeros))    # [1, 2, 5, 8, 9] (nueva lista, no modifica)
print(list(reversed(numeros)))  # [9, 1, 8, 2, 5]
```

## List comprehension

Forma compacta de crear listas:

```python
# Sintaxis: [expresion for elemento in iterable if condicion]

cuadrados = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

pares = [x for x in range(1, 20) if x % 2 == 0]
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

mayusculas = [palabra.upper() for palabra in ["hola", "mundo"]]
# ['HOLA', 'MUNDO']
```

## Iterar listas

```python
colores = ["rojo", "verde", "azul"]

for color in colores:
    print(color)

for i, color in enumerate(colores):
    print(f"{i}: {color}")
```

## Tuplas

Una tupla es una colección **ordenada e inmutable** (no se puede modificar).

```python
punto = (3, 5)
coordenadas = (10.5, -3.2, 0.0)
persona = ("Ana", 25, "Bogotá")
solo_uno = (42,)    # coma necesaria para tupla de un elemento
```

### ¿Cuándo usar tupla vs lista?

| Lista `[]`                     | Tupla `()`                        |
|--------------------------------|-----------------------------------|
| Colección que cambia           | Colección fija (constante)        |
| Ej: carrito de compras         | Ej: coordenadas (x, y)            |
| Más lenta en acceso            | Más rápida en acceso              |
| No puede ser clave de dict     | Puede ser clave de diccionario    |

### Desempaquetado (unpacking)

```python
punto = (3, 5)
x, y = punto
print(x, y)   # 3 5

nombre, edad, ciudad = ("Ana", 25, "Bogotá")
```

### `zip()` — combinar listas en pares

```python
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad} años")
```
