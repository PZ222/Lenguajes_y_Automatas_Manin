import re

# 1. Definición de tokens
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
regex = '|'.join(f'(?P<{token}>{pattern})' for token, pattern in TOKENS.items())

# 3. Manejo de comentarios
def ignore_comments(token):
    return token.group('COMENTARIO') is None

# 4. Prioridad de coincidencia
# La prioridad de coincidencia se maneja en el orden en que se definen los tokens en el diccionario TOKENS.

# 5. Acciones asociadas a los tokens
def handle_token(match):
    token_type = match.lastgroup
    token_value = match.group(token_type)
    if token_type == 'ERROR':
        print(f'Error: Carácter desconocido {token_value!r}')
    else:
        return token_type, token_value

# 6. Manejo de errores
# El manejo de errores se realiza en la función handle_token.

def lexer(input):
    return filter(None, map(handle_token, re.finditer(regex, input, re.MULTILINE)))

# Prueba del analizador léxico
codigo_prueba = """
Define a = 5
Define b = 7
Prueba
    Define resultado = a + b
    Imprime ("El resultado de la suma es: ") + resultado
Excepcion
    Imprime ("Ocurrió un error al realizar la suma")
"""

# Prueba del analizador léxico
print("Tokens reconocidos:")
for token in lexer(codigo_prueba):
    print(f"Tipo: {token[0]}, Valor: {token[1]}")

