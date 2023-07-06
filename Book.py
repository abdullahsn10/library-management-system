import MySQLdb

class Book : 
    def __init__(self,title,price,pages,pub,auth,cat,desc) :
        self.title = title 
        self.price = price 
        self.pages = pages 
        self.pub = pub 
        self.auth = auth 
        self.cat = cat 
        self.desc = desc
    

    def insert_book(self,cursor,db) :
        cursor.execute(f'''
        INSERT INTO book(book_title,book_price,book_pages,book_cat,book_pub,book_auth,book_desc) 
        VALUES ('{self.title}',{self.price},{self.pages},{self.cat},{self.pub},{self.auth},'{self.desc}');
        '''
        )
        db.commit()
        print(f'Done added {self.title}')




    @classmethod
    def book_count(cls,cursor,db) :
        cursor.execute('''
            SELECT COUNT(*)
            FROM book;
        ''')

        data = cursor.fetchall()
        if len(data) != 0 :
            book_count = data[0][0]
        else : 
            book_count = 0
        return book_count

    @classmethod
    def return_book_info(cls,cursor,db,book_code) : 
        cursor.execute(f'''
            SELECT * 
            FROM book b 
            WHERE b.book_code = {book_code};
                       ''')
        data = cursor.fetchall()
        return data
    
    def edit_book(self,cursor,db,book_code) :
        query = """
        UPDATE book
        SET book_title = %s, book_price = %s, book_pages = %s,
            book_cat = %s, book_auth = %s, book_pub = %s, book_desc = %s
        WHERE book_code = %s;
        """
        cursor.execute(query, (self.title, self.price, self.pages,
                                self.cat, self.auth, self.pub, 
                                self.desc, book_code))
        db.commit()
    
    @classmethod
    def delete_book(cls,cursor,db,book_code) : 
        cursor.execute(f'''
        DELETE FROM book b 
        WHERE b.book_code = {book_code} ;
        ''')
        db.commit()

        print(f'deleted book {book_code} ')