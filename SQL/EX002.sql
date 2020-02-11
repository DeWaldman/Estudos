create database cadastro
default character set utf8
default collate utf8_general_ci;
use cadastro;
create table pessoas (
	id_pessoa int not null auto_increment,
	nome varchar (30) not null,
	nascimento date,
	sexo enum ('M', 'F'),
	peso decimal (5,2),
	altura decimal (3,2),
	nacionalidade varchar (20) default 'Brasil',
	primary key (id_pessoa)
)default charset = utf8;

insert into pessoa
values
(default, 'Tia null', '1923-05-30', 'F', '70.50', '1.72', default),
(default, 'gustavo', '2000-05-03', 'M', '60.50', '1.71', default),
(default, 'zé', '2000-11-06', 'M', '60.70', '1.68', default);

insert into pessoa (nome,id_pessoa,nascimento)
values ('dani', default, '2000-07-08');


alter table pessoa add column profissao varchar(10);
alter table pessoa modify profissao varchar(20) not null default '';
alter table pessoa drop column profissao;
