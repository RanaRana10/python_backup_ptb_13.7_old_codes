from telegram.ext import Updater, MessageHandler, Filters

# Define your bot token here
BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'

# Initialize the bot using the defined token
updater = Updater(token=BOT_TOKEN, use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Function to handle sticker messages and retrieve the sticker ID
def get_sticker_id(update, context):
    sticker_file_id = update.message.sticker.file_id
    context.bot.send_message(chat_id=update.message.chat_id, text=f" <b> Your Sticker ID </b>:    <code> {sticker_file_id} </code>", parse_mode='HTML')


# Register a message handler for sticker messages
sticker_handler = MessageHandler(Filters.sticker, get_sticker_id)
dispatcher.add_handler(sticker_handler)

if __name__ == '__main__':
    # Start the bot
    updater.start_polling()
    print(f" - User Starting Command: ")
    # Run the bot until you send a stop signal (Ctrl+C)
    updater.idle()