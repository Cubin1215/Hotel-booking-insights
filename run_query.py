import psycopg2
from tabulate import tabulate
import pandas as pd
import sys
import re

def get_query_number():
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            print("Please provide a valid query number")
            sys.exit(1)
    else:
        print("Please provide a query number as argument")
        print("Example: py run_query.py 1")
        sys.exit(1)

def extract_queries(sql_content):
    # Split the content by section markers
    sections = re.split(r'-- =+.*?=+\s*', sql_content)
    queries = []
    
    for section in sections:
        if section.strip():
            # Find all SQL statements in the section
            sql_statements = re.findall(r'SELECT.*?;', section, re.DOTALL | re.IGNORECASE)
            queries.extend(sql_statements)
    
    return queries

# Use the same connection details from your db_connect.py
connection = psycopg2.connect(
    database="hotel_booking",
    user="postgres",
    password="@Pazad1512",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

# Read the SQL file
with open('exploration.sql', 'r') as sql_file:
    sql_content = sql_file.read()
    queries = extract_queries(sql_content)

# Get the query number from command line
query_number = get_query_number()

# Check if the query number is valid
if query_number < 1 or query_number > len(queries):
    print(f"Invalid query number. Please choose between 1 and {len(queries)}")
    print("\nAvailable queries:")
    for i, query in enumerate(queries, 1):
        print(f"\nQuery {i}:")
        print("-" * 40)
        print(query.strip())
    sys.exit(1)

# Execute the selected query
selected_query = queries[query_number - 1]
print(f"\nExecuting Query {query_number}:")
print("=" * 80)
print(selected_query.strip())
print("=" * 80)

try:
    cursor.execute(selected_query)
    
    # Get column names
    column_names = [desc[0] for desc in cursor.description]
    
    # Fetch results
    results = cursor.fetchall()
    
    # Convert to pandas DataFrame for better formatting
    df = pd.DataFrame(results, columns=column_names)
    
    # Print results in a nice tabular format
    print("\nQuery Results:")
    print("=" * 80)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    print("=" * 80)
    print(f"\nTotal rows: {len(df)}")

except Exception as e:
    print(f"Error executing query: {e}")

cursor.close()
connection.close() 