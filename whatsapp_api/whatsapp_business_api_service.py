import os
import requests


WHATSAPP_BUSINESS_PHONE_NUMBER_ID = os.getenv(
    "WHATSAPP_BUSINESS_PHONE_NUMBER_ID", "-")
WHATSAPP_BUSINESS_ACCESS_TOKEN = os.getenv("WHATSAPP_BUSINESS_ACCESS_TOKEN",
                                           "-")

def send_whatsapp_message(to_number: str, message_text: str):
    """
    Отправляет WhatsApp-сообщение с помощью WhatsApp Business API.
    :param to_number: Номер получателя (в формате "799988877966" без +)
    :param message_text: текст сообщения
    """

    url = f"https://graph.facebook.com/v17.0/{WHATSAPP_BUSINESS_PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_BUSINESS_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {
            "body": message_text
        }
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()