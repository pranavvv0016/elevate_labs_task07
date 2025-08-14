import sqlite3

conn = sqlite3.connect("sales_data.db")
c = conn.cursor()

# Drop the table if it already exists
c.execute("DROP TABLE IF EXISTS sales")

# Create the sales table
c.execute('''
    CREATE TABLE sales (
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Insert some sample data
c.execute("INSERT INTO sales VALUES ('laptop', 2, 1200)")
c.execute("INSERT INTO sales VALUES ('mouse', 5, 25)")
c.execute("INSERT INTO sales VALUES ('keyboard', 3, 75)")
c.execute("INSERT INTO sales VALUES ('laptop', 1, 1200)")
c.execute("INSERT INTO sales VALUES ('mouse', 2, 25)")

conn.commit()
conn.close()