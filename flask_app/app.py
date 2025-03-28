from flask import Flask, request, jsonify#, abort
# from telebot.types import Update

from telebot_app.bot_instance import bot
# from telebot_app.config import WEBHOOK_ENDPOINT
from whatsapp_api.whatsapp_business_api_service import send_whatsapp_message

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


@app.route('/send_order_status_whatsapp', methods=['POST'])
def send_order_status_whatsapp():
    """
    Эндпоинт для отправки статусов в WhatsApp через WhatsApp Business API.
    Пример тела запроса:
    {
        "phone_number": "71234567890",
        "order_id": "1001",
        "status": "Новый"
    }
    """
    data = request.json
    if not data:
        return jsonify({"ok": False, "error": "No JSON data"}), 400

    phone_number = data.get("phone_number")
    order_id = data.get("order_id")
    status = data.get("status")

    if not (phone_number and order_id and status):
        return jsonify({"ok": False, "error": "Неверные поля"}), 400

    message_text = f"Заявка №{order_id} теперь в статусе: {status}"

    try:
        send_whatsapp_message(phone_number, message_text)
        return jsonify(
            {"ok": True, "message": "Сообщение отправлено в WhatsApp"}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
