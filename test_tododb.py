from tododb import DB
import os

dbname = os.environ['TODO_DB']
need_init = not os.path.exists(dbname)
database = DB(dbname)
if need_init:
    database.init()

database.add('test-title1', '2020-06-01')
print(database.list())
