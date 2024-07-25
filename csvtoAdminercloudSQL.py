import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

try:
    print('Opening connection...')
    # Connect to MySQL
    with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password
        ) as connection:

        print('Opening cursor...')
        cursor = connection.cursor()
        print('Inserting new record...')

        # Define the SQL statement to create a table
        create_order_table_query = """
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(255),
            customer_address VARCHAR(300),
            customer_phone VARCHAR(100),
            courier INT,
            status VARCHAR(250),
            items VARCHAR(250)
        );
        """  # Replace column names and types as needed
        create_product_table_query = """
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product VARCHAR(255),
            price INT,
        );
        """
        # Execute the create table query
        cursor.execute(create_order_table_query)
        cursor.execute(create_product_table_query)
        print("Tables created successfully.")
        # Read data from the CSV file

        order_file = 'orders.csv'
        with open(order_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            order_data = [
                (row['customer_name'], row['customer_address'], row['customer_phone'], row['courier'], row['status'], row['items'])
                for row in reader
            ]
        
        # Insert data into the table
        insert_orders_sql = """
        INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.executemany(insert_orders_sql, order_data)
         
         # Read data from the product CSV file

        product_file = 'products.csv'
        with open(product_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            product_data = [
                (row['name'], row['price'])
                for row in reader
            ]

        # Insert data into the product table
        insert_product_sql = """
            INSERT INTO orders (name, price)
            VALUES (%s, %s)
        """
        cursor.executemany(insert_product_sql, product_data)

          # Commit the transaction
        connection.commit()

        print("Data inserted successfully.")

except Exception as ex:
    print('Failed to:',ex)

finally:
    if 'cursor' in locals():
        cursor.close()

print('All done')
