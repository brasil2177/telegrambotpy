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
    response = ""

    if choice == 'formatacao':
        # resposta para a opção de formatação
        response = "Formatação: [Texto da formatação aqui]"
    elif choice == 'limpeza':
        # resposta para a opção de limpeza
        response = "Limpeza: [Texto da limpeza aqui]"
    elif choice == 'ssds':
        # resposta para a opção de SSDS
        response = "SSDS: \n\n"\
                   "SSD SATA: Utiliza a interface SATA, comumente encontrado em laptops e desktops. Valor: R$319\n\n"\
                   "SSD PCIe/NVMe: Utiliza a interface PCIe, oferecendo velocidades de transferência de dados mais rápidas em comparação com o SATA. É comum em sistemas mais avançados. Valor: R$300\n\n"\
                   "M.2 SSD: Um formato compacto que utiliza a interface SATA ou PCIe/NVMe. Muito utilizado em laptops e placas-mãe modernas. Valor: R$330\n\n"\
                   "SAS SSD: Projetado para ambientes corporativos e servidores, utiliza a interface SAS (Serial Attached SCSI). Valor: R$7.445"

        # Adiciona inlines para cada tipo de SSD
        keyboard = [
            [InlineKeyboardButton("SSD SATA", callback_data='ssd_sata')],
            [InlineKeyboardButton(
                "SSD PCIe/NVMe", callback_data='ssd_pcie_nvme')],
            [InlineKeyboardButton("M.2 SSD", callback_data='m2_ssd')],
            [InlineKeyboardButton("SAS SSD", callback_data='sas_ssd')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=query.message.chat_id, text="Escolha um tipo de SSD:", reply_markup=reply_markup)

    elif choice == 'hds':
        # resposta para a opção de HDS
        response = "HDS: \n\n"\
                   "HDD SATA: Utiliza a interface SATA, sendo uma opção mais comum em sistemas mais antigos ou de armazenamento em massa. Valor: R$270\n\n"\
                   "HDD SAS: Projetado para ambientes empresariais, utiliza a interface SAS e oferece maior confiabilidade e desempenho do que os HDDs SATA convencionais. Valor: R$5.771\n\n"\
                   "HDD SSHD (Solid State Hybrid Drive): Combina tecnologia de HDD com uma pequena quantidade de armazenamento SSD para melhorar o desempenho geral, armazenando dados frequentemente acessados no SSD. Valor: R$315\n\n"\
                   "HDD de 2,5 polegadas e 3,5 polegadas: Refere-se ao tamanho físico do disco rígido. HDDs de 2,5 polegadas são comuns em laptops, enquanto HDDs de 3,5 polegadas são mais utilizados em desktops. Valor: R$580/280"

        # Adiciona inlines para cada tipo de HD
        keyboard = [
            [InlineKeyboardButton("HDD SATA", callback_data='hdd_sata')],
            [InlineKeyboardButton("HDD SAS", callback_data='hdd_sas')],
            [InlineKeyboardButton("HDD SSHD", callback_data='hdd_sshd')],
            [InlineKeyboardButton("HDD 2,5 polegadas",
                                  callback_data='hdd_2_5')],
            [InlineKeyboardButton("HDD 3,5 polegadas",
                                  callback_data='hdd_3_5')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=query.message.chat_id, text="Escolha um tipo de HD:", reply_markup=reply_markup)

    elif choice == 'ssd_sata':
        # respostas para a escolha de cada tipo de SSD ou HD
        response = "Você selecionou SSD SATA De 1TB. O valor é de R$319. Aqui está a chave PIX para você realizar o pagamento: [12345678910]"

    elif choice == 'ssd_pcie_nvme':
        response = "Você selecionou SSD PCIe/NVMe De 1TB. O valor é de R$300. Aqui está a chave PIX para você realizar o pagamento: [12345678910] "

    elif choice == 'm2_ssd':
        response = "Você selecionou M.2 SSD De 1TB. O valor é de R$330. Aqui está a chave PIX para você realizar o pagamento: [12345678910]"

    elif choice == 'sas_ssd':
        response = "Você selecionou SAS SSD De 4TB. O valor é de R$7.445. Aqui está a chave PIX para você realizar o pagamento: [12345678910] "

    elif choice == 'hdd_sata':
        response = "Você selecionou HDD SATA De 1TB. O valor é de R$270. Aqui está a chave PIX para você realizar o pagamento: [12345678910]"

    elif choice == 'hdd_sas':
        response = "Você selecionou HDD SAS De 18TB. O valor é de R$5.771. Aqui está a chave PIX para você realizar o pagamento: [12345678910]"

    elif choice == 'hdd_sshd':
        response = "Você selecionou HDD SSHD De 2TB. O valor é de R$315. Aqui está a chave PIX para você realizar o pagamento: [12345678910]"

    elif choice == 'hdd_2_5':
        response = "Você selecionou HDD_2_5 De 2TB. O valor é de R$580. Aqui está a chave PIX para você realizar o pagamento: [12345678910]"

    elif choice == 'hdd_3_5':
        response = "Você selecionou HDD_3_5 De 1TB. O valor é de R$280. Aqui está a chave PIX para você realizar o pagamento: [12345678910]"

    await context.bot.send_message(chat_id=query.message.chat_id, text=response)

if __name__ == '__main__':
    application = ApplicationBuilder().token(
        'TOKEN AQUI').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # manipulador para controlar as respostas das inlines
    application.add_handler(CallbackQueryHandler(handle_choice))

    application.run_polling()
