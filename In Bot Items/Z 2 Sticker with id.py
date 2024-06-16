# Import necessary modules
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

# Define your bot token here
BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'

# Initialize the bot using the defined token
updater = Updater(token=BOT_TOKEN, use_context=True) 


# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Function to handle user messages, including stickers and text


def echo(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}: Name: {user.first_name} {user.last_name or ''}"

    if update.message.text:
        # Handle text messages
        print(f"{user_info} - User Text Message: {update.message.text}")
        if update.message.text == '/a':
            send_sticker_a(update, context)  # Send the sticker for /a command
        else:
            # Respond with a text message asking for stickers
            context.bot.send_message(chat_id=update.message.chat_id, text="Send me stickers!")
    elif update.message.sticker:
        # Handle sticker messages
        print(f"{user_info} - User Sent a Sticker")
        sticker_id = update.message.sticker.file_id

        # Send a message with the sticker ID
        sticker_message = f"Sticker ID: {sticker_id}"
        context.bot.send_message(chat_id=update.message.chat_id, text=sticker_message)

        # Send an additional message
        additional_message = f"Hello {user.first_name}! I have sent you the sticker already. To get more stickers, send me more stickers."
        context.bot.send_message(chat_id=update.message.chat_id, text=additional_message)




# Register a message handler for all messages
message_handler = MessageHandler(Filters.all, echo)
dispatcher.add_handler(message_handler)

# Function to send the /a sticker
def send_sticker_a(update, context):
    # Sticker ID for the desired sticker
    sticker_id = 'CAACAgIAAxkBAAIGrmUeM80gj-Ob2-tqAjQqOEk-Ga3VAAKGAQACK15TC-y96LIuuYA2MAQ'
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker_id)

# Start the bot
updater.start_polling()

# Run the bot until you send a stop signal (Ctrl+C)
updater.idle()
