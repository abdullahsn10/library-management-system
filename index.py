# DATABASE LIBRARY MANAGEMENT SYSTEM 
# STUDENT 1: Abdullah Sami Naser 1201952 
# STUDENT 2: Ahmad Ismail Jabra 
# STUDENT 3: Majd Riyad Abdeddein 1202923

#                DR. ABDULLAH ALNATSHA 



import typing
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget 
from PyQt5.uic import loadUiType
from datetime import date
import MySQLdb
import sys 

#relations 
from Author import *
from Publisher import * 
from Category import *
from Librarian import * 
from Book import * 
from Member import * 
from BookCopy import * 
from Services import * 
from BookBuy import * 
from Permessions import * 
from LibraryHistory import *

MainUI,_ = loadUiType('main.ui')


class Main(QMainWindow, MainUI) :
    # librarian id 
    librarian_id = 0
    def __init__(self,parent=None) :
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db_connect()
        self.UI_changes()
        self.handle_buttons()
        self.show_all_categories()
        self.show_all_authors()
        self.show_all_publishers()
        self.update_count_of_all_books()
        self.update_count_of_all_members()
        self.update_count_of_all_services()
        self.show_all_books()
        self.show_all_members()
        self.show_all_librarians()
        self.show_all_issues()
        self.show_all_sales()
        self.show_history_table()
        self.total_sales_today()
        self.trend_book_thismonth()
        self.trend_salebook_thismonth()
        self.trend_author()
        self.trend_publisher()


    def UI_changes(self) :
        ## Login UI changes
        self.mainTab_widget.tabBar().setVisible(False) 
        self.mainTab_widget.setCurrentIndex(0) 
        # self.groupBox.setVisible(False)



    def db_connect(self) :
        #DB connections 
        self.db = MySQLdb.connect(host = 'localhost' ,user = 'root' ,
                                  password = 'abdullah162906',db = 'DeirQaddis_library')
        self.cur = self.db.cursor()
        print('Connection Established')

    def handle_buttons(self) :
        #handle any button 
        
        #pages buttons
        self.homePage_button.clicked.connect(self.open_homepage_tab)
        self.bookPage_button.clicked.connect(self.open_bookpage_tab)
        self.memPage_button.clicked.connect(self.open_mempage_tab)
        self.libPage_button.clicked.connect(self.open_libpage_tab)
        self.bkdetPage_button.clicked.connect(self.open_bkdetpage_tab)
        self.servPage_button.clicked.connect(self.open_servicespage_tab)
        self.repPage_button.clicked.connect(self.open_reportpage_tab)
        self.settiPage_button.clicked.connect(self.open_settingspage_tab)
        self.histPage_button.clicked.connect(self.open_historypage_tab)
        # ******** add buttons 
        self.add_authButton.clicked.connect(self.add_new_author)
        self.add_pubButton.clicked.connect(self.add_new_publisher)
        self.add_catButton.clicked.connect(self.add_new_category)
        self.add_libButton.clicked.connect(self.add_new_librarian)
        self.add_bookButton.clicked.connect(self.add_new_book)
        self.add_memberButton.clicked.connect(self.add_new_member)
        self.add_copyButton.clicked.connect(self.add_new_copy)
        # ******** show tables buttons and refresh
        self.mem_table_refresh.clicked.connect(self.show_all_members)
        self.search_booktable_Button.clicked.connect(self.search_books_table)
        self.book_table_refresh.clicked.connect(self.show_all_books)
        self.mem_table_search.clicked.connect(self.search_members_table)
        self.search_copyButton.clicked.connect(self.show_all_copies)
        self.lib_table_srchButton.clicked.connect(self.search_librarians_table)
        self.lib_table_refresh.clicked.connect(self.show_all_librarians)
        self.services_srchButton.clicked.connect(self.search_all_services)
        self.serv_table_refresh.clicked.connect(self.show_all_issues)
        self.history_srcButton.clicked.connect(self.search_history_table)
        self.history_refresh.clicked.connect(self.show_history_table)
        # *********** edit delete button 
        self.edit_del_srchButton.clicked.connect(self.edit_book_search)
        self.editbook_Button.clicked.connect(self.edit_book)
        self.delbook_Button.clicked.connect(self.delete_book)
        self.memedit_Button.clicked.connect(self.edit_mem_search)
        self.save_mem_Button.clicked.connect(self.edit_member)
        self.del_mem_Button.clicked.connect(self.delete_member)
        self.libedit_srchButton.clicked.connect(self.edit_lib_search)
        self.save_lib_Button.clicked.connect(self.edit_librarian)
        self.del_lib_Button.clicked.connect(self.delete_librarian)
        self.rent_bookButton.clicked.connect(self.rent_new_book)
        # ********** rent buttons
        self.bcode_rent.textChanged.connect(self.show_rent_book_info)
        self.mem_idrent.textChanged.connect(self.show_rent_mem_info)
        self.rent_no_return.textChanged.connect(self.return_ren_info)
        self.return_Button.clicked.connect(self.return_book)
        self.buy_Button.clicked.connect(self.buy_book)
        self.buy_srchButton.clicked.connect(self.search_sales_table)
        self.buy_refreshButton.clicked.connect(self.show_all_sales)
        self.buy_bcode.textChanged.connect(self.show_salebook_info)
        # ************** settings
        self.check_lib_Button.clicked.connect(self.check_librarian)
        self.change_passButton.clicked.connect(self.change_password)
        self.set_permButton.clicked.connect(self.set_permession)
        # ************* login
        self.login_Button.clicked.connect(self.handle_login)
        self.logoutButton.clicked.connect(self.log_out_button)
        # ************* report 
        self.show_rent_report.clicked.connect(self.show_late_services)
        self.show_top5booksButton.clicked.connect(self.show_top5_rented_books)
        self.show_top5booksButton_2.clicked.connect(self.show_top5_salling_books)
        self.profit_infoButton.clicked.connect(self.show_profit)
        self.top5Mem_Button.clicked.connect(self.show_top5_members)

        self.show_memReportButton.clicked.connect(self.show_mem_feedback)


    def log_out_button(self) :
        hist = LibraryHistory(Main.librarian_id,'logout','None',date.today())
        hist.insert_action(self.cur,self.db)
        self.show_history_table()
        self.user_id_login.clear()
        self.user_pass_login.clear()
        self.mainTab_widget.setCurrentIndex(0) 
        self.bookPage_button.setEnabled(False) 
        self.memPage_button.setEnabled(False) 
        self.libPage_button.setEnabled(False) 
        self.bkdetPage_button.setEnabled(False) 
        self.servPage_button.setEnabled(False) 
        self.histPage_button.setEnabled(False) 
        self.settiPage_button.setEnabled(False) 
        self.groupBox.setEnabled(False)
        # self.groupBox.setVisible(False)

    def handle_login(self) :
        # for login 
        try : 
            user_id = int(self.user_id_login.text().strip())
            user_pass = self.user_pass_login.text().strip()
            data = Librarian.return_lib_info(self.cur,self.db,user_id)
            if len(data) == 0 :
                QMessageBox.warning(self,"fail",'User Not Exist')
                raise Exception
            
            if user_pass == data[0][9] :
                Main.librarian_id = user_id
                self.mainTab_widget.setCurrentIndex(1)
                self.label_35.setText(str(data[0][1]+'.'+data[0][2][0]+'.'+data[0][3][0]))
                self.groupBox.setEnabled(True)
                # self.groupBox.setVisible(True)
                perm = Permessions.return_lib_perm(self.cur,self.db,user_id)
                self.homePage_button.setEnabled(True)
                self.repPage_button.setEnabled(True)
                hist = LibraryHistory(Main.librarian_id,'login','None',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                if perm[0][2] :
                    self.bookPage_button.setEnabled(True) 
                if perm[0][3] :
                    self.memPage_button.setEnabled(True) 
                if perm[0][4] :
                    self.libPage_button.setEnabled(True) 
                if perm[0][5] :
                    self.bkdetPage_button.setEnabled(True) 
                if perm[0][6] :
                    self.servPage_button.setEnabled(True) 
                if perm[0][7] :
                    self.histPage_button.setEnabled(True) 
                if perm[0][8] :
                    self.settiPage_button.setEnabled(True) 
            else : 
                QMessageBox.warning(self,"fail",'Wrong Password!!')
                raise Exception


        except : 
            QMessageBox.information(self,"fail",'Invalid Input')
        



#####################Book############################
    def show_all_books(self,is_default=True,*search_attr) :
        data = ()
        self.all_books_table.clearContents()
        if len(search_attr) != 0 :
                if search_attr[0] == 'code' :
                    self.cur.execute(f'''
                        SELECT b.book_code,b.book_title,b.book_pages,b.book_price,b.book_auth,
                            b.book_pub,b.book_cat
                        FROM book b
                        WHERE b.book_code = {search_attr[1]};
                    ''')
                    data = self.cur.fetchall()
                elif search_attr[0] == 'title' :
                    self.cur.execute(f'''
                        SELECT b.book_code,b.book_title,b.book_pages,b.book_price,b.book_auth,
                            b.book_pub,b.book_cat
                        FROM book b
                        WHERE b.book_title = '{search_attr[1]}';
                    ''')
                    data = self.cur.fetchall()
                elif search_attr[0] == 'cat' :
                    self.cur.execute(f'''
                        SELECT b.book_code,b.book_title,b.book_pages,b.book_price,b.book_auth,
                            b.book_pub,b.book_cat
                        FROM book b
                        WHERE b.book_cat = {search_attr[1]};
                    ''')
                    data = self.cur.fetchall()
        else :
            self.cur.execute(f'''
                    SELECT b.book_code,b.book_title,b.book_pages,b.book_price,b.book_auth,
                        b.book_pub,b.book_cat
                    FROM book b;
                ''')
            data = self.cur.fetchall()

        

        for row,book in enumerate(data) :
            self.all_books_table.insertRow(row)
            for col,item in enumerate(book) :
                if col < 4 :
                    self.all_books_table.setItem(row,col,QTableWidgetItem(str(item)))
                elif col == 4 :
                    self.all_books_table.setItem(row,col,
                        QTableWidgetItem(str(Author.return_auth_name(self.cur,int(item)))))
                elif col == 5 : 
                    self.all_books_table.setItem(row,col,
                        QTableWidgetItem(str(Publisher.return_pub_name(self.cur,int(item)))))
                elif col == 6 : 
                    self.all_books_table.setItem(row,col,
                        QTableWidgetItem(str(Category.return_cat_name(self.cur,int(item)))))
            self.all_books_table.setItem(row,7,
                        QTableWidgetItem(str(BookCopy.count_of_copies(self.cur,book[0]))))


    def search_books_table(self) :
        try :
            # when search in the book table 
            if self.bcode_radioButton.isChecked() : 
                book_code = int(self.table_book_code.text().strip())
                self.show_all_books(False,'code',book_code)

            elif self.btitle_radioButton.isChecked() :
                book_title = self.table_book_title.text().strip().lower()
                self.show_all_books(False,'title',book_title)

            elif self.bcat_radioButton.isChecked() :
                cat_name = self.table_book_cat.currentText().strip().lower()
                self.cur.execute(f'''
                SELECT c.cat_no
                FROM category c 
                WHERE c.cat_name = '{cat_name}';
                ''')  
                book_cat = int(self.cur.fetchall()[0][0])
                self.show_all_books(False,'cat',book_cat)
        except :
            self.error_booktable.setText('ERROR: Invalid Operation')
        



    def add_new_book(self) :
        try:
            book_title = self.book_titTxt.text().strip().lower()
            book_price = int(self.book_priTxt.text().strip())
            book_pages = int(self.book_pagTxt.text().strip())
            book_desc = self.book_descTxt.text().strip().lower()
            #get pub_id
            pub_name = self.pub_comboBox_2.currentText().strip()
            self.cur.execute(f'''
            SELECT p.pub_id
            FROM publisher p 
            WHERE p.pub_name = '{pub_name}';
            ''')  
            book_pub = int(self.cur.fetchall()[0][0])
            #get auth 
            auth_name = self.auth_comboBox.currentText().strip()
            self.cur.execute(f'''
            SELECT a.auth_id
            FROM author a 
            WHERE a.auth_name = '{auth_name}';
            ''')  
            book_auth = int(self.cur.fetchall()[0][0])
            #get cat 
            cat_name = self.cat_comboBox_2.currentText().strip()
            self.cur.execute(f'''
            SELECT c.cat_no
            FROM category c 
            WHERE c.cat_name = '{cat_name}';
            ''')  
            book_cat = int(self.cur.fetchall()[0][0])
            # insert 
            book = Book(book_title,book_price,book_pages
                        ,book_pub,book_auth,book_cat,book_desc)
            book.insert_book(self.cur,self.db)
            self.book_add_label.setText(f'Done Added Book {book_title}')
            QMessageBox.information(self,"success",'Book Added Successfully')
            hist = LibraryHistory(Main.librarian_id,'add','books',date.today())
            hist.insert_action(self.cur,self.db)
            self.show_history_table()
            self.update_count_of_all_books() 
            self.show_all_books()
        except :
           QMessageBox.information(self,"fail",'Invalid Operation')
           

    def edit_book_search(self) :
        # editing book information 
        try : 
            book_code = int(self.book_code_editTxt.text().strip())
            data = Book.return_book_info(self.cur,self.db,book_code)
            if len(data) != 0 :
                # put information in fields
                    # title
                self.btitle_edit.setText(str(data[0][1]))
                    # price
                self.bprice_edit.setText(str(data[0][2]))
                    # pages 
                self.bpage_edit.setText(str(data[0][3]))
                    # copies 
                self.bcopy_edit.setReadOnly(True)
                self.bcopy_edit.setText(str(BookCopy.count_of_copies(self.cur,book_code)))
                    # category 
                self.cat_comboBox.setCurrentText(str(Category.return_cat_name(self.cur,data[0][4])))
                    # pub
                self.pub_comboBox.setCurrentText(str(Publisher.return_pub_name(self.cur,data[0][5])))
                    # auth
                self.auth_comboBox_2.setCurrentText(str(Author.return_auth_name(self.cur,data[0][6])))
                    # desc 
                self.bdesc_edit.setText(str(data[0][7]))
                self.book_editsrch_label.setText('You Can Edit or Delete')
            else :
                self.book_editsrch_label.setText('ERROR : Not Found!!')

        except: 
            QMessageBox.information(self,"fail",'Invalid Operation')
    
    def edit_book(self) :
        # edit book
        try:
            book_code = int(self.book_code_editTxt.text().strip())
            data = Book.return_book_info(self.cur,self.db,book_code)
            if len(data) != 0 :
                book_title = self.btitle_edit.text().strip().lower()
                book_price = int(self.bprice_edit.text().strip())
                book_pages = int(self.bpage_edit.text().strip())
                book_desc = self.bdesc_edit.text().strip().lower()
                #get pub_id
                pub_name = self.pub_comboBox.currentText().strip()
                self.cur.execute(f'''
                SELECT p.pub_id
                FROM publisher p 
                WHERE p.pub_name = '{pub_name}';
                ''')  
                book_pub = int(self.cur.fetchall()[0][0])
                #get auth 
                auth_name = self.auth_comboBox_2.currentText().strip()
                self.cur.execute(f'''
                SELECT a.auth_id
                FROM author a 
                WHERE a.auth_name = '{auth_name}';
                ''')  
                book_auth = int(self.cur.fetchall()[0][0])
                #get cat 
                cat_name = self.cat_comboBox.currentText().strip()
                self.cur.execute(f'''
                SELECT c.cat_no
                FROM category c 
                WHERE c.cat_name = '{cat_name}';
                ''')  
                book_cat = int(self.cur.fetchall()[0][0])
                # insert 
                book = Book(book_title,book_price,book_pages
                            ,book_pub,book_auth,book_cat,book_desc)
                book.edit_book(self.cur,self.db,book_code)
                QMessageBox.information(self,"success",'Book Information Updated Successfully')
                hist = LibraryHistory(Main.librarian_id,'edit','books',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.btitle_edit.clear()
                self.bprice_edit.clear()
                self.bpage_edit.clear()
                self.bcopy_edit.clear()
                self.cat_comboBox.setCurrentIndex(0)
                self.pub_comboBox.setCurrentIndex(0)
                self.auth_comboBox_2.setCurrentIndex(0)
                self.bdesc_edit.clear()
                self.book_code_editTxt.clear()
                # l3 min 35
                self.show_all_books(True)
            else : 
                raise Exception
        except :
            QMessageBox.information(self,"fail",'Invalid Operation')
    
    def delete_book(self) :
        try:
            book_code = int(self.book_code_editTxt.text().strip())
            data = Book.return_book_info(self.cur,self.db,book_code)
            if len(data) != 0 :
                    Book.delete_book(self.cur,self.db,book_code)
                    self.book_editsrch_label.setText(f'Done Delete Book : {book_code}')
                    QMessageBox.information(self,"success",'Book Deleted')
                    self.update_count_of_all_books() 
                    hist = LibraryHistory(Main.librarian_id,'delete','books',date.today())
                    hist.insert_action(self.cur,self.db)
                    self.show_history_table()
                    self.btitle_edit.clear()
                    self.bprice_edit.clear()
                    self.bpage_edit.clear()
                    self.bcopy_edit.clear()
                    self.cat_comboBox.setCurrentIndex(0)
                    self.pub_comboBox.setCurrentIndex(0)
                    self.auth_comboBox_2.setCurrentIndex(0)
                    self.bdesc_edit.clear()
                    self.book_code_editTxt.clear()
                    self.show_all_books(True)
                
            else : 
                raise Exception

        except : 
            QMessageBox.information(self,"fail",'Invalid Operation')
         
    
    def add_new_copy(self) : 
        try : 
            book_code = int(self.copy_book_codeTxt.text().strip())
            copy_status = self.cpy_status.text().strip().lower()
            buy_status = self.buy_status.text().strip().lower()
            if len(copy_status) == 0 or len(buy_status) == 0 :
                raise Exception
            if copy_status == 'new' or copy_status =='used' :
                if buy_status =='yes' or buy_status == 'no' :
                    pass 
                else :
                    QMessageBox.warning(self,"fail",'Input Wrong')
                    raise Exception
            else : 
                 QMessageBox.warning(self,"fail",'Input Wrong')
                 raise Exception
            buy_status = self.buy_status.text().strip().lower()
            cpy = BookCopy(book_code,copy_status,buy_status)
            cpy.add_new_copy(self.cur,self.db)
            self.cur.execute(f'''
                SELECT book_title 
                FROM book 
                WHERE book_code = {book_code};
            ''')
            book_title = self.cur.fetchall()[0][0]
            self.copy_label.setText(f'Done Added A new Copy of ({book_title})')
            hist = LibraryHistory(Main.librarian_id,'add','book_copy',date.today())
            hist.insert_action(self.cur,self.db)
            self.show_history_table()
            QMessageBox.information(self,"success",'Copy Added Successuflly')
            self.show_all_books()
            self.show_all_copies()

        except : 
            QMessageBox.information(self,"fail",'Invalid Operation')
    
    def show_all_copies(self) :
        try : 
            self.bcopy_table.clearContents()
            book_code = int(self.copy_book_codeTxt.text().strip())
            data = BookCopy.all_book_copies(self.cur,self.db,book_code)
            for row,book in enumerate(data) :
                self.bcopy_table.insertRow(row)
                for col,item in enumerate(book) :
                    self.bcopy_table.setItem(row,col,QTableWidgetItem(str(item)))
        except :
            QMessageBox.information(self,"fail",'Invalid Operation')
    
#####################Member############################
    def show_all_members(self,is_default = True,*search_attr) :
        #to show all members
        data = ()
        self.all_mem_Table.clearContents()
        if len(search_attr) != 0 :
            if search_attr[0] == 'id' :
                self.cur.execute(f'''
                    SELECT m.mem_id,m.mem_fname,m.mem_mname,m.mem_lname,m.mem_addr,
                        m.mem_phone_one,m.mem_phone_two,m.mem_mail 
                    FROM members m
                    WHERE m.mem_id = {search_attr[1]};
                    ''')
                data = self.cur.fetchall()
            elif search_attr[0] == 'name' :
                self.cur.execute(f'''
                    SELECT m.mem_id,m.mem_fname,m.mem_mname,m.mem_lname,m.mem_addr,
                        m.mem_phone_one,m.mem_phone_two,m.mem_mail 
                    FROM members m
                    WHERE m.mem_fname = '{search_attr[1]}';
                    ''')
                data = self.cur.fetchall()
        else :
            self.cur.execute(f'''
                    SELECT m.mem_id,m.mem_fname,m.mem_mname,m.mem_lname,m.mem_addr,
                        m.mem_phone_one,m.mem_phone_two,m.mem_mail 
                    FROM members m;
                    ''')
            data = self.cur.fetchall()

        for row,member in enumerate(data) :
            self.all_mem_Table.insertRow(row)
            for col,item in enumerate(member) :
                self.all_mem_Table.setItem(row,col,QTableWidgetItem(str(item)))
                

    def search_members_table(self) :
        try :
        # when search in the book table 
            if self.mem_id_radioButton.isChecked() : 
                mem_id = int(self.mem_id_table.text().strip())
                self.show_all_members(False,'id',mem_id)

            elif self.mem_name_radioButton.isChecked() :
                mem_name = self.mem_name_table.text().strip().lower()
                self.show_all_members(False,'name',mem_name)
        except :
            self.error_memtable.setText('ERROR: Invalid Operation')

    def add_new_member(self) :
        try:
            #get name
            mem_tripname = self.mem_namTxt.text().strip().split(' ')
            if len(mem_tripname) == 3 :
                mem_fname = mem_tripname[0]
                mem_mname = mem_tripname[1]
                mem_lname = mem_tripname[2]
            else : 
                raise Exception
            mem_mail = self.mem_maiTxt.text().strip()
            mem_phoneOne = self.mem_phOTxt.text().strip()
            mem_phoneTwo = self.mem_phTTxt.text().strip()
            mem_address = self.mem_addTxt.text().strip()

            mem = Member(mem_fname,mem_mname,mem_lname,
                            mem_address,mem_mail,mem_phoneOne,mem_phoneTwo)
            mem.insert_member(self.cur,self.db)
            QMessageBox.information(self,"success",'Member Added Succefully')
            hist = LibraryHistory(Main.librarian_id,'add','members',date.today())
            hist.insert_action(self.cur,self.db)
            self.show_history_table()
            self.update_count_of_all_members() 
            self.show_all_members()
        except :
            self.add_mem_label.setText('ERROR : Invalid Operation , Check Fields')

    def edit_mem_search(self) :
        try : 
            mem_id = int(self.mem_srchid.text().strip())
            data = Member.return_member_info(self.cur,self.db,mem_id)
            if len(data) != 0 :
                # put information in fields
                    #fname
                self.mem_fnameedit.setText(str(data[0][1]))
                    #mname
                self.mem_mname_edit.setText(str(data[0][2]))
                    #lname
                self.mem_lname_edit.setText(str(data[0][3]))
                    #address
                self.mem_addr_edit.setText(str(data[0][4]))
                    # phone one 
                self.mem_ph_edit.setText(str(data[0][5]))
                    # phone two 
                self.mem_ph2_edit.setText(str(data[0][6]))
                    # mail 
                self.mem_mail_edit.setText(str(data[0][7])) 

            else :
                QMessageBox.information(self,"fail",'Member Not Found')

        except: 
            QMessageBox.information(self,"fail",'Invalid Operation')

    def edit_member(self) :
        # edit member  
        try:
            mem_id = int(self.mem_srchid.text().strip())
            data = Member.return_member_info(self.cur,self.db,mem_id)
            if len(data) != 0 :
                mem_fname = self.mem_fnameedit.text().strip().lower()
                mem_mname = self.mem_mname_edit.text().strip().lower()
                mem_lname = self.mem_lname_edit.text().strip().lower()
                mem_addr = self.mem_addr_edit.text().strip().lower()
                mem_ph_one = self.mem_ph_edit.text().strip().lower()
                mem_ph_two = self.mem_ph2_edit.text().strip().lower()
                mem_mail = self.mem_mail_edit.text().strip().lower()

                # insert 
                mem = Member(mem_fname,mem_mname,mem_lname,mem_addr,mem_mail,mem_ph_one,
                            mem_ph_two)
                mem.edit_member(self.cur,self.db,mem_id)
                QMessageBox.information(self,"success",'Member Information Updated')
                hist = LibraryHistory(Main.librarian_id,'edit','members',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.mem_fnameedit.clear()
                self.mem_mname_edit.clear()
                self.mem_lname_edit.clear()
                self.mem_addr_edit.clear()
                self.mem_ph_edit.clear()
                self.mem_ph2_edit.clear()
                self.mem_mail_edit.clear()
                self.show_all_members(True)
            else :
                raise Exception

        except :
             QMessageBox.information(self,"fail",'Invalid Operation')
    
    def delete_member(self) :
        try:
            mem_id = int(self.mem_srchid.text().strip())
            data = Member.return_member_info(self.cur,self.db,mem_id)
            if len(data) != 0 :
                Member.delete_member(self.cur,self.db,mem_id)
                QMessageBox.information(self,"success",'Member Deleted')
                hist = LibraryHistory(Main.librarian_id,'delete','members',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.mem_fnameedit.clear()
                self.mem_mname_edit.clear()
                self.mem_lname_edit.clear()
                self.mem_addr_edit.clear()
                self.mem_ph_edit.clear()
                self.mem_ph2_edit.clear()
                self.mem_mail_edit.clear()
                self.show_all_members(True)
            else :
                raise Exception

        except : 
            QMessageBox.information(self,"fails",'Invalid Operation')



#####################Librarian############################
    def show_all_librarians(self,is_default = True,*search_attr) :
        #to show all librarians
        
        data = () 
        self.all_lib_table.clearContents()
        if len(search_attr) != 0 :
            if search_attr[0] == 'id' :
                self.cur.execute(f'''
                    SELECT l.lib_id,l.lib_fname,l.lib_mname,l.lib_lname,
                                 l.lib_city,l.lib_phone,l.lib_mail
                    FROM librarian l
                    WHERE l.lib_id = {search_attr[1]};
                    ''')
                data = self.cur.fetchall() 
        else :
            self.cur.execute(f'''
                    SELECT l.lib_id,l.lib_fname,l.lib_mname,l.lib_lname,
                                 l.lib_city,l.lib_phone,l.lib_mail
                    FROM librarian l;
                    ''')
            data = self.cur.fetchall()

        for row,lib in enumerate(data) :
            self.all_lib_table.insertRow(row)
            for col,item in enumerate(lib) :
                self.all_lib_table.setItem(row,col,QTableWidgetItem(str(item)))

    def search_librarians_table(self) :
        try :
        # when search in the lib table 
            if self.lib_id_radioButton.isChecked() : 
                lib_id = int(self.lib_id_srch.text().strip())
                self.show_all_librarians(False,'id',lib_id)

        except :
            QMessageBox.information(self,"fail",'Invalid Operation')

    def add_new_librarian(self) :
        try: 
            #get name
            lib_tripname = self.lib_namTxt.text().strip().split(' ')
            if len(lib_tripname) == 3 :
                lib_fname = lib_tripname[0].lower()
                lib_mname = lib_tripname[1].lower()
                lib_lname = lib_tripname[2].lower()
            else : 
                raise Exception
            lib_mail = self.lib_mailTxt.text().strip().lower()
            lib_phone = self.lib_phTxt.text().strip().lower()
            lib_city = self.lib_cityTxt.text().strip().lower()
            lib_village = self.lib_vilTxt.text().strip().lower()
            lib_street = self.lib_strTxt.text().strip().lower()
            lib_password = self.lib_passTxt.text().strip().lower()
            lib = Librarian(lib_fname,lib_mname,lib_lname,
                            lib_mail,lib_phone,lib_city,lib_village,
                            lib_street,lib_password)
            lib.insert_librarian(self.cur,self.db)
            self.lib_add_label.setText(f'Done Added Librarian {lib_fname}') 
            QMessageBox.information(self,"success",'Librarian Added Successfully')
            hist = LibraryHistory(Main.librarian_id,'add','librarians',date.today())
            hist.insert_action(self.cur,self.db)
            self.show_all_librarians()
            self.show_history_table()
        except :
            self.lib_add_label.setText('ERROR : Invalid Operation , Check Fields') 

    def edit_lib_search(self) :
        try : 
            lib_id = int(self.lib_id_edit.text().strip())
            data = Librarian.return_lib_info(self.cur,self.db,lib_id)
            if len(data) != 0 :
                # put information in fields
                    #fname
                self.lib_fname_edit.setText(str(data[0][1]))
                    #mname
                self.lib_mname_edit.setText(str(data[0][2]))
                    #lname
                self.lib_lname_edit.setText(str(data[0][3]))
                    #address
                self.lib_addr_edit.setText(str(data[0][5]))
                    # phone one 
                self.lib_ph_edit.setText(str(data[0][8]))
                    # mail 
                self.lib_mail_edit.setText(str(data[0][4])) 

            else :
                QMessageBox.information(self,"fail",'Librarian Not Found')

        except: 
            QMessageBox.information(self,"fail",'Invalid Operation')

    def edit_librarian(self) :
        # edit member  
        try:
            lib_id = int(self.lib_id_edit.text().strip())
            data = Librarian.return_lib_info(self.cur,self.db,lib_id)
            if len(data) != 0 :
                lib_fname = self.lib_fname_edit.text().strip().lower()
                lib_mname = self.lib_mname_edit.text().strip().lower()
                lib_lname = self.lib_lname_edit.text().strip().lower()
                lib_city = self.lib_addr_edit.text().strip().lower()
                lib_ph = self.lib_ph_edit.text().strip().lower()
                lib_mail = self.lib_mail_edit.text().strip().lower()

                # insert 
                Librarian.edit_librarian(self.cur,self.db,lib_id,lib_fname,
                                         lib_mname,lib_lname,
                                         lib_city,lib_ph,lib_mail)
                QMessageBox.information(self,"success",'Librarian Information Updated')
                hist = LibraryHistory(Main.librarian_id,'edit','librarians',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.lib_fname_edit.clear()
                self.lib_mname_edit.clear()
                self.lib_lname_edit.clear()
                self.lib_addr_edit.clear()
                self.lib_ph_edit.clear()
                self.lib_mail_edit.clear()
                self.show_all_librarians(True)

            else :
                raise Exception

        except :
             QMessageBox.information(self,"fail",'Invalid Operation')
    
    def delete_librarian(self) :
        #delete librarian
        try:
            lib_id = int(self.lib_id_edit.text().strip())
            data = Librarian.return_lib_info(self.cur,self.db,lib_id)
            if len(data) != 0 :
                Librarian.delete_librarian(self.cur,self.db,lib_id)
                QMessageBox.information(self,"success",'Librarian Deleted')
                hist = LibraryHistory(Main.librarian_id,'delete','librarians',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.lib_fname_edit.clear()
                self.lib_mname_edit.clear()
                self.lib_lname_edit.clear()
                self.lib_addr_edit.clear()
                self.lib_ph_edit.clear()
                self.lib_mail_edit.clear()
                self.show_all_librarians(True)
            else :
                raise Exception

        except : 
            QMessageBox.information(self,"fails",'Invalid Operation')
#####################Publisher and authors############################

    def add_new_publisher(self) :
        try :
            pub_name = self.pub_namTxt.text().strip().lower()
            if len(pub_name) != 0 :
                pub = Publisher(pub_name)
                pub.insert_publisher(self.cur,self.db)
                self.details_label.setText(f'Done Added Publisher {str(pub_name)} ')
                QMessageBox.information(self,"success",'Publisher Added Successfully')
                hist = LibraryHistory(Main.librarian_id,'add','publishers',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.show_all_publishers()
            else : 
                raise Exception
        except : 
            self.details_label.setText(f'ERROR: Invalid Input')

    def add_new_author(self) :
        try :
            author_name = self.auth_namTxt.text().strip().lower()
            if len(author_name) != 0 :
                auth = Author(author_name)
                auth.insert_author(self.cur,self.db)
                self.details_label.setText(f'Done Added Author {str(author_name)} ')
                QMessageBox.information(self,"success",'Author Added Successfully')
                hist = LibraryHistory(Main.librarian_id,'add','authors',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.show_all_authors()
            else :
                raise Exception
        except : 
            self.details_label.setText(f'ERROR: Invalid Input')

    def add_new_category(self) :
        try :
            cat_name = self.cat_namTxt.text().strip().lower()
            cat_desc = self.cat_descTxt.text().strip().lower()
            if len(cat_name) != 0 and len(cat_desc) != 0 :
                cat = Category(cat_name,cat_desc)
                cat.insert_category(self.cur,self.db)
                self.details_label.setText(f'Done Added Category {str(cat_name)} ')
                QMessageBox.information(self,"success",'Category Added Successfully')
                hist = LibraryHistory(Main.librarian_id,'add','categories',date.today())
                hist.insert_action(self.cur,self.db)
                self.show_history_table()
                self.show_all_categories()
            else : 
                raise Exception

        except : 
            self.details_label.setText(f'ERROR: Invalid Input')
        
    def show_all_categories(self) : 
        self.cat_comboBox.clear()
        self.cat_comboBox_2.clear()
        self.table_book_cat.clear()
        self.cur.execute('''
            SELECT c.cat_name
            FROM category c
        ''')
        categories = self.cur.fetchall()
        for c in categories :
            self.cat_comboBox.addItem(str(c[0]))
            self.cat_comboBox_2.addItem(str(c[0]))
            self.table_book_cat.addItem(str(c[0]))
        
    def show_all_publishers(self) : 
        self.pub_comboBox.clear()
        self.pub_comboBox_2.clear()
        self.cur.execute('''
            SELECT p.pub_name
            FROM publisher p
        ''')
        publishers = self.cur.fetchall()
        for p in publishers :
            self.pub_comboBox.addItem(str(p[0]))  
            self.pub_comboBox_2.addItem(str(p[0]))     

    def show_all_authors(self) : 
        self.auth_comboBox.clear()
        self.auth_comboBox_2.clear()
        self.cur.execute('''
            SELECT a.auth_name
            FROM author a
        ''')
        authors = self.cur.fetchall()
        for a in authors :
            self.auth_comboBox.addItem(str(a[0]))  
            self.auth_comboBox_2.addItem(str(a[0]))

            

    
#####################services############################
    def show_all_issues(self,is_default = True , *search_attr) :
        # show all issue processes
        try : 
            data = ()
            self.rent_table.clearContents()
            if len(search_attr) != 0 :
                if search_attr[0] == 'id' :
                    data = Services.return_mem_services(self.cur,self.db,search_attr[1])

                elif search_attr[0] == 'code' : 
                    data = Services.return_book_services(self.cur,self.db,search_attr[1])
                
                elif search_attr[0] == 'rdate' : 
                    data =  Services.return_rdate_services(self.cur,self.db,search_attr[1])
                
                elif search_attr[0] == 'tdate' :
                    data =  Services.return_tdate_services(self.cur,self.db,search_attr[1])


            else : 
                data = Services.return_all_services(self.cur,self.db)


            for row,srv in enumerate(data) :
                self.rent_table.insertRow(row)
                for col,item in enumerate(srv) :
                    if col == 7 :
                        self.rent_table.setItem(row,col+1,QTableWidgetItem(
                            str(item)))
                        break
                    if col != 6 :
                        self.rent_table.setItem(row,col,QTableWidgetItem(str(item)))
                    else : 
                        print (srv[4])
                        self.rent_table.setItem(row,col,QTableWidgetItem(
                            str(BookCopy.return_book_code(self.cur,self.db,
                                                          srv[4]))))
                        self.rent_table.setItem(row,col+1,QTableWidgetItem(
                            str(BookCopy.return_book_title(self.cur,self.db,srv[4]))))
                      

                    
        except :
            QMessageBox.information(self,"fail",'Invalid Operation')
        
    def search_all_services(self) : 
        try :
            if self.rent_memid_rButton.isChecked() : 
                mem_id = int(self.rent_memid.text().strip())
                self.show_all_issues(False,'id',mem_id)

            elif self.rent_bcode_rButton.isChecked() : 
                book_code = int(self.rent_bcode.text().strip())
                self.show_all_issues(False,'code',book_code)
            
            elif self.rent_rdate_rButton.isChecked() :
                rent_date = self.rent_rdate.date().toPyDate()
                self.show_all_issues(False,'rdate',rent_date)
            
            elif self.rent_tdate_rButton.isChecked() :
                to_date = self.rent_tdate.date().toPyDate()
                self.show_all_issues(False,'tdate',to_date)

        except :
            QMessageBox.information(self,"fail",'Invalid Operation')

    def rent_new_book(self) :
        # add new issue 
        try : 
            # get book code 
            book_code = int(self.bcode_rent.text().strip())
            mem_id = int(self.mem_idrent.text().strip())
            dbook = Book.return_book_info(self.cur,self.db,book_code)
            dmem = Member.return_member_info(self.cur,self.db,mem_id)
            if len(dbook) != 0 and len(dmem) != 0 :
                if self.rent_operation(book_code,mem_id) :
                    QMessageBox.information(self,'success','Rent Operation Done')
                    self.trend_author()
                    self.trend_publisher()
                    self.trend_book_thismonth()
                    hist = LibraryHistory(Main.librarian_id,'rent','services',date.today())
                    hist.insert_action(self.cur,self.db)
                    self.show_history_table()
                    self.show_all_issues(True)
                    self.update_count_of_all_services()
                else : 
                    raise Exception
        
            else : 
                QMessageBox.information(self,'fail','No Corresponding Member and Book')



        except :
            QMessageBox.information(self,'fail','Invalid Operation')



    def show_rent_book_info(self) :
        self.bookdetails_table.clearContents()
        try :
            book_code = int(self.bcode_rent.text().strip())
            data = Book.return_book_info(self.cur,self.db,book_code)
            if len(data) != 0 :
                self.bookdetails_table.insertRow(0)
                self.bookdetails_table.setItem(0,0,QTableWidgetItem(str(data[0][0])))
                self.bookdetails_table.setItem(0,1,QTableWidgetItem(str(data[0][1])))
                self.bookdetails_table.setItem(0,2,QTableWidgetItem(
                    str(BookCopy.count_of_copies(self.cur,book_code))))

        except :
            QMessageBox.information(self,'fail','Invalid Operation')


    def show_rent_mem_info(self) :
        self.memdetails_table.clearContents()
        try :
            mem_id = int(self.mem_idrent.text().strip())
            data = Member.return_member_info(self.cur,self.db,mem_id)
            if len(data) != 0 :
                self.memdetails_table.insertRow(0)
                self.memdetails_table.setItem(0,0,QTableWidgetItem(str(data[0][0])))
                self.memdetails_table.setItem(0,1,QTableWidgetItem(str(data[0][1])))
                self.memdetails_table.setItem(0,2,QTableWidgetItem(str(data[0][7])))

        except :
            QMessageBox.information(self,'fail','Invalid Operation') 

    def return_book(self) :
        # return book 
        try : 
            rent_no = int(self.rent_no_return.text().strip())
            return_date = date.today()
            if not Services.return_book(self.cur,self.db,rent_no,return_date) : 
                QMessageBox.warning(self,'Fail','The Book is already Returned')
                raise Exception
            data = Services.return_rent_info(self.cur,self.db,rent_no)
            BookCopy.update_loan_status(self.cur,self.db,int(data[0][1]),'not_rented')
            self.show_all_issues()
            QMessageBox.information(self,'success','Return Operation Done')
            hist = LibraryHistory(Main.librarian_id,'return','services',date.today())
            hist.insert_action(self.cur,self.db)
            self.show_history_table()

        except : 
            QMessageBox.information(self,'Fail','Invalid Operation')



    def rent_operation(self,book_code,mem_id) : 
        # return all copies of the book 
        copies_data = BookCopy.all_not_rented_copies(self.cur,self.db,book_code)
        if len(copies_data) != 0 : 
            rent_date = date.today()
            print(rent_date)
            to_date = self.to_date.date().toPyDate()
            print(to_date)
            if rent_date > to_date :
                raise Exception('Date Problem')
            rent_status = 'Rented'
            book_copy = copies_data[0][0]
            emp_id = Main.librarian_id
            serv = Services(rent_date,to_date,rent_status,book_copy,mem_id,emp_id)
            serv.insert_new_service(self.cur,self.db)
            BookCopy.set_rent_status(self.cur,self.db,book_copy)
            return True

        else : 
            QMessageBox.warning(self,'Fail','No Copies of this book are available')
            return False

    def return_ren_info(self) : 
        # to show the rent info the table 
        try : 
            self.return_table.clearContents()
            rent_no = int(self.rent_no_return.text().strip())
            data = Services.return_rent_info(self.cur,self.db,rent_no)
            for row,srv in enumerate(data) :
                self.return_table.insertRow(row)
                for col,item in enumerate(srv) :
                    self.return_table.setItem(row,col,QTableWidgetItem(
                            str(item)))
                
                self.return_table.setItem(row,2,QTableWidgetItem(
                            str(BookCopy.return_book_title(self.cur,
                                                           self.db,srv[1]))))


        except : 
             QMessageBox.information(self,'Fail','Wrong Input')

################## Buy Operation ################
    def buy_book(self) : 
        # for buying a book 
        try : 
            # get book code 
            book_code = int(self.buy_bcode.text().strip())
            mem_id = int(self.buy_memid.text().strip())
            dbook = Book.return_book_info(self.cur,self.db,book_code)
            dmem = Member.return_member_info(self.cur,self.db,mem_id)
            if len(dbook) != 0 and len(dmem) != 0 :
                if self.buy_operation(book_code,mem_id) :
                    QMessageBox.information(self,'success','Buy Operation Done')
                    self.trend_salebook_thismonth()
                    hist = LibraryHistory(Main.librarian_id,'buy','book_buy',date.today())
                    hist.insert_action(self.cur,self.db)
                    self.show_all_sales()
                    self.show_history_table()
                    self.update_count_of_all_services()
                    self.total_sales_today()
                else : 
                    raise Exception
        
            else : 
                QMessageBox.information(self,'fail','No Corresponding Member and Book')



        except :
            QMessageBox.information(self,'fail','Invalid Operation') 

    def buy_operation(self,book_code,mem_id) :
          # return all copies of the book 
        copies_data = BookCopy.return_all_avail_buy_copies(self.cur,self.db,book_code)
        if len(copies_data) != 0 : 
            buy_date = date.today()
            book_copy = copies_data[0][0]
            emp_id = Main.librarian_id
            book_price = BookCopy.return_book_price(self.cur,self.db,book_copy)
            buy = BookBuy(buy_date,book_copy,mem_id,emp_id,book_price)
            buy.inser_new_sale(self.cur,self.db)
            BookCopy.update_loan_status(self.cur,self.db,book_copy,'sold')
            return True

        else : 
            QMessageBox.warning(self,'Fail','No Copies of this book are available')
            return False

    def show_all_sales(self,is_default = True , *search_attr) :
        # show all sales processes
        try : 
            data = ()
            self.buy_table.clearContents()
            if len(search_attr) != 0 :
                if search_attr[0] == 'id' :
                    data = BookBuy.return_mem_sales(self.cur,self.db,search_attr[1])

                elif search_attr[0] == 'code' : 
                    data = BookBuy.return_book_sales(self.cur,self.db,search_attr[1])
                
                elif search_attr[0] == 'bdate' : 
                    data =  BookBuy.return_bdate_sales(self.cur,self.db,search_attr[1])


            else : 
                data = BookBuy.return_all_sales(self.cur,self.db)


            for row,srv in enumerate(data) :
                self.buy_table.insertRow(row)
                for col,item in enumerate(srv) :
                    if col != 4 :
                        if col != 5 :
                            self.buy_table.setItem(row,col,QTableWidgetItem(str(item)))
                        else : 
                            self.buy_table.setItem(row,col+1,QTableWidgetItem(str(item)))
                    else : 
                        self.buy_table.setItem(row,col,QTableWidgetItem(
                            str(BookCopy.return_book_code(self.cur,self.db,
                                                          int(srv[2])))))
                        self.buy_table.setItem(row,col+1,QTableWidgetItem(
                            str(BookCopy.return_book_title(self.cur,self.db,int(srv[2])))))

                      

                    
        except :
            QMessageBox.information(self,"fail",'Invalid Operation')

    def search_sales_table(self) : 
        try :
            if self.buy_memradioButton.isChecked() : 
                mem_id = int(self.buy_table_mem_id.text().strip())
                self.show_all_sales(False,'id',mem_id)

            elif self.buy_coderadioButton.isChecked() : 
                book_code = int(self.buy_table_bcode.text().strip())
                self.show_all_sales(False,'code',book_code)
            
            elif self.buy_dateradioButton.isChecked() :
                buy_date = self.buy_table_bdate.date().toPyDate()
                print(buy_date)
                self.show_all_sales(False,'bdate',buy_date)

        except :
            QMessageBox.information(self,"fail",'Invalid Operation')

    def show_salebook_info(self) : 
        try : 
            book_code = int(self.buy_bcode.text().strip())
            data = Book.return_book_info(self.cur,self.db,book_code)
            if len(data) != 0  :
                self.bcode_rent_3.setText(str(data[0][1]))
                self.bcode_rent_4.setText(str(data[0][2]) + ' $')
        except : 
            QMessageBox.information(self,"fail",'Invalid Operation')

#####################permissions############################

    def check_librarian(self) : 
        try : 
            lib_id = int(self.lib_id_settings.text().strip())
            lib_pass = self.lib_pass_setting.text().strip().lower()
            data = Librarian.return_lib_info(self.cur,self.db,lib_id)
            if len(data) != 0 : 
                if data[0][9] == lib_pass : 
                    self.libGroup.setEnabled(True) 
                else : 
                    QMessageBox.warning(self,"fail",'Wrong Password!!')
                    raise Exception
            else : 
                QMessageBox.warning(self,"fail",'User not exist')
                raise Exception

        except: 
            QMessageBox.information(self,"fail",'Invalid Operation')

    def change_password(self) : 
        try : 
            lib_id = int(self.lib_id_settings.text().strip())
            lib_pass = self.new_pass_lib.text().strip()
            lib_pass2 = self.renew_pass_lib.text().strip()

            if lib_pass == lib_pass2 : 
                 Librarian.update_lib_password(self.cur,self.db,lib_id,lib_pass)
                 QMessageBox.information(self,"success",'Password Updated')
                 hist = LibraryHistory(Main.librarian_id,'change password','librarians',date.today())
                 hist.insert_action(self.cur,self.db)
                 self.show_history_table()
            else : 
                QMessageBox.warning(self,"fail",'Passwords are not matching')
                raise Exception
        except: 
            QMessageBox.information(self,"fail",'Invalid Operation')


    def set_permession(self) :
        try : 
            lib_id = int(self.lib_id_perm.text().strip())
            ldata = Librarian.return_lib_info(self.cur,self.db,lib_id)
            if len(ldata) == 0 : 
                QMessageBox.warning(self,"fail",'User not exist')
                raise Exception
            
            book_tab =0
            mem_tab =0
            lib_tab =0
            det_tab =0
            serv_tab =0
            hist_tab =0
            sett_tab =0
            if self.books_chBox.isChecked() : 
                book_tab = 1
            if self.mem_chBox.isChecked() : 
                mem_tab = 1
            if self.lib_chBox.isChecked() : 
                lib_tab = 1
            if self.det_chBox.isChecked() : 
                det_tab = 1
            if self.srv_chBox.isChecked() : 
                serv_tab = 1
            if self.srv_chBox.isChecked() : 
                sett_tab = 1
            if self.hist_chBox.isChecked() : 
                hist_tab = 1
            perm = Permessions(lib_id,book_tab,mem_tab,lib_tab,
                               det_tab,serv_tab,hist_tab,sett_tab)
            perm.insert_permession(self.cur,self.db) 
            QMessageBox.information(self,"success",'Permession Set Successfully')
            hist = LibraryHistory(Main.librarian_id,'set','permissions',date.today())
            hist.insert_action(self.cur,self.db)
            self.show_history_table()
        except: 
            QMessageBox.information(self,"fail",'Invalid Operation')
######################history############################
    def show_history_table(self,is_default=True,*search_attr) : 
        try : 
            self.history_table.clearContents()
            if len(search_attr) != 0 :
                if search_attr[0] == 'id' : 
                    data =  LibraryHistory.return_all_emp_actions(self.cur,
                                                                  self.db,search_attr[1]) 
                elif search_attr[0] == 'date' :
                    data = LibraryHistory.return_all_date_actions(self.cur,self.db,
                                                                  search_attr[1])
                else : 
                    data =  LibraryHistory.return_all_table_actions(self.cur,
                                                                    self.db,search_attr[1])   
            else : 
                data = LibraryHistory.return_all_actions(self.cur,self.db) 
            for row,action in enumerate(data) :
                self.history_table.insertRow(row)
                for col,item in enumerate(action) :
                    self.history_table.setItem(row,col,QTableWidgetItem(str(item)))

        except : 
            QMessageBox.information(self,"fail",'Invalid Operation')

    def search_history_table(self) : 
        try :
            if self.empid_rButton.isChecked() : 
                emp_id = int(self.emp_idTxt.text().strip())
                self.show_history_table(False,'id',emp_id)

            elif self.histT_rButton.isChecked() : 
                hist_table = self.actionTable_combo.currentText().strip()
                self.show_history_table(False,'hist_table',hist_table)
            
            elif self.actdate_rButton.isChecked() :
                action_date = self.action_dateTxt.date().toPyDate()
                print(action_date)
                self.show_history_table(False,'date',action_date)

        except :
            QMessageBox.information(self,"fail",'Invalid Operation')
#####################report############################
    def show_late_services(self) : 
        try : 
            self.rent_report_table.clearContents() 
            data = Services.return_late_returned(self.cur)
            for row,serv in enumerate(data) :
                self.rent_report_table.insertRow(row)
                for col,item in enumerate(serv) :
                    self.rent_report_table.setItem(row,col,QTableWidgetItem(str(item)))
        except : 
            QMessageBox.information(self,"fail",'Invalid Operation') 


    def show_top5_rented_books(self) : 
        try : 
            from_data = self.from_top5.date().toPyDate()
            to_date = self.to_top5.date().toPyDate()
            data = Services.top_5_books(self.cur,from_data,to_date)
            self.top_5renBook_table.clearContents()
            for row,book in enumerate(data) :
                self.top_5renBook_table.insertRow(row)
                for col,item in enumerate(book) :
                    self.top_5renBook_table.setItem(row,col,QTableWidgetItem(str(item)))
        except : 
            QMessageBox.information(self,"fail",'Invalid Operation') 

    def show_top5_salling_books(self) : 
        try : 
            from_data = self.from_top5salling.date().toPyDate()
            to_date = self.to_top5salling.date().toPyDate()
            data = BookBuy.top_5_books(self.cur,from_data,to_date)
            self.top5_sellbookTable.clearContents()
            for row,book in enumerate(data) :
                self.top5_sellbookTable.insertRow(row)
                for col,item in enumerate(book) :
                    self.top5_sellbookTable.setItem(row,col,QTableWidgetItem(str(item)))
        except : 
            QMessageBox.information(self,"fail",'Invalid Operation') 

    def show_profit(self) : 
        try : 
            from_date = self.from_top5salling.date().toPyDate()
            to_date = self.to_top5salling.date().toPyDate()
            data = BookBuy.get_profit(self.cur,from_date,to_date)
            if len(data) == 0 :
                profit = 0
            else :
                profit = data[0][0]

            self.trendsel_label_3.setText(str(profit) + ' $')


        except : 
            QMessageBox.information(self,"fail",'Invalid Operation') 

    
    def show_top5_members(self) : 
        try : 
            from_data = self.from_top5salling.date().toPyDate()
            to_date = self.to_top5salling.date().toPyDate()
            data = BookBuy.top_5_members(self.cur,from_data,to_date)
            self.top5_memTable.clearContents()
            for row,mem in enumerate(data) :
                self.top5_memTable.insertRow(row)
                for col,item in enumerate(mem) :
                    self.top5_memTable.setItem(row,col,QTableWidgetItem(str(item)))
        except : 
            QMessageBox.information(self,"fail",'Invalid Operation') 


    def show_mem_feedback(self) : 
        try: 
            mem_id = int(self.mem_idreport.text().strip())
            rent_operations = Services.return_mem_num_of_services(self.cur,mem_id)
            buy_operations = BookBuy.return_mem_num_of_operations(self.cur,mem_id)
            last_book_borrowed = Services.return_mem_lastbook(self.cur,mem_id)
            last_book_bought = BookBuy.return_mem_lastbook(self.cur,mem_id)
            preferred_category = Services.return_mem_prefCat(self.cur,mem_id)
            paid_to_library = BookBuy.return_mem_paid(self.cur,mem_id)

            self.rent_op.setText(str(rent_operations))
            self.buy_op.setText(str(buy_operations))
            self.last_borr.setText(str(last_book_borrowed))
            self.last_buy.setText(str(last_book_bought))
            self.pref_cat.setText(str(preferred_category))
            self.paid_to.setText(str(paid_to_library) + ' $')

        except : 
            QMessageBox.information(self,"fail",'Invalid Operation') 
###########################################################
    def open_homepage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(1)
    
    def open_bookpage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(2)
    
    def open_mempage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(3)
    
    def open_libpage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(4)
    
    def open_bkdetpage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(5)
    
    def open_servicespage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(6)

    def open_reportpage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(8)
    
    def open_historypage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(7)
    
    def open_settingspage_tab(self) : 
        self.mainTab_widget.setCurrentIndex(9)
####################Number of main page####################
    def update_count_of_all_books(self) : 
        book_count = Book.book_count(self.cur,self.db)
        self.no_of_books_label.setText(str(book_count))

    def update_count_of_all_members(self) : 
        member_count = Member.mem_count(self.cur,self.db)
        self.no_of_mem_label.setText(str(member_count))

    def update_count_of_all_services(self) : 
        rent_services_count = Services.services_count(self.cur,self.db)
        buy_services_count = BookBuy.sales_count(self.cur,self.db)
        count = rent_services_count + buy_services_count
        self.no_of_serv_label.setText(str(count))

    def total_sales_today(self) : 
        overall_sales = BookBuy.get_overall_sale(self.cur,self.db,date.today())
        if overall_sales is None :
            overall_sales = 0
        label = f'{overall_sales} $'
        self.sales_label.setText(str(label))
    
    def trend_book_thismonth(self) : 
        trend_book = Services.most_rented_book_thismonth(self.cur)
        self.most_renlabel.setText(trend_book)

    def trend_salebook_thismonth(self):
        trend_salebook = BookBuy.most_selling_book_thismonth(self.cur)
        self.trendsel_label.setText(trend_salebook)
    
    def trend_author(self) :
        trend_author = Services.trend_author_thismonth(self.cur)
        self.trendauth_label.setText(trend_author)
    
    def trend_publisher(self) : 
        trend_pub= Services.trend_publisher_thismonth(self.cur)
        self.trendpub_label.setText(trend_pub)


def main() : 
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__' :
    main()
