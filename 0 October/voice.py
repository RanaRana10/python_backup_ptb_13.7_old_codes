from telegram.ext import MessageHandler, Filters

# Define a function to handle voice messages
def handle_voice(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
    # Your logic for handling voice messages goes here
    # You can access the voice information using update.message.voice
    voice = update.message.voice
    
    # You can then send a reply or perform any actions with the voice message
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Received a voice message from {user_info}.")
    
    # For example, you can send the voice message back to the chat
    context.bot.send_voice(chat_id=update.message.chat_id, voice=voice.file_id)

voice_handler = MessageHandler(Filters.voice, handle_voice)
