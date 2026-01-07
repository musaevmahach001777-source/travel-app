import os
import telebot
from telebot import types

# Render сам подставит токен из настроек (Environment Variables), которые мы укажем позже
token = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру с большой кнопкой
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Твоя ссылка на приложение (GitHub Pages)
    # Убедись, что ссылка именно такая, как ты настраивал в GitHub Settings -> Pages
    web_app_url = "https://musaevmahach001777-source.github.io/travel-app/"
    
    web_app = types.WebAppInfo(web_app_url)
    item = types.KeyboardButton("🚀 Открыть путеводитель", web_app=web_app)
    markup.add(item)

    # Приветственное сообщение
    bot.send_message(
        message.chat.id, 
        f"Привет, {message.from_user.first_name}! 🌍\n\nЯ помогу тебе найти лучшие места в новой стране. Нажми на кнопку ниже, чтобы открыть приложение.", 
        reply_markup=markup
    )

print("Бот запущен и ожидает сообщений...")
bot.infinity_polling()
