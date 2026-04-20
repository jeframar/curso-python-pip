# MÓDULO 10 — Retos finales
# Extensiones del proyecto principal. Modifica ejercicios.py para implementarlas.

# ── Reto 1 — Editar tarea ────────────────────────────────────
# Agrega la opción "8. Editar tarea" al menú.
# El usuario elige una tarea por número y puede cambiar:
#   - El título
#   - La prioridad
# Si deja vacío el campo, conserva el valor actual.


# ── Reto 2 — Ordenar lista ───────────────────────────────────
# Agrega la opción "9. Ordenar tareas" al menú.
# Permite ordenar por:
#   a) Prioridad (alta → media → baja)
#   b) Alfabéticamente por título
#   c) Estado (pendientes primero)


# ── Reto 3 — Guardar en archivo ──────────────────────────────
# Agrega una función guardar_tareas(tareas, archivo) que escriba
# todas las tareas en un archivo .txt, una por línea, con formato:
#   ID|titulo|prioridad|completada
# Ejemplo: 1|Estudiar Python|alta|False
# Y una función cargar_tareas(archivo) que las cargue de vuelta.
# Pista: usa open(), write(), readline(), split().


# ── Reto 4 — Buscar tarea ────────────────────────────────────
# Agrega la opción "Buscar por texto" al menú.
# El usuario escribe una palabra clave y el programa muestra
# todas las tareas cuyo título la contenga (sin importar mayúsculas).


# ── Reto 5 — Fecha límite (deadline) ────────────────────────
# Modifica crear_tarea() para aceptar un campo opcional "deadline"
# con formato "YYYY-MM-DD". Al listar tareas, muestra cuántos días
# faltan para el deadline (puedes usar strings simples sin necesidad de datetime).


# ── Reto 6 (desafío final) — Calculadora ─────────────────────
# Construye una calculadora interactiva SEPARADA de la agenda.
# Crea el archivo: calculadora.py
# La calculadora debe:
#   - Mostrar un menú: suma, resta, multiplicación, división, potencia, raíz
#   - Pedir dos números al usuario
#   - Manejar errores: división por cero, raíz de número negativo
#   - Guardar historial de operaciones en una lista de dicts:
#       {"operacion": "suma", "a": 5, "b": 3, "resultado": 8}
#   - Opción para ver el historial
#   - Opción para limpiar el historial
#   - Continuar hasta que el usuario elija "Salir"
