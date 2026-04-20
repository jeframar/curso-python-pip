# Módulo 02 — Tipos de Datos

## Tipos básicos en Python

Python tiene varios tipos de datos incorporados. Los más fundamentales son:

| Tipo    | Nombre   | Ejemplo            |
|---------|----------|--------------------|
| Entero  | `int`    | `42`, `-10`, `0`   |
| Decimal | `float`  | `3.14`, `-0.5`     |
| Texto   | `str`    | `"hola"`, `'mundo'`|
| Booleano| `bool`   | `True`, `False`    |

## int — Números enteros

```python
edad = 30
temperatura = -5
cantidad = 1_000_000   # guión bajo como separador visual
```

Operaciones:
```python
print(10 + 3)   # 13
print(10 // 3)  # 3   (división entera)
print(10 % 3)   # 1   (módulo / resto)
print(2 ** 8)   # 256 (potencia)
```

## float — Números decimales

```python
precio = 19.99
pi = 3.14159
```

Cuidado con la precisión:
```python
print(0.1 + 0.2)   # 0.30000000000000004 (normal en todos los lenguajes)
```

## str — Cadenas de texto

```python
nombre = "Python"
saludo = 'Hola'
multilinea = """Esto
ocupa varias
líneas"""
```

Las comillas simples y dobles son equivalentes. Usa triples para texto multilínea.

## bool — Booleanos

Solo dos valores posibles: `True` o `False` (con mayúscula inicial).

```python
activo = True
completado = False
```

Los booleanos son el resultado de comparaciones:
```python
print(5 > 3)    # True
print(5 == 3)   # False
```

## La función `type()`

Devuelve el tipo de cualquier valor:

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hola"))   # <class 'str'>
print(type(True))     # <class 'bool'>
```

## Conversión de tipos (casting)

Puedes convertir entre tipos con funciones:

| Función  | Convierte a | Ejemplo                       |
|----------|-------------|-------------------------------|
| `int()`  | entero      | `int("42")` → `42`            |
| `float()`| decimal     | `float("3.14")` → `3.14`      |
| `str()`  | texto       | `str(100)` → `"100"`          |
| `bool()` | booleano    | `bool(0)` → `False`           |

### Valores que se convierten a `False`

```python
bool(0)       # False
bool(0.0)     # False
bool("")      # False
bool(None)    # False
# Todo lo demás es True
```

## Resumen

- `int` → números sin decimales
- `float` → números con decimales
- `str` → texto entre comillas
- `bool` → True o False
- `type()` → consultar el tipo
- `int()`, `float()`, `str()`, `bool()` → convertir entre tipos
