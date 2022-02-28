from msilib.schema import Class
from optparse import Values
from django.db import connection
import mysql.connector, datetime
from mysql.connector import errorcode
from pygame import init
from sistema import login_manager


def ConnectDB():
    try:
        connection = mysql.connector.connect(
                        host = 'localhost',
                        user = 'root',
                        password = 'M@dotate314159',
                        database = 'db_escola'
        )
        print("Conexão realizada com sucesso!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe!")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha estão errados!")    
        else:
            print("ERRO!")
    return connection


class Professor():
    def __init__(self, nome,email,tel,endereco,senha):
        self.nome = nome                
        self.email = email                
        self.tel = tel                
        self.endereco = endereco                
        self.senha = senha 

    def  profregister(self):
        connection = ConnectDB()
        sql = "INSERT INTO Professores (nome_professor, email, tel, endereco, senha) VALUES (%s, %s, %s, %s, %s)"
        cursor = connection.cursor()
        values = (self.nome,
                  self.email,
                  self.tel,
                  self.endereco,
                  self.senha)     
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()






            



