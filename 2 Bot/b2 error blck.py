import sqlite3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import Unauthorized

BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define your group chat IDs
TEXT_Group_CHAT_ID = -1001556470556
PHOTO_GROUP_CHAT_ID = -1001950066626
VIDEO_GROUP_CHAT_ID = -1001937706377
STICKER_GROUP_CHAT_ID = -1001812365681
LOCATION_GROUP_CHAT_ID = -1001836993384
FILES_GROUP_CHAT_ID = -1001872993214

def error_block(update, context, user_info):
    try:
        yield  # This is a placeholder for the code that sends messages; it will be replaced later.
    except Unauthorized:
        # Handle the case where the user has blocked the bot
        print(f"{user_info} - User has blocked the bot")

def start(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    reply_message_id = update.message.message_id
    print(f"{user_info} - User Starting Command: {update.message.text}")

    message1 = f"Welcome <b>{user.first_name} {user.last_name or ''}</b>\n(@{user.username}), \nYour user ID is <code>{user.id}</code>"
    context.bot.send_message(chat_id=update.message.chat_id, text=message1, parse_mode='HTML')

    buttons = [
        InlineKeyboardButton("Facebook", url="https://www.facebook.com"),
        InlineKeyboardButton("YouTube", url="https://www.youtube.com"),
        InlineKeyboardButton("Google", url="https://www.google.com"),
        InlineKeyboardButton("Twitter", url="https://www.twitter.com"),
        InlineKeyboardButton("Instagram", url="https://www.instagram.com"),
        InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com"),
    ]
    keyboard = [
        [buttons[0], buttons[1], buttons[2]],  # First row with the first three buttons
        [buttons[3], buttons[4]],  # Second row with the next two buttons
        [buttons[5]]  # Third row with the last button
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(message1, reply_markup=reply_markup, parse_mode='HTML')

commands = ['start', 'begin', 'starting', 'new', 'manik', 'shruti']
for command in commands:
    dispatcher.add_handler(CommandHandler(command, start))
def handle_text(update, context):
    user = update.message.from_user
    user_message = update.message.text
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Message: {user_message}")

    def send_messages():
        capitalized_message = user_message.upper()
        character_count = len(user_message)
        count_message = f"Your message has {character_count} character(s)."
        banana_emojis = "🍌" * character_count

        context.bot.send_message(chat_id=TEXT_Group_CHAT_ID, text=user_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=capitalized_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=count_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=banana_emojis)

    # error_block(update, context, user_info)  # Handle Unauthorized exceptions

    try:
        send_messages()
    except Unauthorized:
        # Handle the case where the user has blocked the bot
        print(f"{user_info} - User has blocked the bot while sending a text message")

dispatcher.add_handler(MessageHandler(Filters.text, handle_text))


def handle_photo(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Photo")

    def send_message():
        context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand images, {user_info}. Please send text messages.")

    error_block(update, context, user_info)
    send_message()

dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))

def handle_video(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Video")

    def send_message():
        context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand videos, {user_info}. Please send text messages.")

    error_block(update, context, user_info)
    send_message()

dispatcher.add_handler(MessageHandler(Filters.video, handle_video))

def handle_sticker(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Sticker")

    def send_message():
        context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand This Sticker, {user_info}. Please send text messages.")

    sticker_id = update.message.sticker.file_id
    sticker_message = f"<b>This Sticker ID</b>: \n<code>{sticker_id}</code>"
    context.bot.send_message(chat_id=update.message.chat_id, text=sticker_message, parse_mode="HTML")
    additional_message = f"Hello {user.first_name}! I have sent you the sticker already. To get more stickers, send me more stickers."
    context.bot.send_message(chat_id=update.message.chat_id, text=additional_message)

    error_block(update, context, user_info)
    send_message()

dispatcher.add_handler(MessageHandler(Filters.sticker, handle_sticker))

def handle_document(update, context):
    user = update.message.from_user
    document = update.message.document
    file_type = document.mime_type
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Document: {file_type}")

    def send_message():
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Thank you for sharing a {file_type} file, {user.first_name}!")

    context.bot.forward_message(chat_id=FILES_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

    error_block(update, context, user_info)
    send_message()

dispatcher.add_handler(MessageHandler(Filters.document, handle_document))

def handle_contact(update, context):
    user = update.message.from_user
    contact_info = update.message.contact
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"@{user.username} Send a Contact")

    def send_message():
        reply_message = f"Sorry, I can't read contact information. Here's the contact you shared:\n\n"
        reply_message += f"Name: {contact_info.first_name} {contact_info.last_name or ''}\n"
        reply_message += f"Phone Number: {contact_info.phone_number}"
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)

    context.bot.forward_message(chat_id=FILES_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

    error_block(update, context, user_info)
    send_message()

dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))

def handle_voice(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Voice Message")

    def send_message():
        reply_message = f"Sorry, {user_info}, I cannot process voice messages at the moment. Please send text messages instead."
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)

    context.bot.forward_message(chat_id=FILES_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

    error_block(update, context, user_info)
    send_message()

dispatcher.add_handler(MessageHandler(Filters.voice, handle_voice))

def handle_audio(update, context):
    user = update.message.from_user
    audio_info = update.message.audio
    caption = update.message.caption
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"@{user.username} Send a Audio")

    def send_message():
        reply_message = f"Received an audio file from {user.first_name} {user.last_name or ''}:\n\n"
        reply_message += f"Audio File Name: {audio_info.file_name}\n"
        reply_message += f"Audio File Size: {audio_info.file_size / 1024 / 1024:.2f} MB\n"
        reply_message += f"Audio Bit Rate: {audio_info.file_name}\n"
        reply_message += f"Additional Caption Information:\n{caption}"
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)

    error_block(update, context, user_info)
    send_message()

