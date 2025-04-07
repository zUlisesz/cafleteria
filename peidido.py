class Pedido:
    elementos = []
    
    @staticmethod
    def calcularCarrito(carro ):
        suma  = 0 
        for element in carro:
            suma += element.precioXcantidad()
            
        return suma
    
    @staticmethod
    def addElement(objeto) -> bool :
        value  = False
        if( objeto not in Pedido.elementos):
            Pedido.elementos.append(objeto)
            value = True
           
        return value 
    
