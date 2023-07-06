import MySQLdb



class LibraryHistory: 
    def __init__(self,emp_id,hist_action,hist_table,action_date) : 
        self.emp_id = emp_id
        self.hist_action = hist_action
        self.hist_table = hist_table
        self.action_date = action_date



    def insert_action(self,cursor,db) : 
        cursor.execute(f'''
        INSERT INTO library_history(emp_id,hist_action,hist_table,action_date) 
        VALUES ({self.emp_id},'{self.hist_action}','{self.hist_table}',
        '{self.action_date}');
        '''
        )
        db.commit()
        print(f'Done added')
    
    @classmethod
    def return_all_actions(cls,cursor,db) :
        cursor.execute(f'''
            SELECT * 
            FROM library_history;
                       ''')
        data = cursor.fetchall()
        return data    

    @classmethod
    def return_all_emp_actions(cls,cursor,db,emp_id) : 
        cursor.execute(f'''
            SELECT * 
            FROM library_history lh
            WHERE lh.emp_id = {emp_id};
                       ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_all_date_actions(cls,cursor,db,action_date) : 
        cursor.execute(f'''
            SELECT * 
            FROM library_history lh
            WHERE lh.action_date = '{action_date}';
                       ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_all_table_actions(cls,cursor,db,hist_table) : 
        cursor.execute(f'''
            SELECT * 
            FROM library_history lh
            WHERE lh.hist_table = '{hist_table}';
                       ''')
        data = cursor.fetchall()
        return data