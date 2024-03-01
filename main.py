# main.py
import curso
import estudiantes
def main():
    # Obtener información del curso
    curso.curso_mostrar_informacion_curso()

    # Obtener información de los estudiantes
    estudiantes.estudiantes_mostrar_estadisticas_estudiantes()

if __name__ == "__main__":
    main()
