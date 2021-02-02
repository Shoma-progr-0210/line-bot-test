from reminder.app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Schedule(Base):
    __tablename__ = 'schedule'

    name = db.Column(db.String(30))
    message = db.Column(db.String(255))
    time = db.Column(db.DateTime, nullable=False)

    @classmethod
    def create(cls, id, name, message, time):
        """
        リマインドスケジュールを作成する
        :param id:
        :param name:
        :param message:
        :param time:
        :return: Schedule
        """
        obj = cls(id=id, name=name, message=message, time=time)
        db.session.add(obj)
        return obj

    @classmethod
    def get_by_id(cls, id):
        """
        IDを指定して登録済みスケジュールを取得
        :param id:
        :return: ユーザScheduleリスト
        """
        return db.session.query(cls).filter(cls.id == id).one_or_none()

    # @classmethod
    # def get_all(cls):
    #     """
    #     全スケジュールを取得
    #     :return: 全Scheduleリスト
    #     """
    #     return db.session.query(cls).all()

    @classmethod
    def delete_by_id(cls, id):
        """
        IDを指定してスケジュール削除
        :param id:
        :return: なし
        """
        obj = db.session.query(cls).filter(cls.id == id).first()
        db.session.delete(obj)

    @classmethod
    def delete_by_time(cls, time):
        """
        時間を指定してスケジュール削除
        :param time:
        :return: なし
        """
        obj = db.session.query(cls).filter(cls.time < time).first()
        db.session.delete(obj)


    def __init__(self, name, message, time):
        self.name = name
        self.message = message
        self.time = time

    def __repr__(self):
        return 'Schedule(id={0}, name={1}, message={2}, time{3})'.format(
            self.id, self.name, self.message, self.time
        )
