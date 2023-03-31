import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = 6181819295:AAFmN9IenOLnnxI25-eixIgTBgdW9qP20OA 'YOUR_TOKEN_HERE'
CHAT_ID = 634743800 'YOUR_CHAT_ID_HERE'

bot = telegram.Bot(token=TOKEN)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для обратной связи. Отправьте мне свой вопрос или сообщение.")

def forward_message(update, context):
    text = update.message.text
    bot.send_message(chat_id=CHAT_ID, text=f'Сообщение от {update.message.from_user.username}: {text}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()





