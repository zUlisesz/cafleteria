from conex import Connection
from pedido import Pedido
from datetime import date
import mysql.connector

class Query:
    
    @staticmethod
    def sendPackage(carrito):
        key = Connection.connectBD()
        if  key  is None:
            print("No se pudo establecer la conexión con la base de datos.")
            return
        
        cursor = key.cursor()
        
        query = '''
        INSERT INTO cafeteria.pedidos(pastel,flan , docena_galletas, brownie, americano, malteada ,smoothie, fecha, total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);\ncommit; '''
        
        values = (
            carrito[0].cantidad,
            carrito[1].cantidad,
            carrito[2].cantidad,
            carrito[3].cantidad,
            carrito[4].cantidad,
            carrito[5].cantidad,
            carrito[6].cantidad,
            date.today(),
            Pedido.calcularCarrito(carrito),
        )
        
        try:
            cursor.execute(query, values)
            print("Pedido enviado correctamente.")
        except mysql.connector.Error as error:
            print('Error: {}'.format(error))
        finally:
            cursor.close()
            key.close()
    
######### HAsta la línea 42 el código funciona eficientemente           
    @staticmethod
    def getAll( tree):
        
        for row in tree.get_children():
                tree.delete(row)
        
        key = Connection.connectBD()
        
        if key is None:
            print("No se pudo establecer la conexión con la base de datos.")
            return
        
        cursor = key.cursor()
        
        try:
            cursor.execute("SELECT * FROM pedido")
            myresult = cursor.fetchall()
            
            for row in myresult:
                tree.insert("", "end", values=row)
                
        except mysql.connector.Error as error:
            print('Error: {}'.format(error))
        finally:
            cursor.close()
            key.close()
