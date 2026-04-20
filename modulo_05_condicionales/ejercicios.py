# MÓDULO 05 — Condicionales
# Ejercicios guiados

# ── 1. if simple ────────────────────────────────────────────
temperatura = 35
if temperatura > 30:
    print("Hace calor")

# ── 2. if / else ────────────────────────────────────────────
hora = 14
if hora < 12:
    print("Buenos días")
else:
    print("Buenas tardes/noches")

# ── 3. if / elif / else — clasificar nota ───────────────────
nota = 85

if nota >= 90:
    calificacion = "Sobresaliente"
elif nota >= 80:
    calificacion = "Notable"
elif nota >= 70:
    calificacion = "Aprobado"
elif nota >= 60:
    calificacion = "Regular"
else:
    calificacion = "Reprobado"

print(f"Nota: {nota} → {calificacion}")

# ── 4. Condiciones con and ──────────────────────────────────
edad = 22
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print("No puede conducir")

# ── 5. Condiciones con or ───────────────────────────────────
es_fin_de_semana = False
es_festivo = True

if es_fin_de_semana or es_festivo:
    print("¡Día libre!")
else:
    print("Día de trabajo")

# ── 6. Condición con not ────────────────────────────────────
esta_lloviendo = False

if not esta_lloviendo:
    print("Buen día para salir")

# ── 7. Operador ternario ─────────────────────────────────────
numero = 7
paridad = "par" if numero % 2 == 0 else "impar"
print(f"{numero} es {paridad}")

# ── 8. if anidado ───────────────────────────────────────────
saldo = 1500
monto_retiro = 1000
tiene_cuenta = True

if tiene_cuenta:
    if saldo >= monto_retiro:
        saldo -= monto_retiro
        print(f"Retiro exitoso. Saldo restante: {saldo}")
    else:
        print("Saldo insuficiente")
else:
    print("No tiene cuenta bancaria")

# ── 9. Valores truthy/falsy ──────────────────────────────────
nombre = input("Ingresa tu nombre (Enter para omitir): ") if False else ""
nombre = "Ana"   # simulamos para poder ejecutar sin input

if nombre:
    print(f"Hola, {nombre}")
else:
    print("No ingresaste tu nombre")

# ── 10. Comparar rangos ──────────────────────────────────────
imc = 22.5   # Índice de Masa Corporal

if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"IMC {imc} → {categoria}")

# ── 11. Múltiple comparación encadenada ──────────────────────
x = 10
print(1 < x < 20)    # True (Python permite esta sintaxis)
print(0 < x < 5)     # False

# ── 12. Comparar strings ─────────────────────────────────────
opcion = "s"

if opcion.lower() in ("s", "si", "sí", "yes"):
    print("Confirmado")
else:
    print("Cancelado")
