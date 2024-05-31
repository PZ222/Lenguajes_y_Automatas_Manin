# Tarea 5.2 Desarrollo de un Analizador Sintáctico para un Lenguaje de Programación Simple

# Analizador Sintáctico "El Lenguaje de los Manines"
## ¿Qué es un analizador sintáctico?

Un analizador sintáctico (parser) es un componente crucial dentro del proceso de compilación y procesamiento de un lenguaje de programación. El objetivo principal de este es tomar una secuencia de tokens, los cuales son generados mediante el analizador léxico (lexer) y construir una estructura de datos conocida como árbol sintáctico o árbol de análisis, el cual representa la estructura gramatical del código fuente de acuerdo a las reglas antes definidas.

## Proposito del analizador
Estamos analizando un subconjunto del lenguaje de programación (Llamado "Lenguaje de los Manines") que incluye operaciones aritméticas básicas, asignaciones de variables, declaraciones condicionales y funciones. El propósito del analizador sintáctico es verificar la corrección sintáctica del código fuente y generar una representación intermedia que se puede utilizar para la compilación o interpretación posterior.
## Aplicaciones

Un analizador sintáctico a menudo es utilizado para convertir cadenas de texto en una nueva estructura, como lo es un árbol sintáctico, que expresa la disposición jerárquica de los elementos generados. El uso de este tipo de analizador es utilizado en:

- *Compiladores de Lenguajes de Programación:* En donde la lectura de un lenguaje de programación es realizada por un analizador. Este proporciona una estructura de datos al compilador que se utiliza para generar el código máquina o bytecode. El árbol sintáctico generado permite al compilador entender la lógica y la estructura del programa, facilitando la optimización y la generación de código eficiente.

- *Navegadores Web:* El código HTML, al principio, es solo una cadena de caracteres para un ordenador. Este código debe ser analizado por el analizador contenido en el navegador web, que proporciona una descripción de la página web como una estructura de datos. Esta estructura se proyecta por un motor de diseño en la pantalla, permitiendo la correcta visualización e interacción con la página web.

- *Motores de Búsqueda:* Los motores de búsqueda como Google extraen (analizan) texto relevante de las páginas web descargadas con rastreadores. Estos analizadores procesan los datos y permiten que la información relevante se utilice para la indexación y navegación, mejorando la precisión y eficiencia de las búsquedas en línea.

## Tabla de Tokens

| *Categoría*       | *Tokens*                                                                 |
|---------------------|----------------------------------------------------------------------------|
| Palabras Clave      | Define, Imprime, Prueba, Excepcion, Entero, Caracter, Entonces, Finalmente |
| Identificadores     | a-z, A-Z                                                                   |
| Asignaciones        | -, *, /, +, =                                                              |
| Valor               | 0-9                                                                        |
| Operadores          | + (suma), - (resta), * (multiplicación), / (división)                      |
| Símbolos Especiales | (, ), {, }, ;                                                              |
| Comentarios         | ~ (comentario de una línea)                                                |
| Cadena de Texto     | " "                                                                        |

## Tabla de Expresiones Regulares

| *Token*               | *Expresión Regular*                               | *Descripción*                                              |
|-------------------------|-----------------------------------------------------|--------------------------------------------------------------|
| PALABRA_CLAVE         | (Define\|Imprime\|Prueba\|Excepcion\|Entero\|Caracter\|Entonces\|Finalmente)\b | Palabras clave reservadas del lenguaje                        |
| IDENTIFICADOR         | [a-zA-Z_][a-zA-Z0-9_]*                            | Identificadores (nombres de variables, funciones, etc.)       |
| OPERADOR              | \+|-|\*|/                                         | Operadores aritméticos                                       |
| ASIGNACION            | =                                                 | Operador de asignación                                        |
| VALOR                 | \d+                                               | Valores numéricos enteros                                    |
| CADENA                | \".*?\"                                           | Cadenas de texto entre comillas dobles                        |
| COMENTARIO            | ~.*                                               | Comentarios que empiezan con el carácter ~                  |
| ESPACIO               | \s+                                               | Espacios en blanco                                            |
| SIMBOLOS_ESPECIALES   | \(|\)|\{|\}|;                                     | Símbolos especiales como paréntesis, llaves y punto y coma    |
| ERROR                 | .                                                 | Cualquier carácter desconocido que no coincida con otro token |

