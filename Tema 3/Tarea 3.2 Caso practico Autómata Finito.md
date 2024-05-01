# Tarea 3.2
## Caso practico Autómata Finito
### ¿Que es un Automata Finito?
Un autómata finito es un modelo matemático que se utiliza para representar sistemas de control o procesos que siguen una serie de reglas predefinidas.
Está compuesto por un conjunto finito de estados, un alfabeto de entrada, una función de transición y un estado inicial y uno o varios estados de aceptación.

El funcionamiento de un autómata finito se basa en su capacidad para leer una cadena de símbolos de entrada y cambiar de estado de acuerdo con la función de transición.
La función de transición es una tabla que especifica para cada estado y cada símbolo de entrada, el estado al que se debe mover el autómata.

![EuhnpaPXIAAHc_n-removebg-preview](https://github.com/PZ222/Lenguajes_y_Automatas_Manin/assets/103959963/5d7ddacb-8111-499f-9c18-787b190fa10d)

### Caso de Uso
En mi caso de uso usare un ejemplo con el cual tengo mas de 5 años de relacion y es con el juego “Age of Mythology”, pero **¿Que es?** “Age of Mythology” es un videojuego de estrategia en tiempo real desarrollado por Ensemble Studios y publicado por Microsoft Games en 2002
Este juego es una variante de la serie “Age of Empires”, pero en lugar de centrarse en la historia, se enfoca en la mitología y leyendas de las culturas egipcias, griegas y nórdicas.

Bien ahora como entran los autómatas finitos aquí, bueno los autómatas finitos se pueden ver en acción en la forma de una unidad mítica llamada Autómata, esta unidad tiene varias cosas que tenemos que puntuar.
- Los autómatas tienen la habilidad especial de reparar (curar) otros Autómatas, a un ratio de 15 PR/segundo.
- Cuando un Autómata es derrotado, no muere, pero se rompe, dejando sus restos en el suelo con 1 PR.
- Puede ser reparado por otros Autómatas hasta que alcance todos sus PR, y volverá a poder luchar otra vez.
- Cuando un autómata se deja roto durante 36 segundos, sus restos desaparecen para siempre.

![imagen_2024-05-01_171142936-removebg-preview](https://github.com/PZ222/Lenguajes_y_Automatas_Manin/assets/103959963/85492d13-9eac-4aa1-b8e3-18ba9cd3c0f4)

Ahora poniendo esto mas como un ejemplo de un autómata finito en el que los estados podrían ser “funcionando”, “roto” y “desaparecido”. La función de transición se basa en eventos como “ser atacado”, “ser reparado” y “ser ignorado”. Por ejemplo, si un Autómata en el estado “funcionando” es atacado y derrotado, cambia al estado “roto”. Si otro Autómata lo repara, vuelve al estado “funcionando”. Si se ignora durante 36 segundos, cambia al estado “desaparecido”.

Esto se puede ver con todas las unidades dentro del juego, pero elegi esta por el nombre y por el concepto de automata que tenia al inicio de la materia

![imagen_2024-05-01_171343871](https://github.com/PZ222/Lenguajes_y_Automatas_Manin/assets/103959963/ff05c902-317f-4838-9611-08ec029793c7)

**Jorge Rafael Garcia Sandoval 21200601**
