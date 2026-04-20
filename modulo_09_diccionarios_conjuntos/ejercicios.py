# MÓDULO 09 — Diccionarios y Conjuntos
# Ejercicios guiados

# ── 1. Crear y acceder ───────────────────────────────────────
producto = {
    "nombre": "Laptop",
    "precio": 2_500_000,
    "stock": 10,
    "disponible": True
}

print(producto["nombre"])
print(producto["precio"])
print(producto.get("garantia", "Sin garantía"))   # clave inexistente

# ── 2. Modificar y agregar ───────────────────────────────────
producto["precio"] = 2_300_000
producto["marca"] = "TechCo"
print(producto)

# ── 3. Eliminar ──────────────────────────────────────────────
del producto["disponible"]
stock = producto.pop("stock")
print(f"Stock retirado: {stock}")
print(producto)

# ── 4. Iterar ────────────────────────────────────────────────
persona = {"nombre": "Ana", "edad": 28, "ciudad": "Bogotá", "lenguaje": "Python"}

print("\n--- Claves ---")
for clave in persona.keys():
    print(clave)

print("\n--- Valores ---")
for valor in persona.values():
    print(valor)

print("\n--- Pares ---")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# ── 5. Comprobar existencia ──────────────────────────────────
config = {"debug": True, "version": "1.0", "puerto": 8080}

if "debug" in config:
    print(f"Modo debug: {config['debug']}")

if "log_file" not in config:
    config["log_file"] = "app.log"
    print("Log file configurado por defecto")

# ── 6. update() — fusionar diccionarios ─────────────────────
base = {"nombre": "App", "version": "1.0"}
actualizacion = {"version": "2.0", "autor": "Ana"}
base.update(actualizacion)
print(base)

# ── 7. Diccionario anidado ───────────────────────────────────
estudiantes = {
    "E001": {"nombre": "Carlos", "nota": 88, "aprobado": True},
    "E002": {"nombre": "Laura", "nota": 55, "aprobado": False},
    "E003": {"nombre": "Pedro", "nota": 92, "aprobado": True},
}

for codigo, info in estudiantes.items():
    estado = "✓ Aprobado" if info["aprobado"] else "✗ Reprobado"
    print(f"{codigo} | {info['nombre']:10} | {info['nota']} | {estado}")

# ── 8. Dict comprehension ────────────────────────────────────
cuadrados = {x: x**2 for x in range(1, 8)}
print(cuadrados)

precios = {"manzana": 1000, "pera": 1500, "uva": 2000, "naranja": 800}
caros = {fruta: precio for fruta, precio in precios.items() if precio >= 1200}
print(f"Frutas caras: {caros}")

# ── 9. Conjuntos básicos ─────────────────────────────────────
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(f"Unión:       {a | b}")
print(f"Intersección:{a & b}")
print(f"Diferencia:  {a - b}")
print(f"Sim. Dif.:   {a ^ b}")

# ── 10. Eliminar duplicados con set ──────────────────────────
visitas = ["inicio", "productos", "inicio", "contacto", "productos", "inicio"]
paginas_unicas = set(visitas)
print(f"\nPáginas únicas visitadas: {paginas_unicas}")
print(f"Total visitas: {len(visitas)} | Páginas únicas: {len(paginas_unicas)}")

# ── 11. add, discard, remove ─────────────────────────────────
permisos = {"leer", "escribir"}
permisos.add("ejecutar")
permisos.discard("borrar")    # no da error si no existe
print(permisos)
print("leer" in permisos)     # True

# ── 12. Contar frecuencias con dict ──────────────────────────
frase = "el cielo es azul y el mar es azul"
frecuencias = {}
for palabra in frase.split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

for palabra, veces in sorted(frecuencias.items(), key=lambda x: -x[1]):
    print(f"  {palabra:10} → {veces}")
