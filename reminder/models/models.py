from reminder.database import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Schedule(Base):
    __tablename__ = 'schedule'

    user_id = db.Column(db.String(50))
    name = db.Column(db.String(30))
    message = db.Column(db.String(255))
    time = db.Column(db.DateTime, nullable=False)

    @classmethod
    def create(cls, user_id, name, message, time):
        """
        リマインドスケジュールを作成する
        :param user_id:
        :param name:
        :param message:
        :param time:
        :return: Schedule
        """
        obj = cls(user_id=user_id, name=name, message=message, time=time)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def get_by_id(cls, user_id):
        """
        user_idを指定して登録済みスケジュールを取得
        :param user_id:
        :return: ユーザScheduleリスト
        """
        return db.session.query(cls).filter(cls.user_id == user_id).one_or_none()

    # @classmethod
    # def get_all(cls):
    #     """
    #     全スケジュールを取得
    #     :return: 全Scheduleリスト
    #     """
    #     return db.session.query(cls).all()

    @classmethod
    def delete_by_id(cls, user_id):
        """
        user_idを指定してスケジュール削除
        :param user_id:
        :return: なし
        """
        obj = db.session.query(cls).filter(cls.user_id == user_id).first()
        db.session.delete(obj)
        db.session.commit()

    @classmethod
    def delete_by_time(cls, time):
        """
        時間を指定してスケジュール削除
        :param time:
        :return: なし
        """
        obj = db.session.query(cls).filter(cls.time < time).first()
        db.session.delete(obj)
        db.session.commit()


    def __init__(self, user_id, name, message, time):
        self.user_id = user_id
        self.name = name
        self.message = message
        self.time = time

    def __repr__(self):
        return 'Schedule(id={0}, user_id={1}, name={2}, message={3}, time{4})'.format(
            self.id, self.user_id, self.name, self.message, self.time
        )
