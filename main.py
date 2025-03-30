from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Токен бота (замени на свой)
TOKEN = "7551484776:AAEDioTRxrxHDBrWn-oaennFDr1-KTvZ_UQ"

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Я бот спортивных событий 🏆")

# Ответ на неизвестные сообщения
async def unknown(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Извините, я не понимаю эту команду 🤷‍♂️")

def main():
    app = Application.builder().token(TOKEN).build()

    # Обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
