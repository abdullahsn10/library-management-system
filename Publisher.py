import MySQLdb

class Publisher : 
    def __init__(self,name) :
        self.name = name 


    def insert_publisher(self,cursor,db) :
        cursor.execute(f'''
        INSERT INTO publisher(pub_name) VALUES ('{self.name}');
        '''
        )
        db.commit()
        print(f'Done added {self.name}')
    

    @classmethod
    def return_pub_name(cls,cursor,pub_id) :
        cursor.execute(f'''
                    SELECT p.pub_name
                    FROM publisher p 
                    WHERE p.pub_id = {pub_id};
                       ''')
        pub_name = cursor.fetchall()[0][0]
        return pub_name