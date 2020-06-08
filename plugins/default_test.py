from slackbot.bot import default_reply

@default_reply(r'hoge(.*)')
def test_msg(message):
    message.send('default test')
