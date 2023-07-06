import MySQLdb


class Librarian : 
    def __init__(self,fname,mname,lname,mail,phone,city,village,street,password) :
        self.id = id 
        self.fname = fname 
        self.mname = mname
        self.lname = lname 
        self.mail = mail 
        self.phone = phone 
        self.city = city 
        self.village = village 
        self.street = street
        self.password = password 


    def insert_librarian(self,cursor,db) :
        cursor.execute(f'''
        INSERT INTO librarian(lib_fname,lib_mname,
                       lib_lname,lib_mail,lib_city,
                       lib_village,lib_street,lib_phone,sup_id,lib_password) 
        VALUES ('{self.fname}','{self.mname}','{self.lname}',
        '{self.mail}','{self.city}','{self.village}',
        '{self.street}','{self.phone}',9990003,'{self.password}');
        '''
        )
        db.commit()
        print(f'Done added {self.fname}')


    @classmethod
    def return_lib_info(cls,cursor,db,lib_id) : 
        cursor.execute(f'''
            SELECT * 
            FROM librarian l 
            WHERE l.lib_id = {lib_id};
                       ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def edit_librarian(cls,cursor,db,lib_id,lib_fname,lib_mname,lib_lname,
                                         lib_city,lib_ph,lib_mail) : 
        query = """
        UPDATE librarian
        SET lib_fname = %s, lib_mname = %s, lib_lname = %s,
            lib_city = %s, lib_phone = %s, lib_mail = %s
        WHERE lib_id = %s;
        """
        cursor.execute(query, (lib_fname,lib_mname,lib_lname,
                               lib_city,lib_ph,lib_mail,lib_id))
        db.commit()
    
    @classmethod
    def delete_librarian(cls,cursor,db,lib_id) :
        cursor.execute(f'''
        DELETE from librarian l 
        WHERE l.lib_id = {lib_id};
        ''')

        db.commit()
        print(f'deleted librarian {lib_id} ') 

    @classmethod
    def update_lib_password(cls,cursor,db,lib_id,lib_pass): 
        cursor.execute( f'''
        UPDATE librarian
        SET lib_password = '{lib_pass}'
        WHERE lib_id = {lib_id};
        ''')
        db.commit()
        print('password updated')