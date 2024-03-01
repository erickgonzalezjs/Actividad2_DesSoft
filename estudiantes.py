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
    Muestra estadísticas de los estudiantes y permite dejar un comentario al final.
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

    dejar_comentario()

def dejar_comentario():
    """
    Permite a los estudiantes dejar un comentario sobre la clase.
    """
    print("\n¡Es tu oportunidad de dejar un comentario sobre la clase!")
    comentario = input("Por favor, escribe tu comentario: ")
    print("\n¡Gracias por tu comentario! Aquí está lo que opinas sobre la clase:")
    print(comentario)

