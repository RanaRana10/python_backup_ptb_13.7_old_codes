from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters

# Define a function to handle photo messages
def handle_photo(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
    # logic for handling photo messages goes here
    # can access the photo using update.message.photo
    # example, to get the largest photo:
    largest_photo = update.message.photo[-1]
    
    # You can then send a reply or perform any actions with the photo
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Received a photo from {user_info}.")
    context.bot.send_photo(chat_id=update.message.chat_id, photo=largest_photo.file_id)



    buttons = [
    InlineKeyboardButton("View Profile", url="tg://user?id=6690362261"),
    InlineKeyboardButton("Join Now", url="https://t.me/+xCO9bXRSlX1iZDc1"),
]

    keyboard = [[buttons[0], buttons[1]]]

    # Create a reply_markup with the keyboard
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a reply message with buttons
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Received a photo from {user_info}.", reply_markup=reply_markup)

# Add photo_handler with the updated handle_photo function to your dispatcher
photo_handler = MessageHandler(Filters.photo, handle_photo)



