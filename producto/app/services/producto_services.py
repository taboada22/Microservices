from app.models.producto import Producto  
from app.repositories.producto_repository import ProductoRepository  

class ProductoService:  
    def __init__(self):  
        self.repository = ProductoRepository()  

    def agregar_producto(self, nombre: str, precio: float) -> Producto:  
        nuevo_producto = Producto(nombre=nombre, precio=precio)  
        return self.repository.save(nuevo_producto)  

    def delete_producto(self, id_producto: int) -> bool:  
        producto = self.repository.find_by_id(id_producto)  
        if producto:  
            self.repository.delete(producto)  
            return True  
        return False  

    def get_producto_by_id(self, id_producto: int) -> Producto:  
        return self.repository.find_by_id(id_producto)  

    def get_producto_by_nombre(self, nombre: str) -> Producto:  
        return self.repository.find_by_nombre(nombre)  

    def update_producto(self, id_producto: int, nombre: str , precio: float ) -> Producto:  
        producto = self.repository.find_by_id(id_producto)  
        if producto:  
            if nombre is not None:  
                producto.nombre = nombre  
            if precio is not None:  
                producto.precio = precio  
            if producto.activado == False:  
                producto.activado = True
            
            return self.repository.update(producto)  
        return None