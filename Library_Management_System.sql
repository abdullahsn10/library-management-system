create database DeirQaddis_library;
use DeirQaddis_library;

-- create tables 

create table Publisher (
	pub_id int primary key auto_increment,
    pub_name varchar(30) not null
    );
alter table publisher auto_increment = 2200;

create table Author ( 
	auth_id int primary key auto_increment,
    auth_fname varchar(30) not null, 
    auth_lname varchar(30) not null
    ); 
alter table author auto_increment=1100;

 
 create table Category (
	cat_no int primary key auto_increment,
    cat_name varchar(20) not null,
    cat_desc varchar(80)
    ); 
alter table category auto_increment=8800;

create table Book (
	book_code int unique not null primary key auto_increment,
    book_title varchar(25) not null,
    book_price int,
    book_pages int,
    book_cat int not null,
    book_pub int not null,
    book_auth int not null,
    foreign key(book_cat) references Category(cat_no),  
    foreign key(book_pub) references Publisher(pub_id),
    foreign key(book_auth) references Author(auth_id)
    );
    select * from book;
alter table book auto_increment=56560000;
alter table book drop column book_title;
alter table book add column book_title varchar(90) not null after book_code;
create table book_copy (
	copy_no int primary key auto_increment,
    book_code int not null,
    loan_status varchar(25) not null default 'not_rented',
    copy_status varchar(20) not null default 'new',
    foreign key (book_code) references book(book_code)
    );
alter table book_copy auto_increment = 0;

create table Members (
	mem_id int primary key auto_increment,
    mem_fname varchar(30) not null,
    mem_mname varchar(30) not null,
    mem_lname varchar(30) not null,
    mem_addr varchar(30) not null,
    mem_phone_one varchar(35) not null,
    mem_phone_two varchar(35),
    mem_mail varchar(50) not null
    ); 
alter table members auto_increment=1200000;


create table Librarian (
	lib_id int not null unique primary key auto_increment,
    lib_fname varchar(30) not null,
    lib_mname varchar(30) not null,
    lib_lname varchar(30) not null,
    lib_main varchar(50) not null,
    lib_city varchar(20) not null,
    lib_village varchar(20),
    lib_street varchar(20),
    lib_phone int not null,
    lib_password varchar(30) not null,
    sup_id int not null,
    foreign key(sup_id) references Librarian(lib_id)
    );
alter table librarian auto_increment=9989999;

create table Services ( 
	rent_no int primary key auto_increment ,
    rent_date date not null,
    to_date date not null,
    rent_status enum('Rented','Returned'),
    book_copy int not null,
    mem_id int not null,
    emp_id int not null,
    foreign key(book_copy) references book_copy(copy_no),  
    foreign key(mem_id) references Members(mem_id),
    foreign key(emp_id) references Librarian(lib_id)
    );
alter table library_history auto_increment=1;
create table Library_History ( 
	hist_no int not null auto_increment primary key,
    emp_id int not null,
    hist_action enum('Login','Update','Add','Delete'),
    hist_table enum('Book','Members','Librarian','Publisher','Author','Category','Reports','Services','Login'),
    foreign key(emp_id) references Librarian(lib_id)
    );
alter table library_history drop column hist_action;
alter table library_history add column action_date date;

alter table librarian add column lib_password varchar(30) not null after lib_lname;
alter table book add column book_desc varchar(80);
alter table members modify column mem_phone_two varchar(30);
alter table author add  column auth_name varchar(40) not null;
-- select * from author;

-- select from tables 
select * from author;
select * from publisher;
select * from category;
select * from book; 
select * from members;
select * from librarian;
select * from book_copy;
alter table librarian rename column lib_main to lib_mail;
INSERT INTO librarian(lib_fname,lib_mname,lib_lname,lib_mail,lib_city,lib_village,lib_street,lib_phone,sup_id,lib_password) 
VALUES ('Abdullah','Sami','Naser','1201952@student.birzeit.edu','Ramallah','DeirQaddis','str2','0598813310',9990003,'admin111');
SET FOREIGN_KEY_CHECKS = 1;
delete from librarian where lib_id = 9990002;
delete from category where cat_no=8804;
delete from publisher where pub_id=2204;

insert into book_copy(book_code) values (1);

				SELECT COUNT(*)
                FROM book_copy c
                GROUP BY c.book_code
                HAVING c.book_code = 2;

