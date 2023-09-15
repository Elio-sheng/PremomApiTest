# -*- coding: gbk -*-

import pymysql
import os
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["mysql"]     #获取config/setting.ini 文件里的MySQL配置数据

DB_CONF = {
    "host": data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWD"],
    "db": data["MYSQL_DB"]
}


class MysqlDb:
    """
    A class representing a MySQL database connection.

    Attributes:
        conn: The MySQL connection object.
        cur: The cursor object to execute queries.

    Methods:
        __init__: Initializes the MySQL connection and cursor.
        __del__: Closes the cursor and connection.
        select_db: Executes a SELECT query and returns the results.
        execute_db: Executes an UPDATE/INSERT/DELETE query.
    """

    def __init__(self, db_conf=DB_CONF):
        """
        Initializes the MySQL connection and cursor.

        Args:
            db_conf: A dictionary containing the MySQL database configuration.
        """
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        """
        Closes the cursor and connection.
        """
        self.cur.close()
        self.conn.close()

    def select_db(self, sql):
        """
        Executes a SELECT query and returns the results.

        Args:
            sql: The SELECT query to execute.

        Returns:
            The query results as a list of dictionaries.
        """
        self.conn.ping(reconnect=True)    #确保数据库连接仍然有效。通过调用 ping 方法并传入 reconnect=True，它将会尝试重新连接数据库，从而保持连接的活跃状态。
        self.cur.execute(sql)     #执行了传入的 SQL 查询语句。self.cur 是一个执行数据库操作的游标对象，通过调用 execute 方法并传入 sql 参数，实现执行查询的功能
        data = self.cur.fetchall()   #获取查询结果集中的所有数据。self.cur.fetchall() 方法返回所有的查询结果，存储在名为 data 的变量中。
        return data

    def execute_db(self, sql):
        """
        Executes an UPDATE/INSERT/DELETE query.

        Args:
            sql: The UPDATE/INSERT/DELETE query to execute.
        """
        try:
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("An error occurred while operating MySQL, reason: {}".format(e))
            self.conn.rollback()


db = MysqlDb(DB_CONF)

if __name__ == '__main__':

    db.select_db("select user_id,email from ezhome.all_login where email like 'test5_%';")