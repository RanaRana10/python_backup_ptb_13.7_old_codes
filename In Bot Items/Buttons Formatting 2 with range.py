from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Initialize the dictionary to track referrals
referrals = {}

# Function to handle users joining through a referral link

def handle_referral(update, context):
    user_id = update.message.from_user.id

    if context.args:
        custom_code = context.args[0]  # Extract the custom code from the /start command

        referrer_id = int(custom_code)  # You would map the custom code to a user ID

        # Check if the referrer is already in the referrals dictionary
        if referrer_id not in referrals:
            referrals[referrer_id] = []

        # Add the new user to the list of referrals for the referrer
        referrals[referrer_id].append(user_id)

        # Notify the referrer about the successful referral
        context.bot.send_message(referrer_id, f"You've successfully referred a new user!")

        # Notify the new user about receiving a token for the referral
        context.bot.send_message(user_id, "Welcome to the bot! You have received 1 token for joining through a referral link.")

    else:
        # Welcome the new user who started with just /start
        context.bot.send_message(user_id, "Welcome to the bot!\nYou have start without any referal code")



# Command handler to generate a referral link
def get_referral_link(update, context):
    user_id = update.message.from_user.id
    referral_code = user_id

    # Generate a deep link with the user's ID as the referral code
    deep_link = f"https://t.me/Fake999Bot?start={referral_code}"
    context.bot.send_message(user_id, f"Here's your referral link: {deep_link}")

    from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Define your buttons with labels and URLs
    buttons = [
    ("1", "https://www.google.com"),
    ("2", "https://www.youtube.com"),
    ("3", "https://www.facebook.com"),
    ("4", "https://www.twitter.com"),
    ("5", "https://www.instagram.com"),
    ("6", "https://www.linkedin.com"),
    ("7", "https://www.reddit.com"),
    ("8", "https://www.amazon.com"),
    ("9", "https://www.netflix.com"),
    ("10", "https://www.nytimes.com"),
    ("11", "https://www.cnn.com"),
    ("12", "https://www.bbc.com"),
    ("13", "https://www.wikipedia.org"),
    ("14", "https://www.apple.com"),
    ("15", "https://www.microsoft.com"),
    ("16", "https://www.github.com"),
    ("17", "https://www.stackoverflow.com"),
    ("18", "https://www.instagram.com"),
    ("19", "https://www.pinterest.com"),
    ("20", "https://www.twitch.tv"),
]


    # Determine the number of buttons to display in each row
    buttons_per_row = [5, 1, 3, 2, 2, 5, 2]

    # Create the keyboard with buttons arranged in rows
    keyboard = []

    for i in range(len(buttons_per_row)):
        row = []
        for j in range(buttons_per_row[i]):
            label, url = buttons.pop(0)
            row.append(InlineKeyboardButton(label, url=url))
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(user_id, "Here's your referral link:", reply_markup=reply_markup)







# Set up the bot
updater = Updater(token='6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw', use_context=True)
dispatcher = updater.dispatcher

# Add a handler for the /getreferrallink command to generate a referral link
dispatcher.add_handler(CommandHandler('getreferrallink', get_referral_link))
dispatcher.add_handler(CommandHandler('a', get_referral_link))

# Start the bot
updater.start_polling()
updater.idle()
