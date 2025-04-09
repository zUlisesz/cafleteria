import mysql.connector

class Connection:
    
    def connectBD():
        try:
            conex = mysql.connector.connect(
                user= 'root',
                password='Interesting.Eminem',
                host= '127.0.0.1',
                database= 'cafeteria',
                port= '3306'
            )      
        except mysql.connector.Error as error:
            print('Error durante la conexión: {}'.format(error))
             
        return conex
