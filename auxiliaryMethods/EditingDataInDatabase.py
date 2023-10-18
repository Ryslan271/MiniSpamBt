from models.DatabaseStructure import UserIDs, Messages
from models.DatabaseConnection import db_session
from auxiliaryMethods.Methods import quantity_check_users_ids, quantity_check_message
from pyrogram import filters
from main import app


@app.on_message(filters.command("adduser", prefixes='!') & filters.me)
def text_set_users_ids(message):
    session = db_session.create_session()

    user_all = session.query(UserIDs).all()

    for user in user_all:
        if user.ListIds == str(message.text)[1:]:
            app.send_message(message.chat.id,
                             'Такой пользователь уже есть в списке,'
                             ' прошу проверить командой "Вывести всех получателей"')
            return

    new_users_id = UserIDs(
        senderId=message.chat.id,
        ListIds=message.text.split("!adduser ", maxsplit=1)[1].strip()
    )
    session.add(new_users_id)
    session.commit()

    app.send_message(message.chat.id,
                     'Новые пользователи добавлены')


@app.on_message(filters.command("deletemessage", prefixes='!') & filters.me)
def text_delete_users_id(message):
    session = db_session.create_session()
    user_all = session.query(UserIDs).all()

    if not quantity_check_users_ids(message):
        return

    if message.text.split("!deletemessage ", maxsplit=1)[1].strip() not in [user.ListIds for user in user_all]:
        app.send_message(message.chat.id,
                         "Прошу проверить ник, такого пользователя нет")
        return

    user_all = session.query(UserIDs).all()

    current_user =\
    [user.id for user in user_all if user.ListIds == message.text.split("!deletemessage ", maxsplit=1)[1].strip()][0]

    session.delete(session.query(UserIDs).get(current_user))
    session.commit()

    app.send_message(message.chat.id,
                     'Получатель удален из списка')

    if quantity_check_users_ids(message):
        session = db_session.create_session()
        user_all = session.query(UserIDs).all()
        app.send_message(message.chat.id,
                         "Вот новый список получателей:\n" +
                         "\n".join([user.ListIds for user in user_all]))


@app.on_message(filters.command("send", prefixes='!') & filters.me)
def text_sending_message(message):

    pass

    if not quantity_check_message(message) or not quantity_check_users_ids(message):
        return

    text = message.text.split("!send ", maxsplit=1)[1].strip()

    users_ids = [" ".join(text.split(", ")[0]).split(' ')]
    message_id = str(text.split(", ")[1])

    session = db_session.create_session()
    user_current_recipient = [session.query(Messages).get(user_id) for user_id in users_ids]
    user_current_message = session.query(UserIDs).get(message_id)

    app.send_message(chat_id=user_current_recipient.ListIds, text=user_current_message.text)

    app.send_message(message.chat.id,
                     'Сообщение отправлено')


@app.on_message(filters.command("newmessage", prefixes='!') & filters.me)
def text_set_message(message):
    session = db_session.create_session()

    new_messages = Messages(
        senderId=message.chat.id,
        text=message.text.split("!newmessage ", maxsplit=1)[1]
    )
    session.add(new_messages)
    session.commit()

    app.send_message(message.chat.id,
                     'Новые сообщение добавлено')