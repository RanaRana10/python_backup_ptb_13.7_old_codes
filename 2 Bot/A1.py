# Import necessary modules, # Initialize the bot using the defined token, # Get the dispatcher to register handlers #using @RanaUniverse in Telegram & pip python-telegram-bot 13.7
#start this with some buttons in /start for checking

import sqlite3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


TEXT_Group_CHAT_ID = -1001556470556
PHOTO_GROUP_CHAT_ID = -1001950066626  
VIDEO_GROUP_CHAT_ID = -1001937706377  
STICKER_GROUP_CHAT_ID = -1001812365681
LOCATION_GROUP_CHAT_ID = -1001836993384 
FILES_GROUP_CHAT_ID = -1001872993214



# Function to handle the /start command
def start(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    reply_message_id = update.message.message_id
    print(f"{user_info} - User Starting Command: {update.message.text}")

    message1 = f"Welcome <b>{user.first_name} {user.last_name or ''}</b>\n(@{user.username}), \nYour user ID is <code>{user.id}</code>."
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

    
    # Register the /start, /begin, /starting, and /new command handler
commands = ['start', 'begin', 'starting', 'new', 'manik', 'shruti']
for command in commands:
    
    dispatcher.add_handler(CommandHandler(command, start))





# Function to handle text messages
def handle_text(update, context):
    user = update.message.from_user
    user_message = update.message.text

    if  update.message.text:
        capitalized_message = user_message.upper()
        character_count = len(user_message)
        count_message = f"Your message has {character_count} character(s)."
        banana_emojis = "🍌" * character_count
        user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
        print(f"{user_info} - User Message: {user_message}")

        context.bot.send_message(chat_id=TEXT_Group_CHAT_ID, text=user_message)

        context.bot.send_message(chat_id=update.message.chat_id, text=capitalized_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=count_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=banana_emojis)


dispatcher.add_handler(MessageHandler(Filters.text, handle_text))



# Function to handle photo messages
def handle_photo(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Photo")
    context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand images, {user_info}. Please send text messages.")

    message = f"This Photo Has Been Forwarded From The User: \n<b>Username: @{user.username}\nName: {user.first_name} {user.last_name or ''}\nUserID: </b><code>{user.id}</code>"
    
    context.bot.forward_message(chat_id=PHOTO_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    context.bot.send_message(chat_id=PHOTO_GROUP_CHAT_ID, text=message, parse_mode='HTML')
    context.bot.send_photo(chat_id=PHOTO_GROUP_CHAT_ID, photo=update.message.photo[-1]) #copy the photo and send


dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))




# Function to handle video messages
def handle_video(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Video")
    message = f"This Video Has Been Forwarded From The User:\n<b>Name:{user.first_name} {user.last_name or ''}</b>\nUsername: @{user.username}\nUserID: <code>{user.id}</code>"
    context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand videos, {user_info}. Please send text messages.")

    context.bot.forward_message(VIDEO_GROUP_CHAT_ID,update.message.chat_id,update.message.message_id)
    context.bot.send_message(VIDEO_GROUP_CHAT_ID, message, parse_mode='HTML')

dispatcher.add_handler(MessageHandler(Filters.video, handle_video))





# Function to handle sticker messages
def handle_sticker(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Sticker")
    
    context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand This Sticker, {user_info}. Please send text messages.")

    sticker_id = update.message.sticker.file_id
    sticker_message = f"<b>This Sticker ID</b>: \n<code>{sticker_id}</code>"
    context.bot.send_message(chat_id=update.message.chat_id, text=sticker_message, parse_mode="HTML")
    additional_message = f"Hello {user.first_name}! I have sent you the sticker already. To get more stickers, send me more stickers."
    context.bot.send_message(chat_id=update.message.chat_id, text=additional_message)

    context.bot.forward_message(STICKER_GROUP_CHAT_ID, update.message.chat_id, update.message.message_id)
    context.bot.send_message(STICKER_GROUP_CHAT_ID,f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}")

dispatcher.add_handler(MessageHandler(Filters.sticker, handle_sticker))





# Function to handle document messages
def handle_document(update, context):
    user = update.message.from_user
    document = update.message.document
    file_type = document.mime_type

    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Document: {file_type}")

    # Forward the document to a specific group
    # context.bot.forward_message(FILES_GROUP_CHAT_ID, chat_id=update.message.chat_id, document=update.message.document.file_id)
    context.bot.forward_message(chat_id=FILES_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    
    # Respond with a message
    response = f"Thank you for sharing a {file_type} file, {user.first_name}!"
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

    message = f"This File Has Been Forwarded From The User: \n<b>Name:{user.first_name} {user.last_name or ''}</b>\nUsername: @{user.username}\nUserID: <code>{user.id}</code>"
    context.bot.send_message(chat_id=FILES_GROUP_CHAT_ID, text=message, parse_mode='HTML')

dispatcher.add_handler(MessageHandler(Filters.document, handle_document))





def handle_contact(update, context):
    user = update.message.from_user
    contact_info = update.message.contact
    
    # Send a reply to the user explaining that the bot can't read contact information
    reply_message = f"Sorry, I can't read contact information. Here's the contact you shared:\n\n"
    reply_message += f"Name: {contact_info.first_name} {contact_info.last_name or ''}\n"
    reply_message += f"Phone Number: {contact_info.phone_number}"
    context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)
    print(f"@{user.username} Send a Contact")
    # Forward the contact message to your group
    context.bot.forward_message(chat_id=FILES_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

# Add the handler to respond to contact messages
dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))



def handle_voice(update, context):
    # Get information about the user who sent the voice message
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Sent a Voice Message")

    reply_message = f"Sorry, {user_info}, I cannot process voice messages at the moment. Please send text messages instead."

    context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)
    
    context.bot.forward_message(FILES_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

dispatcher.add_handler(MessageHandler(Filters.voice, handle_voice))




def handle_audio(update, context):
    user = update.message.from_user
    audio_info = update.message.audio
    caption = update.message.caption
    print(f"@{user.username} Send a Audio")
    # Send a reply with the audio file information and additional caption information
    reply_message = f"Received an audio file from {user.first_name} {user.last_name or ''}:\n\n"
    reply_message += f"Audio File Name: {audio_info.file_name}\n"
    reply_message += f"Audio File Size: {audio_info.file_size / 1024 / 1024:.2f} MB\n"
    reply_message += f"Audio Bit Rate: {audio_info.file_name}\n"
    reply_message += f"Additional Caption Information:\n{caption}"
    
    context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)

# Add the handler to respond to audio messages
dispatcher.add_handler(MessageHandler(Filters.audio, handle_audio))




# Function to handle venue messages
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
    print(f"@{user.username} Sent a Venue")
    context.bot.send_message(chat_id=update.message.chat_id, text=venue_message)
    context.bot.forward_message(LOCATION_GROUP_CHAT_ID, update.message.chat_id, update.message.message_id)

dispatcher.add_handler(MessageHandler(Filters.venue, handle_venue))




# Function to handle location messages
def handle_location(update: Update, context):
    user = update.message.from_user
    message = update.message
    
    # Extract latitude and longitude from the location
    latitude = message.location.latitude
    longitude = message.location.longitude
    
    location_message = f"Received a Location Message From @{user.username}:\nLatitude: {latitude}\nLongitude: {longitude}"
    print(f"@{user.username} Sent a Location")
    
    context.bot.send_message(chat_id=update.message.chat_id, text=location_message)
    context.bot.forward_message(LOCATION_GROUP_CHAT_ID, update.message.chat_id, update.message.message_id)

# Register the Message Handler without the Filters.location filter


dispatcher.add_handler(MessageHandler(Filters.venue, handle_location))





def all_response(update:Update,context):
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Hello")
    context.bot.forward_message(TEXT_Group_CHAT_ID, update.message.chat_id, update.message.message_id)
    context.bot.send_message(TEXT_Group_CHAT_ID, text=f"This has in Others Type 🍌🍌🍌 @RanaUniverse (Filters.all)")

dispatcher.add_handler(MessageHandler(Filters.all, all_response))







# Start the bot
# Run the bot until you send a stop signal (Ctrl+C)
updater.start_polling()
updater.idle()