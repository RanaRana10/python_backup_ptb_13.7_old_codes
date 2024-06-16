
from telegram.ext import MessageHandler, Filters

# Define a function to handle text messages
def handle_text(update, context):
    user = update.message.from_user
    user_message = update.message.text

    if user_message:
        capitalized_message = user_message.upper()
        character_count = len(user_message)
        count_message = f"Your message has {character_count} character(s."
        banana_emojis = "🍌" * character_count
        user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"

        context.bot.send_message(chat_id=update.message.chat_id, text=user_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=capitalized_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=count_message)
        context.bot.send_message(chat_id=update.message.chat_id, text=banana_emojis)

user_id_list = [6690362261, 987654321, 555555555]
text_message_handler = MessageHandler(Filters.text & ~Filters.command & Filters.user(user_id_list), handle_text)


def new_text(update, context):
    user = update.message.from_user
    
    user_message = update.message.text

    if user_message:
        
        context.bot.send_message(chat_id=update.message.chat_id, text=f"this is new text")
       

user_new_id_list = [6689031799, 7868687]
new_text_message_handler = MessageHandler(Filters.text & ~Filters.command & Filters.user(user_new_id_list), new_text)

def text_1 (update,context):
    user = update.message.from_user
    user_message = update.message.text

    if user_message:
        context.bot.send_message(chat_id = update.message.chat_id, text = f"This is text 1")

text_1_handler = MessageHandler(Filters.text, text_1)