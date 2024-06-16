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


    # Create a keyboard with a referral link button
    keyboard = [
        [InlineKeyboardButton("1", url=deep_link),
        InlineKeyboardButton("2", url=deep_link),
        InlineKeyboardButton("3", url=deep_link),
        InlineKeyboardButton("4", url=deep_link),],
        
        [InlineKeyboardButton("5", url=deep_link),
        InlineKeyboardButton("6", url=deep_link),
        InlineKeyboardButton("7", url=deep_link),
        InlineKeyboardButton("8", url=deep_link),],

        [InlineKeyboardButton("9", url=deep_link),
        InlineKeyboardButton("10", url=deep_link)],
    ]

    # keyboard = [
        # [InlineKeyboardButton("Referral Link", url=deep_link)],
        # [InlineKeyboardButton("Referral Link", url=deep_link)],
    # ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(user_id, "Here's your referral link:", reply_markup=reply_markup)

# Command handler for users to check their referral count
def check_referrals(update, context):
    user_id = update.message.from_user.id

    if user_id in referrals:
        referred_users = referrals[user_id]
        referral_count = len(referred_users)
        referred_users_text = ", ".join([str(user) for user in referred_users])
        message = f"You've referred {referral_count} users: {referred_users_text}"
    else:
        message = "You haven't referred any users yet."

    context.bot.send_message(user_id, message)

# Set up the bot
updater = Updater(token='6653295841:AAGIP4GdaWiZGPOW-dfktXKPn82Ao9T3Kjw', use_context=True)
dispatcher = updater.dispatcher

# Add a handler for the /start command to handle referral links
dispatcher.add_handler(CommandHandler('start', handle_referral, pass_args=True))

# Add a handler for the /getreferrallink command to generate a referral link
dispatcher.add_handler(CommandHandler('getreferrallink', get_referral_link))
dispatcher.add_handler(CommandHandler('a', get_referral_link))

# Add a handler for the /checkreferrals command to check referral count
dispatcher.add_handler(CommandHandler('checkreferrals', check_referrals))
dispatcher.add_handler(CommandHandler('b', check_referrals))

# Start the bot
updater.start_polling()
updater.idle()
