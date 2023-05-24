	
import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="currensee",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS coins;')

cur.execute('CREATE TABLE coins (id serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'ticker varchar (50) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO coins (name, ticker)'
            'VALUES (%s, %s)',
            ('Tether',
             'USDT',
)
            )

conn.commit()

cur.close()
conn.close()