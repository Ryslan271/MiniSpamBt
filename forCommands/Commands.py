from models.DatabaseStructure import UserIDs, Messages
from models.DatabaseConnection import db_session
from auxiliaryMethods.Methods import quantity_check_users_ids, quantity_check_message


# region Команда для начала сообщений
def handle_message(client, message, app):
    if message.from_user is not None:
        app.send_message(message.chat.id,
                         "Привет, напомню свои команды:\n"
                         "/Users\n"
                         "/Message\n")
# endregion


# region Вывод всех получателей списком
def withdraw_all_user_ids(client, message, app):
    if message.from_user is not None:
        session = db_session.create_session()

        user_all = session.query(UserIDs).all()

        if not quantity_check_users_ids(message, app):
            return

        list_user = ""

        for user in user_all:
            if user.senderId == message.chat.id:
                list_user += str(user.id) + " - " + user.ListIds + "//"

        app.send_message(message.chat.id,
                         "Вот список получателей:\n" +
                         "\n".join(list_user.split("//")))
# endregion


# region Вывод сообщений рассылки
def get_messages(client, message, app):
    session = db_session.create_session()

    new_messages = session.query(Messages).all()

    if not quantity_check_message(message, app  ):
        return

    mes_text = ""

    for mes in new_messages:
        if mes.senderId == message.chat.id:
            mes_text += str(mes.id) + " - " + mes.text + "//"

    app.send_message(message.chat.id,
                     "Вот сообщение для получателей:\n" +
                     "\n".join(mes_text.split('//')))
# endregion