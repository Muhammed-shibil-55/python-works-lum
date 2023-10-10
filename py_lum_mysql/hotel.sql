show databases;
create database hotel;
create database cakebox;
-- to use database
use hotel;
-- creating table in the database
create table items(
                  id int unique,
                  name varchar(120) not null,
                  catogory varchar(150) not null,
                  price int not null,
                  type varchar(150) not null
			      );
-- listing all tables
show tables;
-- inserting records into the table
insert into items(id,name,catogory,price,type) values(1,'vegfriedrice','veg',130,'chinese');
insert into items(id,name,catogory,price,type) values(2,'biriyani','nonveg',50,'indian');
insert into items(id,name,catogory,price,type) values(3,'fishfry','nonveg',40,'seafood');
insert into items(id,name,catogory,price,type) values(4,'ghee roast','veg',70,'indian');
insert into items(id,name,catogory,price,type) values(5,'alfaham mandi','nonveg',170,'arabic');
insert into items(id,name,catogory,price,type) values(6,'chilli gopi','veg',90,'chinese');
insert into items(id,name,catogory,price,type) values(7,'masala bonda','veg',10,'indian');
-- display table
select * from items;

select id,name,price from items;

-- select items available under rs 130
select * from items where price < 130;

-- select items available betwwen rs 150 and 200
select * from items where price > 150 and price < 200;

-- products name whose type not equal to chinese
select name from items where type != "chinese";

-- aggregate functions sum() min() max() avg() count()
select count(*) from items;
-- costly item
select max(price) from items;

select sum(price) from items;

select * from items where price = (select max(price) from items);

select * from items where price = (select min(price) from items);

select * from items where price = (select max(price) from items where catogory = "nonveg");

select max(price) from items where price != (select max(price) from items);

select * from items where price = (select max(price) from items where price != (select max(price) from items));

select catogory,count(*) from items group by(catogory);
select type,count(*) from items group by(type);

-- employee id name dept salary location


create database company;
show databases;
use company;
create table employee(id int unique,
                      name varchar(150) not null,
                      dept varchar(150) not null,
                      salary int not null,
                      location varchar(150) not null
                      );
insert into employee(id,name,dept,salary,location) values(100,'shibil','hr',150000,'perumbilavu');
insert into employee(id,name,dept,salary,location) values(101,'vishnu','sales',100000,'guruvayoor');
insert into employee(id,name,dept,salary,location) values(102,'sooraj','hr',150000,'pattambi');
insert into employee(id,name,dept,salary,location) values(103,'harshan','sales',120000,'vadakkanchery');
insert into employee(id,name,dept,salary,location) values(104,'rajas','delivery',75000,'edappal');
insert into employee(id,name,dept,salary,location) values(105,'harshavardhan','delivery',70000,'kakkanad');

show tables;
select * from employee;
select id,name,dept from employee; 
select * from employee where salary < 100000;
select * from employee where salary > 100000 and salary < 200000;
select * from employee where dept != "sales";
select count(*) from employee;
select max(salary) from employee;
select sum(salary) from employee;
select * from employee where salary = (select max(salary) from employee);
select * from employee where salary = (select min(salary) from employee);
select * from employee where salary = (select max(salary) from employee where dept = "delivery");
select max(salary) from employee where salary != (select max(salary) from employee);
select * from employee where salary = (select max(salary) from employee where salary != (select max(salary) from employee));
select dept,count(*) from employee group by dept;
select location,count(*) from employee group by location;

use hotel;

-- sort records
select * from items order by price asc;
select * from items order by price desc;
select * from items order by price asc limit 4;

select count(*) from items where name="biriyani";

update items set price=60 where id=2;
select * from items;

update items set catogory="nonveg" where id=7;
delete from items where id=3;

-- truncate items; delete all records from table only empty table remains
-- drop table items; wipe out the entire table

alter table items add column course enum("maincourse","starter","dessert") default "maincourse";
update items set course="starter" where id=7;
update items set course="starter" where id =6;

-- model relationship