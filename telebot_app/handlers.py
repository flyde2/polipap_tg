import telebot


def register_handlers(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def start_cmd(message):
        bot.send_message(
            message.chat.id,
            "Привет! Я бот, который уведомляет о новом статусы заказа."
        )
