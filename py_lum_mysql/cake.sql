create database cakehut;
use cakehut;
create table cake(id int auto_increment primary key,
				  name varchar(200) not null
                  );
insert into cake(name) values('vanko cake');
insert into cake(name) values('chocolate cake');
insert into cake(name) values('dream cake');
insert into cake(name) values('red velvet cake');
insert into cake(name) values('black forest'),('white forest');
insert into cake(name) values('blueberry cake');

select * from cake;

create table cakevarients(id int auto_increment primary key,
                          weight enum('1kg','2kg','3kg','4kg','5kg') default '1kg',
                          price int not null,
                          flavour varchar(200) not null,
                          shape enum('round','rectangle','square','triangle') default 'round',
                          cake_id int,
                          foreign key(cake_id) references cake(id) on delete cascade,
                          unique(weight,price,flavour,shape,cake_id)
                          );
                          
insert into cakevarients(weight,price,flavour,cake_id) values('1kg',700,'cheese',1);
insert into cakevarients(weight,price,flavour,cake_id) values('2kg',1400,'cheese',1);
insert into cakevarients(weight,price,flavour,cake_id) values('1kg',800,'spanish delight',2);
insert into cakevarients(weight,price,flavour,cake_id) values('3kg',2300,'spanish delight',2);
insert into cakevarients(weight,price,flavour,cake_id) values('1kg',900,'chocolate',3);
insert into cakevarients(weight,price,flavour,cake_id) values('4kg',3600,'chocolate',3);
insert into cakevarients(weight,price,flavour,cake_id) values('1kg',750,'red velvet',4);
insert into cakevarients(weight,price,flavour,cake_id) values('3kg',2100,'red velvet',4);
insert into cakevarients(weight,price,flavour,cake_id) values('1kg',550,'chocolate',5);
insert into cakevarients(weight,price,flavour,cake_id) values('2kg',1100,'chocolate',5);
insert into cakevarients(weight,price,flavour,cake_id) values('1kg',550,'white chocolate',6);
insert into cakevarients(weight,price,flavour,cake_id) values('2kg',1100,'white chocolate',6);
insert into cakevarients(weight,price,flavour,cake_id) values('1kg',1000,'blueberry',7);
insert into cakevarients(weight,price,flavour,cake_id) values('2kg',2000,'blueberry',7);

select * from cakevarients;

select cake.name,cakevarients.weight,cakevarients.price from cake,cakevarients where cake.id=cakevarients.cake_id;

-- select 1kg cakenames
select cake.name,cakevarients.weight from cake,cakevarients where cake.id=cakevarients.cake_id and cakevarients.weight="1kg";