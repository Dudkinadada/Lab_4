import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests


TOKEN = '7551484776:AAEDioTRxrxHDBrWn-oaennFDr1-KTvZ_UQ'

# API-ключ TheSportsDB
API_KEY = '3'


# Функция для поиска команды
def search_team(team_name: str):
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/searchteams.php?t={team_name}"
    logging.info(f"Запрашиваем данные для команды: {team_name}")
    response = requests.get(url)

    logging.info(f"Ответ от API: {response.text}")  # Логируем ответ от API

    if response.status_code == 200:
        data = response.json()
        if data['teams']:
            team = data['teams'][0]
            team_info = f"**{team['strTeam']}**\n"
            team_info += f"Страна: {team['strCountry']}\n"
            team_info += f"Менеджер: {team.get('strManager', 'Неизвестно')}\n"
            team_info += f"Стадион: {team.get('strStadium', 'Неизвестно')}\n"
            team_info += f"Описание: {team['strDescriptionEN'][:200]}...\n"
            team_info += f"Логотип: {team['strLogo']}"
            return team_info
        else:
            return "Команда не найдена."
    else:
        logging.error(f"Ошибка при запросе: {response.status_code}")
        return "Произошла ошибка при получении данных."


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Получена команда /start от пользователя {update.message.chat_id}")
    await update.message.reply_text("Привет! Я твой футбольный бот. Напиши команду для поиска информации.")


# Обработчик команды /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Получена команда /help от пользователя {update.message.chat_id}")
    await update.message.reply_text(
        "Я футбольный бот! Используй команду /team <название_команды>, чтобы получить информацию о команде."
    )


# Обработчик команды /team
async def team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Получена команда /team от пользователя {update.message.chat_id}")
    logging.info(f"Аргументы команды: {context.args}")  # Логируем аргументы

    if context.args:
        team_name = ' '.join(context.args)  # Собираем все аргументы в строку
        logging.info(f"Ищем информацию для команды: {team_name}")
        team_info = search_team(team_name)
        logging.info(f"Информация о команде: {team_info}")
        await update.message.reply_text(team_info)
    else:
        logging.warning("Не указано название команды.")
        await update.message.reply_text(
            "Пожалуйста, укажи название команды после команды /team. Например: /team Arsenal"
        )


# Основная функция для запуска бота
def main():
    # Включаем логирование для отладки
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Создаем объект Application и передаем токен
    application = Application.builder().token(TOKEN).build()

    # Получаем диспетчер для обработки команд
    dp = application

    # Регистрация обработчиков команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))  # Обработчик для /help
    dp.add_handler(CommandHandler("team", team))  # Обработчик для /team

    # Запуск бота
    logging.info("Запуск бота...")
    application.run_polling()


if __name__ == '__main__':
    main()
