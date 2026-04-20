# Módulo 01 — Introducción a Python

## ¿Qué es Python?

Python es un lenguaje de programación interpretado, de propósito general y fácil de leer. Es uno de los lenguajes más populares del mundo, usado en web, ciencia de datos, inteligencia artificial y automatización.

## El intérprete (REPL)

Puedes ejecutar Python de dos formas:

1. **Modo interactivo (REPL):** Escribe `python` en la terminal y ejecuta líneas una a una.
2. **Modo script:** Crea un archivo `.py` y ejecútalo con `python archivo.py`.

```
$ python
>>> print("Hola mundo")
Hola mundo
>>> exit()
```

## Tu primer programa

```python
print("Hola, mundo!")
```

`print()` muestra texto en la pantalla. Es la función más básica de Python.

## Comentarios

Los comentarios son notas en el código que Python ignora al ejecutar:

```python
# Esto es un comentario de una línea
print("Esto sí se ejecuta")
```

## Variables

Una variable es un nombre que apunta a un valor almacenado en memoria.

```python
nombre = "Ana"
edad = 25
altura = 1.68
```

- No se declara el tipo (Python lo infiere automáticamente).
- Los nombres son sensibles a mayúsculas: `nombre` ≠ `Nombre`.
- Usa `snake_case` para nombres de variables: `mi_variable`.

## Reglas para nombres de variables

| Válido       | Inválido      |
|--------------|---------------|
| `nombre`     | `1nombre`     |
| `mi_edad`    | `mi-edad`     |
| `_privado`   | `class`       |
| `dato2`      | `dato 2`      |

## La función `print()`

```python
print("Hola")               # texto simple
print("Hola", "mundo")      # múltiples argumentos
print("Edad:", 30)          # mezcla de texto y número
print()                     # línea vacía
```

## Resumen

| Concepto    | Ejemplo                    |
|-------------|----------------------------|
| Comentario  | `# esto es un comentario`  |
| Variable    | `nombre = "Python"`        |
| Imprimir    | `print(nombre)`            |
