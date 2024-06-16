pip install python-telegram-bot==13.7



update.message.text          
update.message.photo         
update.message.sticker       
update.message.document      
update.message.voice         
update.message.location      
update.message.caption       
update.message.reply_to_message 


Here will only send message:
context.bot.send_message(chat_id=update.message.chat_id, text=banana_emojis)


For reply to same chat id 

