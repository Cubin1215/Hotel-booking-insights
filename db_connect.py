import psycopg2

try:
    connection = psycopg2.connect(
        database="hotel_booking",
        user="postgres",         # default user is postgres
        password="@Pazad1512",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()
    print("Connected to the database!")

    # Optional: Check existing tables
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cursor.fetchall()
    print("Tables:", tables)

    cursor.close()
    connection.close()

except Exception as error:
    print("Error while connecting to PostgreSQL", error)
