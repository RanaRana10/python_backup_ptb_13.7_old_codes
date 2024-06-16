from telegram.ext import MessageHandler, Filters

# Define a function to handle sticker messages
def handle_sticker(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
    # Your logic for handling sticker messages goes here
    # You can access the sticker ID using update.message.sticker.file_id
    sticker_id = update.message.sticker.file_id
    
    # You can then send a reply or perform any actions with the sticker
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Received a sticker from {user_info}.")
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker_id)

sticker_handler = MessageHandler(Filters.sticker, handle_sticker)
