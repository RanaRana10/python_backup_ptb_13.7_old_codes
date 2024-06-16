from telegram.ext import MessageHandler, Filters

# Define a function to handle video messages
def handle_video(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
    # Your logic for handling video messages goes here
    # You can access the video using update.message.video
    # For example, to get the video file ID:
    video_file_id = update.message.video.file_id
    
    # You can then send a reply or perform any actions with the video
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Received a video from {user_info}.")
    context.bot.send_video(chat_id=update.message.chat_id, video=video_file_id)

video_handler = MessageHandler(Filters.video, handle_video)
