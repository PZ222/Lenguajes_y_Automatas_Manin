# Importa las bibliotecas necesarias
import logging
import re
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Configura el registro para facilitar la depuración
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Define las expresiones regulares para detectar ciertos mensajes
expresion_regular_hola = re.compile(r"hi|hola", re.IGNORECASE)  # Detecta saludos
expresion_regular_estado = re.compile(r"Bien|Mal|Mas o menos", re.IGNORECASE)  # Detecta respuestas a "¿Cómo estás?"
expresion_regular_gracias = re.compile(r"gracias|muchas gracias", re.IGNORECASE)  # Detecta gracias
expresion_regular_despedida = re.compile(r"adios", re.IGNORECASE)  # Detecta despedidas
expresion_regular_correo = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")  # Detecta correos electrónicos

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje cuando se emite el comando /start."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje cuando se emite el comando /help."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Hace eco del mensaje del usuario si coincide con la expresión regular."""
    message_text = update.message.text
    if expresion_regular_hola.search(message_text):  # Si el usuario saluda
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif expresion_regular_estado.search(message_text):  # Si el usuario responde a "¿Cómo estás?"
        if "Bien" in message_text:
            await update.message.reply_text("¡Que bueno me alegro que de todo vaya muy bien por ti!")
        elif "Mal" in message_text:
            await update.message.reply_text("¡Que mal, espero que pronto te logres recuperar, recuerda que la vida se conforma de picos de felicidad y tristeza!")
        elif "Mas o menos" in message_text:
            await update.message.reply_text("Manin no entiende, decide si bien o mal, pq asi no te puedo aconsejar :(")
    elif expresion_regular_gracias.search(message_text):  # Si el usuario da las gracias
        await update.message.reply_text("De nada chamito, por cierto ¿Podrías proporcionarme tu correo para afiliarte al partido politico de Manin?")
    elif expresion_regular_correo.search(message_text):  # Si el usuario proporciona un correo electrónico
        await update.message.reply_text("¡Muchas gracias chams! El equipo de logistica de Manin ha recibido tu correo electrónico.")
    elif expresion_regular_despedida.search(message_text):
        await update.message.reply_text("¡Espero que todo vaya bien para ti! Te deseo lo mejor chams.")
    else:  # Si el bot no entiende el mensaje
        await update.message.reply_text("No entendí tu mensaje.")

def main() -> None:
    """Inicia el bot."""
    application = Application.builder().token("7050419479:AAG1f9unmqNwaoz1S2xQCfi0MjEZhRNraho").build()

    # Agrega los manejadores de comandos y mensajes
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia la encuesta de actualizaciones
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Ejecuta el bot si este archivo se ejecuta como un script
if __name__ == "__main__":
    main()