SELECT m.mem_id,m.mem_fname,m.mem_mname,m.mem_lname,m.mem_addr,
                   m.mem_phone_one,m.mem_phone_two,m.mem_mail 
            FROM members m;
SELECT c.copy_no,c.loan_status,c.copy_status
            FROM book_copy c 
            WHERE c.book_code = 56560003;

alter table members modify column mem_id int auto_increment;

alter table librarian drop constraint sup_fk;
alter table book_copy add constraint 
		on_del_cas foreign key(book_code) references book (book_code) on delete cascade;
alter table librarian modify column sup_id int;

alter table librarian add constraint sup_fk 
			foreign key(sup_id) references librarian(lib_id) on delete set null;
delete from book where book_code = 56560002;

select * from members;


update librarian l
set l.sup_id = null
where l.lib_id = 9990003;


select * from librarian;

delete from librarian l 
where l.lib_id = 9990006;


select * from services;
select * from book;
select * from members;
select * from librarian;
select * from book_copy;
select * from library_history;
select * from author;
select * from publisher;
select * from category;
select * from author;
select * from book_copy;
select * from book_buy;

delete 
from services 
where rent_no = 9;


select s.rent_no,s.rent_date,s.to_date,s.rent_status,s.book_copy,s.mem_id,s.emp_id 
from services s,book b , book_copy c 
where b.book_code = 56560000 and
	  b.book_code =  c.book_code and 
	  c.copy_no = s.book_copy;
      
-- members who reserved all books 

select m.mem_fname,m.mem_lname 
from members m 
where not exists (
		select b.book_code 
        from book b 
        where b.book_code not in (
				select c.book_code 
                from book_copy c 
                where c.copy_no in (
						select s.book_copy
                        from services s 
                        where s.mem_id = m.mem_id
									)
								  )
				);

alter table book_copy add column buy_status varchar(20) default 'yes';
select * from book_copy;



create table book_buy (
	buy_no int primary key auto_increment ,
    buy_date date,
    book_copy int not null,
    mem_id int not null,
    emp_id int not null,
    foreign key(book_copy) references book_copy(copy_no),  
    foreign key(mem_id) references Members(mem_id),
    foreign key(emp_id) references Librarian(lib_id)
    );
alter table book_buy auto_increment=1;
delete from book_copy where copy_no = 47;
select * from book_copy;

alter table services add column return_date date null;
select * from services;

delete from book_copy c 
where c.copy_no = 27;
select * from book_buy;

SELECT COUNT(*)
            FROM book_buy;
select * from librarian;


create table librarian_permissions ( 
	perm_no int primary key auto_increment,
    lib_id int not null,
    book_tab int,
    mem_tab int,
    lib_tab int,
    det_tab int,
    serv_tab int,
    hist_tab int,
    sett_tab int,
    constraint lib_per_fk foreign key(lib_id) references librarian(lib_id)
    );
select * from librarian;
select * from librarian_permissions;

select * from library_history;

delete from book_buy;
select * from book_buy;
alter table book_buy add column book_price int ;
update book_buy y,book_copy c , book b 
set y.book_price  = b.book_price 
where y.book_copy = c.copy_no and 
	  c.book_code = b.book_code;
SET SQL_SAFE_UPDATES = 0;

delete from book;
delete from members;
delete from services;
delete from book_buy;
delete from author;
delete from book_copy;
delete from category;
delete from library_history;
delete from publisher;

select * from book_buy;
select sum(10 * b.book_price)
from book_buy b;

 select * from library_history;
 
 
SELECT * 
            FROM library_history lh
            WHERE lh.action_date = '2023-06-24';
            
            
select * from services s
where to_date < '2023-07-6' and 
		rent_status != 'Returned';
select * from services s ;

SELECT b.book_title
FROM services s,book_copy c , book b
WHERE s.book_copy = c.copy_no and 
	c.book_code = b.book_code and 
    MONTH(s.rent_date) = '7'
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

select * from book_buy;

SELECT b.book_title
FROM book_buy s,book_copy c , book b
WHERE s.book_copy = c.copy_no and 
	c.book_code = b.book_code and 
    MONTH(s.buy_date) = '7'
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

select * from services s;
select * from book;
select * from author ;
select * from publisher;


