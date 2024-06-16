from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, run_async

BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'  # Replace with your bot token
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Function to handle the /start command
@run_async
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    reply_message_id = update.message.message_id
    print(f"{user_info} - User Starting Command: {update.message.text}")

    for i in range(1, 1001):
        message = f"This is {i}"
        context.bot.send_message(chat_id=user.id, text=message)

# Function to handle text messages
@run_async
def handle_text(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_message = update.message.text

    print(f"User Message: {user_message}")

# Add a handler for the /start command
dispatcher.add_handler(CommandHandler('start', start))

# Add a handler for text messages
dispatcher.add_handler(MessageHandler(Filters.text, handle_text))

# Start the bot
updater.start_polling()

# Run the bot until you send a stop signal (Ctrl+C)
updater.idle()
