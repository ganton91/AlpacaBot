#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.notifier import send_telegram

result = send_telegram("👋 <b>AlpacaBot test message</b>\n\nTelegram notifications are working correctly!")
print("✅ Sent successfully" if result else "❌ Failed — check TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID")