SELECT a.pub_name
FROM services s,book_copy c , book b , publisher a
WHERE s.book_copy = c.copy_no and 
c.book_code = b.book_code and 
b.book_pub = a.pub_id and 
 MONTH(s.rent_date) = 7
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

select b.book_title,count(*)
from services s ,book_copy c , book b 
where s.book_copy=c.copy_no and 
	c.book_code  = b.book_code and 
    s.rent_date >= '2023-7-1' and 
    s.rent_date <= '2023-7-6'
group by b.book_title
order by count(*) desc;


SELECT b.book_title,SUM(y.book_price) 
            FROM book_buy y ,book_copy c , book b 
            WHERE y.book_copy=c.copy_no and 
                c.book_code  = b.book_code and 
                y.buy_date >= '2023-7-1' and 
				y.buy_date <= '2023-7-6'
            GROUP BY b.book_title 
            ORDER BY SUM(y.book_price)  desc
            LIMIT 5;
select * from book_buy;
select * from members;

select m.mem_id,sum(y.book_price)
from book_buy y,members m 
where y.mem_id = m.mem_id and 
	y.buy_date >= '2023-6-1' and 
	y.buy_date <= '2023-7-6'
group by m.mem_id
order by sum(y.book_price) desc;

           
select * from author;
SELECT SUM(y.book_price)
from book_buy y 
where                 y.buy_date >= '2023-7-5' and 
				y.buy_date <= '2023-7-6';
select * from book_buy;

SELECT b.book_title,y.book_price
from book b , book_buy y , book_copy c , author a 
where y.book_copy = c.copy_no and
      c.book_code = b.book_code 
	 --  b.book_auth = a.auth_id and 
--       a.auth_id = 1111 
group by b.book_title , y.book_price
order by sum(y.book_price) desc;








-- FROM services s,book_copy c , book b , publisher a
-- WHERE s.book_copy = c.copy_no and 
-- c.book_code = b.book_code and 
-- b.book_pub = a.pub_id and 
--  MONTH(s.rent_date) = 7
-- GROUP BY a.pub_name
-- HAVING COUNT(*) = (
--     SELECT COUNT(*)
--     FROM services s2,book_copy c1 , book b1 , publisher a1
--    WHERE s2.book_copy = c1.copy_no and 
-- 	c1.book_code = b1.book_code and 
-- 	b1.book_pub = a1.pub_id and 
--     MONTH(s2.rent_date) = 7
--     GROUP BY a1.pub_name
--     ORDER BY COUNT(*) DESC
--     LIMIT 1
-- );

select * 
from librarian;

select * from services;

select count(*)
from services s 
group by s.mem_id
having mem_id = 1200000;


select * from book_buy;

select sum(y.book_price)
from book_buy y
group by y.mem_id
having y.mem_id = 1200001;


select b.book_title
from services s,book_copy c,book b 
where s.book_copy = c.copy_no and 
	c.book_code = b.book_code
group by s.mem_id,b.book_title,s.rent_date
having s.mem_id = 1200000
order by s.rent_date desc
limit 1;

select b.book_title
            from book_buy s,book_copy c,book b 
            where s.book_copy = c.copy_no and 
                c.book_code = b.book_code
            group by s.mem_id,b.book_title,s.buy_date
            having s.mem_id = 1200001
            order by s.buy_date desc
            limit 1;
    select * from book;        
            
select s.mem_id,b.book_title,t.cat_name 
from services s , book_copy c , book b , category t
where s.book_copy = c.copy_no and 
	  c.book_code = b.book_code and 
      b.book_cat = t.cat_no 
group by s.mem_id,b.book_title,t.cat_name
having s.mem_id = 1200000;

SELECT t.cat_name
FROM services s
JOIN book_copy c ON s.book_copy = c.copy_no
JOIN book b ON c.book_code = b.book_code
JOIN category t ON b.book_cat = t.cat_no
WHERE s.mem_id = 1200000
GROUP BY s.mem_id, t.cat_name
ORDER BY COUNT(*) DESC
LIMIT 1;

select * from book_buy;
select t.cat_name,count(*)
from services s , book_copy c , book b , category t
where s.book_copy = c.copy_no and 
	  c.book_code = b.book_code and 
      b.book_cat = t.cat_no 
group by t.cat_name,s.mem_id
having s.mem_id = 1200000
order by count(*) desc;












