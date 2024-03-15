from mysql import connector as cnt
db=cnt.connect(
    host='LocalHost',
    user='Kishore',
    password='dk1119',
    port=3000
)
cur=db.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS pw')
print(cur)
db.close()