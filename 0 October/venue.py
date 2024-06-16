from telegram.ext import MessageHandler, Filters

# Define a function to handle venue messages
def handle_venue(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
    # Your logic for handling venue messages goes here
    # You can access the venue information using update.message.venue
    venue = update.message.venue
    
    # You can then send a reply or perform any actions with the venue message
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Received a venue message from {user_info}.")
    
    # For example, you can send the venue message back to the chat
    context.bot.send_venue(chat_id=update.message.chat_id, venue=venue)

venue_handler = MessageHandler(Filters.venue, handle_venue)
