import psycopg2

# Use the same connection details from your db_connect.py
connection = psycopg2.connect(
    database="hotel_booking",
    user="postgres",
    password="@Pazad1512",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

# Read and execute the SQL file
with open('exploration.sql', 'r') as sql_file:
    sql_query = sql_file.read()
    cursor.execute(sql_query)
    
    # Fetch and print results
    results = cursor.fetchall()
    for row in results:
        print(row)

cursor.close()
connection.close() 