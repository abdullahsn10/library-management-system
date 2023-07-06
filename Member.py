import MySQLdb


class Member : 
    def __init__(self,fname,mname,lname,address,mail,phone_one,phone_two) : 
        self.fname  = fname
        self.mname = mname 
        self.lname = lname  
        self.address = address
        self.mail = mail 
        self.phone_one = phone_one
        self.phone_two = phone_two
    
    def insert_member(self,cursor,db) : 
        cursor.execute(f'''
        INSERT INTO members(mem_fname,mem_mname,mem_lname,
                       mem_addr,mem_phone_one,mem_phone_two,mem_mail) 
        VALUES ('{self.fname}','{self.mname}','{self.lname}',
        '{self.address}','{self.phone_one}','{self.phone_two}','{self.mail}');
        '''
        )
        db.commit()
        print(f'Done added {self.fname}')

    @classmethod
    def mem_count(cls,cursor,db) : 
        cursor.execute('''
            SELECT COUNT(*)
            FROM members;
        ''')
        data = cursor.fetchall()
        if len(data) > 0 :
            mem_count = data[0][0]
        else :
            mem_count = 0 
        return mem_count

    @classmethod
    def return_member_info(cls,cursor,db,mem_id) : 
        cursor.execute(f'''
            SELECT * 
            FROM members m 
            WHERE m.mem_id = {mem_id};
                       ''')
        data = cursor.fetchall()
        return data
    
    def edit_member(self,cursor,db,mem_id) : 
        query = """
        UPDATE members
        SET mem_fname = %s, mem_mname = %s, mem_lname = %s,
            mem_addr = %s, mem_phone_one = %s, mem_phone_two = %s, mem_mail = %s
        WHERE mem_id = %s;
        """
        cursor.execute(query, (self.fname,self.mname,self.lname,
                               self.address,self.phone_one,self.phone_two,
                               self.mail,mem_id))
        db.commit()
    
    @classmethod
    def delete_member(cls,cursor,db,mem_id) : 
        cursor.execute(f'''
        DELETE FROM members m 
        WHERE m.mem_id = {mem_id} ;
        ''')
        db.commit()
        print(f'deleted member {mem_id} ') 