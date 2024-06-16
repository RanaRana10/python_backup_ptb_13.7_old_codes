from telegram.ext import MessageHandler, Filters
TEXT_Group_CHAT_ID = "-1001556470556"

# Define a function to handle other types of messages
def handle_other_messages(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Hello")
    context.bot.forward_message(TEXT_Group_CHAT_ID, update.message.chat_id, update.message.message_id)
    context.bot.send_message(TEXT_Group_CHAT_ID, text=f"This has in Others Type 🍌🍌🍌 @RanaUniverse (Filters.all)")

other_message_handler = MessageHandler(Filters.all, handle_other_messages)

