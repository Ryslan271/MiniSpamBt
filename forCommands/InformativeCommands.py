# region Информация о изменении списка получателей
async def get_help(message, app):
    app.send_message(message.chat.id,
                     "Для вызова команд следует написать префикс '!' и опеределенную команду\n"
                     "Пример:\n"
                     "!deletemessage (Номер сообщения, номер вы можете узнать командой Message без префекса)")
# endregion

