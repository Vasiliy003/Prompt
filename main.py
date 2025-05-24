from pyrogram import Client, filters

api_id = 25598825  # замените на свой api_id
api_hash = "90c582eb762a278430d8e7785f165cdc"  # замените на свой api_hash
bot_token = "8127107082:AAFfWLCYLgtjKaWmLuoCBjqi1nl_g4V4zJU"  # замените на свой токен бота

app = Client("simple_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text)
def reply_a(client, message):
    message.reply_text("а")

app.run()