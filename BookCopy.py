import MySQLdb


class BookCopy : 
    def __init__(self,book_code,copy_status,buy_status) :
        self.book_code = book_code
        self.copy_status = copy_status
        self.buy_status = buy_status

    

    def add_new_copy(self,cursor,db) : 
        cursor.execute(f'''
        INSERT INTO book_copy(book_code,copy_status,buy_status) 
                       VALUES ({self.book_code},'{self.copy_status}',
                       '{self.buy_status}');
        '''
        )
        db.commit()
        print(f'Done added Copy ')
    
    @classmethod
    def count_of_copies(cls,cursor,book_code) :
        cursor.execute (f'''
                SELECT COUNT(*)
                FROM book_copy c
                GROUP BY c.book_code
                HAVING c.book_code = {book_code};
                        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            count = 0 
        else :
            count = data[0][0]
        return count 
    
    @classmethod
    def all_book_copies(cls,cursor,db,book_code) :
        cursor.execute(f'''
            SELECT c.copy_no,c.loan_status,c.copy_status,c.buy_status
            FROM book_copy c 
            WHERE c.book_code = {book_code};
                       ''') 
        data = cursor.fetchall()
        return data
    
    @classmethod
    def all_not_rented_copies(cls,cursor,db,book_code) :
        cursor.execute(f'''
            SELECT c.copy_no,c.loan_status,c.copy_status
            FROM book_copy c 
            WHERE c.book_code = {book_code} and 
                  c.loan_status = 'not_rented';
                       ''') 
        data = cursor.fetchall()
        return data
    
    @classmethod
    def set_rent_status(cls,cursor,db,copy_no) :
        cursor.execute(f"""
        UPDATE book_copy 
        SET loan_status = 'rented',copy_status='used'
        WHERE copy_no = {copy_no};
        """)
        # cursor.execute(query, (copy_no))
        db.commit()

    @classmethod
    def return_book_code(cls,cursor,db,copy_no) :
        cursor.execute(f"""
        SELECT c.book_code
        FROM book_copy c 
        WHERE c.copy_no = {copy_no};
        """)
        data = cursor.fetchall()
        return data[0][0]
    
    @classmethod
    def return_book_title(cls,cursor,db,copy_no) : 
        cursor.execute(f'''
        SELECT b.book_title
        FROM book b , book_copy c 
        WHERE c.copy_no = {copy_no} and 
              c.book_code = b.book_code;
        ''')
        data = cursor.fetchall() 
        return data[0][0]
    
    @classmethod
    def return_book_price(cls,cursor,db,copy_no) : 
        cursor.execute(f'''
        SELECT b.book_price
        FROM book b , book_copy c 
        WHERE c.copy_no = {copy_no} and 
              c.book_code = b.book_code;
        ''')
        data = cursor.fetchall() 
        return data[0][0]
    

    @classmethod
    def update_loan_status(cls,cursor,db,copy_no,status) :
        cursor.execute(f"""
        UPDATE book_copy 
        SET loan_status = '{status}'
        WHERE copy_no = {copy_no};
        """)
        # cursor.execute(query, (copy_no))
        db.commit()

    @classmethod
    def return_all_avail_buy_copies(cls,cursor,db,book_code) :
        cursor.execute(f'''
            SELECT c.copy_no,c.loan_status,c.copy_status
            FROM book_copy c 
            WHERE c.book_code = {book_code} and 
                  c.loan_status = 'not_rented' and 
                  c.buy_status = 'yes';
                       ''') 
        data = cursor.fetchall()
        return data
    
