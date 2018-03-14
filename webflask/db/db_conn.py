import ibm_db

class Db_coon():
    def __init__(self):
        self.url = "DATABASE=webdb;HOSTNAME=192.168.8.7;PORT=60000;PROTOCOL=TCPIP;UID=web_dba;PWD=web_dba;"

    def select(self,sql,*args):
        try:
            conn = ibm_db.connect(self.url,"","")
            if conn:
                stmt = ibm_db.prepare(conn,sql)
                ibm_db.execute(stmt, args)
                result = ibm_db.fetch_both(stmt)
                return result
            else:
                return None
        except Exception as e:
            print(e)
        finally:
            ibm_db.close(conn)

