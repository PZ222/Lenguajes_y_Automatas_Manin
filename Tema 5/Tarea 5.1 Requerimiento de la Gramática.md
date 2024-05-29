# Tarea 5.1 Requerimiento de la Gramática



1.  **Introducción**
    
   Estamos analizando un subconjunto del lenguaje de programación (Llamado "Lenguaje de los Manines") que incluye operaciones aritméticas básicas, asignaciones de variables, declaraciones condicionales y funciones. El propósito del analizador sintáctico es verificar la corrección sintáctica del código fuente y generar una representación intermedia que se puede utilizar para la compilación o interpretación posterior.
    
2.  **Símbolos Terminales**
    
    Los símbolos terminales de este subconjunto del lenguaje incluyen:
    
    -   Palabras clave:  `Define`,  `Imprime`,  `Prueba`,  `Excepcion`,  `Entero`,  `Caracter`,  `Entonces`,  `Finalmente`
    -   Identificadores: a-z, A-Z
    -   Asignaciones:  `-`,  `*`,  `/`,  `+`,  `=`
    -   Valor: 0-9
    -   Operadores:  `+`  (suma),  `-`  (resta),  `*`  (multiplicación),  `/`  (división)
    -   Símbolos Especiales:  `(`,  `)`,  `{`,  `}`,  `;`
    -   Comentarios:  `//`  (comentario de una línea),  `/* ... */`  (comentario de varias líneas)
    -   Cadena de Texto:  `","`
3.  **Símbolos No Terminales**
    
    Los símbolos no terminales que representan categorías o estructuras sintácticas en este subconjunto del lenguaje incluyen:
    
    -   `P`  (Programa)
    -   `D`  (Declaración)
    -   `E`  (Expresión)
    -   `T`  (Término)
    -   `F`  (Factor)
4.  **Producciones y Reglas**
    
    Las producciones que describen cómo los símbolos no terminales se descomponen en otros no terminales y terminales son:
    
    ```
    P -> D P | ε
    D -> id = E ;
    E -> E + T | E - T | T
    T -> T * F | T / F | F
    F -> ( E ) | id | num
    ```
    
5.  **Símbolo Inicial**
    
    El símbolo inicial de la gramática es  `P`  (Programa).
    
6.  **Precedencia y Asociatividad**
    
    Las reglas de precedencia y asociatividad para los operadores en este subconjunto del lenguaje son:
    
    -   Operadores multiplicativos (`*`,  `/`): mayor precedencia, asociatividad izquierda.
    -   Operadores aditivos (`+`,  `-`): menor precedencia, asociatividad izquierda.
    -   Operadores de asignación (`=`): menor precedencia, asociatividad derecha.

7.  **Comentarios y Anotaciones**
    No le entendimos c:

![Integrantes](https://github.com/PZ222/Lenguajes_y_Automatas_Manin/assets/103959963/367b85dd-5b68-4ce0-836f-a7156f4b845a)

