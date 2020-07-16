#!/usr/local/bin/python3.7
import pymysql


class MyDb:
    # 句柄
    cursor = ''
    # 打开数据库连接
    db = ''
    '''
        定义构造方法
        host：127.0.0.1
        username:root
        password:root
        dbname:testdb
        db:test
        cursor:获取游标句柄
    '''
    def __init__(self, host, username, password, dbname):

        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname

        self.db = pymysql.connect(self.host, self.username, self.password,
                                  self.dbname)
        self.cursor = self.db.cursor()

    # 获取所有的结果集
    def getAllResult(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    # 获取所有的结果集
    def getSignleResult(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchone()
        return results

    # 插入或更新数据
    def insertOrUdateInfo(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        #返回受影响的行数
        return self.cursor.rowcount

    # 关闭链接
    def close(self):
        self.db.close()