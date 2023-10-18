from pyrogram import filters
from main import app


# region Информация о изменении списка получателей
@app.on_message(filters.command("help", prefixes='!') & filters.me)
async def set_help(message):
    app.send_message(message.chat.id,
                     "Для вызова команд следует написать префикс '!' и опеределенную команду\n"
                     "Пример:\n"
                     "!deletemessage (Номер сообщения, номер вы можете узнать командой Message без префекса)")
# endregion

