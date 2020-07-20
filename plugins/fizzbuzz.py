from slackbot.bot import respond_to

def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    return 'Nothing'

@respond_to(r'^fizzbuzz\s+(\d+)$')
def respond_fizzbuzz(message, digitstr):
    fb = fizzbuzz(int(digitstr))
    message.reply(f'{digitstr}: {fb}')
