from pyrogram import Client, filters
from userData.Data import api_id, api_hash

app = Client("my_account", api_id, api_hash)  # Подключение к клиенту


@app.on_message(filters.command("start"))
def handle_message(client, message):
    if message.from_user is not None:
        app.send_message(message.chat.id,
                         "Привет, напоню свои команды:\n"
                         "/Users\n"
                         "/Сообщения\n")


@app.on_message(filters.command("type", prefixes='!') & filters.me)
def handle_message(client, message):
    if message.from_user is not None:
        app.send_message(message.chat.id,
                         "Привет, напоню свои команды:\n"
                         "/Users\n"
                         "/Сообщения\n")


app.run()
