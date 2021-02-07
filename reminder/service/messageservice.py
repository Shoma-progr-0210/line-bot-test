from datetime import datetime
import copy

from reminder.view.messagebubble import SCHEDULE_BUBBLE, REMIND_BUBBLE, CAROUSEL

class MessageService():

    def create_reminds_from_list(self, schedules):
        remind_msgs = {}
        for row in schedules:
            if not row["user_id"] in remind_msgs:
                remind_msgs[row["user_id"]] = []
            remind_msgs[row["user_id"]].append(self.create_bubble(row, copy.deepcopy(REMIND_BUBBLE)))

        return remind_msgs

    def create_carousel_from_list(self, schedules):
        carousel = copy.deepcopy(CAROUSEL)
        for row in schedules:
            bubble = self.create_bubble(row, copy.deepcopy(SCHEDULE_BUBBLE))
            carousel["contents"].append(bubble)

        return carousel

    def create_bubble(self, schedule, bubble):
        for k, v in schedule.items():
            if k == "time":
                bubble["header"]["contents"]["contents"][0]["text"] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M')
            else:
                for i, content in enumerate(bubble["body"]["contents"]):
                    if content["text"] == k:
                        bubble["body"]["contents"][i]["text"] = v
        
        return bubble

