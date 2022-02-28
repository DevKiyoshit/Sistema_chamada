create database if not exists db_escola;
use db_escola;

create table if not exists Alunos(
id_aluno int primary key  not null auto_increment,
nome_aluno varchar(45) not null,
email varchar(45) not null,
tel varchar(20) not null,
recado varchar(20),
endereco varchar(120),
senha varchar(250)
) default charset = utf8;

create table if not exists Professores(
id_professor int primary key  not null auto_increment,
nome_professor varchar(45) not null,
email varchar(45) not null,
tel varchar(20) not null,
recado varchar(20),
endereco varchar(120),
senha varchar(250)
) default charset = utf8;

create table if not exists Cursos(
id_curso int primary key not null auto_increment,
nome_curso varchar(45) not null,
turno varchar(20) not null,
id_professor int not null,
id_aluno int not null,
foreign key (id_professor) references Professores(id_professor),
foreign key (id_aluno) references Alunos(id_aluno)
) default charset= utf8;
