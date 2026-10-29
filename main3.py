from Tele_bot import TOKEN
import telebot
from random import choice
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    result = choice(["🦅 ОРЕЛ", "🪙 РЕШКА"])
    text = f"Ты бросил монетку: {result}"

    # Создаём клавиатуру с одной кнопкой
    markup = types.InlineKeyboardMarkup()
    btn_retry = types.InlineKeyboardButton("🔁 Бросить ещё", callback_data='throw_coin')
    markup.add(btn_retry)

    bot.reply_to(message, text, reply_markup=markup)

# Обработчик нажатия на кнопку
@bot.callback_query_handler(func=lambda call: call.data == 'throw_coin')
def retry_coin(call):
    result = choice(["🦅 ОРЕЛ", "🪙 РЕШКА"])
    text = f"Ты снова бросил монетку: {result}"

    # Обновляем только текст сообщения (кнопки остаются)
    bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)

    # Обязательно отвечаем на callback, чтобы убрать «часики» загрузки у кнопки
    bot.answer_callback_query(call.id)

print("Бот запущен...")
bot.polling(none_stop=True, interval=0)