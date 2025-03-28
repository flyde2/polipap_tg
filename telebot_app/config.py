import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "https://example.com")
WEBHOOK_ENDPOINT = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_ENDPOINT}"