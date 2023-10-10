create database vegbox;
use vegbox;
create table items(
	id int auto_increment primary key,
    name varchar(200) not null unique
);
insert into items(name) values("pottatto"),("onion"),("drumstick"),("tomato");
select * from items;

create table stocks(
	id int auto_increment primary key,
    item_id int not null unique,
    qty int not null,
    price int not null,
    selling int not null,
    foreign key(item_id) references items(id) on delete cascade
    
);
insert into stocks(item_id,qty,price,selling) values(1,10,30,45),(3,50,25,40),(2,40,20,35),(4,10,80,100);
select * from stocks;

create table bills(
	id int auto_increment primary key,
    user varchar(200) not null,
    phone varchar(200) not null unique,
    date varchar(200) not null
);
insert into bills(user,phone,date) values("vinu","6531492299","3-9-2023");
select * from bills;

create table billitems(
	id int auto_increment primary key,
    bill_id int not null,
    item_id int not null,
    qty int not null,
    foreign key(bill_id) references bills(id) on delete no action,
    foreign key(item_id) references items(id) on delete no action
);
insert into billitems(bill_id,item_id,qty) values(2,2,2),(2,1,1),(1,4,2),(1,3,1);
select * from billitems;

