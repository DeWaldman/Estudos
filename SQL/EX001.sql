create database condominio_x
default character set utf8
default collate utf8_general_ci;
use condominio_x;

create table moradores (
	cpf char(11) not null,
    rg varchar(20) not null,
    nome varchar(50) not null,
    nascimento date not null,
    email varchar(50) not null,
    numero_fixo varchar(20) not null,
    senha varchar(100) not null
)default charset = utf8;

insert into moradores(
cpf,rg,nome,nascimento,email,numero_fixo,senha)
values(
"12345678909",
"1122334455",
"gabriel","19800513"
,"551240028922",
"123456789");