## Analizador Léxico

    import  re
    
      
    
    # Definición de los tokens
    
    TOKENS = {
    
    'PALABRA_CLAVE': r'(Define|Imprime|Prueba|Excepcion|Entero|Caracter|Entonces|Finalmente)\b', # Palabras clave del lenguaje
    
    'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*', # Identificadores de variables
    
    'OPERADOR': r'\+|-|\*|/', # Operadores matemáticos
    
    'ASIGNACION': r'=', # Operador de asignación
    
    'VALOR': r'\d+', # Valores numéricos
    
    'CADENA': r'\".*?\"', # Cadenas de texto
    
    'COMENTARIO': r'~.*', # Comentarios
    
    'ESPACIO': r'\s+', # Espacios en blanco
    
    'SIMBOLOS_ESPECIALES': r'\(|\)|\{|\}|;', # Símbolos especiales como paréntesis y punto y coma
    
    'ERROR': r'.'  # Cualquier otro carácter se considera un error
    
    }
    
      
    
    # Expresiones regulares
    
    regex = '|'.join(f'(?P<{token}>{pattern})'  for  token, pattern  in  TOKENS.items()) # Compila todas las expresiones regulares en una sola
    
      
    
    # Manejo de comentarios y espacios
    
    def  ignore_comments_and_spaces(token):
    
    return  token.group('COMENTARIO') is  None  and  token.group('ESPACIO') is  None  # Ignora los comentarios y los espacios en blanco
    
      
    
    # Acciones asociadas a los tokens
    
    def  handle_token(match):
    
    token_type = match.lastgroup # Obtiene el tipo de token
    
    token_value = match.group(token_type) # Obtiene el valor del token
    
    if  token_type == 'ERROR': # Si el token es un error, imprime un mensaje de error
    
    print(f'Error: Carácter desconocido {token_value!r}')
    
    return  None  # Ignora los tokens de error
    
    elif  token_type != 'COMENTARIO'  and  token_type != 'ESPACIO': # No imprime comentarios ni espacios
    
    return  token_type, token_value  # Devuelve el tipo y el valor del token
    
      
    
    # Función de entrada del analizador léxico
    
    def  Entrada(input):
    
    return  filter(None, map(handle_token, filter(ignore_comments_and_spaces, re.finditer(regex, input, re.MULTILINE)))) # Aplica las funciones definidas anteriormente para analizar la entrada

