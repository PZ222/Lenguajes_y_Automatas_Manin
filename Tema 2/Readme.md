# Nota de Clase 15/03/24

**Orden de precedencia**

-   Cerradura Kleene
-   Concatenación
-   Unión.

## Ejemplo
w= a^*b U c

## Cerradura Kleene

| w= a^* |ε 					|	aa									  |	aaa									 |	aaaa|
|----|----|----|-----|----|

## Concatenación 

| w= a^*b | {b, ab, aab, aaab, …} |
|----|----|
## Unión

| w= a^*b U c | {b, c, ab, aab, aaab, …}
|-----|------|
## Ejemplo 2
Z={0,1}

Z={0,1,00,11,010,0101,1100}

Una expresión regular que incluya dos ceros

L=1^*0 1^* 0 1^*

Expresión Regular = Sufijo 110

L=(0 U 1)^* 110

> **Nota:** Otros ejemplos están en libreta.
