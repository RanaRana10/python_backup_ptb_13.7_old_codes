from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Define your predefined responses
responses = {
    "button1": "Response for Button 1",
    "button2": "Response for Button 2",
    "button3": "Response for Button 3",
    "button4": "Response for Button 4",
    "button5": "You have not any active plan",
    "button6": "You have not any active plan",
    "button7": "You have not any active plan",
    "button8": "You have not any active plan",
}

# Function to create and send a keyboard in the desired format
def send_keyboard(update, message_text, button_data):
    buttons = [InlineKeyboardButton(label, data) for label, data in button_data]
    
    # Define the layout of buttons
    keyboard = [
        buttons[:3],  # First row with the first three buttons
        buttons[3:5],  # Second row with the next two buttons
        [buttons[5]]  # Third row with the last button
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(message_text, reply_markup=reply_markup, parse_mode='HTML')

# Function to handle the /start command
def start(update, context):
    button_data = [
        ("Facebook", "https://www.facebook.com"),
        ("YouTube", "https://www.youtube.com"),
        ("Google", "https://www.google.com"),
        ("Twitter", "https://www.twitter.com"),
        ("Instagram", "https://www.instagram.com"),
        ("LinkedIn", "https://www.linkedin.com"),
    ]
    
    message_text = "Choose a button:"
    
    send_keyboard(update, message_text, button_data)

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
dispatcher.add_handler(CallbackQueryHandler(handle_button_click))

# Start the bot
updater.start_polling()
updater.idle()