## Analizador Sintáctico

    class  AnalizadorSintactico:
    
    def  __init__(self, tokens):
    
    self.tokens = tokens  # Almacena los tokens
    
    self.current_token = None  # Almacena el token actual
    
    self.history = [] # Historial de tokens esperados
    
    self.next_token() # Obtiene el primer token
    
    def  next_token(self):
    
    self.current_token = next(self.tokens, None) # Obtiene el siguiente token
    
    print(f"Token actual: {self.current_token}") # Imprime el token actual para depuración
    
    def  error(self, expected):
    
    """Lanza una excepción con un mensaje de error detallado."""
    
    message = (f"Error de sintaxis: Se esperaba {expected} "
    
    f"pero se encontró {self.current_token}. "
    
    f"Historia de tokens esperados: {self.history}")
    
    raise  Exception(message)
    
    def  eat(self, token_type):
    
    self.history.append(token_type) # Agrega el tipo de token esperado al historial
    
    if  self.current_token  and  self.current_token[0] == token_type: # Si el token actual es del tipo esperado
    
    self.next_token() # Obtiene el siguiente token
    
    self.history.pop() # Elimina el último token esperado del historial
    
    else: # Si el token actual no es del tipo esperado
    
    self.error(f"Se esperaba {token_type} pero se encontró {self.current_token}") # Lanza un error
    
    def  programa(self):
    
    while  self.current_token  is  not  None: # Mientras haya tokens
    
    self.declaracion() # Procesa una declaración
    
    def  declaracion(self):
    
    if  self.current_token  and  self.current_token[0] == 'PALABRA_CLAVE': # Si el token actual es una palabra clave
    
    if  self.current_token[1] == 'Define': # Si la palabra clave es 'Define'
    
    self.eat('PALABRA_CLAVE') # Consume la palabra clave
    
    self.eat('IDENTIFICADOR') # Consume el identificador
    
    self.eat('ASIGNACION') # Consume el operador de asignación
    
    self.expresion() # Procesa la expresión
    
    elif  self.current_token[1] == 'Imprime': # Si la palabra clave es 'Imprime'
    
    self.eat('PALABRA_CLAVE') # Consume la palabra clave
    
    self.eat('SIMBOLOS_ESPECIALES') # (
    
    self.expresion() # Procesa la expresión
    
    self.eat('SIMBOLOS_ESPECIALES') # )
    
    # Para manejar concatenaciones después de la cadena
    
    while  self.current_token  and  self.current_token[0] == 'OPERADOR':
    
    self.eat('OPERADOR')
    
    self.expresion()
    
    elif  self.current_token[1] == 'Prueba': # Si la palabra clave es 'Prueba'
    
    self.eat('PALABRA_CLAVE') # Consume la palabra clave
    
    self.eat('SIMBOLOS_ESPECIALES') # {
    
    self.bloque() # Procesa el bloque de código
    
    self.eat('SIMBOLOS_ESPECIALES') # }
    
    if  self.current_token  and  self.current_token[1] == 'Excepcion': # Si la siguiente palabra clave es 'Excepcion'
    
    self.eat('PALABRA_CLAVE') # Consume la palabra clave
    
    self.eat('SIMBOLOS_ESPECIALES') # {
    
    self.bloque() # Procesa el bloque de código
    
    self.eat('SIMBOLOS_ESPECIALES') # }
    
    elif  self.current_token[1] == 'Excepcion': # Si la palabra clave es 'Excepcion'
    
    self.eat('PALABRA_CLAVE') # Consume la palabra clave
    
    self.eat('SIMBOLOS_ESPECIALES') # {
    
    self.bloque() # Procesa el bloque de código
    
    self.eat('SIMBOLOS_ESPECIALES') # }
    
    else:
    
    self.error(f"Palabra clave inesperada {self.current_token[1]}") # Lanza un error si la palabra clave es inesperada
    
    else:
    
    self.error("Se esperaba una palabra clave") # Lanza un error si no se encuentra una palabra clave
    
    def  bloque(self):
    
    while  self.current_token  and  self.current_token[0] in ('PALABRA_CLAVE', 'IDENTIFICADOR'): # Mientras el token actual sea una palabra clave o un identificador
    
    self.declaracion() # Procesa una declaración
    
    def  expresion(self):
    
    self.termino() # Procesa un término
    
    while  self.current_token  and  self.current_token[0] == 'OPERADOR': # Mientras el token actual sea un operador
    
    self.eat('OPERADOR') # Consume el operador
    
    self.termino() # Procesa el siguiente término
    
    def  termino(self):
    
    self.factor() # Procesa un factor
    
    while  self.current_token  and  self.current_token[0] == 'OPERADOR': # Mientras el token actual sea un operador
    
    self.eat('OPERADOR') # Consume el operador
    
    self.factor() # Procesa el siguiente factor
    
    def  factor(self):
    
    if  self.current_token  and  self.current_token[0] == 'IDENTIFICADOR': # Si el token actual es un identificador
    
    self.eat('IDENTIFICADOR') # Consume el identificador
    
    elif  self.current_token  and  self.current_token[0] == 'VALOR': # Si el token actual es un valor
    
    self.eat('VALOR') # Consume el valor
    
    elif  self.current_token  and  self.current_token[0] == 'CADENA': # Si el token actual es una cadena
    
    self.eat('CADENA') # Consume la cadena
    
    else:
    
    self.error("Se esperaba un identificador, un valor o una cadena") # Lanza un error si no se encuentra un identificador, un valor o una cadena

