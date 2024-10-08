from app import db
from app.models.producto import Producto
from sqlalchemy.exc import IntegrityError, NoResultFound

class ProductoRepository:
    def save(self, producto: Producto) -> Producto:
        try:
            db.session.add(producto) 
            db.session.commit()
            return producto
        except IntegrityError:
            db.session.rollback()
            print("Rollback en repository 1")
            
            
    def delete(self, producto: Producto) -> None:
        try:
            db.session.delete(producto)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print("Rollback en repository 2")
            
    def find_by_id(self, id: int) -> Producto :
        try:
            return db.session.query(Producto).filter(Producto.id_producto == id).one()
        except NoResultFound:
            return None
        
    def find_by_nombre(self, nombre: str):
        try:
            return db.session.query(Producto).filter(Producto.nombre == nombre).one_or_none()
        except NoResultFound:
            return None
        
    def update(self, producto: Producto) -> Producto:
        try:
            db.session.add(producto)
            db.session.commit()
            return producto
        except IntegrityError:
            print("Rollback en update")
            db.session.rollback()
            return None
            