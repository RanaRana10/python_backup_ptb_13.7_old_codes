 # Import necessary modules
import sqlite3, pytz
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Define your Bot Token
BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


# Create or connect to the database
conn = sqlite3.connect('user_data_b5.db')
cursor = conn.cursor()

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


PHOTO_GROUP_CHAT_ID = -1001950066626
ADMIN_USER_IDS = [6690362261, 6689031799]

def check_user_in_database(user_id):
    conn = sqlite3.connect('user_data_b5.db')
    cursor = conn.cursor()
    cursor.execute('SELECT UserId FROM users WHERE UserId = ?', (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data is not None

def get_user_data(user_id):
    conn = sqlite3.connect('user_data_b5.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE UserId = ?', (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data


def get_user_list_from_db():
    conn = sqlite3.connect('user_data_b5.db')
    cursor = conn.cursor()
    cursor.execute('SELECT UserId, UserName FROM users')
    user_data = cursor.fetchall()
    conn.close()
    return user_data





def users(update: Update, context):
    user = update.message.from_user
    user_id = update.message.from_user.id
    
    # Check if the user is an admin
    if user_id in ADMIN_USER_IDS:
        # If the user is an admin, retrieve the user list from the database
        user_data = get_user_list_from_db()
        
        if user_data:
            # Create a formatted user list
            user_info = "\n".join([f"{user[0]}: {user[1]}" for user in user_data])
            update.message.reply_text(f"List of Users:\n{user_info}")
            update.message.reply_text(f"To Add Users use /add")
        else:
            update.message.reply_text("No user data found in the database.\nAnyone need to /start this bot to use this function")
    else:
        # If the user is not an admin, inform them that they can't use this command
        update.message.reply_text("Sorry, you are not authorized to use this command.")
    print(f"{user_id} & @{user.username} Send /users  ")
dispatcher.add_handler(CommandHandler('user', users))
dispatcher.add_handler(CommandHandler(['users', 'user', 'u'], users))










# State constants for conversation handler
USER_ID, USERNAME, FIRST_NAME, LAST_NAME, TIME = range(5)

# Function to check if the user is an admin
def is_admin(update):
    return update.message.from_user.id in ADMIN_USER_IDS

# Function to start the /add command
def add(update: Update, context: CallbackContext):
    if is_admin(update):
        update.message.reply_text("Please provide the following information for the new user:\n"
                                  "User ID, Username, First Name, Last Name, and Time (or type '---' if not specified).\n"
                                  "Separate the information with commas.")

        return USER_ID
    else:
        update.message.reply_text("Sorry, you are not authorized to use this command.")
        return ConversationHandler.END

# Function to receive user information
def receive_user_info(update: Update, context: CallbackContext):
    user_input = update.message.text
    user_info = user_input.split(',')

    if len(user_info) != 5:
        update.message.reply_text("Please provide all five pieces of information.")
        return

    user_id, username, first_name, last_name, time = user_info
    if time == '---':
        time = None

    # Insert this user information into the database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (UserId, FirstName, LastName, UserName, StartTime) VALUES (?, ?, ?, ?, ?)',
                   (user_id, first_name, last_name, username, time))
    conn.commit()
    conn.close()

    update.message.reply_text("User added successfully!")

    return ConversationHandler.END

# Create a conversation handler
conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('add', add)],
    states={
        USER_ID: [MessageHandler(Filters.text & ~Filters.command, receive_user_info)]
    },
    fallbacks=[]
)

# Add the conversation handler to the dispatcher
dispatcher.add_handler(conversation_handler)











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
        conn = sqlite3.connect('user_data_b5.db')
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



def all_response(update:Update,context):
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Hello")
    context.bot.forward_message(-1001556470556, update.message.chat_id, update.message.message_id)
    context.bot.send_message(-1001556470556, text=f"This has in Others Type 🍌🍌🍌 @RanaUniverse (Filters.all)")

dispatcher.add_handler(MessageHandler(Filters.all, all_response))



# Start the bot
updater.start_polling()
updater.idle()
