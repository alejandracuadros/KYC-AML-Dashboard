from db_utils import _connect_to_db, close_db_connection, DbConnectionError

class DatabaseConnection:

    def __init__(self, db_name='regulatory_compliance'):
        try:
            self.db_name = db_name
            self.db_connection = _connect_to_db(self.db_name)
            self.cur = self.db_connection.cursor()
            print(f"Connected to DB: {self.db_name}")
        except Exception as e:
            raise DbConnectionError("Failed to connect to database: {}".format(e))
        
    def execute_query(self, query, data):
        try:
            self.cur.execute(query,data)
            self.db_connection.commit()
        except Exception as e:
            self.db_connection.rollback()
            raise DbConnectionError("Error executing query: {}".format(e))
        
    def close_connection(self):
        if self.cur:
            self.cur.close()
        if self.db_connection:
            close_db_connection(self.db_connection)
            print("DB connection is closed")


    def add_to_startups(self, st_data):
            
            query = """
            INSERT INTO startups (startup_id, startup_name, country, date_of_incorporation, company_size, employees)
            VALUES
            (%s,%s,%s,%s,%s,%s);  
            """
            data= (st_data.registration_number,st_data.startup_name,st_data.country_of_incorporation,st_data.date_of_incorporation,
                    st_data.company_size,st_data.number_employees)
            
            self.execute_query(query,data)



    def add_to_founders_details(self, st_data):

            for founder in st_data.founders:
                query = """
                INSERT INTO founders_details (passport_id, full_name, date_of_birth, nationality, birth_place, residence_place, gender, phone_number, 
                email, startup_id, role_in_startup)
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); 
                """
                data=(founder['passport_number'],founder['first_name']+" "+founder['last_name'],founder['date_of_birth'],
                        founder['nationality'],founder['place_of_birth'],founder['place_of_residence'],founder['gender'],
                        founder['phone_number'],founder['email'],st_data.registration_number,founder['role'])

                self.execute_query(query,data)



    def add_to_startup_profile(self, st_data):
        
            query = """
            INSERT INTO startup_profile (startup_id, industry, last_year_revenue, current_projected_revenue, next_year_revenue, 
            amount_raised)
            VALUES
            (%s,%s,%s,%s,%s,%s)  
            """
            data = (st_data.registration_number,st_data.industry,st_data.last_year_revenue,st_data.current_projected_revenue,
                    st_data.next_year_revenue,st_data.amount_raised)

            self.execute_query(query,data)

    
    
    def add_to_investors(self, st_data):

            for investor in st_data.investors:
                query = """
                INSERT INTO investors (startup_id, investor_name, passport_id)
                VALUES
                (%s,%s,%s)  
                """
                data=(st_data.registration_number,investor['first_name']+" "+investor['last_name'],investor['passport_id'])

                self.execute_query(query,data)


    
    def add_to_board_members(self, st_data):
    
            for member in st_data.board_members:
                query = """
                INSERT INTO board_members (startup_id, member_name, passport_id)
                VALUES
                (%s,%s,%s)  
                """
                data=(st_data.registration_number,member['first_name']+" "+member['last_name'],
                        member['passport_id'])

                self.execute_query(query,data)

    
    
    def add_to_sustainability(self, st_data):
            
            query = """
            INSERT INTO sustainability (startup_id, goals, impact, social_contribution)
            VALUES
            (%s,%s,%s,%s)  
            """
            data=(st_data.registration_number,st_data.sustainability_goals,st_data.environment_impact_description,
                        st_data.social_impact_contributions)

            self.execute_query(query,data)