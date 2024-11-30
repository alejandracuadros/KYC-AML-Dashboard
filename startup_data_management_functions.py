from db_utils import _connect_to_db, close_db_connection


# Function to fetch all startups in high-risk countries
def fetch_startups_in_high_risk_countries(connection):
    cursor = None
    try:
        cursor = connection.cursor()
        query = """
        SELECT 
            s.startup_id,
            s.name AS startup_name,
            s.country AS startup_country,
            hrc.country_name AS high_risk_country
        FROM
            regulatory_compliance.startups s
        JOIN
            eu_countries_blacklist.high_risk_countries hrc
        ON s.country = hrc.country_name;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print(f"Startups in high-risk countries:")
        for row in result:
            print(row)
    except Exception as e:
        print(f"There was an error while fetching startups in high-risk countries: {e}")
    finally:
        if cursor:
            cursor.close()


# Function to fetch startups with pep founders
def fetch_startups_with_pep_founders(connection):
    cursor = None
    try:
        cursor = connection.cursor()
        query = """
        SELECT 
            s.startup_id,
            s.name AS startup_name,
            s.founder_name AS founder_name,
            p.full_name AS pep_name,
            p.class AS pep_class,
            p.country AS pep_country
        FROM
            regulatory_compliance.startups s
        JOIN
            PEP_Identification.pep_individuals p
        ON s.founder_name = p.full_name;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print(f"Startups with PEP founders:")
        for row in result:
            print(row)
    except Exception as e:
        print(f"There was an error while fetching startups with PEP founders: {e}")
    finally:
        if cursor:
            cursor.close()


# Function to flag startups in high-risk countries
def flag_startups_based_on_risk(connection):
    cursor = None
    try:
        cursor = connection.cursor()
        query = """
        SELECT 
            s.startup_id,
            s.name AS startup_name,
            CASE
            WHEN hrc.country_name IS NOT NULL THEN 'High-Risk Country'
            WHEN p.full_name IS NOT NULL THEN 'PEP Founder'
            ELSE 'Low Risk'
            END AS risk_level
        FROM
            regulatory_compliance.startups s
        JOIN
            eu_countries_blacklist.high_risk_countries hrc
        ON s.country = hrc.country_name
        JOIN
            PEP_Identification.pep_individuals p
        ON s.founder_name = p.full_name;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print(f"Startups in high risk countries:")
        for row in result:
            print(row)
    except Exception as e:
        print(f"There was an error while flagging startups based on risk: {e}")
    finally:
        if cursor:
            cursor.close()


def main():
    connection = None
    try:
        # To connect to the database
        connection = _connect_to_db('regulatory_compliance')
        # some function calls
        fetch_startups_in_high_risk_countries(connection)
        fetch_startups_with_pep_founders(connection)
        flag_startups_based_on_risk(connection)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if connection is not None:
            close_db_connection(connection)


if __name__ == '__main__':
    main()
