# Módulo 03 — Operadores y Expresiones

## Operadores aritméticos

| Operador | Nombre          | Ejemplo      | Resultado |
|----------|-----------------|--------------|-----------|
| `+`      | Suma            | `5 + 3`      | `8`       |
| `-`      | Resta           | `5 - 3`      | `2`       |
| `*`      | Multiplicación  | `5 * 3`      | `15`      |
| `/`      | División        | `5 / 2`      | `2.5`     |
| `//`     | División entera | `5 // 2`     | `2`       |
| `%`      | Módulo (resto)  | `5 % 2`      | `1`       |
| `**`     | Potencia        | `2 ** 3`     | `8`       |

> La división `/` siempre devuelve `float`, aunque sea exacta: `4 / 2` → `2.0`

## Operadores de comparación

Devuelven `True` o `False`:

| Operador | Significado      | Ejemplo   | Resultado |
|----------|------------------|-----------|-----------|
| `==`     | Igual a          | `5 == 5`  | `True`    |
| `!=`     | Distinto de      | `5 != 3`  | `True`    |
| `>`      | Mayor que        | `5 > 3`   | `True`    |
| `<`      | Menor que        | `5 < 3`   | `False`   |
| `>=`     | Mayor o igual    | `5 >= 5`  | `True`    |
| `<=`     | Menor o igual    | `5 <= 4`  | `False`   |

## Operadores lógicos

Combinan condiciones booleanas:

| Operador | Significado                     | Ejemplo              |
|----------|---------------------------------|----------------------|
| `and`    | Ambas condiciones son True      | `5 > 3 and 2 < 4`   |
| `or`     | Al menos una condición es True  | `5 > 3 or 2 > 4`    |
| `not`    | Invierte el booleano            | `not True` → `False` |

### Tabla de verdad `and`
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### Tabla de verdad `or`
| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

## Operadores de asignación

```python
x = 10
x += 5    # equivale a x = x + 5  → 15
x -= 3    # equivale a x = x - 3  → 12
x *= 2    # equivale a x = x * 2  → 24
x //= 5   # equivale a x = x // 5 → 4
x **= 3   # equivale a x = x ** 3 → 64
x %= 10   # equivale a x = x % 10 → 4
```

## Precedencia de operadores

Python evalúa en este orden (de mayor a menor prioridad):

1. `()` — paréntesis
2. `**` — potencia
3. `*`, `/`, `//`, `%` — multiplicación y división
4. `+`, `-` — suma y resta
5. `==`, `!=`, `<`, `>`, `<=`, `>=` — comparaciones
6. `not` — negación lógica
7. `and` — y lógico
8. `or` — o lógico

```python
# Sin paréntesis:
print(2 + 3 * 4)    # 14 (multiplica primero)

# Con paréntesis:
print((2 + 3) * 4)  # 20 (suma primero)
```

**Regla práctica:** ante la duda, usa paréntesis para dejar clara la intención.

## Operador `in`

Comprueba si un elemento está dentro de una secuencia:

```python
print("a" in "hola")      # True
print("z" in "hola")      # False
print(3 in [1, 2, 3])     # True
```
