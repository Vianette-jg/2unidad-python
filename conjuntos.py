# Función para registrar estudiantes en un curso
def registrar_estudiantes(curso):
    estudiantes = set()
    print(f"Ingrese los nombres de los estudiantes inscritos en {curso}. Escriba 'fin' para terminar:")
    while True:
        nombre = input("Nombre: ").strip()
        if nombre.lower() == 'fin':
            break
        estudiantes.add(nombre)
    return estudiantes

# Registrar estudiantes en Programación y en Redes
programacion = registrar_estudiantes("Programación")
redes = registrar_estudiantes("Redes")

# Calcular estudiantes en ambos cursos, solo en Programación y solo en Redes
ambos_cursos = programacion & redes
solo_programacion = programacion - redes
solo_redes = redes - programacion

# Mostrar resultados
print("\nEstudiantes inscritos en ambos cursos:")
print(ambos_cursos)

print("\nEstudiantes inscritos solo en Programación:")
print(solo_programacion)

print("\nEstudiantes inscritos solo en Redes:")
print(solo_redes)
