
# ETH Whale Alert Bot 🐋

यह बॉट Binance पर ETH/USDT ट्रेड्स को मॉनिटर करता है और यदि कोई बड़ा ट्रेड (उदा. 1000 ETH+) होता है, तो आपको Telegram पर अलर्ट भेजता है।

## 🛠 आवश्यकताएँ

1. एक टेलीग्राम बॉट (BotFather से बनाएँ)
2. आपकी Telegram User ID ([@userinfobot](https://t.me/userinfobot) से प्राप्त करें)
3. GitHub और Render खाता

## 🚀 Render पर डिप्लॉय कैसे करें?

1. [Render.com](https://render.com/) पर एक फ्री अकाउंट बनाएँ
2. एक नई Web Service बनाएँ
3. GitHub से इस प्रोजेक्ट को कनेक्ट करें
4. Environment Variables सेट करें:

   ```
   TELEGRAM_BOT_TOKEN=आपका बॉट टोकन
   TELEGRAM_USER_ID=आपका टेलीग्राम यूजर आईडी
   ETH_THRESHOLD=1000
   ```

5. **Start Command**: `python whale_alert_bot.py`

## ✅ अलर्ट उदाहरण:

```
🚨 Whale Trade Detected!

📊 Direction: BUY 🟩
💰 Amount: 1123.45 ETH
💵 Value: $3,780,123.00
📈 Price: $3363.00
```
