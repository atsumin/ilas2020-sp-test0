import os
import datetime as dt
import time
from tododb import DB
from . import tools


class Notice():

    def __init__(self):
        self.__notice_notdone()

    def notice(self):
        self.__notice_notdone()


    def __notice_notdone(self):
        self.now = dt.datetime.now()
        db = DB(os.environ['TODO_DB'])
        self.dict_list = db.dict_list()
        self.channel = os.environ['SLACK_CHANNEL']
        for dict in self.dict_list:
            # 前バージョンとの互換性を保つ
            if not "noticetime" in dict.keys():
                continue
            noticetime = int(dict['noticetime'])
            try:
                self.__limit_at = dt.datetime.strptime(dict["limit_at"], '%Y/%m/%d %H:%M')
                # statusの更新
                if self.now > self.__limit_at and dict['status'] == '未':
                    db.change_id(dict['id'], 'status', '期限切れ')
            except:
                break
            color = ''
            text = ''
            post = False
            if dict["status"] == '未':                
                if self.__limit_at < self.now + dt.timedelta(hours=1) and noticetime == 1:
                    text = "期限まであと１時間。ひょっとして提出し忘れてるんじゃ？:face_with_rolling_eyes::face_with_rolling_eyes:"
                    noticetime = 0
                    color = 'ff4500'
                    post = True
                elif self.__limit_at < self.now + dt.timedelta(days=1) and noticetime == 2:
                    text = "期限まであと１日もありません！！のんびりしてる暇なんてありませんね:sweat_drops:"
                    noticetime = 1
                    color = 'ffff00'
                    post = True
                elif self.__limit_at < self.now + dt.timedelta(days=3) and noticetime == 3:
                    text = "期限まであと３日。そろそろとりかかろう...:sunglasses:"
                    noticetime = 2
                    color = '7cfc00'
                    post = True
            if post == True:
                attachments = [
                    {
                        "color":color,
                        "blocks":[
                            {
                                "type":"section",
                                "text":{
                                    "type":"mrkdwn",
                                    "text": '*'+ dict["title"] + '*\n' + '期限：' + dict["limit_at"] + '\nid：' + dict["id"]
                                }
                            }
                        ]
                    }
                ] 
                tools.postMessage(text, attachments, channel=self.channel, icon_emoji=":panda_face:")
                db.change_id(dict['id'], 'noticetime', noticetime)


