from app import db  
from app.models import Compra  
from sqlalchemy.exc import IntegrityError, NoResultFound

class CompraRepository:  
    def save(self, compra: Compra) -> Compra:  
        db.session.add(compra)  
        try:  
            db.session.commit()  
            return compra  
        except IntegrityError:  
            db.session.rollback()  
            return None  

    def find_by_id(self, id: int) -> Compra :
        try:
            return db.session.query(Compra).filter(Compra.id_compra == id).one()
        except NoResultFound:
            return None
    def delete(self, compra: Compra) -> None:  
        db.session.delete(compra)  
        db.session.commit()  

    def find_all(self) -> list:  
        return db.session.query.all()
    
    
    def update(self, compra: Compra) -> Compra:
        try:
            db.session.commit()
            return compra
        except IntegrityError:
            print("Rollback en update")
            db.session.rollback()
            return None
            