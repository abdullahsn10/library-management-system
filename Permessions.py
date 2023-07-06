import MySQLdb

class Permessions : 
    def __init__(self,lib_id,book_tab,mem_tab,lib_tab,det_tab,serv_tab,
                 hist_tab,sett_tab) : 

        self.lib_id = lib_id
        self.book_tab = book_tab
        self.mem_tab = mem_tab
        self.lib_tab = lib_tab
        self.det_tab = det_tab
        self.serv_tab = serv_tab
        self.hist_tab = hist_tab
        self.sett_tab = sett_tab
    


    def insert_permession(self,cursor,db): 
        cursor.execute(f'''
            SELECT * 
            FROM librarian_permissions s
            WHERE s.lib_id = {self.lib_id};
        ''')
        data = cursor.fetchall()
        if len(data) == 0 :
            cursor.execute(f'''
            INSERT INTO librarian_permissions(lib_id,book_tab,mem_tab,lib_tab,
                        det_tab,serv_tab,hist_tab,sett_tab) 
            VALUES ({self.lib_id},{self.book_tab},{self.mem_tab},{self.lib_tab},
            {self.det_tab},{self.serv_tab},{self.hist_tab},{self.sett_tab});
            '''
            )
            db.commit()
            print(f'Done added')
        else : 
            cursor.execute(f"""
            UPDATE librarian_permissions
            SET book_tab ={self.book_tab},mem_tab={self.mem_tab},lib_tab={self.mem_tab},
                        det_tab={self.det_tab},serv_tab={self.serv_tab},
                        hist_tab={self.hist_tab},sett_tab={self.sett_tab}
            WHERE lib_id = {self.lib_id};
            """)
            db.commit()

    @classmethod
    def return_lib_perm(cls,cursor,db,lib_id) : 
        cursor.execute(f'''
            SELECT * 
            FROM librarian_permissions s
            WHERE s.lib_id = {lib_id};
        ''')
        data = cursor.fetchall()
        return data