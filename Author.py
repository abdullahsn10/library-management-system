import MySQLdb
#author class 
class Author : 
    def __init__(self,name) :
        self.name = name 

    def insert_author(self,cursor,db) :
        cursor.execute(f'''
        INSERT INTO author(auth_name) VALUES ('{self.name}');
        '''
        )
        db.commit()
        print(f'Done added {self.name}')

    @classmethod
    def return_auth_name(cls,cursor,auth_id) :
        cursor.execute(f'''
                    SELECT a.auth_name
                    FROM author a 
                    WHERE a.auth_id = {auth_id};
                       ''')
        auth_name = cursor.fetchall()[0][0]
        return auth_name