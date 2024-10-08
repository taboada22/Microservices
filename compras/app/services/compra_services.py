from app.models import Compra  
from app.repositories.compra_repository import CompraRepository  

class CompraService:  
    def __init__(self):  
        self.repository = CompraRepository()  

    def agregar_compra(self, id_producto: int, cantidad: int) -> Compra:  
        nueva_compra = Compra(id_producto=id_producto, cantidad=cantidad)  
        return self.repository.save(nueva_compra)  

    def delete_compra(self, id_compra: int) -> bool:  
        compra = self.repository.find_by_id(id_compra)  
        if compra:  
            self.repository.delete(compra)  
            return True  
        return False  
    
    def get_compra_by_id(self, id_compra: int) -> Compra:  
        return self.repository.find_by_id(id_compra)  

    def get_all_compras(self) -> list:  
        return self.repository.find_all()
    
    def update_compra(self, id_compra: int, cantidad: int) -> Compra:  
        compra = self.repository.find_by_id(id_compra)  
        if compra:  
            compra.cantidad = cantidad  
            return self.repository.update(compra)  
        return None  