# Módulo 09 — Diccionarios y Conjuntos

## Diccionarios

Un diccionario almacena pares **clave: valor**. Es mutable y no permite claves duplicadas.

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}
```

### Acceder a valores

```python
print(persona["nombre"])          # Ana
print(persona.get("edad"))        # 25
print(persona.get("email", "N/A")) # N/A (valor por defecto si no existe)
```

Usa `.get()` para evitar `KeyError` cuando la clave puede no existir.

### Modificar y agregar

```python
persona["edad"] = 26           # modifica
persona["email"] = "a@b.com"   # agrega nueva clave
```

### Eliminar

```python
del persona["ciudad"]
valor = persona.pop("email")    # elimina y devuelve el valor
```

## Métodos de diccionarios

```python
d = {"a": 1, "b": 2, "c": 3}
```

| Método         | Resultado                       |
|----------------|---------------------------------|
| `.keys()`      | vista de todas las claves       |
| `.values()`    | vista de todos los valores      |
| `.items()`     | vista de pares (clave, valor)   |
| `.get(k, v)`   | valor de k, o v si no existe    |
| `.pop(k)`      | elimina clave k y devuelve valor|
| `.update(d2)`  | fusiona con otro diccionario    |
| `.clear()`     | vacía el diccionario            |
| `k in d`       | True si k es clave en d         |

## Iterar un diccionario

```python
inventario = {"laptop": 5, "mouse": 12, "teclado": 8}

for clave in inventario:
    print(clave)

for valor in inventario.values():
    print(valor)

for clave, valor in inventario.items():
    print(f"{clave}: {valor}")
```

## Diccionarios anidados

```python
empleados = {
    "E001": {"nombre": "Ana", "cargo": "Dev", "salario": 5000},
    "E002": {"nombre": "Luis", "cargo": "QA", "salario": 4000},
}

print(empleados["E001"]["nombre"])   # Ana
```

## Dict comprehension

```python
cuadrados = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

precios = {"manzana": 1000, "pera": 1500, "uva": 2000}
con_iva = {fruta: precio * 1.19 for fruta, precio in precios.items()}
```

## Conjuntos (`set`)

Un conjunto es una colección **no ordenada de elementos únicos**. No permite duplicados.

```python
vocales = {"a", "e", "i", "o", "u"}
primos = {2, 3, 5, 7, 11, 13}
vacio = set()   # NO usar {} (eso crea un dict vacío)
```

### Operaciones de conjuntos

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(A | B)    # Unión:        {1,2,3,4,5,6,7}
print(A & B)    # Intersección: {3,4,5}
print(A - B)    # Diferencia:   {1,2}
print(A ^ B)    # Diferencia simétrica: {1,2,6,7}
```

### Métodos de conjuntos

```python
s = {1, 2, 3}
s.add(4)           # agrega un elemento
s.discard(10)      # elimina si existe, sin error
s.remove(2)        # elimina, error si no existe
print(3 in s)      # True
```

### Caso de uso — eliminar duplicados de una lista

```python
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4]
unicos = list(set(lista_con_duplicados))
print(unicos)   # [1, 2, 3, 4] (orden no garantizado)
```

## ¿Cuándo usar cada uno?

| Estructura     | Cuando necesitas...                          |
|----------------|----------------------------------------------|
| `dict`         | Asociar clave con valor (índice por nombre)  |
| `set`          | Colección sin duplicados, operaciones matemáticas de conjuntos |
| `list`         | Secuencia ordenada que puede tener duplicados|
| `tuple`        | Secuencia ordenada e inmutable               |
