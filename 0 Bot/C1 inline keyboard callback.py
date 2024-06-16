# Import necessary modules
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

TEXT_Group_CHAT_ID = -1001556470556

# Define your Bot Token
BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'  # Replace with your bot token
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define a state for the conversation
SEE_1, SEE_2 = range(2)

# Function to handle the /see command
def see_1(update, context):
    user = update.message.from_user
    context.user_data['user_id'] = user.id
    message = "Press the button to see the photo."
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("See Photo", callback_data='see_2')]])

    update.message.reply_text(message, reply_markup=reply_markup)
    context.bot.send_message(chat_id=update.message.chat_id, text=f"This is Send Message",reply_markup=reply_markup)

    return SEE_2

# Function to handle the "See Photo" button
# Function to handle the "See Photo" button
def see_2(update, context):
    query = update.callback_query
    user_id = context.user_data.get('user_id')
    chat_id = query.message.chat_id

    if user_id is None:
        # If user_id is not set, we can't verify the user
        context.bot.send_message(chat_id=chat_id, text="Sorry, we couldn't verify your identity.")
    elif query.from_user.id == user_id:
        # Send the image to the user
        image_file_id = "AgACAgUAAxkBAAIoRGUvVMa6kt3aGZDnOfFMcg4UzLpaAAK1tzEb-OShVFgnfLkHemIvAQADAgADcwADMAQ"
        context.bot.send_photo(chat_id=chat_id, photo=image_file_id)
    else:
        # Send a message to the chat that the user is not allowed
        user = query.from_user
        username = f"@{user.username}" if user.username else user.first_name
        message = f"{username}, you are not allowed to perform this action."
        context.bot.send_message(chat_id=chat_id, text=message)
        query.answer(message)  # Send the message as an answer to the button press

    query.answer()
    return ConversationHandler.END

# Create a ConversationHandler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('see', see_1)],
    states={
        SEE_2: [CallbackQueryHandler(see_2)]
    },
    fallbacks=[]
)

# Add the conversation handler to the dispatcher
updater.dispatcher.add_handler(conv_handler)

def all_response(update: Update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=f"(This is All type of Reply\nThanks For)")
    context.bot.forward_message(TEXT_Group_CHAT_ID, update.message.chat_id, update.message.message_id)
    context.bot.send_message(TEXT_Group_CHAT_ID, text="This has in Others Type 🍌🍌🍌 @RanaUniverse (Filters.all)")

dispatcher.add_handler(MessageHandler(Filters.all, all_response))

# Start the bot
updater.start_polling()
updater.idle()
