import pymysql
import random

if __name__ == '__main__':
    db = pymysql.connect('localhost','root','huzhu0313','wenda',charset='utf8')
    try:
        cursor = db.cursor()
        sql = 'insert into question(title, content, user_id, created_date, comment_count) values ("%s","%s",%d, %s, %d)' % (
        'title', 'content', random.randint(1, 10), 'now()', 0)
        # print sql
        cursor.execute(sql)
        qid = cursor.lastrowid
        db.commit()
        print(qid)

        # sql = 'select * from question order by id desc limit 2'
        # cursor.execute(sql)
        # for each in cursor.fetchall():
        #     print(each)

    except Exception as e:
        print(e)
        db.rollback()
    db.close()