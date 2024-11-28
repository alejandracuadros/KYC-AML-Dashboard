# check if in there are any empty (NULL) values in a given column in a specific table in a database
#The goal of this function, is to make sure that all the information are complete, since these are critical when comes to AML/KYC checking



def validate_data(field_name, value, expected_type):
    if not isinstance(value, str) or any(char.isdigit() for char in value):
        raise ValueError(f"{field_name} should be a valid string without numbers. Invalid value: {value} ")
    elif expected_type == "value":
        if not isinstance(value, (int,float)) or any(char.isalpha() for char in str(value)):
            raise ValueError(f"{field_name} should be a valid string without alphanumerics. Invalid value: {value}")
        elif expected_type == "date":
            try:
                # here we can check it the data entered is a valid date with the YYYY-MM-DD format
                import datetime
                datetime.datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"{field_name} should be a valid date. Invalid value: {value}")
            return True
# Check for invalid date ranges in the PEP table
def check_invalid_date_rages(connection):
    try:
        cursor = connection.cursor()
        query = """
        SELECT id, full_name, date_of_birth FROM PEP_Identification.pep_individuals
        WHERE pep_individuals.date_of_birth < '1900-01-01' OR date_of_birth < CURDATE()
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print("Invalid date ranges detected:")
            for row in rows:
                print(row)
        else:
            print("No valid date ranges detected.")
    except Exception as e:
        print(f" There is an error while checking date ranges: {e}")

# Function to check and ensure there is no null or empty values entered during the input
def ensure_not_null(field_name, value):
    if value is None or value == '':
        raise ValueError(f"{field_name} should not be empty. Invalid value: {value}")
    return True

# This funcion can be used to check in a specific column in a specific table
def check_null_values(table_name, column_name):
    try:
        #I use paid Pycharm, so if you dont please make sure that is a connection with the database before running this code
        cursor = connection.cursor()
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} IS NULL"
        cursor.execute(query)
        result = cursor.fetchone()
        print(f"NULL values in {table_name} ({column_name}): {result[0]}")
    except Exception as e:
        print(f" There is an error while checking: {e}")

#to call the function above use:
#check_null_values("startups", "name")
#check_null_values("startups", "country")

# Function to insert PEP data with validation checks, on each point

def insert_pep(connection, full_name, job_title, country, date_of_birth):
    try:
        ensure_not_null("full_name", full_name)
        validate_data("full_name", full_name, str)
        ensure_not_null("job_title", job_title)
        validate_data("job_title", job_title, str)
        ensure_not_null("country", country)
        validate_data("country", country, str)
        ensure_not_null("date_of_birth", date_of_birth)
        validate_data("date_of_birth", date_of_birth,"date_of_birth")

#if all checks pass it can be inserted into the database
        cursor = connection.cursor()
        query = """
        INSERT INTO PEP_Identification.pep_individuals (full_name, job_title, country, date_of_birth)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (full_name, job_title, country, date_of_birth))
        connection.commit()
        print("PEP inserted successfully.")
    except ValueError as validation_error:
        print(f"Validation Error: {validation_error}")
    except Exception as db_error:
        print(f" There is an error while inserting: {db_error}")

# Check if a startup operates in a high-risk country
def check_eu_countries_blacklist(connection,country):
    try:
        cursor = connection.cursor()
        query = "Select * FROM eu_countries_blacklist WHERE country_name = %s"
        cursor.execute(query, (country,))
        result = cursor.fetchone()
        if result:
            print(f"Warning: The country {country} is classified as high risk.")
        else:
            print(f"The country {country} is not classified as high risk.")
    except Exception as e:
        print(f" There is an error while checking: {e}")
