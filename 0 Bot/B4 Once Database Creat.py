# Import necessary modules
import sqlite3, pytz
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define your Bot Token
BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

PHOTO_GROUP_CHAT_ID = -1001950066626

# Create or connect to the database
conn = sqlite3.connect('user_data_b4.db')
cursor = conn.cursor()

# Create a table to store user data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        UserNo INTEGER PRIMARY KEY,
        UserId INTEGER,
        FirstName TEXT,
        LastName TEXT,
        UserName TEXT,
        StartTime TEXT
    )
''')
# Commit the changes and close the connection
conn.commit()
conn.close()


def check_user_in_database(user_id):
    conn = sqlite3.connect('user_data_b4.db')
    cursor = conn.cursor()
    cursor.execute('SELECT UserId FROM users WHERE UserId = ?', (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data is not None

def get_user_data(user_id):
    conn = sqlite3.connect('user_data_b4.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE UserId = ?', (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data




# Function to handle the /start command
def start(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Starting Command: {update.message.text}")

    message1 = f"Welcome <b>{user.first_name} {user.last_name or ''}</b>\n(@{user.username}), \nYour user ID is <code>{user.id}</code>."
    if check_user_in_database(user.id):
        # Fetch user's row from the database
        user_data = get_user_data(user.id)
        
        if user_data:
            # Customize the message with user's data
            message = f"You are already registered in our bot. Here's your information:\n"
            message += f"User ID: {user_data[1]}\n"
            message += f"First Name: {user_data[2]}\n"
            message += f"Last Name: {user_data[3]}\n"
            message += f"Username: {user_data[4]}\n"
            message += f"Start Time: {user_data[5]}\n"
            
            context.bot.send_message(chat_id=update.message.chat_id, text=message)
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="There was an issue retrieving your information.")
   
    else:
        # Capture the user's start time
        start_time_utc = update.message.date
        ist = pytz.timezone('Asia/Kolkata')
        start_time_530 = start_time_utc.astimezone(ist)
        start_time = start_time_530.strftime("%Y-%m-%d %H:%M:%S")
        context.bot.send_message(chat_id=update.message.chat_id, text=f"{start_time}, {ist}")

        username = f"@{user.username}" if user.username else "---"

        # Insert user data into the database, including the start time
        conn = sqlite3.connect('user_data_b4.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (UserId, FirstName, LastName, Username, StartTime) VALUES (?, ?,?, ?, ?)',
                       (user.id, user.first_name, user.last_name, username, start_time))
        conn.commit()
        conn.close()

        update.message.reply_text(f"Kon Ho", parse_mode='HTML')
        context.bot.send_message(chat_id=update.message.chat_id, text=message1, parse_mode='HTML')
        
# Register the /start command handler
dispatcher.add_handler(CommandHandler('start', start))




# Function to handle photo messages
def handle_photo(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
    if check_user_in_database(user.id):
        # User ID is found in the database, proceed with photo handling
        print(f"{user_info} - User Sent a Photo")
        context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand images, {user_info}. Please send text messages.")

        start_time_utc = update.message.date
        ist = pytz.timezone('Asia/Kolkata')
        start_time_530 = start_time_utc.astimezone(ist)
        start_time = start_time_530.strftime("%Y-%m-%d %H:%M:%S")


        message = f"This Photo Has Been Forwarded From The User: \n<b>Username: @{user.username}\nName: {user.first_name} {user.last_name or ''}\nUserID: </b><code>{user.id}</code>\n<b>Time:</b>{start_time} "
    
        context.bot.forward_message(chat_id=PHOTO_GROUP_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.send_message(chat_id=PHOTO_GROUP_CHAT_ID, text=message, parse_mode='HTML')
    else:
        # User ID is not found in the database, reply with a message
        context.bot.send_message(chat_id=update.message.chat_id, text="You can't use this photo function.")


dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
#






def handle_video(update, context):
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    
 
    if check_user_in_database(user.id):
        # User ID is found in the database, proceed with video handling
        print(f"{user_info} - User Sent a Video")
        context.bot.send_message(chat_id=update.message.chat_id, text=f"I don't understand videos, {user_info}. Please send text messages.")
    
        message = f"This video Has Been Forwarded From The User: \n<b>Username: @{user.username}\nName: {user.first_name} {user.last_name or ''}\nUserID: </b><code>{user.id}</code>"
    
        context.bot.forward_message(chat_id=-1001937706377, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.send_message(chat_id=-1001937706377, text=message, parse_mode='HTML')
    else:
        # User ID is not found in the database, reply with a message
        context.bot.send_message(chat_id=update.message.chat_id, text="You can't use this video function.")


dispatcher.add_handler(MessageHandler(Filters.video, handle_video))




# Start the bot
updater.start_polling()
updater.idle()
