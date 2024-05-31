import re

# Definición de los tokens
TOKENS = {
    'PALABRA_CLAVE': r'(Define|Imprime|Prueba|Excepcion|Entero|Caracter|Entonces|Finalmente)\b',  # Palabras clave del lenguaje
    'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',  # Identificadores de variables
    'OPERADOR': r'\+|-|\*|/',  # Operadores matemáticos
    'ASIGNACION': r'=',  # Operador de asignación
    'VALOR': r'\d+',  # Valores numéricos
    'CADENA': r'\".*?\"',  # Cadenas de texto
    'COMENTARIO': r'~.*',  # Comentarios
    'ESPACIO': r'\s+',  # Espacios en blanco
    'SIMBOLOS_ESPECIALES': r'\(|\)|\{|\}|;',  # Símbolos especiales como paréntesis y punto y coma
    'ERROR': r'.'  # Cualquier otro carácter se considera un error
}

# Expresiones regulares
regex = '|'.join(f'(?P<{token}>{pattern})' for token, pattern in TOKENS.items())  # Compila todas las expresiones regulares en una sola

# Manejo de comentarios y espacios
def ignore_comments_and_spaces(token):
    return token.group('COMENTARIO') is None and token.group('ESPACIO') is None  # Ignora los comentarios y los espacios en blanco

# Acciones asociadas a los tokens
def handle_token(match):
    token_type = match.lastgroup  # Obtiene el tipo de token
    token_value = match.group(token_type)  # Obtiene el valor del token
    if token_type == 'ERROR':  # Si el token es un error, imprime un mensaje de error
        print(f'Error: Carácter desconocido {token_value!r}')
        return None  # Ignora los tokens de error
    elif token_type != 'COMENTARIO' and token_type != 'ESPACIO':  # No imprime comentarios ni espacios
        return token_type, token_value  # Devuelve el tipo y el valor del token

# Función de entrada del analizador léxico
def Entrada(input):
    return filter(None, map(handle_token, filter(ignore_comments_and_spaces, re.finditer(regex, input, re.MULTILINE))))  # Aplica las funciones definidas anteriormente para analizar la entrada
