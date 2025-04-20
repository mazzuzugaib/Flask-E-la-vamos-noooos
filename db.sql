create database playMusica;
use playmusica;
select * from musica;
select * from usuario;
create table musica(
	tb_id int primary key auto_increment not null,
    tb_titulo varchar(30) not null,
    tb_artista varchar(30) not null,
    tb_genero varchar(30) not null);
insert into musica(tb_titulo, tb_artista, tb_genero)
values('Hysteria', 'Muse', 'Rock');

create table usuario(
	id_us int primary key auto_increment not null,
    nome_us varchar(50) not null,
    login_us varchar(10) not null,
    senha_us varchar(10)not null);
insert into usuario(nome_us, login_us, senha_us)
values('Lorem Ipsum', 'lorem', 'ipsum');
alter table usuario
add unique (login_us);