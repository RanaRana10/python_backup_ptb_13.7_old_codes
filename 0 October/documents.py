from telegram.ext import MessageHandler, Filters

# Define a function to handle document messages
def handle_document(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
    # Your logic for handling document messages goes here
    # You can access the document information using update.message.document
    document = update.message.document
    
    # You can then send a reply or perform any actions with the document
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Received a document from {user_info}.")
    
    # For example, you can send the document back to the chat
    context.bot.send_document(chat_id=update.message.chat_id, document=document.file_id)

document_handler = MessageHandler(Filters.document, handle_document)
