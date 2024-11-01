alumno = {
    "matricula": "",
    "nombre": "",
    "apellido": "",
    "correo": "",
    "No telefono": "",
    "sexo": "",
    "edad": ""
}

alumno["matricula"] = input("Ingresar la matricula: ")
alumno["nombre"] = input("Ingresar el nombre: ")
alumno["apellido"] = input("Ingresar el apellido: ")
alumno["correo"] = input("Ingresar el correo: ")
alumno["No telefono"] = input("Ingresar el No de telefono: ")
alumno["sexo"] = input("Ingresar el sexo: ")
alumno["edad"] = input("Ingresar la edad: ")

print("\n--- Información del Alumno ---")
print("Matrícula:       " + alumno["matricula"])
print("Nombre:          " + alumno["nombre"])
print("Apellido:        " + alumno["apellido"])
print("Correo:          " + alumno["correo"])
print("No. de Teléfono: " + alumno["No telefono"])
print("Sexo:            " + alumno["sexo"])
print("Edad:            " + alumno["edad"])
