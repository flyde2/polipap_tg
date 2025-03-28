from flask import Flask, request, jsonify, abort
from telebot.types import Update

from telebot_app.bot_instance import bot
from telebot_app.config import WEBHOOK_ENDPOINT

app = Flask(__name__)


# @app.route(WEBHOOK_ENDPOINT, methods=['POST'])
# def webhook():
#     if request.headers.get('content-type') == 'application/json':
#         json_string = request.get_data().decode('utf-8')
#         update = Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return '', 200
#     else:
#         abort(403)

@app.route('/send_order_status', methods=['POST'])
def send_order_status():
    data = request.json
    if not data:
        return jsonify({"ok": False, "error": "No JSON data"}), 400

    chat_id = data.get("chat_id")
    order_id = data.get("order_id")
    status = data.get("status")

    if not (chat_id and order_id and status):
        return jsonify({"ok": False, "error": "Неверные поля"}), 400

    message_text = f"Заявка №{order_id} теперь в статусе: {status}"

    try:
        bot.send_message(chat_id, message_text)
        return jsonify({"ok": True, "message": "Сообщение отправлено"}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
