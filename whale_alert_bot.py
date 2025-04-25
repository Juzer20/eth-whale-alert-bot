
import json
import requests
import websocket
import threading
import os
from flask import Flask

# ======= CONFIG =======
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_USER_ID = os.environ.get("TELEGRAM_USER_ID")
ETH_THRESHOLD = float(os.environ.get("ETH_THRESHOLD", 1000))

# ======= TELEGRAM ALERT =======
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_USER_ID, "text": message}
    requests.post(url, data=payload)

# ======= WEBSOCKET CALLBACK =======
def on_message(ws, message):
    data = json.loads(message)
    price = float(data['p'])
    quantity = float(data['q'])
    is_sell = data['m']

    if quantity >= ETH_THRESHOLD:
        direction = "SELL 🟥" if is_sell else "BUY 🟩"
        total = price * quantity
        alert_msg = (
            f"🚨 Whale Trade Detected!\n\n"
            f"📊 Direction: {direction}\n"
            f"💰 Amount: {quantity:.2f} ETH\n"
            f"💵 Value: ${total:,.2f}\n"
            f"📈 Price: ${price:,.2f}"
        )
        send_telegram_alert(alert_msg)

def on_error(ws, error):
    print("WebSocket Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket Closed")

def on_open(ws):
    print("WebSocket Connected")

def run_ws():
    url = "wss://stream.binance.com:9443/ws/ethusdt@trade"
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

# ======= FLASK APP FOR RENDER =======
app = Flask(__name__)

@app.route('/')
def home():
    return "Whale Alert Bot is running!"

if __name__ == "__main__":
    threading.Thread(target=run_ws).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
