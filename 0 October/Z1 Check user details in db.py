import sqlite3
from datetime import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Initialize the bot
BOT_TOKEN = '6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw'  # Replace with your bot token
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Function to create the database and 'users' table if they don't exist
def create_database():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            joining_time DATETIME
        )
    ''')
    conn.commit()
    conn.close()

# Create the database and 'users' table
create_database()

# Function to handle the /start command
def start(update: Update, context: CallbackContext):
    # Create a new database connection
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    
    user = update.message.from_user
    user_info = (user.id, user.username, user.first_name, user.last_name)

    # Check if the user is already in the database
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user.id,))
    existing_user = cursor.fetchone()

    if existing_user:
        message = "Welcome back! You've interacted with the bot before.\n"
        message += "Here's your information:\n"
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user.id,))
        user_data = cursor.fetchone()
        message += f"User ID: <code>{user_data[1]}</code>(Press Here to Copy)\n"
        message += f"Username: <b>{user_data[2]}</b>\n"
        message += f"First Name: {user_data[3]}\n"
        message += f"Last Name: {user_data[4]}\n"
        message += f"Starting Time: {user_data[5]}"
        
    else:
        # Insert the user's information into the database
        joining_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO users (user_id, username, first_name, last_name, joining_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_info[0], user_info[1], user_info[2], user_info[3], joining_time))
        conn.commit()
        message = "Welcome to the bot! You are a new user, and your information has been recorded."

    # Close the database connection
    conn.close()

    update.message.reply_text(message,parse_mode='html')

# Add the /start command handler
dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
updater.idle()
