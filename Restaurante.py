# Solicitar platos de Persona 1 y Persona 2
platos_persona1 = set(input("Ingrese los platos favoritos de la Persona 1, separados por comas: ").split(","))
platos_persona2 = set(input("Ingrese los platos favoritos de la Persona 2, separados por comas: ").split(","))

# Encontrar platos en común y platos únicos
platos_en_comun = platos_persona1 & platos_persona2
platos_unicos_persona1 = platos_persona1 - platos_persona2
platos_unicos_persona2 = platos_persona2 - platos_persona1

# Imprimir resultados
print("Platos en común:", platos_en_comun)
print("Platos exclusivos de Persona 1:", platos_unicos_persona1)
print("Platos exclusivos de Persona 2:", platos_unicos_persona2)
