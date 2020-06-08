from slackbot.bot import listen_to

@listen_to('what')
def listen_what(message):
    message.reply('??')
    
