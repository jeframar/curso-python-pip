# Módulo 05 — Condicionales

## La estructura `if`

Ejecuta un bloque de código solo si una condición es verdadera.

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
```

**Importante:** Python usa indentación (4 espacios) para delimitar bloques, no llaves `{}`.

## `if / else`

El bloque `else` se ejecuta cuando la condición es falsa:

```python
edad = 15

if edad >= 18:
    print("Puedes votar")
else:
    print("Aún no puedes votar")
```

## `if / elif / else`

Cuando hay más de dos casos posibles:

```python
nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 60:
    print("Regular")
else:
    print("Reprobado")
```

- `elif` se evalúa solo si los anteriores fueron `False`.
- Python evalúa de arriba hacia abajo y se detiene en el primero verdadero.
- Puede haber tantos `elif` como necesites.
- El `else` es opcional.

## Condiciones compuestas

Combina condiciones con `and`, `or`, `not`:

```python
temperatura = 25
llueve = False

if temperatura > 20 and not llueve:
    print("Perfecto para salir")

edad = 17
tiene_permiso = True

if edad >= 18 or tiene_permiso:
    print("Puede entrar")
```

## Operador ternario

Escribe un `if/else` simple en una sola línea:

```python
# Sintaxis: valor_si_true if condicion else valor_si_false
edad = 20
estado = "mayor" if edad >= 18 else "menor"
print(estado)   # "mayor"

# Equivale a:
if edad >= 18:
    estado = "mayor"
else:
    estado = "menor"
```

## `if` anidado

Un `if` dentro de otro `if`:

```python
tiene_cuenta = True
saldo = 500

if tiene_cuenta:
    if saldo >= 100:
        print("Puede retirar")
    else:
        print("Saldo insuficiente")
else:
    print("No tiene cuenta")
```

Preferir condiciones compuestas sobre anidamiento excesivo cuando sea posible.

## Comparar con `None`

Usa `is` (no `==`) para comparar con `None`:

```python
resultado = None

if resultado is None:
    print("Sin resultado todavía")

if resultado is not None:
    print("Hay resultado:", resultado)
```

## Valores truthy y falsy

En un `if`, Python convierte el valor a booleano:

```python
nombre = ""
if nombre:          # False porque es string vacío
    print("Tiene nombre")
else:
    print("Nombre vacío")

lista = [1, 2, 3]
if lista:           # True porque la lista no está vacía
    print("Hay elementos")
```
