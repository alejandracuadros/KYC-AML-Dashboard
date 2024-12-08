from db_utils import _connect_to_db, close_db_connection, DbConnectionError

def add_to_startups(st_data):
    try:
        db_name = 'regulatory_compliance'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        
        query = """
        INSERT INTO startups (startup_id, startup_name, country, date_of_incorporation, company_size, employees)
        VALUES
        ({},'{}','{}','{}','{}',{});  
        """.format(st_data.registration_number,st_data.startup_name,st_data.country_of_incorporation,st_data.date_of_incorporation,
                   st_data.company_size,st_data.number_employees)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from regulatory_compliance - startups")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_to_founders_details(st_data):
    try:
        db_name = 'regulatory_compliance'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        for founder in st_data.founders:
            query = """
            INSERT INTO founders_details (passport_id, full_name, date_of_birth, nationality, birth_place, residence_place, gender, phone_number, 
            email, startup_id, role_in_startup)
            VALUES
            ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}'); 
            """.format(founder['passport_number'],founder['first_name']+" "+founder['last_name'],founder['date_of_birth'],
                       founder['nationality'],founder['place_of_birth'],founder['place_of_residence'],founder['gender'],
                       founder['phone_number'],founder['email'],st_data.registration_number,founder['role'])

            cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from regulatory_compliance - founders_details")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_to_startup_profile(st_data):
    try:
        db_name = 'regulatory_compliance'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        
        query = """
        INSERT INTO startup_profile (startup_id, industry, last_year_revenue, current_projected_revenue, next_year_revenue, 
        amount_raised)
        VALUES
        ({},'{}',{},{},{},{})  
        """.format(st_data.registration_number,st_data.industry,st_data.last_year_revenue,st_data.current_projected_revenue,
                   st_data.next_year_revenue,st_data.amount_raised)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from regulatory_compliance - startup_profile")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_to_investors(st_data):
    try:
        db_name = 'regulatory_compliance'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        for investor in st_data.investors:
            query = """
            INSERT INTO investors (startup_id, investor_name, passport_id)
            VALUES
            ({},'{}','{}')  
            """.format(st_data.registration_number,investor['first_name']+" "+investor['last_name'],investor['passport_id'])

            cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from regulatory_compliance - investors")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_to_board_members(st_data):
    try:
        db_name = 'regulatory_compliance'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        for member in st_data.board_members:
            query = """
            INSERT INTO board_members (startup_id, member_name, passport_id)
            VALUES
            ({},'{}','{}')  
            """.format(st_data.registration_number,member['first_name']+" "+member['last_name'],
                    member['passport_id'])

            cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from regulatory_compliance - board_members")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_to_sustainability(st_data):
    try:
        db_name = 'regulatory_compliance'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = """
        INSERT INTO sustainability (startup_id, goals, impact, social_contribution)
        VALUES
        ({},'{}','{}','{}')  
        """.format(st_data.registration_number,st_data.sustainability_goals,st_data.environment_impact_description,
                    st_data.social_impact_contributions)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from regulatory_compliance - sustainability")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")