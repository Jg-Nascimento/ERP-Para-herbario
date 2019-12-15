create database herbario;

insert into cadastros(nome, senha, nivel) values ('admin', '1234', 2);
select *from cadastros;		
create table cadastros(
id int primary key auto_increment,
nome varchar(50) not null,
senha varchar(20) not null,
nivel int not null

);

select * from exsicatas where especie LIKE '%sda%';

drop table exsicatas;

create table exsicatas(
familia varchar(200),
genero varchar(200),
especie varchar(200),
nomeVulgar varchar(200),
localColeta varchar(200),
coletor varchar(200),
dataColeta varchar(15),
numeroTombamento int primary key auto_increment,
observacoes varchar(2000)

);

select * from exsicatas;

insert into exsicatas (familia, genero, especie, nomeVulgar, localColeta, coletor, dataColeta) values ('sasdasdfsadfasddsfsdafdsfasfsa
sdfsdafsdafsdafsda', 'adfa', 'ewqrwrw', 'fasfs', 'dsfasdfs', 'sdafsdfsa', '23421332	');