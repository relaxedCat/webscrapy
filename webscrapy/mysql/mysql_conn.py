__author__ = 'xXl'
import MySQLdb
def dbHandle():
    conn =  MySQLdb.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='crapy',
        charset = 'utf8')
    return conn