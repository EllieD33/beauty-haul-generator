import mysql.connector

from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


# Establishes a connection to the given database
def _connect_to_db(database_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=database_name
    )
    return connection


# Saves a new user routine
def insert_new_user_routine(user_routine):
    db_name = "beauty_haul_generator"
    db_connection = None
    try:
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()

        # First add a new record to the user_routines table
        query = """INSERT INTO user_routines (user_id) VALUES (1)"""  # We only have guest user currently, 1 is the guest id.
        cursor.execute(query)

        # Get the routine_id that was just created in DB
        routine_id = cursor.lastrowid

        # Insert each product to the routine_products table
        for product in user_routine:
            product_dict = product.routine_to_dict()
            query = """INSERT INTO routine_products (routine_id, brand, product, price, product_desc, score)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (
                routine_id,
                product_dict['Brand'],
                product_dict['Product'],
                product_dict['Price'],
                product_dict['Description'],
                product_dict['Score']
            ))

        db_connection.commit()

        # select most recently added routine id, and get associated products, print to terminal
        cursor.execute("""
        SELECT brand, product, price, product_desc
        FROM routine_products 
        WHERE routine_id = (
            SELECT MAX(id) FROM user_routines
            )
        """)
        print("\n✨Here is your most recently saved routine: ")
        for row in cursor.fetchall():
            cleaned_row = [str(cell) for cell in row if cell is not None]
            if cleaned_row:  # Skip empty rows
                print(" | ".join(cleaned_row))

    except Exception:
        raise DbConnectionError("\n⚠️ Error: Failed to write routine to DB")
    finally:
        if db_connection:
            db_connection.close()

def retrieve_routine():
    db_name = "beauty_haul_generator"
    db_connection = None
    try:
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()

        query = """
        SELECT routine_id, brand, product, price, product_desc, score
        FROM routine_products
        WHERE routine_id = (
            SELECT MAX(id) FROM user_routines
        )
        """
        cursor.execute(query)

        results = cursor.fetchall()

        routine_data = []
        for row in results:
            product_dict = {
                "Brand": row[1],
                "Product": row[2],
                "Price": row[3],
                "Description": row[4],
                "Score": row[5]
            }

            routine_data.append(product_dict)

        return routine_data

    except Exception:
        raise DbConnectionError("\n⚠️ Error: Failed to write routine to DB")
    finally:
        if db_connection:
            db_connection.close()

if __name__ == "__main__":
    pass