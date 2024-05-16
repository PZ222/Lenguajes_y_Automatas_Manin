# Tarea 4.2

1.  **Utilizar tu tabla de tokens**

| Categoría         | Tokens                                                                 |
|-------------------|------------------------------------------------------------------------|
| Palabras Clave   | Define, Imprime, Prueba, Excepcion, Entero, Caracter, Entonces, Finalmente |
| Identificadores  | a-z, A-Z                                                               |
| Asignaciones     | -, *, /, +, =                                                          |
| Valor            | 0-9                                                                    |
| Operadores       | + (suma), - (resta), * (multiplicación), / (división)                  |
| Símbolos Especiales | (, ), {, }, ;                                                          |
| Comentarios      | // (comentario de una línea), /* ... */ (comentario de varias líneas)  |
| Cadena de Texto  | ","                                                                    |

2.  **Escribir las reglas de coincidencia**: Para cada token en nuestra tabla, necesitamos escribir una regla de coincidencia que defina cómo se reconoce ese token en el texto de entrada:
    
    -   Identificadores:  `[a-zA-Z]+`
    -   Operadores:  `\+|-|\*|/`
    -   Asignaciones:  `=`
    -   Valor:  `[0-9]+`
	-   Operadores y asignaciones: `[();{}]+`
	-   Comentarios de una linea: `\/\/.*`
	-   Comentarios de varias lineas: `\/\*[\s\S]*?\*\/`
	-   Cadenas de Texto:  `\".*\"`
	
3.  **Asociar acciones a las reglas**:
	-   Identificadores: Cuando se reconoce un identificador, el objetivo es almacenarlo en una tabla de símbolos para su uso posterior.
	-   Operadores: Cuando se reconoce un operador, debemos empujarlo a una pila de operadores para su uso en la evaluación de expresiones.
	-   Asignaciones: Cuando se reconoce una asignación, debemos asociar el valor a la variable correspondiente en nuestra tabla de símbolos.
	-   Valor: Cuando se reconoce un valor, se debe convertir a su representación numérica y almacenarlo para su uso en la evaluación de expresiones.

4.  **Manejo de casos especiales**:
	-   Si el símbolo “-” aparece entre dos identificadores o valores (por ejemplo, “a - b” o “5 - 3”), entonces se trata de un operador de resta.
	-   Si el símbolo “-” aparece antes de un identificador o valor y no está precedido por otro identificador o valor (por ejemplo, “-a” o “-3”), entonces se trata de un signo de negación.
	-   Si una comilla doble es precedida por un espacio, un operador o el inicio de la línea (es decir, no está inmediatamente después de un identificador o un valor), entonces se trata del inicio de una cadena de texto.
	-   Si una comilla doble es seguida por un espacio, un operador o el final de la línea (es decir, no está inmediatamente antes de un identificador o un valor), entonces se trata del final de una cadena de texto. 
5. **Pruebas de las reglas**:
	- **Prueba de identificadores**: se puede probar con “a”, “Z”, “Manin”, “ManineS”.
    
	- **Prueba de operadores**: se puede probar con “+”, “-”, “*”, “/” o mas completo como "3+5" donde aquí ya utilizamos valores. 
    
	- **Prueba de asignaciones**: se puede probar con “=”. o mas completo como "3+5=8" donde aquí ya utilizamos valores y operadores.
    
	- **Prueba de valores**: se puede probar con “0”, “1”, “19”, “123”. 
    
	- **Prueba de cadenas de texto**: se puede probar con “"Hola, manines"”, “"Todo es real"”.

# Equipo
- Jorge Rafael Garcia Sandoval
- Juan de Dios Benitez Nava
