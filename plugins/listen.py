from slackbot.bot import listen_to
from . import todo
import time, re

# 初めの文字が!ならコマンドと判断
@listen_to(r'^!.*')
def com_set(message):
    text = message.body['text'][1:]

    todo_add = re.search(r'^add\s+(\S+)\s+(\S+)$', text)
    todo_list = re.search(r'^list$', text)
    todo_reset = re.search(r'^reset$', text)
    todo_search = re.search(r'^search\s+(\S+)$', text)
    todo_change_id = re.search(r'^change\s+(\S+)\s+(\S+)\s+(\S+)$', text)

    if todo_add:
        todo.todo_add(message, todo_add.group(1), todo_add.group(2))
    elif todo_list:
        todo.todo_list(message)
    elif todo_reset:
        todo.todo_reset(message)
    elif todo_search:
        todo.todo_search(message, todo_search.group(1))
    elif todo_change_id: 
        todo.todo_change_id(message, todo_change_id.group(1), \
            todo_change_id.group(2), todo_change_id.group(3))
    else:
        message.reply('このコマンドは無効です')

@listen_to('what')
def listen_what(message):
    message.reply('??')