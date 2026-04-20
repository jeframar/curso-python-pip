# Módulo 04 — Strings y Entrada del Usuario

## La función `input()`

Permite que el usuario escriba datos desde el teclado. **Siempre devuelve un string.**

```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

Si necesitas un número, debes convertirlo:
```python
edad = int(input("¿Cuántos años tienes? "))
precio = float(input("Precio: "))
```

## f-strings (formato moderno)

La forma más legible de construir strings con variables. Se escribe poniendo `f` antes de las comillas:

```python
nombre = "Ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
```

Puedes poner expresiones dentro de las llaves:
```python
precio = 100
print(f"Con IVA: {precio * 1.19:.2f}")  # :.2f → 2 decimales
print(f"El doble de 7 es {7 * 2}")
```

### Formato de números en f-strings

| Formato  | Significado       | Ejemplo                       |
|----------|-------------------|-------------------------------|
| `:.2f`   | 2 decimales       | `f"{3.14159:.2f}"` → `3.14`   |
| `:,`     | separador miles   | `f"{1000000:,}"` → `1,000,000`|
| `:>10`   | alinear derecha   | `f"{'hi':>10}"` → `        hi`|
| `:^10`   | centrar           | `f"{'hi':^10}"` → `    hi    `|

## Métodos de strings

Los strings tienen métodos incorporados que se llaman con punto:

```python
texto = "  Hola Mundo  "
```

| Método             | Resultado               |
|--------------------|-------------------------|
| `.upper()`         | `"  HOLA MUNDO  "`      |
| `.lower()`         | `"  hola mundo  "`      |
| `.strip()`         | `"Hola Mundo"`          |
| `.replace("o","0")`| `"  H0la Mund0  "`      |
| `.split()`         | `["Hola", "Mundo"]`     |
| `.startswith("Ho")`| `False` (tiene espacios)|
| `.count("o")`      | `2`                     |
| `.find("Mundo")`   | `7` (posición)          |
| `.len()` → `len()` | Es función: `len(texto)`|

## Concatenación y repetición

```python
saludo = "Hola" + " " + "Mundo"   # "Hola Mundo"
linea = "-" * 30                   # 30 guiones
```

## Indexado y slicing

Cada carácter tiene una posición:

```python
texto = "Python"
#        0 1 2 3 4 5   (índices positivos)
#       -6-5-4-3-2-1   (índices negativos)

print(texto[0])     # P
print(texto[-1])    # n
print(texto[0:3])   # Pyt
print(texto[2:])    # thon
print(texto[:3])    # Pyt
print(texto[::2])   # Pto (cada 2 caracteres)
print(texto[::-1])  # nohtyP (invertido)
```

## Strings multilínea

```python
poema = """
Rosas son rojas,
violetas son azules,
Python es genial
"""
print(poema)
```

## Caracteres especiales

| Secuencia | Significado     |
|-----------|-----------------|
| `\n`      | Salto de línea  |
| `\t`      | Tabulación      |
| `\\`      | Barra invertida |
| `\"`      | Comilla doble   |
