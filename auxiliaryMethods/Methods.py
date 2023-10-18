from models.DatabaseConnection import db_session
from models.DatabaseStructure import UserIDs, Messages
from main import app


def quantity_check_users_ids(message):
    session = db_session.create_session()
    user_all = session.query(UserIDs).all()

    list_user = 0

    for user_id in user_all:
        if user_id.senderId == message.chat.id:
            list_user += 1

    if list_user <= 0:
        app.send_message(message.chat.id,
                         "Список пустой)\n"
                         "Можете добавить получателей командой 'Изменить список получателей'")
        return False

    return True


def quantity_check_message(message):
    session = db_session.create_session()
    user_all = session.query(Messages).all()

    list_user = 0

    for user_id in user_all:
        if user_id.senderId == message.chat.id:
            list_user += 1

    if list_user <= 0:
        app.send_message(message.chat.id,
                         "Список пустой)\n"
                         "Можете добавить сообщение командой 'Изменить сообщение для рассылки'")
        return False

    return True
