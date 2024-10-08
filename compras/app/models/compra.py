from dataclasses import dataclass
from app import db  
from datetime import datetime  


@dataclass
class Compra(db.Model):  
    __tablename__ = 'compras'  

    id_compra = db.Column(db.Integer, primary_key=True)  
    id_producto = db.Column(db.Integer, nullable=False)  
    
    cantidad = db.Column(db.Integer, nullable=False)  
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow)  
    
    #id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)  

    #producto = db.relationship('Producto', back_populates='compras', lazy=True)