## Main

    from  analex  import  Entrada
    
    from  sintax  import  AnalizadorSintactico
    
      
    
    # Prueba del analizador léxico y sintáctico
    
    codigo_prueba = """~Manitas
    
    Define a = 5
    
    Define b = 7
    
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
    
    except  Exception  as  e:
    
    print(" ")
    
    print(e)
    
    print(" ")

## Explicacion de clases
-   `analex.py` contiene el código del analizador léxico.
-   `sintax.py` contiene el código del analizador sintáctico.
-   `main.py` es el archivo principal donde ejecuta el código.
- __init__.py`el archivo `__init__.py` puede estar vacío. Su presencia hace que el directorio `Tema 5` sea un paquete de Python.

## Resultado
Sin errores:

    Token actual: ('PALABRA_CLAVE', 'Define')
    Token actual: ('IDENTIFICADOR', 'a')
    Token actual: ('ASIGNACION', '=')
    Token actual: ('VALOR', '5')
    Token actual: ('PALABRA_CLAVE', 'Define')
    Token actual: ('IDENTIFICADOR', 'b')
    Token actual: ('ASIGNACION', '=')
    Token actual: ('VALOR', '7')
    Token actual: ('PALABRA_CLAVE', 'Prueba')
    Token actual: ('SIMBOLOS_ESPECIALES', '{')
    Token actual: ('PALABRA_CLAVE', 'Define')
    Token actual: ('IDENTIFICADOR', 'resultado')
    Token actual: ('ASIGNACION', '=')
    Token actual: ('IDENTIFICADOR', 'a')
    Token actual: ('OPERADOR', '+')
    Token actual: ('IDENTIFICADOR', 'b')
    Token actual: ('PALABRA_CLAVE', 'Imprime')
    Token actual: ('SIMBOLOS_ESPECIALES', '(')
    Token actual: ('CADENA', '"El resultado de la suma es: "')
    Token actual: ('SIMBOLOS_ESPECIALES', ')')
    Token actual: ('OPERADOR', '+')
    Token actual: ('IDENTIFICADOR', 'resultado')
    Token actual: ('SIMBOLOS_ESPECIALES', '}')
    Token actual: ('PALABRA_CLAVE', 'Excepcion')
    Token actual: ('SIMBOLOS_ESPECIALES', '{')
    Token actual: ('PALABRA_CLAVE', 'Imprime')
    Token actual: ('SIMBOLOS_ESPECIALES', '(')
    Token actual: ('CADENA', '"Ocurrió un error al realizar la suma"')
    Token actual: ('SIMBOLOS_ESPECIALES', ')')
    Token actual: ('SIMBOLOS_ESPECIALES', '}')
    Token actual: None
    El análisis sintáctico se completó sin errores.
Con algún error de gramática

    Token actual: ('PALABRA_CLAVE', 'Define')
    Token actual: ('IDENTIFICADOR', 'a')
    Token actual: ('ASIGNACION', '=')
    Token actual: ('VALOR', '5')
    Token actual: ('PALABRA_CLAVE', 'Define')
    Token actual: ('IDENTIFICADOR', 'b')
    Token actual: ('ASIGNACION', '=')
    Token actual: ('VALOR', '7')
    Token actual: ('IDENTIFICADOR', 'a')
    
    Error de sintaxis: Se esperaba Se esperaba una palabra clave pero se encontró ('IDENTIFICADOR', 'a'). Historia de tokens esperados: []


![Integrantes](https://github.com/PZ222/Lenguajes_y_Automatas_Manin/assets/103959963/8bd82512-3cbd-46a9-a8a5-4735d016322c)
