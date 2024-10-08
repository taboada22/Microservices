import os  
import unittest  
from flask import current_app  
from app import create_app, db  
from app.models.producto import Producto  
from app.services.producto_services import ProductoService  

class ProductoTestCase(unittest.TestCase):   

    def setUp(self):  
        
        self.app = create_app()  
        self.app_context = self.app.app_context()  
        self.app_context.push()  
        db.create_all()  

        self.NOMBRE_PRUEBA = 'Pancho'  
        self.PRECIO_PRUEBA = 100.0  
               
        self.producto_service = ProductoService()  

    def tearDown(self):  
        db.session.remove()  
        db.drop_all()  
        self.app_context.pop()  

    def test_app(self):  
        self.assertIsNotNone(current_app)  

    def test_producto_create(self):  
        producto = self.__get_producto()  
        saved_producto = self.producto_service.agregar_producto(producto.nombre, producto.precio)  
        
        self.assertIsNotNone(saved_producto)  
        self.assertGreaterEqual(saved_producto.id_producto, 1)  
        self.assertEqual(saved_producto.nombre, self.NOMBRE_PRUEBA)  
        self.assertEqual(saved_producto.precio, self.PRECIO_PRUEBA)  

    def test_producto_find_by_id(self):  
        producto = self.__get_producto()  
        saved_producto = self.producto_service.agregar_producto(producto.nombre, producto.precio)  

        found_producto = self.producto_service.get_producto_by_id(saved_producto.id_producto)  
        self.assertIsNotNone(found_producto)  
        self.assertEqual(found_producto.id_producto, saved_producto.id_producto)  

    def test_producto_update(self):  
        producto = self.__get_producto()  
        saved_producto = self.producto_service.agregar_producto(producto.nombre, producto.precio)  

        updated_producto = self.producto_service.update_producto(saved_producto.id_producto, nombre='Producto B', precio=150.0)  
        self.assertIsNotNone(updated_producto)  
        self.assertEqual(updated_producto.nombre, 'Producto B')  
        self.assertEqual(updated_producto.precio, 150.0)  

    def test_producto_delete(self):  
        producto = self.__get_producto()  
        saved_producto = self.producto_service.agregar_producto(producto.nombre, producto.precio)  

        self.producto_service.delete_producto(saved_producto.id_producto)  
        deleted_producto = self.producto_service.get_producto_by_id(saved_producto.id_producto)  
        self.assertIsNone(deleted_producto)  

    def __get_producto(self):  
        producto = Producto()  
        producto.nombre = self.NOMBRE_PRUEBA  
        producto.precio = self.PRECIO_PRUEBA  
        return producto  

if __name__ == '__main__':  
    unittest.main()