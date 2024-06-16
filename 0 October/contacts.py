from telegram.ext import MessageHandler, Filters

# Define a function to handle contact messages
def handle_contact(update, context):
    user = update.message.from_user
    contact_info = update.message.contact

    # Send a reply to the user explaining that the bot can't read contact information
    reply_message = f"Sorry, I can't read contact information. Here's the contact you shared:\n\n"
    reply_message += f"Name: {contact_info.first_name} {contact_info.last_name or ''}\n"
    reply_message += f"Phone Number: {contact_info.phone_number}"
    context.bot.send_message(chat_id=update.message.chat_id, text=reply_message)

contact_handler = MessageHandler(Filters.contact, handle_contact)
