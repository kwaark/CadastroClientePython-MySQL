# CadastroClientePython-MySQL
Programa para cadastro de clientes através do Python usando MySQL como banco de dados.

Sistema de cadastro consiste em NOME;IDADE;CPF;NACIONALIDADE;SEXO >

Iremos usar a biblioteca "mysql.connector" para fazer a conexão com o banco de dados MySQL

- Conexão concluída

##########################################################################################################
###### Alguns comandos utilizados para a criação do novo banco de dados no MySQL ######
-Criar novo banco de dados-
CREATE DATABASE funcionarios;

-Mostrar bancos de dados existentes-
show databases;

-Usar/Selecionar o banco de dados-
USE funcionarios;

-Criar uma tabela-
CREATE TABLE cadastros(nome VARCHAR(50) NOT NULL, idade INT NOT NULL, cpf VARCHAR(20) NOT NULL, nacionalidade VARCHAR(50) DEFAULT "BRASILEIRO", sexo VARCHAR(20));

-Mostrar tabelas do banco e tipos-
DESCRIBE cadastros;

-Inserir valores na tabela-
INSERT INTO cadastros VALUE("Junior", 29, "06076146310", "AMERICADO", "MASCULINO");

-Ver oque há na tabela-
SELECT * FROM cadastros

-Deletar uma linha-
DELETE FROM cadastros WHERE nome='Junior' and cpf='06076146310';


-usuario cadastrado para utilizar o banco MySQL:
login: kwaark1@localhost
senha: GFh@#0871

##########################################################################################################

Iremos agora fazer um interface gráfica utilizando a biblioteca "TKINTER"

















