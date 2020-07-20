# slack-todo
ToDo 管理とその他さまざまな反応をする slackbot

## 機能
* plugins/hello.py
  - `@bot hello`: bot 宛の 'hello を含む文字列' に対して「こんにちは」と返す

* plugins/fizzbuzz.py
  - `@bot fizzbuzz {数字}`: bot 宛の 'fizzbuzz {数字}' に対して Fizz Buzz ゲームの反応

* plugins/listen.py
  - チャンネル内で 'what' を含む文字列の発言に対して「??」と返す
  - ! で始まるものをコマンドとみなし、todo.pyと同様の内容を実行する(todoの入力は省略)

* plugins/todo.py
  - `@bot todo add 'タイトル' [締切]`: ToDo 内容を登録する
  - `@bot todo list`: ToDo の一覧を表示する
  - `@bot todo reset`: ToDo の DB をリセットする
  - `@bot todo search '検索文字列'`: 検索文字列がtitleに含まれている場合、その内容を表示する

## ToDo DBのスキーマ
| id | title |     limit_at     |    update_at     | status |  noticetime  |    user     |
|----|-------|------------------|------------------|--------|--------------|-------------|
|  1 | test1 | 2020/04/30 23:59 | 2020/04/01 13:10 |   済   |       0      | S2340A7K6Q4 |
|  2 | test2 | 2020/07/30 7:05  | 2020/06/01 17:00 |   未   |       3      | S2340A7K6Q4 |
* 上のuseridは存在しないものである

## ToDo DBの操作関数
* `add(title, limit_at)`: title と limit_at (有効期限) を登録
* `add(title)`: title を無期限の有効期限として登録
* `list()`: ToDo DB のデータを一覧した文字列を返す
* `reset()`: ToDo DB の内容を削除し，空のデータベースを作成
* `add_dict(data)`:列名をkey、データの値をvalueとするdictのデータをToDo DBに登録　#6　に詳細あり
* `dict_list()`ToDo DB の各データをそれぞれdictにして、dictのリストを返す #6　に詳細あり
* `select_id(id)`指定したidのデータをdictにして返す #6　に詳細あり
* `clean()`主に開発時、テーブルの列の更新、不正なデータの削除を行う
* `change_id(id, column, value)`指定したidのデータの値を変更する
* `search(column, text)`columnの値にtextが含まれる場合そのデータをlist形式(要素はdict形式)で返す

## 諸機能の補助関数(tools.py)
* `getmsginfo(message)`:messageからユーザー情報を取得
* `datetrans(limit_at, now, mode=0)`:userが入力した文字列(limit_at)を既定の形式に変換する
* `limit_datetime(assignment, mode=0)`:datetime型でlimit_atを返す
* `autostatus(assignment, now, mode=0)`:assignmentの期限と現在時刻からstatusを判定
* `postMessage(text, attachments, channel, username="お知らせ", icon_emoji)`:messageをpost
* `updateMessage(text, attachments, ts, channel, username="お知らせ", icon_emoji)`:messageを編集
* `noticetimeSet(limit_at:datetime, now)`:期限から残り通知回数を定める

## テスト用プログラム
* test_regex.py
  - 正規表現の確認プログラム
  - 正規表現のパターンを入力し，その後，文字列を入力するとパターンにマッチしているかどうかを判定
  - `python test_regex.py`

* test_tododb.py
  - tododb.py のテストプログラム
  - tododb.py で定義した関数をテストするためのプログラム
