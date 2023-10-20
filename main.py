from pyrogram import Client, filters
from userData.Data import api_id, api_hash
from forCommands.Commands import get_messages, handle_message, withdraw_all_user_ids
from auxiliaryMethods.EditingDataInDatabase import text_set_users_ids, text_delete_users_id,\
                                                   text_sending_message, text_set_message
from forCommands.InformativeCommands import get_help


app = Client("my_account", api_id, api_hash)  # Подключение к клиенту


# region Команда для начала сообщений
@app.on_message(filters.command("start"))
def call_handle_message(client, message):
    handle_message(client, message, app)
# endregion


# region Вывод всех получателей списком
@app.on_message(filters.command("users"))
def call_withdraw_all_user_ids(client, message):
    withdraw_all_user_ids(client, message, app)
# endregion


# region Вывод сообщений рассылки
@app.on_message(filters.command("messages"))
def call_get_messages(client, message):
    get_messages(client, message, app)
# endregion


# region Команда добавления нового получателя
@app.on_message(filters.command("adduser", prefixes='!') & filters.me)
def cell_text_set_users_ids(client, message):
    text_set_users_ids(message, app)
# endregion


# region Команда для удаления сообщения из бд
@app.on_message(filters.command("deletemessage", prefixes='!') & filters.me)
def cell_text_delete_users_id(client, message):
    text_delete_users_id(message, app)
# endregion


# region Команда для отправки сообщений
@app.on_message(filters.command("send", prefixes='!') & filters.me)
def cell_text_sending_message(client, message):
    text_sending_message(message, app)
# endregion


# region Команда для создания нового сообщения из бд
@app.on_message(filters.command("newmessage", prefixes='!') & filters.me)
def cell_text_set_message(client, message):
    text_set_message(message, app)
# endregion


# region Команда для вызова помощи
@app.on_message(filters.command("help", prefixes='!') & filters.me)
def cell_get_help(message, app):
    get_help(message, app)
# endregion


app.run()
