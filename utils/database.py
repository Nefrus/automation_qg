"""
sqlite 存储

video的操作是每天都可以清除的，因为目前只看新闻联播，暂时不删
"""
import sqlite3
from datetime import datetime, timedelta


class DB(object):
    def __init__(self, db_path="database.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def create_table(self):
        article_sql = 'CREATE TABLE if not exists "article" (' \
                      '"id" integer PRIMARY KEY AUTOINCREMENT, ' \
                      '"title" text(200), ' \
                      '"create_time" text(100))'
        self.cursor.execute(article_sql)
        video_sql = 'CREATE TABLE if not exists "video" (' \
                    '"id" integer PRIMARY KEY AUTOINCREMENT, ' \
                    '"title" text(200), ' \
                    '"create_time" text(100))'
        self.cursor.execute(video_sql)
        self.conn.commit()

    def insert_article(self, title):
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'insert into article (title, create_time) values (?, ?)'
        self.cursor.execute(sql, (title, create_time))
        self.conn.commit()

    def insert_video(self, title):
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'insert into video (title, create_time) values (?, ?)'
        self.cursor.execute(sql, (title, create_time))
        self.conn.commit()

    def generate_data(self, rows):
        names = [d[0] for d in self.cursor.description]
        data = [dict(zip(names, row)) for row in rows]
        return data

    def query_article_by_title(self, title):
        sql = 'select * from article where title=?'
        self.cursor.execute(sql, (title,))
        rows = self.cursor.fetchall()
        if rows:
            rows = self.generate_data(rows)
        # print(rows)
        return rows

    def query_video_by_title(self, title):
        sql = 'select * from video where title=?'
        self.cursor.execute(sql, (title,))
        rows = self.cursor.fetchall()
        if rows:
            rows = self.generate_data(rows)
        # print(rows)
        return rows

    def get_today_time_range(self):
        # 获取当前时间
        now = datetime.now()
        # 获取今天零点
        zero_today = now - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                     microseconds=now.microsecond)
        # 获取23:59:59
        last_today = zero_today + timedelta(hours=23, minutes=59, seconds=59)
        return zero_today, last_today

    def query_article_today_number(self):
        """
        获取当日文章阅读的数量
        :return:
        """
        zero_today, last_today = self.get_today_time_range()
        sql = 'select count(*) from article where ? <= create_time < ?'
        self.cursor.execute(sql, (zero_today, last_today))
        rows = self.cursor.fetchall()
        # print(rows[0][0])
        if not rows:
            return 0
        return rows[0][0]

    def query_video_today_number(self):
        """
        获取当日视频观看的数量
        :return:
        """
        zero_today, last_today = self.get_today_time_range()
        sql = 'select count(*) from video where ? <= create_time < ?'
        self.cursor.execute(sql, (zero_today, last_today))
        rows = self.cursor.fetchall()
        # print(rows[0][0])
        if not rows:
            return 0
        return rows[0][0]


db = DB()

if __name__ == "__main__":
    # db.insert_article("s")
    # db.query_article_by_title("s")
    # db.insert_video("v")
    # db.query_video_by_title("v")
    # db.query_video_by_title("s")
    db.query_article_today_number()
    db.query_video_today_number()
    pass