dispatcher.add_handler(MessageHandler(Filters.audio, handle_audio))

def handle_venue(update: Update, context):
    user = update.message.from_user
    message = update.message

    latitude = message.location.latitude
    longitude = message.location.longitude
    location_message = f"Received a Location Message From @{user.username}:\nLatitude: {latitude}\nLongitude: {longitude}"
    context.bot.send_message(chat_id=update.message.chat_id, text=location_message)

    venue = message.venue
    venue_name = venue.title
    venue_address = venue.address
    venue_message = f"Received a Venue Location Message From @{user.username}:\nVenue Name: {venue_name}\nVenuAddress: {venue_address}"
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"@{user.username} Sent a Venue")
    context.bot.send_message(chat_id=update.message.chat_id, text=venue_message)
    context.bot.forward_message(LOCATION_GROUP_CHAT_ID, update.message.chat_id, update.message.message_id)

    error_block(update, context, user_info)

dispatcher.add_handler(MessageHandler(Filters.venue, handle_venue))

def handle_location(update: Update, context):
    user = update.message.from_user
    message = update.message

    latitude = message.location.latitude
    longitude = message.location.longitude
    location_message = f"Received a Location Message From @{user.username}:\nLatitude: {latitude}\nLongitude: {longitude}"
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"@{user.username} Sent a Location")

    context.bot.send_message(chat_id=update.message.chat_id, text=location_message)
    context.bot.forward_message(LOCATION_GROUP_CHAT_ID, update.message.chat_id, update.message.message_id)

    error_block(update, context, user_info)

dispatcher.add_handler(MessageHandler(Filters.location, handle_location))

def all_response(update: Update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Hello")
    context.bot.forward_message(TEXT_Group_CHAT_ID, update.message.chat_id, update.message.message_id)
    context.bot.send_message(TEXT_Group_CHAT_ID, text=f"This has in Others Type 🍌🍌🍌 @RanaUniverse (Filters.all)")

dispatcher.add_handler(MessageHandler(Filters.all, all_response))

updater.start_polling()
updater.idle()
