class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens  # Almacena los tokens
        self.current_token = None  # Almacena el token actual
        self.history = []  # Historial de tokens esperados
        self.next_token()  # Obtiene el primer token
    
    def next_token(self):
        self.current_token = next(self.tokens, None)  # Obtiene el siguiente token
        print(f"Token actual: {self.current_token}")  # Imprime el token actual para depuración
    
    def error(self, expected):
        """Lanza una excepción con un mensaje de error detallado."""
        message = (f"Error de sintaxis: Se esperaba {expected} "
                   f"pero se encontró {self.current_token}. "
                   f"Historia de tokens esperados: {self.history}")
        raise Exception(message)
    
    def eat(self, token_type):
        self.history.append(token_type)  # Agrega el tipo de token esperado al historial
        if self.current_token and self.current_token[0] == token_type:  # Si el token actual es del tipo esperado
            self.next_token()  # Obtiene el siguiente token
            self.history.pop()  # Elimina el último token esperado del historial
        else:  # Si el token actual no es del tipo esperado
            self.error(f"Se esperaba {token_type} pero se encontró {self.current_token}")  # Lanza un error
    
    def programa(self):
        while self.current_token is not None:  # Mientras haya tokens
            self.declaracion()  # Procesa una declaración
    
    def declaracion(self):
        if self.current_token and self.current_token[0] == 'PALABRA_CLAVE':  # Si el token actual es una palabra clave
            if self.current_token[1] == 'Define':  # Si la palabra clave es 'Define'
                self.eat('PALABRA_CLAVE')  # Consume la palabra clave
                self.eat('IDENTIFICADOR')  # Consume el identificador
                self.eat('ASIGNACION')  # Consume el operador de asignación
                self.expresion()  # Procesa la expresión
            elif self.current_token[1] == 'Imprime':  # Si la palabra clave es 'Imprime'
                self.eat('PALABRA_CLAVE')  # Consume la palabra clave
                self.eat('SIMBOLOS_ESPECIALES')  # (
                self.expresion()  # Procesa la expresión
                self.eat('SIMBOLOS_ESPECIALES')  # )
                # Para manejar concatenaciones después de la cadena
                while self.current_token and self.current_token[0] == 'OPERADOR':
                    self.eat('OPERADOR')
                    self.expresion()
            elif self.current_token[1] == 'Prueba':  # Si la palabra clave es 'Prueba'
                self.eat('PALABRA_CLAVE')  # Consume la palabra clave
                self.eat('SIMBOLOS_ESPECIALES')  # {
                self.bloque()  # Procesa el bloque de código
                self.eat('SIMBOLOS_ESPECIALES')  # }
                if self.current_token and self.current_token[1] == 'Excepcion':  # Si la siguiente palabra clave es 'Excepcion'
                    self.eat('PALABRA_CLAVE')  # Consume la palabra clave
                    self.eat('SIMBOLOS_ESPECIALES')  # {
                    self.bloque()  # Procesa el bloque de código
                    self.eat('SIMBOLOS_ESPECIALES')  # }
            elif self.current_token[1] == 'Excepcion':  # Si la palabra clave es 'Excepcion'
                self.eat('PALABRA_CLAVE')  # Consume la palabra clave
                self.eat('SIMBOLOS_ESPECIALES')  # {
                self.bloque()  # Procesa el bloque de código
                self.eat('SIMBOLOS_ESPECIALES')  # }
            else:
                self.error(f"Palabra clave inesperada {self.current_token[1]}")  # Lanza un error si la palabra clave es inesperada
        else:
            self.error("Se esperaba una palabra clave")  # Lanza un error si no se encuentra una palabra clave
    
    def bloque(self):
        while self.current_token and self.current_token[0] in ('PALABRA_CLAVE', 'IDENTIFICADOR'):  # Mientras el token actual sea una palabra clave o un identificador
            self.declaracion()  # Procesa una declaración
    
    def expresion(self):
        self.termino()  # Procesa un término
        while self.current_token and self.current_token[0] == 'OPERADOR':  # Mientras el token actual sea un operador
            self.eat('OPERADOR')  # Consume el operador
            self.termino()  # Procesa el siguiente término
    
    def termino(self):
        self.factor()  # Procesa un factor
        while self.current_token and self.current_token[0] == 'OPERADOR':  # Mientras el token actual sea un operador
            self.eat('OPERADOR')  # Consume el operador
            self.factor()  # Procesa el siguiente factor
    
    def factor(self):
        if self.current_token and self.current_token[0] == 'IDENTIFICADOR':  # Si el token actual es un identificador
            self.eat('IDENTIFICADOR')  # Consume el identificador
        elif self.current_token and self.current_token[0] == 'VALOR':  # Si el token actual es un valor
            self.eat('VALOR')  # Consume el valor
        elif self.current_token and self.current_token[0] == 'CADENA':  # Si el token actual es una cadena
            self.eat('CADENA')  # Consume la cadena
        else:
            self.error("Se esperaba un identificador, un valor o una cadena")  # Lanza un error si no se encuentra un identificador, un valor o una cadena
