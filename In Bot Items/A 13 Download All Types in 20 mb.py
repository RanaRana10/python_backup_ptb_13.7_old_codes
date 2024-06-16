import os
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'
# Specify the directory where files will be saved
SAVE_DIR = 'Download 13'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your file-saving bot. Send a file (image, video, PDF, etc.), and I will save it to my directory.")
    update.message.reply_text("Who Are You Just Message Here, I will surprise You! 😢😁🍌🐱‍👤🤳🎂🎉🌹💋👏😜")

dispatcher.add_handler(CommandHandler('start', start))

def handle_files(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_name = update.effective_user.username
    file = None
    file_extension = None
    file_size = None

    if update.message.document:
        file = update.message.document
        file_extension = file.file_name.split('.')[-1].lower()
        file_size = file.file_size
    elif update.message.photo:
        file = update.message.photo[-1]
        file_extension = 'jpg'  # For photos, set the extension to 'jpg'
        file_size = file.file_size

    if file_extension is None:
        update.message.reply_text("Please send a valid file.")
        return

    file_id = file.file_id
    new_file = context.bot.get_file(file_id)
    file_name = f"{user_id}_{file.file_id}.{file_extension}"
    file_path = os.path.join(SAVE_DIR, file_name)
    new_file.download(file_path)
    message = f"File '{file_name}'({file_extension}) \n of size {file_size} bytes \n has been saved to my directory by {user_name}."
    update.message.reply_text(message)
    print(f"Received: {message}")

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

dispatcher.add_handler(MessageHandler(Filters.document | Filters.photo, handle_files))

updater.start_polling()
updater.idle()
