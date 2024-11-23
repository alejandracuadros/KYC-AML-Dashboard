# check if in there are any empty (NULL) values in a given column in a specific table in a database
# also it will COUNT and print if is there any empty values.
#The goal of this function, is to make sure that all the information are complete, since these are critical when comes to AML/KYC checking
def check_null_values(connection, table_name, column_name):
    try:
        cursor = connection.cursor()
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} IS NULL"
        cursor.execute(query)
        result = cursor.fetchone()
        print(f"Null values in {table_name}: {result[0]}")
    except Exception as e:
        print(f"There is an error while checking for null values: {e}")

# This function aimns to secure data accuracy, so when a date_of_birth is inserted, we keep it in a certain range
def check_invalid_date_ranges(connection):
    try:
        cursor = connection.cursor
        query = """
        SELECT id, full_name, date_of_birth FROM PEP_Identification.pep_individuals
        WHERE date_of_birth < '1900-01-01' OR date_of_birth > CURDATE()
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Invalid date ranges:")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"There is an error while checking for invalid date ranges: {e}")

# insert_pep function serves to handle errors during data insertion to keep its integrety
def insert_pep(connection, full_name, job_title, country, date_of_birth):
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO PEP_Identification.pep_individuals (full_name, job_title, country, date_of_birth)
        VALUES (%s, %s,%s, %s)
        """
        cursor.execute(query, (full_name, job_title, country, date_of_birth))
        connection.commit()
        print("PEP inserted successfully")
    except Exception as error:
        print(f"Something went wrong: {error}")


