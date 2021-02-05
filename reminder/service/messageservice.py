from datetime import datetime

from reminder.view.messagebubble import SCHEDULE_BUBBLE, CAROUSEL, FLEX_MESSAGE

class MessageService():
    def create_message_from_list(self, schedules):
        reply_lines = []
        reply_lines.append("予定一覧")
        reply_lines.append("----------------------------------")

        for row in schedules:
            reply_lines.append(f"予定名: {row['name']}")
            reply_lines.append(f"時間: {datetime.strptime(row['time'], '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M')}")
            reply_lines.append(f"メッセージ: {row['message']}")
            reply_lines.append("----------------------------------")

        return "\n".join(reply_lines)

    def create_reminds_from_list(self, schedules):
        remind_msgs = {}
        for row in schedules:
            remind_lines = []

            remind_lines.append("リマインド")
            remind_lines.append("----------------------------------")
            remind_lines.append(f"予定名: {row['name']}")
            remind_lines.append(f"時間: {datetime.strptime(row['time'], '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M')}")
            remind_lines.append(f"メッセージ: {row['message']}")
            remind_lines.append("----------------------------------")

            remind_msgs[row["user_id"]] = "\n".join(remind_lines)

        return remind_msgs

    def create_bubbles_from_list(self, schedules):
        flex_message = FLEX_MESSAGE
        carousel = CAROUSEL
        for row in schedules:
            bubble = SCHEDULE_BUBBLE
            for k, v in row.items():
                if k == "time":
                    bubble["header"]["contents"][0]["text"] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M')
                else:
                    for content in bubble["body"]["contents"]:
                        if content["text"] == k:
                            content["text"] = v
            carousel["contents"].append(bubble)

        flex_message["contents"] = carousel
        return flex_message

