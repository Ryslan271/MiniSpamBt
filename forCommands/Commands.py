from pyrogram import filters
from models.DatabaseStructure import UserIDs, Messages
from models.DatabaseConnection import db_session
from auxiliaryMethods.Methods import quantity_check_users_ids, quantity_check_message
from main import app


# region Вывод всех получателей списком
@app.on_message(filters.command("Users"))
def withdraw_all_user_ids(client, message):
    if message.from_user is not None:
        session = db_session.create_session()

        user_all = session.query(UserIDs).all()

        if not quantity_check_users_ids(message):
            return

        list_user = ""

        for user in user_all:
            if user.senderId == message.chat.id:
                list_user += str(user.id) + " - " + user.ListIds + "//"

        app.send_message(client.chat.id,
                               "Вот список получателей:\n" +
                               "\n".join(list_user.split("//")))
# endregion


# region Вывод сообщений рассылки
@app.on_message(filters.command("Messages"))
def get_messages(client, message):
    session = db_session.create_session()

    new_messages = session.query(Messages).all()

    if not quantity_check_message(message):
        return

    mes_text = ""

    for mes in new_messages:
        if mes.senderId == client.chat.id:
            mes_text += str(mes.id) + " - " + mes.text + "//"

    app.send_message(message.chat.id,
                     "Вот сообщение для получателей:\n" +
                     "\n".join(mes_text.split('//')))
# endregion


