create database imdb;

use imdb;
create table language(
        id int auto_increment primary key,
        name varchar(200) not null unique
);

insert into language(name) values("malayalam"),("tamil"),("english"),("hindi");
select * from language order by id;

create table movies(
       id int auto_increment primary key,
       name varchar(200) not null unique,
       year varchar(200) not null,
       language_id int not null,
       foreign key(language_id) references language(id) on delete no action
);

desc movies;

insert into movies(name,year,language_id) values("2018","2023",1),("jailer","2023",2),("home","2023",1),("leo","2023",2),("jawan","2023",4),("avengers","2012",3),("rdx","2023",1);
select * from movies;

select movies.name,movies.year,language.name from movies,language where movies.language_id=language.id;

-- print malayalam movies names
select name from movies where language_id=1;

select movies.name,language.name from movies,language where language.id=1 and movies.language_id=1;

select movies.name from movies,language where movies.language_id=language.id and language.name="malayalam";

create table reviews(
		id int auto_increment primary key,
		comment varchar(200) not null,
        rating int check(rating <6),
        user varchar(200) not null,
        movies_id int,
        foreign key(movies_id) references movies(id) on delete cascade
        );
        

insert into reviews(comment,rating,user,movies_id) values("peda sanam",4,"sooraj",1),("must watch",5,"shibil",1),("good",4.5,"vishnu",1);
insert into reviews(comment,rating,user,movies_id) values("thee padam",5,"sooraj",2),("supperb movie",5,"shibil",2),("kozhappilla",4,"vishnu",2);
insert into reviews(comment,rating,user,movies_id) values("good",4.3,"sooraj",3),("feel good",4,"shibil",3),("one time",3.5,"vishnu",3);

select * from reviews;

select movies.name,reviews.comment,reviews.rating,reviews.user from movies inner join reviews on movies.id=reviews.movies_id;

select movies.name,reviews.comment,reviews.rating,reviews.user from movies left join reviews on movies.id=reviews.movies_id;

-- right join - right table all records and left table matching records
select distinct(r1.movies_id) from reviews as r1,reviews as r2 where r1.movies_id=r2.movies_id and r1.id!=r2.id; -- self join
select name from movies where id in (select distinct(r1.movies_id) from reviews as r1 , reviews as r2 where r1.movies_id=r2.movies_id and r1.id != r2.id);