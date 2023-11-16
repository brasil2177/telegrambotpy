# Bot 1.1
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # resposta após o start
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, Em Que Posso Te Ajudar ?")

    # Envia a mensagem "Serviços Disponíveis" com as opções seguintes:
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


async def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    choice = query.data

    if choice == 'formatacao':
        # resposta para a opção formatação
        response = "Formatação: [Texto da formatação aqui]"
    elif choice == 'limpeza':
        # resposta para a opção limpeza
        response = "Limpeza: [Texto da limpeza aqui]"
    elif choice == 'ssds':
        # resposta para a opção de SSDS
        response = "SSDS: \n\n"\
                   "SSD SATA: Utiliza a interface SATA, comumente encontrado em laptops e desktops.\n"\
                   "SSD PCIe/NVMe: Utiliza a interface PCIe, oferecendo velocidades de transferência de dados mais rápidas em comparação com o SATA. É comum em sistemas mais avançados.\n"\
                   "M.2 SSD: Um formato compacto que utiliza a interface SATA ou PCIe/NVMe. Muito utilizado em laptops e placas-mãe modernas.\n"\
                   "SAS SSD: Projetado para ambientes corporativos e servidores, utiliza a interface SAS (Serial Attached SCSI)."

    # caso queira adicionar mais opções, de um espaço aqui e inicie mais blocos de comando

    await context.bot.send_message(chat_id=query.message.chat_id, text=response)

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # manipulador para controlar as respostas das inlines
    application.add_handler(CallbackQueryHandler(handle_choice))

    application.run_polling()
