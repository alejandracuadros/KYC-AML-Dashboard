from db_utils import _connect_to_db, close_db_connection


# Function to check for incomplete data and null values
def check_null_startup_data(connection):
    cursor = None
    try:
        cursor = connection.cursor()
        query = """
        SELECT COUNT(*)
        FROM regulatory_compliance.startups
        WHERE name IS NULL OR country IS NULL OR founder_name IS NULL;
        """
        cursor.execute(query)
        result = cursor.fetchone()
        print(f"Startups with incomplete data: {result[0]}")
    except Exception as e:
        print(f"There was an error while checking for incomplete startup data: {e}")
    finally:
        if cursor:
            cursor.close()


# Function to check for invalid funding stages in startups
def check_invalid_funding_stages(connection):
    cursor = None
    try:
        cursor = connection.cursor()
        query = """
        SELECT startup_id, name, funding_stage
        FROM regulatory_compliance.startups
        WHERE funding_stage NOT IN ('Seed', 'Series A', 'Series B', 'Series C', 'IPO');
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print(f"Startups with invalid funding stages:")
        for row in result:
            print(row)
    except Exception as e:
        print(f"There was an error while checking for invalid funding stages: {e}")
    finally:
        if cursor:
            cursor.close()


# Function to insert a new startup
def insert_new_startup(connection, name, country, founder_name, industry, funding_stage, is_sustainable):
    cursor = None
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO regulatory_compliance.startups (
        name, country, founder_name, industry, funding_stage, is_sustainable)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, country, founder_name, industry, funding_stage, is_sustainable))
        connection.commit()
        print("Startup successfully inserted")
    except Exception as error:
        print(f"Something went wrong while inserting a new startup: {error}")
    finally:
        if cursor:
            cursor.close()


def main():
    connection = None
    try:
        # To connect to the database
        connection = _connect_to_db('regulatory_compliance')
        # some function calls
        check_null_startup_data(connection)
        check_invalid_funding_stages(connection)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if connection is not None:
            close_db_connection(connection)


if __name__ == '__main__':
    main()
