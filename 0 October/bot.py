import telegram
from telegram.ext import Updater
from commands import start_command
from messages import text_message_handler, new_text_message_handler, text_1_handler
from photos import photo_handler
from videos import video_handler
from stickers import sticker_handler
from documents import document_handler
from contacts import contact_handler
from voice import voice_handler
from audio import audio_handler
from venue import venue_handler
from other_messages import other_message_handler




# Initialize the bot
updater = Updater(token='6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw', use_context=True)
dispatcher = updater.dispatcher

# Set up event handlers for different message types
dispatcher.add_handler(start_command)

dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(new_text_message_handler)
dispatcher.add_handler(text_1_handler)

dispatcher.add_handler(photo_handler)
dispatcher.add_handler(video_handler)
dispatcher.add_handler(sticker_handler)

dispatcher.add_handler(document_handler)
dispatcher.add_handler(contact_handler)
dispatcher.add_handler(voice_handler)

dispatcher.add_handler(audio_handler)
dispatcher.add_handler(venue_handler)
dispatcher.add_handler(other_message_handler)

# Start the bot
updater.start_polling()
updater.idle()
