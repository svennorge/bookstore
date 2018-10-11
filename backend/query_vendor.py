#!/usr/bin/python

import psycopg2
from config import config

def get_vendors(param1):
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    #    cur.execute("SELECT * FROM users")
        cur.execute("SELECT array_to_json(array_agg(row_to_json(users))) FROM users WHERE name = %s", (param1,))
        print(param1)
        row = cur.fetchone()
        user = row
        while row is not None:
            row = cur.fetchone()
        cur.close()
        return user
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    name = 'sven'
    Users = get_vendors(name)
    print(Users)