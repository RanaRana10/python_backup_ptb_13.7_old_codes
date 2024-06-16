from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Define your predefined responses
responses = {
    "button1": "Response for Button fff1",
    "button2": "Response for Button 2",
    "button3": "Response for Button 3",
    "button4": "Response for Button 4",
    "button5": "You have not any active plan",
    "button6": "You have not any active plan",
    "button7": "You have not any active plan",
    "button8": "You have not any active plan",
}

# Function to handle the /start command
def start(update, context):
    buttons = [
        InlineKeyboardButton("Google", url="https://www.google.com"),
        InlineKeyboardButton("Button 2", url="tg://user?id=6690362261"),
        InlineKeyboardButton("Button 3", url="www.com"),],
    [   InlineKeyboardButton("Button 4", callback_data="button4"),
        InlineKeyboardButton("Button 5", callback_data="button5"),],
    [   InlineKeyboardButton("Button 6", callback_data="button6"),
        InlineKeyboardButton("Button 7", callback_data="button7"),
        InlineKeyboardButton("Button 8", callback_data="button8"),
    ]
    reply_markup = InlineKeyboardMarkup([buttons])

    update.message.reply_text("Choose a button:", reply_markup=reply_markup)

# Define a callback query handler
def handle_button_click(update, context):
    query = update.callback_query
    button_clicked = query.data

    if button_clicked in responses:
        response_text = responses[button_clicked]
        context.bot.send_message(chat_id=query.message.chat_id, text=response_text)

# Set up the bot
updater = Updater(token='6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw', use_context=True)
dispatcher = updater.dispatcher

# Add handlers for the /start command and callback queries
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('a', start))
dispatcher.add_handler(CallbackQueryHandler(handle_button_click))

# Start the bot
updater.start_polling()
updater.idle()
