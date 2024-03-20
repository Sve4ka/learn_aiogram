import pprint

import psycopg2

from db.config import NAME_DB, NAME_U, PASS, HOST


def add_apple():
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    c2 = conn.cursor()
    c2.execute('UPDATE fruit SET count = {} WHERE fruit_id =1'.format(count_apple() + 1))
    c2.close()
    conn.commit()
    conn.close()


def eat_apple():
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    c3 = conn.cursor()
    c3.execute('UPDATE fruit SET count = {} WHERE fruit_id =1'.format(count_apple() - 1))
    c3.close()
    conn.commit()
    conn.close()


def count_apple():
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)

    c1 = conn.cursor()
    c1.execute("SELECT count FROM fruit WHERE fruit_id = 1")
    count = c1.fetchone()[0]
    c1.close()
    conn.close()
    return int(count)


def my_fruit_count(id):
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cur = conn.cursor()
    cur.execute("SELECT * FROM fruit WHERE saler_id = {}".format(id))
    fruit = cur.fetchall()
    print(fruit)
    return fruit


def search_user(id):
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    lst = [i[3] for i in users]
    return id in lst


def add_user(id, name):
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    c3 = conn.cursor()
    c3.execute("insert into users values ({}, '{}', true, {})".format(free_user_id() + 1, "@" + name, id))
    c3.close()
    conn.commit()
    conn.close()


def add_fruits(id, price, name, count):
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    c3 = conn.cursor()
    print(free_fruit_id() + 1, id, price, name, count)
    # c3.execute("insert into fruit values ({}, {}, {}, '{}', {})".format(free_fruit_id()+1, id, price, name, count))
    sql_query = "insert into fruit values (%s, %s, %s, %s, %s)"
    c3.execute(sql_query, (free_fruit_id() + 1,
                           id,
                           price,
                           name,
                           count))
    c3.close()
    conn.commit()
    conn.close()


def free_user_id():
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    maxx = max([i[0] for i in users])
    return maxx


def free_fruit_id():
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cur = conn.cursor()
    cur.execute("SELECT * FROM fruit")
    users = cur.fetchall()
    tmp = [i[0] for i in users]
    maxx = max(tmp)
    print(maxx)
    return maxx


try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)

    cursor = conn.cursor()
    # add_apple()
    cursor.execute('SELECT * FROM fruit')
    all_users = cursor.fetchall()
    cursor.close()  # закрываем курсор
    conn.close()
    print(count_apple())
    pprint.pprint(all_users)
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
