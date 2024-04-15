import re

# Definir patrones de expresiones regulares
patron_origen_destino_fecha = r"volar de (\w+) a (\w+) el (\d{1,2} de \w+)"
patron_precio = r"cuánto cuesta un vuelo de (\w+) a (\w+)"
patron_ida_vuelta = r"un vuelo de ida y vuelta de (\w+) a (\w+)"

# Definir las consultas de los usuarios
consultas = [
    "Quiero volar de México a Japón el 25 de marzo",
    "cuánto cuesta un vuelo de Mexico a Alemania",
    "Necesito un vuelo de ida y vuelta de Londres a Roma"
]

# Procesar las consultas
for consulta in consultas:
    # Verificar si la consulta coincide con alguno de los patrones
    if re.search(patron_origen_destino_fecha, consulta):
        origen_destino_fecha = re.search(patron_origen_destino_fecha, consulta)
        origen = origen_destino_fecha.group(1)
        destino = origen_destino_fecha.group(2)
        fecha = origen_destino_fecha.group(3)
        print(f"Buscar vuelo de {origen} a {destino} para el {fecha}")
    elif re.search(patron_precio, consulta):
        precio = re.search(patron_precio, consulta)
        origen = precio.group(1)
        destino = precio.group(2)
        print(f"Consultar precio de vuelo de {origen} a {destino}")
    elif re.search(patron_ida_vuelta, consulta):
        ida_vuelta = re.search(patron_ida_vuelta, consulta)
        origen = ida_vuelta.group(1)
        destino = ida_vuelta.group(2)
        print(f"Buscar vuelo de ida y vuelta de {origen} a {destino}")
    else:
        print("Lo siento, no puedo entender tu consulta.")