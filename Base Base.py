# Bot Base
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Envia a mensagem inicial
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, Em Que Posso Te Ajudar ?")

    # Envia a mensagem "Serviços Disponíveis" com as opções de inline keyboard
    keyboard = [
        [InlineKeyboardButton("Formatação", callback_data='formatacao')],
        [InlineKeyboardButton("Limpeza", callback_data='limpeza')],
        [InlineKeyboardButton("SSDS", callback_data='ssds')],
        [InlineKeyboardButton("HDS", callback_data='hds')],
        [InlineKeyboardButton(
            "Placas De Video", callback_data='placas_de_video')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Serviços Disponíveis:", reply_markup=reply_markup)

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
