

class MessageService():
    def create_message_from_list(self, schedules):
        reply_lines = []
        reply_lines.append("予定一覧")
        reply_lines.append("---------------------")

        for row in schedules:
            reply_lines.append(f"予定名: {row.name}")
            reply_lines.append(f"時間: {row.time}")
            reply_lines.append(f"メッセージ: {row.message}")
            reply_lines.append("---------------------")

        return "\n".join(reply_lines)
        

