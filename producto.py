class Producto:
    def __init__(self, nombre, precio , cantidad):
        self.nombre = nombre 
        self.precio = precio
        self.cantidad = cantidad
        self.id = 0
         
    def getPrecio(self):
        return self.precio
    
    def detalles(self):
        return 'Producto: {}, precio ${}, cantidad: {}'.format(self.nombre , self.precio, self.cantidad)
    
    def precioXcantidad(self):
        return self.cantidad * self.precio
    
    def increment(self)-> int:
        self.cantidad  = self.cantidad + 1
        return self.cantidad
      
