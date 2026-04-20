# Módulo 07 — Funciones

## ¿Qué es una función?

Una función es un bloque de código reutilizable que realiza una tarea específica. Evita repetir código y hace el programa más organizado.

```python
def saludar():
    print("¡Hola!")

saludar()   # llamar la función
saludar()   # se puede llamar cuantas veces quieras
```

## Parámetros y argumentos

Los **parámetros** son variables que la función recibe:

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")    # "Ana" es el argumento
saludar("Luis")
```

### Múltiples parámetros

```python
def sumar(a, b):
    print(a + b)

sumar(3, 5)   # 8
```

## `return` — devolver un valor

Sin `return`, una función devuelve `None`. Con `return`, entrega un resultado:

```python
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)   # 15

# Se puede usar directamente en expresiones:
print(sumar(3, 7) * 2)   # 20
```

## Parámetros con valor por defecto

Si el argumento no se pasa, se usa el valor predeterminado:

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")            # "Hola, Ana!"
saludar("Ana", "Buenos días")  # "Buenos días, Ana!"
```

Los parámetros con default siempre van al final.

## Argumentos por nombre (keyword arguments)

```python
def ficha(nombre, edad, ciudad):
    print(f"{nombre}, {edad} años, {ciudad}")

ficha(edad=25, ciudad="Bogotá", nombre="Ana")   # el orden no importa
```

## Scope — ámbito de las variables

Las variables creadas dentro de una función son **locales** (no existen fuera):

```python
def mi_funcion():
    x = 10      # variable local
    print(x)

mi_funcion()
# print(x)    # ERROR: x no existe aquí
```

Las variables fuera de la función son **globales** y la función puede leerlas:

```python
pi = 3.14159   # global

def area_circulo(radio):
    return pi * radio ** 2

print(area_circulo(5))
```

## Funciones que retornan múltiples valores

```python
def minmax(lista):
    return min(lista), max(lista)

minimo, maximo = minmax([3, 1, 7, 2, 9])
print(minimo, maximo)   # 1 9
```

## Funciones integradas (built-ins)

Python incluye funciones listas para usar:

| Función       | Descripción                      |
|---------------|----------------------------------|
| `print()`     | Imprimir                         |
| `input()`     | Leer teclado                     |
| `len()`       | Longitud de una secuencia        |
| `type()`      | Tipo de un objeto                |
| `int()`       | Convertir a entero               |
| `float()`     | Convertir a decimal              |
| `str()`       | Convertir a texto                |
| `abs()`       | Valor absoluto                   |
| `round()`     | Redondear                        |
| `min()`       | Mínimo de una secuencia          |
| `max()`       | Máximo de una secuencia          |
| `sum()`       | Suma de una secuencia            |
| `sorted()`    | Ordenar y devolver nueva lista   |
| `range()`     | Generar secuencia de números     |

## Funciones lambda (anónimas)

Funciones de una sola expresión:

```python
cuadrado = lambda x: x ** 2
print(cuadrado(5))   # 25

# Equivale a:
def cuadrado(x):
    return x ** 2
```

Útiles para operaciones simples pasadas como argumento.
