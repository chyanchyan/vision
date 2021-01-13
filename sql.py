import psycopg2 as pg

conn = pg.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

cur = conn.cursor()

sql = 'select * from auth_user'

cur.execute(sql)

print(cur.fetchall())
