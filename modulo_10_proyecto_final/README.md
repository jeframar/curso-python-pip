# Módulo 10 — Proyecto Final: Agenda de Tareas

## Objetivo

Construir una aplicación completa de **agenda de tareas** (To-Do List) que integra todos los conceptos del curso:

| Concepto            | Dónde se usa                                      |
|---------------------|---------------------------------------------------|
| Variables y tipos   | Datos de cada tarea                               |
| Operadores          | Cálculo de prioridades y filtros                  |
| Strings y f-strings | Mostrar la interfaz y los mensajes                |
| Condicionales       | Validar opciones del menú y estados de tareas     |
| Bucles              | Menú principal, listar tareas                     |
| Funciones           | Cada operación de la agenda es una función        |
| Listas              | Almacenar las tareas                              |
| Diccionarios        | Estructura de cada tarea                          |

## Funcionalidades

La aplicación permite:

1. **Agregar** una tarea (título, prioridad: alta/media/baja)
2. **Listar** todas las tareas con su estado
3. **Completar** una tarea por su número
4. **Eliminar** una tarea por su número
5. **Filtrar** tareas por prioridad
6. **Estadísticas** del total, completadas y pendientes
7. **Salir**

## Estructura de una tarea

Cada tarea es un diccionario:
```python
{
    "id": 1,
    "titulo": "Estudiar Python",
    "prioridad": "alta",
    "completada": False
}
```

## Cómo ejecutar

```bash
python ejercicios.py
```

## Lo que practicarás

- Diseño de funciones con responsabilidad única
- Manipulación de listas de diccionarios
- Validación de entrada del usuario
- Formateo de salida con f-strings
- Control de flujo con bucles y condicionales
