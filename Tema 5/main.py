from analex import Entrada
from sintax import AnalizadorSintactico

# Prueba del analizador léxico y sintáctico
codigo_prueba = """~Manitas
Define a = 5
Define b = 7
?
Prueba {
    Define resultado = a + b
    Imprime ("El resultado de la suma es: ") + resultado
} Excepcion {
    Imprime ("Ocurrió un error al realizar la suma")
}
"""

try:
    # Ejecutar el analizador léxico y pasar los tokens al analizador sintáctico
    tokens = iter(Entrada(codigo_prueba))
    analizador = AnalizadorSintactico(tokens)
    analizador.programa()
    print(" ")
    print("El análisis sintáctico se completó sin errores.")
    print(" ")
except Exception as e:
    print(" ")
    print(e)
    print(" ")
