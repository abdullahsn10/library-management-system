import MySQLdb

class Category : 
    def __init__(self,name,desc) :
        self.name  = name 
        self.desc = desc 
    
    def insert_category(self,cursor,db) :
        cursor.execute(f'''
        INSERT INTO category(cat_name,cat_desc) VALUES ('{self.name}','{self.desc}');

        '''
        )
        db.commit()
        print(f'Done added {self.name}')
    
    @classmethod
    def return_cat_name(cls,cursor,cat_no) :
        cursor.execute(f'''
                    SELECT c.cat_name
                    FROM category c
                    WHERE c.cat_no = {cat_no};
                       ''')
        cat_name = cursor.fetchall()[0][0]
        return cat_name