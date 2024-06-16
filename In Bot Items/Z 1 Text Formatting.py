# this is just text formatting not works at all

# Function to handle the /b command with HTML formatting
def b_command(update, context):
    # Provide an example message with different formatting styles
    user = update.message.from_user
    user_info = f"Username: @{user.username}, Name: {user.first_name} {user.last_name or ''}"
    print(f"{user_info} - User Command: {update.message.text}")

    # Format the text with different styles using HTML
    b_example_message = """
    # <b>Bold Text</b>: This is an example of <b>bold text</b>.
    # <i>Italic Text</i>: This is an example of <i>italic text</i>.
    # <u>Underlined Text</u>: This is an example of <u>underlined text</u>.
    # <s>Strikethrough Text</s>: This is an example of <s>strikethrough text</s>.
    # <span class="tg-spoiler">Spoiler Text</span>: This is an example of spoiler text.
    # <a href="http://www.example.com">Inline Link</a>: This is an inline link.
    # <a href="tg://user?id=123456789">Inline Mention of a User</a>: This is an inline mention of a user.
    # <tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>: This is an inline emoji.
    # <code>Inline Fixed-Width Code</code>: This is inline fixed-width code.
    # <pre>Pre-formatted Fixed-Width Code Block</pre>: This is a pre-formatted fixed-width code block.
    """

    # Send the formatted text with HTML parse mode
    context.bot.send_message(chat_id=update.message.chat_id, text=b_example_message, parse_mode='HTML')

