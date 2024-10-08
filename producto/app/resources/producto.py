from flask import Blueprint, jsonify, request
from app.services.producto_services import ProductoService


producto = Blueprint('producto', __name__, url_prefix='/api/producto')
producto_services = ProductoService()


@producto.route('/agregarproducto', methods=['POST'])
def agregarproducto():
    data = request.get_json()  
    nombre = data.get('nombre')  
    precio = data.get('precio')  
    
    if not nombre or not isinstance(precio, (int, float)):  
        return jsonify({'error': 'agregar nombre y precio'}), 400  
    
    nuevo_producto = producto_services.agregar_producto(nombre, precio)  
    return jsonify({'id_producto': nuevo_producto.id_producto}), 201  

@producto.route('/find_by_id/<int:id>',methods=['GET'])
def find_by_id(id):
    producto = producto_services.get_producto_by_id(id)  
    if producto:  
        return jsonify({  
            'id_producto': producto.id_producto,  
            'nombre': producto.nombre,  
            'precio': producto.precio,  
            'activado': producto.activado  
        }), 200  
    return jsonify({'error': 'Producto no encontrado'}), 404 

@producto.route('/find_by_nombre/<string:nombre>',methods=['GET'])
def find_by_nombre(nombre):
    producto = producto_services.get_producto_by_nombre(nombre)  
    if producto:  
        return jsonify({  
            'id_producto': producto.id_producto,  
            'nombre': producto.nombre,  
            'precio': producto.precio,  
            'activado': producto.activado  
        }), 200  
    return jsonify({'error': 'Producto no encontrado'}), 404 

@producto.route('/update/<int:id>',methods=['PUT'])
def update_producto (id):
    data = request.get_json()  
    nombre = data.get('nombre')  
    precio = data.get('precio')  

    producto_actualizado = producto_services.update_producto(id, nombre, precio)  
    if producto_actualizado:  
        return jsonify({  
            'id_producto': producto_actualizado.id_producto,  
            'nombre': producto_actualizado.nombre,  
            'precio': producto_actualizado.precio,  
            'activado': producto_actualizado.activado  
        }), 200  
    return jsonify({'error': 'Error al actualizar'}), 404  



@producto.route('/delete/<int:id>', methods=['DELETE'])  
def delete_producto(id):  
    eliminado = producto_services.delete_producto(id)  
    if eliminado:  
        return jsonify({'mensaje': 'Producto eliminado con éxito'}), 200  
    return jsonify({'error': 'Producto no encontrado'}), 404  