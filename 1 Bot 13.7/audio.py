from telegram.ext import MessageHandler, Filters

# Define a function to handle audio messages
def handle_audio(update, context):
    user = update.message.from_user
    audio_info = update.message.audio
    caption = update.message.caption

    # Send a reply with the audio file information and additional caption information
    reply_message = f"Received an audio file from {user.first_name} {user.last_name or ''}:\n\n"
    reply_message += f"Audio File Name: {audio_info.file_name}\n"
    reply_message += f"Audio File Size: {audio_info.file_size / 1024 / 1024:.2f} MB\n"
    reply_message += f"Additional Caption Information:\n{caption}"

    context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)

audio_handler = MessageHandler(Filters.audio, handle_audio)
