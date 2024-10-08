from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass

class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column('id_producto', db.Integer, primary_key=True, autoincrement= True)
    nombre = db.Column('nombre', db.String(100), nullable=False)
    precio = db.Column('precio', db.Float, nullable=False)
    activado = db.Column('activado', db.Boolean, default=True, nullable=False)
    
    #compras = db.relationship('Compra', back_populates='productos')