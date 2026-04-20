# MÓDULO 10 — Proyecto Final: Agenda de Tareas
# Aplicación completa que integra todos los módulos del curso.

PRIORIDADES = {"alta": 1, "media": 2, "baja": 3}
SIMBOLOS = {"alta": "🔴", "media": "🟡", "baja": "🟢"}


# ── Funciones de la agenda ───────────────────────────────────

def crear_tarea(id_tarea, titulo, prioridad):
    return {
        "id": id_tarea,
        "titulo": titulo,
        "prioridad": prioridad,
        "completada": False
    }


def mostrar_tarea(tarea):
    estado = "[✓]" if tarea["completada"] else "[ ]"
    simbolo = SIMBOLOS.get(tarea["prioridad"], "⚪")
    print(f"  {tarea['id']:2}. {estado} {simbolo} {tarea['titulo']}")


def listar_tareas(tareas, filtro=None):
    if not tareas:
        print("  No hay tareas registradas.")
        return

    if filtro:
        visibles = [t for t in tareas if t["prioridad"] == filtro]
        print(f"\n  Tareas con prioridad '{filtro}':")
    else:
        visibles = tareas
        print("\n  Todas las tareas:")

    if not visibles:
        print("  No hay tareas con ese filtro.")
        return

    pendientes = [t for t in visibles if not t["completada"]]
    completadas = [t for t in visibles if t["completada"]]

    if pendientes:
        print("  --- Pendientes ---")
        for tarea in sorted(pendientes, key=lambda t: PRIORIDADES.get(t["prioridad"], 9)):
            mostrar_tarea(tarea)

    if completadas:
        print("  --- Completadas ---")
        for tarea in completadas:
            mostrar_tarea(tarea)


def agregar_tarea(tareas, siguiente_id):
    titulo = input("  Título de la tarea: ").strip()
    if not titulo:
        print("  El título no puede estar vacío.")
        return siguiente_id

    print("  Prioridad: (1) alta  (2) media  (3) baja")
    opcion_prioridad = input("  Elige: ").strip()
    mapa = {"1": "alta", "2": "media", "3": "baja"}
    prioridad = mapa.get(opcion_prioridad, "media")

    tarea = crear_tarea(siguiente_id, titulo, prioridad)
    tareas.append(tarea)
    print(f"  ✓ Tarea '{titulo}' agregada con prioridad {prioridad}.")
    return siguiente_id + 1


def completar_tarea(tareas):
    listar_tareas(tareas)
    try:
        id_objetivo = int(input("\n  Número de tarea a completar: "))
    except ValueError:
        print("  Número inválido.")
        return

    for tarea in tareas:
        if tarea["id"] == id_objetivo:
            if tarea["completada"]:
                print("  La tarea ya estaba completada.")
            else:
                tarea["completada"] = True
                print(f"  ✓ Tarea '{tarea['titulo']}' marcada como completada.")
            return

    print("  No se encontró esa tarea.")


def eliminar_tarea(tareas):
    listar_tareas(tareas)
    try:
        id_objetivo = int(input("\n  Número de tarea a eliminar: "))
    except ValueError:
        print("  Número inválido.")
        return

    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_objetivo:
            eliminada = tareas.pop(i)
            print(f"  ✓ Tarea '{eliminada['titulo']}' eliminada.")
            return

    print("  No se encontró esa tarea.")


def filtrar_por_prioridad(tareas):
    print("  Filtrar por: (1) alta  (2) media  (3) baja")
    opcion = input("  Elige: ").strip()
    mapa = {"1": "alta", "2": "media", "3": "baja"}
    prioridad = mapa.get(opcion)
    if prioridad:
        listar_tareas(tareas, filtro=prioridad)
    else:
        print("  Opción inválida.")


def mostrar_estadisticas(tareas):
    total = len(tareas)
    completadas = sum(1 for t in tareas if t["completada"])
    pendientes = total - completadas

    print(f"\n  {'─'*30}")
    print(f"  Total de tareas  : {total}")
    print(f"  Completadas      : {completadas}")
    print(f"  Pendientes       : {pendientes}")
    if total > 0:
        porcentaje = completadas / total * 100
        barra = "█" * int(porcentaje / 10) + "░" * (10 - int(porcentaje / 10))
        print(f"  Progreso: [{barra}] {porcentaje:.0f}%")
    print(f"  {'─'*30}")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("       AGENDA DE TAREAS")
    print("=" * 40)
    print("  1. Agregar tarea")
    print("  2. Listar todas las tareas")
    print("  3. Completar tarea")
    print("  4. Eliminar tarea")
    print("  5. Filtrar por prioridad")
    print("  6. Estadísticas")
    print("  7. Salir")
    print("=" * 40)


# ── Programa principal ───────────────────────────────────────

def main():
    tareas = []
    siguiente_id = 1

    # Datos de ejemplo para empezar
    tareas.append(crear_tarea(siguiente_id, "Completar Módulo 10", "alta"))
    siguiente_id += 1
    tareas.append(crear_tarea(siguiente_id, "Repasar funciones", "media"))
    siguiente_id += 1
    tareas.append(crear_tarea(siguiente_id, "Practicar diccionarios", "baja"))
    siguiente_id += 1

    print("Bienvenido a tu Agenda de Tareas")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción: ").strip()

        if opcion == "1":
            siguiente_id = agregar_tarea(tareas, siguiente_id)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            filtrar_por_prioridad(tareas)
        elif opcion == "6":
            mostrar_estadisticas(tareas)
        elif opcion == "7":
            print("\n  ¡Hasta luego! Sigue practicando Python.")
            break
        else:
            print("  Opción no válida. Elige entre 1 y 7.")


if __name__ == "__main__":
    main()
