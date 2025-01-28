from telegram.ext import Updater, CommandHandler
import logging
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)
# Your bot's token
TOKEN = 'THE--BOT--TOKEN'
# Your chat ID
CHAT_ID = 'YOUR--CHAT--ID'/.
# Define a function to send a message
def send_notification(update, context):
context.bot.send_message(chat_id=CHAT_ID, text="Hello! This is anotification from your bot.")
def main():
# Create the Updater and pass it your bot's token
updater = Updater(TOKEN, use_context=True)
# Get the dispatcher to register handlers
dp = updater.dispatcher
# Register a handler for the /start command
dp.add_handler(CommandHandler("start", send_notification))
# Start the Bot
updater.start_polling()
# Run the bot until you press Ctrl-C
updater.idle()
if __name__ == '__main__':
main()
