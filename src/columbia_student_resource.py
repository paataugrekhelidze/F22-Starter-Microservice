import pymysql


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        conn = pymysql.connect(
            user="paugre",
            password="password",
            host="localhost",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students_hw where uni=%s;"
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

