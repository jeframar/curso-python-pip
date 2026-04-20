# MÓDULO 07 — Funciones
# Ejercicios guiados

# ── 1. Función sin parámetros ───────────────────────────────
def bienvenida():
    print("Bienvenido al curso de Python")
    print("=" * 35)

bienvenida()

# ── 2. Función con parámetros ───────────────────────────────
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")
saludar("Carlos")

# ── 3. Función con return ───────────────────────────────────
def cuadrado(numero):
    return numero ** 2

print(cuadrado(5))    # 25
print(cuadrado(12))   # 144

# ── 4. Múltiples parámetros ─────────────────────────────────
def area_rectangulo(base, altura):
    return base * altura

area = area_rectangulo(10, 5)
print(f"Área: {area}")

# ── 5. Parámetro por defecto ─────────────────────────────────
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))      # 9  (usa 2 por defecto)
print(potencia(3, 3))   # 27

# ── 6. Keyword arguments ─────────────────────────────────────
def ficha_persona(nombre, edad, ciudad="Sin ciudad"):
    print(f"Nombre: {nombre} | Edad: {edad} | Ciudad: {ciudad}")

ficha_persona("Ana", 25, "Bogotá")
ficha_persona(edad=30, nombre="Luis")
ficha_persona("María", ciudad="Cali", edad=28)

# ── 7. Retornar múltiples valores ────────────────────────────
def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

datos = [4, 7, 2, 9, 1, 6]
minimo, maximo, promedio = estadisticas(datos)
print(f"Mín: {minimo} | Máx: {maximo} | Promedio: {promedio:.2f}")

# ── 8. Scope local vs global ─────────────────────────────────
mensaje_global = "Soy global"

def mostrar_scope():
    mensaje_local = "Soy local"
    print(mensaje_local)
    print(mensaje_global)   # puede leer la global

mostrar_scope()
print(mensaje_global)
# print(mensaje_local)   # ERROR: no existe aquí

# ── 9. Funciones que llaman a otras funciones ────────────────
def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32

def descripcion_temperatura(celsius):
    f = celsius_a_fahrenheit(celsius)
    if celsius < 0:
        estado = "bajo cero"
    elif celsius < 20:
        estado = "frío"
    elif celsius < 30:
        estado = "templado"
    else:
        estado = "caluroso"
    return f"{celsius}°C = {f:.1f}°F ({estado})"

print(descripcion_temperatura(-5))
print(descripcion_temperatura(22))
print(descripcion_temperatura(38))

# ── 10. Built-ins más usados ─────────────────────────────────
numeros = [15, 3, 9, 1, 22, 7]
print(f"Lista:    {numeros}")
print(f"Mínimo:   {min(numeros)}")
print(f"Máximo:   {max(numeros)}")
print(f"Suma:     {sum(numeros)}")
print(f"Longitud: {len(numeros)}")
print(f"Ordenada: {sorted(numeros)}")
print(f"Valor abs de -42: {abs(-42)}")
print(f"Redondeo: {round(3.14159, 2)}")

# ── 11. Lambda ───────────────────────────────────────────────
doble = lambda x: x * 2
es_par = lambda x: x % 2 == 0
saludo_lambda = lambda nombre: f"Hola, {nombre}!"

print(doble(7))
print(es_par(8))
print(saludo_lambda("Python"))

# ── 12. Función que valida entrada ───────────────────────────
def es_positivo(numero):
    return numero > 0

def raiz_cuadrada(numero):
    if not es_positivo(numero):
        return "Error: el número debe ser positivo"
    return numero ** 0.5

print(raiz_cuadrada(25))
print(raiz_cuadrada(-4))
