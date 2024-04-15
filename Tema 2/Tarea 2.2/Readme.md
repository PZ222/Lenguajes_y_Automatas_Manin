# Nota de Practica 21/03/24

**Creación del Bot**
Se crea el Bot en la clase mediante BotFather, le pongo el nombre de @Manin_Y_Los_Manines.
Lo personalizo y le incluyo una imagen y descripción
 ![1380567945_img_2992](https://github.com/PZ222/Lenguajes_y_Automatas_Manin/assets/103959963/322c1cd6-bfbc-46dd-9834-a0cd3e9c60de)

para este punto el Bot solo responde a un hola
 
# Nota de Practica 11/04/24

**Modificación del Bot**
Ahora que comprendo mejor como son las expresiones regulares en la practica.
Tenia la idea de lo que respondería el Bot pero no sabia como implementarlo, ahora que ya se como se manejan las regex (usare **regex** para simplificar expresiones regulares) puedo implementarlo
lo primero fue prueba y error.
implementar una nueva regex que me saliera inmediatamente después de la primera respuesta del usuario
`Estuve con puro error todo el dia, pero aprendi en lo que estaba mal`

# Nota de Practica 12/04/24

**Modificación del Bot**
Ingreso las primeras dos regex que usare y que funcionaron bien, hasta cierto punto.
>expresion_regular_estado = re.compile(r"bien|mal|mas o menos|Bien|Mal|Chidote|Buenardo", re.IGNORECASE)

>expresion_regular_despedida = re.compile(r"gracias|muchas gracias|adios|chido", re.IGNORECASE)l

Funcionaban con bien, mal, mas o menos, pero con lo demás no, seguiré comprobando
**Actualización del Bot**
Quite algunas respuestas, que no me parecieron (no me gustaron)
>expresion_regular_estado = re.compile(r"bien|mal|mas o menos", re.IGNORECASE)

>expresion_regular_despedida = re.compile(r"gracias|muchas gracias|adios", re.IGNORECASE)

así ya funciona normalmente, me gusto el resultado, pero quiero seguir mejorándolo.
**nota** `No adjunto captura, por que se me olvido tomarlas, pero siempre borraba el chat con el bot entre cada nueva prueba, seria imposible ponerlas todas`
# Nota de Practica 13/04/24

**Modificación del Bot**
agrego una nueva regex, tomando en cuenta la ultima clase en la que trabajos, un correo electrónico, lo valida perfectamente **creo** 

>expresion_regular_correo = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

**nota** `No adjunto captura, por que se me olvido tomarlas, pero siempre borraba el chat con el bot entre cada nueva prueba, seria imposible ponerlas todas`

 ya quedo listo el Bot, me gusta el resultado, pero puede quedar mejor mañana, a mimir.

# Nota de Practica 14/04/24

**Modificación del Bot**
Me levante inspirado, modifique todas las respuestas, ahora es mas fácil hablar con el, le puse de mi cosecha, ahora responde mas a mi estilo.
Ya esta documentado y listo para enviar.

adjunto capturas del Bot
![WhatsApp Image 2024-04-14 at 8 18 39 PM](https://github.com/PZ222/Lenguajes_y_Automatas_Manin/assets/103959963/7d44ed9f-386c-4e87-966a-ac6b2b0aaaee)
