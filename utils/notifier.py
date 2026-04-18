import os
import requests


def send_telegram(message: str) -> bool:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
    }

    try:
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        return True
    except Exception:
        return False


def notify_success(report: str) -> None:
    send_telegram(f"✅ <b>AlpacaBot ran successfully</b>\n\n{report}")


def notify_failure(error: str) -> None:
    send_telegram(f"🚨 <b>AlpacaBot FAILED</b>\n\n{error}")
