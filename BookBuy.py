import MySQLdb
from datetime import date
class BookBuy : 

    def __init__(self,buy_date,book_copy,mem_id,emp_id,book_price) : 
        self.buy_date = buy_date
        self.book_copy =book_copy
        self.mem_id = mem_id
        self.emp_id = emp_id
        self.book_price = book_price

    def inser_new_sale(self,cursor,db) : 
        cursor.execute(f'''
        INSERT INTO book_buy(buy_date,book_copy,mem_id,emp_id,book_price) 
        VALUES ('{self.buy_date}','{self.book_copy}','{self.mem_id}',
            {self.emp_id},{self.book_price});
        '''
        )
        db.commit()
        print(f'Done added')



    @classmethod
    def sales_count(cls,cursor,db) :
        cursor.execute('''
            SELECT COUNT(*)
            FROM book_buy;
        ''')

        data = cursor.fetchall()
        if len(data) != 0 :
            buy_count = data[0][0]
        else : 
            buy_count = 0
        return buy_count
    
    @classmethod
    def return_all_sales(cls,cursor,db) : 
        cursor.execute('''
            SELECT * 
            FROM book_buy
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_mem_sales(cls,cursor,db,mem_id) : 
        cursor.execute(f'''
            SELECT * 
            FROM book_buy y
            WHERE y.mem_id = {mem_id};
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_bdate_sales(cls,cursor,db,buy_date) : 
        cursor.execute(f'''
            SELECT * 
            FROM book_buy y
            WHERE y.buy_date = '{buy_date}';
        ''')
        data = cursor.fetchall()
        return data
    
    
    @classmethod
    def return_book_sales(cls,cursor,db,book_code) : 
        cursor.execute(f'''
            SELECT s.buy_no,s.buy_date,s.book_copy,s.mem_id,s.emp_id,s.book_price
            FROM book_buy s,Book b , book_copy c 
            WHERE b.book_code = {book_code} and
	              b.book_code =  c.book_code and 
	              c.copy_no = s.book_copy;
            ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def get_overall_sale(cls,cursor,db,buy_date) : 
        cursor.execute(f'''
            SELECT SUM(y.book_price)
            FROM book_buy y 
            WHERE  y.buy_date = '{buy_date}';
            ''')
        data = cursor.fetchall()
        return data[0][0]
    
    @classmethod
    def most_selling_book_thismonth(cls,cursor) : 
        today_month = date.today().month
        cursor.execute(f'''
            SELECT b.book_title
            FROM book_buy s,book_copy c , book b
            WHERE s.book_copy = c.copy_no and 
                c.book_code = b.book_code and 
                MONTH(s.buy_date) = '{today_month}'
            GROUP BY b.book_title
            HAVING COUNT(*) = (
                SELECT COUNT(*)
                FROM book_buy s2,book_copy c1,book b1
                where s2.book_copy = c1.copy_no and 
                c1.book_code = b1.book_code 
                GROUP BY b1.book_title
                ORDER BY COUNT(*) DESC
                LIMIT 1
            );
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return None
        else :
            return data[0][0]
        
    @classmethod 
    def top_5_books(cls,cursor,from_date,to_date) : 
        cursor.execute(f'''
            SELECT b.book_title,SUM(y.book_price) 
            FROM book_buy y ,book_copy c , book b 
            WHERE y.book_copy=c.copy_no and 
                c.book_code  = b.book_code and 
                y.buy_date >= '{from_date}' and 
				y.buy_date <= '{to_date}'
            GROUP BY b.book_title 
            ORDER BY SUM(y.book_price)  desc
            LIMIT 5;
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def get_profit(cls,cursor,from_date,to_date) : 
        cursor.execute(f'''
            SELECT SUM(y.book_price)
            FROM book_buy y 
            WHERE                
                y.buy_date >= '{from_date}' and 
				y.buy_date <= '{to_date}';
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod 
    def top_5_members(cls,cursor,from_date,to_date) : 
        cursor.execute(f'''
            select m.mem_id,sum(y.book_price)
            from book_buy y,members m 
            where y.mem_id = m.mem_id and 
                y.buy_date >= '{from_date}' and 
                y.buy_date <= '{to_date}'
            group by m.mem_id
            order by sum(y.book_price) desc
            LIMIT 5;
        ''')
        data = cursor.fetchall()
        return data
    

    @classmethod
    def return_mem_num_of_operations(cls,cursor,mem_id) : 
        cursor.execute(f'''
            select count(*)
            from book_buy y 
            group by y.mem_id
            having mem_id = {mem_id};
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0 
        else : 
            return data[0][0]

    @classmethod
    def return_mem_paid(cls,cursor,mem_id) : 
        cursor.execute(f'''
            select sum(y.book_price)
            from book_buy y
            group by y.mem_id
            having y.mem_id = {mem_id};
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0 
        else : 
            return data[0][0]
        

    @classmethod
    def return_mem_lastbook(cls,cursor,mem_id) : 
        cursor.execute(f'''
            select b.book_title
            from book_buy s,book_copy c,book b 
            where s.book_copy = c.copy_no and 
                c.book_code = b.book_code
            group by s.mem_id,b.book_title,s.buy_no
            having s.mem_id = {mem_id}
            order by s.buy_no desc
            limit 1;
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 'None' 
        else : 
            return data[0][0]