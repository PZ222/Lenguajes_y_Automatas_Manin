import re

# 1. Definición de tokens
# Aquí estamos definiendo los tokens que nuestro analizador léxico debe reconocer.
# Cada token tiene un nombre y una expresión regular que define cómo se reconoce ese token en el texto de entrada.
TOKENS = {
    'PALABRA_CLAVE': r'(Define|Imprime|Prueba|Excepcion|Entero|Caracter|Entonces|Finalmente)\b',
    'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'OPERADOR': r'\+|-|\*|/',
    'ASIGNACION': r'=',
    'VALOR': r'\d+',
    'CADENA': r'\".*?\"',
    'COMENTARIO': r'//.*',
    'ESPACIO': r'\s+',
    'SIMBOLOS_ESPECIALES': r'\(|\)|\{|\}|;',
    'ERROR': r'.'
}

# 2. Expresiones regulares
# Aquí estamos creando una única expresión regular que combina todas las expresiones regulares de los tokens.
# Esta expresión regular se utilizará para buscar tokens en el texto de entrada.
regex = '|'.join(f'(?P<{token}>{pattern})' for token, pattern in TOKENS.items())

# 3. Manejo de comentarios
# Esta función se utiliza para ignorar los comentarios en el texto de entrada.
# Cuando se reconoce un comentario, esta función devuelve False, lo que hace que el comentario sea ignorado por el analizador léxico.
def ignore_comments(token):
    return token.group('COMENTARIO') is None

# 4. Prioridad de coincidencia
# La prioridad de coincidencia se maneja en el orden en que se definen los tokens en el diccionario TOKENS.
# Es decir, los tokens que se definen primero tienen prioridad sobre los que se definen después.

# 5. Acciones asociadas a los tokens
# Esta función se llama cuando se reconoce un token.
# Si el token es de tipo 'ERROR', imprime un mensaje de error.
# De lo contrario, devuelve el tipo y el valor del token.
# Esta parte del código se refiere a la función que vamos a utilizar para manejar las acciones que se deben realizar cuando se reconoce un token.
def handle_token(match):
    token_type = match.lastgroup
    token_value = match.group(token_type)
    if token_type == 'ERROR':
        print(f'Error: Carácter desconocido {token_value!r}')
    else:
        return token_type, token_value

# 6. Manejo de errores
# Cómo vamos a manejar los errores que puedan ocurrir durante el análisis léxico?
# El manejo de errores se realiza en la función handle_token.
# Cuando se reconoce un token de tipo 'ERROR', la función handle_token imprime un mensaje de error.


# Esta es la función principal del analizador léxico.
# Toma un texto de entrada y devuelve una lista de tokens reconocidos en ese texto.
def lexer(input):
    return filter(None, map(handle_token, re.finditer(regex, input, re.MULTILINE)))
# Esta parte del código se refiere a la función principal del analizador léxico que vamos a utilizar para analizar el texto de entrada.



# Prueba del analizador léxico
# Aquí tenemos un código de prueba que vamos a analizar.
codigo_prueba = """
Define a = 5
Define b = 7
Prueba
    Define resultado = a + b
    Imprime ("El resultado de la suma es: ") + resultado
Excepcion
    Imprime ("Ocurrió un error al realizar la suma")
"""

# Aquí estamos ejecutando el analizador léxico en el código de prueba y imprimiendo los tokens reconocidos.
print("Tokens reconocidos:")
for token in lexer(codigo_prueba):
    print(f"Tipo: {token[0]}, Valor: {token[1]}")

