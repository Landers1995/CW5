create table vacancies
(
id integer primary key,
name varchar(255) not null,
url varchar(255) not null,
type varchar(50) not null,
salary_from integer,
salary_to integer,
employer_id integer not null,
foreign key (employer_id) references employers (id) on delete cascade
);