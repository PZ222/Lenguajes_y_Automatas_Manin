import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresiones regulares para detectar mensajes
expresion_regular_hola = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
expresion_regular_estado = re.compile(r"bien|mal|mas o menos|Bien|Mal|Chidote|Buenardo", re.IGNORECASE)
expresion_regular_despedida = re.compile(r"gracias|muchas gracias|adios|chido", re.IGNORECASE)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    message_text = update.message.text
    if expresion_regular_hola.search(message_text):
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif expresion_regular_estado.search(message_text):
        if "bien" in message_text:
            await update.message.reply_text("¡Que bueno me alegro que de todo vaya muy bien por ti!")
        elif "mal" in message_text:
            await update.message.reply_text("¡Que mal, espero que pronto te logres recuperar, recuerda que la vida se conforma de picos de felicidad y tristeza!")
        elif "mas o menos" in message_text:
            await update.message.reply_text("Manin no entiende, decide si bien o mal, pq asi no te puedo aconsejar :(")
    elif expresion_regular_despedida.search(message_text):
        await update.message.reply_text("¡Espero que todo vaya bien para ti! Te deseo lo mejor chams")
    else:
        await update.message.reply_text("No entendí tu mensaje.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7050419479:AAG1f9unmqNwaoz1S2xQCfi0MjEZhRNraho").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
