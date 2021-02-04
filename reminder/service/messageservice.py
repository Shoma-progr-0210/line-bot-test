

class MessageService():
    def create_message_from_list(self, schedules):
        reply_lines = []
        reply_lines.append("予定一覧")
        reply_lines.append("----------------------------------")

        for row in schedules:
            reply_lines.append(f"予定名: {row['name']}")
            reply_lines.append(f"時間: {row['time'].strftime('%Y/%m/%d %H:%M')}")
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
            remind_lines.append(f"時間: {row['time'].strftime('%Y/%m/%d %H:%M')}")
            remind_lines.append(f"メッセージ: {row['message']}")
            remind_lines.append("----------------------------------")

            remind_msgs[row["user_id"]] = "\n".join(remind_lines)

        return remind_msgs

