import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

# Вставь свой Telegram Bot API токен
TOKEN = '7551484776:AAEDioTRxrxHDBrWn-oaennFDr1-KTvZ_UQ'

# API-ключ TheSportsDB
API_KEY = '3'


# Функция для поиска команды
def search_team(team_name: str):
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/searchteams.php?t={team_name}"
    response = requests.get(url)
    data = response.json()

    if data['teams']:
        team = data['teams'][0]
        team_info = f"**{team['strTeam']}**\n"
        team_info += f"Страна: {team['strCountry']}\n"
        team_info += f"Менеджер: {team['strManager']}\n"
        team_info += f"Стадион: {team['strStadium']}\n"
        team_info += f"Описание: {team['strDescriptionEN'][:200]}...\n"
        team_info += f"Логотип: {team['strLogo']}"
        return team_info
    else:
        return "Команда не найдена."


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой футбольный бот. Напиши команду для поиска информации.")


# Обработчик команды /team
async def team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        team_name = ' '.join(context.args)
        team_info = search_team(team_name)
        await update.message.reply_text(team_info)
    else:
        await update.message.reply_text(
            "Пожалуйста, укажи название команды после команды /team. Например: /team Arsenal")


# Основная функция для запуска бота
def main():
    # Включаем логирование для отладки
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Создаем объект Application и передаем токен
    application = Application.builder().token(TOKEN).build()

    # Получаем диспетчер для обработки команд
    dp = application.dispatcher

    # Обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("team", team))

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main
