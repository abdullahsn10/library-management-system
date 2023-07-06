import MySQLdb
from datetime import date

class Services  : 
    def __init__(self,rent_date,to_date,rent_status,book_copy, 
                    mem_id,emp_id) :
        self.rent_date = rent_date
        self.to_date = to_date
        self.rent_status  = rent_status
        self.book_copy = book_copy
        self.mem_id  = mem_id
        self.emp_id = emp_id

    def insert_new_service(self,cursor,db) :
        cursor.execute(f'''
        INSERT INTO services(rent_date,to_date,rent_status,book_copy,mem_id,emp_id) 
        VALUES ('{self.rent_date}','{self.to_date}','{self.rent_status}',
            {self.book_copy},{self.mem_id},{self.emp_id});
        '''
        )
        db.commit()
        print(f'Done added')

    @classmethod
    def return_all_services(cls,cursor,db) : 
        cursor.execute('''
            SELECT * 
            FROM services 
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def services_count(cls,cursor,db) :
        cursor.execute('''
            SELECT COUNT(*)
            FROM services;
        ''')

        data = cursor.fetchall()
        if len(data) != 0 :
            serv_count = data[0][0]
        else : 
            serv_count = 0
        return serv_count
    
    @classmethod
    def return_mem_services(cls,cursor,db,mem_id) : 
        cursor.execute(f'''
            SELECT * 
            FROM services s
            WHERE s.mem_id = {mem_id};
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_rdate_services(cls,cursor,db,rent_date) : 
        cursor.execute(f'''
            SELECT * 
            FROM services s
            WHERE s.rent_date = '{rent_date}';
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_tdate_services(cls,cursor,db,to_date) : 
        cursor.execute(f'''
            SELECT * 
            FROM services s
            WHERE s.to_date = '{to_date}';
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_book_services(cls,cursor,db,book_code) : 
        cursor.execute(f'''
            SELECT s.rent_no,s.rent_date,s.to_date,s.rent_status,
                       s.book_copy,s.mem_id,s.emp_id 
            FROM Services s,Book b , book_copy c 
            WHERE b.book_code = {book_code} and
	              b.book_code =  c.book_code and 
	              c.copy_no = s.book_copy;
            ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def return_rent_info(cls,cursor,db,rent_no)  :
        cursor.execute(f'''
            SELECT s.mem_id,s.book_copy
            FROM  services s
            WHERE s.rent_no = {rent_no};
            ''')
        data = cursor.fetchall()
        # print(data)
        return data

    @classmethod
    def return_book(cls,cursor,db,rent_no,return_date) : 
        cursor.execute(f'''
            SELECT s.rent_status 
            FROM services s
            WHERE s.rent_no = '{rent_no}';
        ''')
        d1 = cursor.fetchall()
        if d1[0][0] == 'Returned' :
            return False
        cursor.execute(f"""
        UPDATE services
        SET rent_status = 'Returned' , return_date = '{return_date}'
        WHERE rent_no = {rent_no};
        """)
        db.commit()
        return True
    
    @classmethod
    def return_late_returned(cls,cursor) : 
        today_date = date.today()

        cursor.execute(f'''
            SELECT * 
            FROM services s
            WHERE s.to_date <= '{today_date}' AND 
                  s.rent_status != 'Returned'; 
        ''')
        data = cursor.fetchall()
        return data
    
    @classmethod
    def count_operations_thismonth(cls,cursor) : 
        today_month = date.today().month
        # print(today_month)
        cursor.execute(f'''
            SELECT COUNT(*) 
            FROM services s
            WHERE MONTH(s.rent_date) = '{today_month}';
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0
        else :
            return data[0][0]
        

    @classmethod
    def most_rented_book_thismonth(cls,cursor) : 
        today_month = date.today().month
        cursor.execute(f'''
            SELECT b.book_title
            FROM services s,book_copy c , book b
            WHERE s.book_copy = c.copy_no and 
	                c.book_code = b.book_code and 
                    MONTH(s.rent_date) = '{today_month}'
            GROUP BY b.book_title
            HAVING COUNT(*) = (
                    SELECT COUNT(*)
                    FROM services s2,book_copy c1,book b1
                    where s2.book_copy = c1.copy_no and 
                    c1.book_code = b1.book_code 
                    GROUP BY b1.book_title
                    ORDER BY COUNT(*) DESC
                    LIMIT 1
                            );
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0
        else :
            return data[0][0]
        
    @classmethod
    def most_rented_book_thismonth(cls,cursor) : 
        today_month = date.today().month
        cursor.execute(f'''
            SELECT b.book_title
            FROM services s,book_copy c , book b
            WHERE s.book_copy = c.copy_no and 
	                c.book_code = b.book_code and 
                    MONTH(s.rent_date) = '{today_month}'
            GROUP BY b.book_title
            HAVING COUNT(*) = (
                    SELECT COUNT(*)
                    FROM services s2,book_copy c1,book b1
                    where s2.book_copy = c1.copy_no and 
                    c1.book_code = b1.book_code 
                    GROUP BY b1.book_title
                    ORDER BY COUNT(*) DESC
                    LIMIT 1
                            );
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0
        else :
            return data[0][0]
        
    @classmethod
    def trend_author_thismonth(cls,cursor) : 
        today_month = date.today().month
        cursor.execute(f'''
            SELECT a.auth_name
            FROM services s,book_copy c , book b , author a
            WHERE s.book_copy = c.copy_no and 
            c.book_code = b.book_code and 
            b.book_auth = a.auth_id and 
            MONTH(s.rent_date) = '{today_month}'
            GROUP BY a.auth_name
            HAVING COUNT(*) = (
                SELECT COUNT(*)
                FROM services s2,book_copy c1 , book b1 , author a1
            WHERE s2.book_copy = c1.copy_no and 
                c1.book_code = b1.book_code and 
                b1.book_auth = a1.auth_id and 
                MONTH(s2.rent_date) = 7
                GROUP BY a1.auth_name
                ORDER BY COUNT(*) DESC
                LIMIT 1
            );
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0
        else :
            return data[0][0]
    
    @classmethod
    def trend_publisher_thismonth(cls,cursor) : 
        today_month = date.today().month
        cursor.execute(f'''
            SELECT a.pub_name
            FROM services s,book_copy c , book b , publisher a
            WHERE s.book_copy = c.copy_no and 
            c.book_code = b.book_code and 
            b.book_pub = a.pub_id and 
            MONTH(s.rent_date) = '{today_month}'
            GROUP BY a.pub_name
            HAVING COUNT(*) = (
                SELECT COUNT(*)
                FROM services s2,book_copy c1 , book b1 , publisher a1
            WHERE s2.book_copy = c1.copy_no and 
                c1.book_code = b1.book_code and 
                b1.book_pub = a1.pub_id and 
                MONTH(s2.rent_date) = 7
                GROUP BY a1.pub_name
                ORDER BY COUNT(*) DESC
                LIMIT 1
            );
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0
        else :
            return data[0][0]
        

    @classmethod 
    def top_5_books(cls,cursor,from_date,to_date) : 
        cursor.execute(f'''
            SELECT b.book_title,COUNT(*) 
            FROM services s ,book_copy c , book b 
            WHERE s.book_copy=c.copy_no and 
                c.book_code  = b.book_code and 
                s.rent_date >= '{from_date}' and 
                s.rent_date <= '{to_date}'
            GROUP BY b.book_title 
            ORDER BY COUNT(*) desc
            LIMIT 5;
        ''')
        data = cursor.fetchall()
        return data
        
    
    @classmethod
    def return_mem_num_of_services(cls,cursor,mem_id) : 
        cursor.execute(f'''
            select count(*)
            from services s 
            group by s.mem_id
            having mem_id = {mem_id};
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
            from services s,book_copy c,book b 
            where s.book_copy = c.copy_no and 
                c.book_code = b.book_code
            group by s.mem_id,b.book_title,s.rent_no
            having s.mem_id = {mem_id}
            order by s.rent_no desc
            limit 1;
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 0 
        else : 
            return data[0][0]

    @classmethod
    def return_mem_prefCat(cls,cursor,mem_id) : 
        cursor.execute(f'''
            select t.cat_name
            from services s , book_copy c , book b , category t
            where s.book_copy = c.copy_no and 
                c.book_code = b.book_code and 
                b.book_cat = t.cat_no 
            group by t.cat_name,s.mem_id
            having s.mem_id = {mem_id}
            order by count(*) desc
            limit 1;
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            return 'None'
        else : 
            return data[0][0]

