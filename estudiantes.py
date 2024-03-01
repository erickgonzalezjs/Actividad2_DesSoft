# estudiantes.py

def estudiantes_calcular_promedio(notas):
    """
    Calcula el promedio de un estudiante dado sus notas.
    """
    total = sum(notas)
    cantidad = len(notas)
    if cantidad == 0:
        return 0
    else:
        return total / cantidad

def estudiantes_mostrar_estadisticas_estudiantes():
    """
    Muestra estadísticas de los estudiantes.
    """
    estudiantes = [
        {"nombre": "Juan", "notas": [35, 40, 48]},
        {"nombre": "María", "notas": [35, 40, 32]},
        {"nombre": "Pedro", "notas": [20, 42, 37]},
        # Agrega más estudiantes según sea necesario
    ]

    for estudiante in estudiantes:
        nombre = estudiante["nombre"]
        notas = estudiante["notas"]
        promedio = estudiantes_calcular_promedio(notas)
        print(f"Estudiante: {nombre}")
        print("Notas:", notas)
        print("Promedio:", promedio)
        print()
