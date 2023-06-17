from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.constants import ChatType
from database import Database
from dotenv import load_dotenv
import os

load_dotenv()


class TelegramBot():

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="""[指令列表]
/help 印出這個列表
/run <SQL> 執行 SQL 語法 
""")

    async def run_sql(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        args = " ".join(update.message.text.split()[1:])
        result = self.database.run_sql(args)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(result))

    async def reset_database(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        args = update.message.text.split()
        if len(args) != 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='參數錯誤')
            return
        self.database.reset_database()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='成功重製')

    def __init__(self):
        TGBOT_TOKEN = os.getenv("TGBOT_TOKEN", "TOKENISMISSING")
        self.app = ApplicationBuilder().token(TGBOT_TOKEN).build()
        self.database = Database()

        self.app.add_handler(CommandHandler('help', self.help))
        self.app.add_handler(CommandHandler('run', self.run_sql))
        self.app.add_handler(CommandHandler('reset', self.reset_database))
        print(TGBOT_TOKEN)

    def run(self):
        self.app.run_polling()
        pass


if __name__ == "__main__":
    telegrambot = TelegramBot()
    telegrambot.run()
