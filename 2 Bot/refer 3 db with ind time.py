import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime
import pytz


# Set up the bot
updater = Updater(token='6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw', use_context=True)
dispatcher = updater.dispatcher



# Create a SQLite database and table
conn = sqlite3.connect('refer3.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY,
        referrer_id INTEGER,
        referred_user_id INTEGER,
        time TEXT
    )
''')
conn.commit()

# Function to handle users joining through a referral link
def handle_referral(update, context):
    user_id = update.message.from_user.id

    # Create a new connection and cursor in this thread
    conn = sqlite3.connect('refer3.db')
    cursor = conn.cursor()

    if context.args:
        custom_code = context.args[0]  # Extract the custom code from the /start command

        referrer_id = int(custom_code)

        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute('INSERT INTO referrals (referrer_id, referred_user_id, time) VALUES (?, ?, ?)', (referrer_id, user_id, current_time))
        conn.commit()


        # Notify the referrer about the successful referral
        context.bot.send_message(referrer_id, "You've successfully referred a new user!")

        # Notify the new user about receiving a token for the referral
        context.bot.send_message(user_id, "Welcome to the bot! You have received 1 token for joining through a referral link.")
    else:
        context.bot.send_message(user_id, "Welcome to the bot!\nYou have started without any referral code")

    # Close the connection
    conn.close()






# Command handler to generate a referral link
def get_referral_link(update, context):
    user_id = update.message.from_user.id
    referral_code = user_id

    deep_link = f"https://t.me/Fake999Bot?start={referral_code}"
    ru = f"tg://user?id=6690362261"
    context.bot.send_message(user_id, f"Here's your referral link: {deep_link}")

    keyboard = [
        [InlineKeyboardButton("Referral Link", url=deep_link)],
        [InlineKeyboardButton("Channel Link", url=ru)],
    ]

    context.bot.send_message(user_id, "Here's your referral link:", reply_markup=InlineKeyboardMarkup(keyboard))

# Command handler for users to check their referral count and list of referred users
# Command handler for users to check their referral count and list of referred users
def check_referrals(update, context):
    user_id = update.message.from_user.id

    conn = sqlite3.connect('refer3.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM referrals WHERE referrer_id = ?', (user_id,))
    referral_count = cursor.fetchone()[0]

    if referral_count > 0:
        cursor.execute('SELECT referred_user_id, referred_user_name, time FROM referrals WHERE referrer_id = ?', (user_id,))
        referred_users = cursor.fetchall()
        
        message = f"You've referred <b>{referral_count}</b> users:\n"
        for user in referred_users:
            referred_user_id, referred_user_name, time = user
            # Displaying the referred user's ID, name, and the timestamp
            message += f"User ID: {referred_user_id}, Name: {referred_user_name}, Referral Time: <b>{time}</b>\n\n"
            if len(message) > 2000:
                context.bot.send_message(user_id, message, parse_mode='html')
                message = ""

        # Send the last part of the message if any
        # if message:
        #     context.bot.send_message(user_id, message, parse_mode='html')

    else:
        message = "You haven't referred any users yet.\n<b>To Refer a New User</b>, press /a"

    context.bot.send_message(user_id, message, parse_mode='html')
    conn.close()


    
dispatcher.add_handler(CommandHandler('start', handle_referral, pass_args=True))

dispatcher.add_handler(CommandHandler('getreferrallink', get_referral_link))
dispatcher.add_handler(CommandHandler('a', get_referral_link))
dispatcher.add_handler(CommandHandler('about', get_referral_link))

dispatcher.add_handler(CommandHandler('checkreferrals', check_referrals))
dispatcher.add_handler(CommandHandler('b', check_referrals))

# Start the bot
updater.start_polling()
updater.idle()
