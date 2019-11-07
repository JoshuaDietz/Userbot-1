from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.command("joinmod", ".") & Filters.me)
def joining(bot: BOT, message: Message):
    result = message.reply_to_message.click(0)
    message.delete()
    code = result.replace("https://t.me/werewolfbot?start=", "")
    bot.send_message(message.reply_to_message.from_user.id, "/start " + code)
