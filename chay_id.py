import os
import requests

TELEGRAM_BOT_TOKEN = "Tu_token_de_aplicacion_aqui"  # Reemplaza con tu token real

# Obtiene las actualizaciones recientes del bot
response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates")
data = response.json()

if "result" in data and len(data["result"]) > 0:
    chat_id = data["result"][0]["message"]["chat"]["id"]
    print(f"Tu Chat ID es: {chat_id}")
else:
    print("No se encontraron mensajes recientes. Envía un mensaje al bot y vuelve a ejecutar el script.")
