from flask import Blueprint, jsonify, request  
import requests  
from app.services.compra_services import CompraService  

compra = Blueprint('compra', __name__, url_prefix='/api/compra')  
compra_services = CompraService()  

  
PRODUCTO_API_URL = 'http://productocontainer:5000/api/producto'  

@compra.route('/agregarcompra', methods=['POST'])  
def agregarcompra():  
    data = request.get_json()  
    id_producto = data.get('id_producto')  
    cantidad = data.get('cantidad')  

    if not id_producto or not isinstance(cantidad, int):  
        return jsonify({'error': 'Falta agregar id y cantidad'}), 400  
 
    try:
        response = requests.get(f'{PRODUCTO_API_URL}/find_by_id/{id_producto}')
        response.raise_for_status()
    except requests.exceptions.ConnectionError as e:
        print(f"Error connecting to {PRODUCTO_API_URL}: {e}")

    nueva_compra = compra_services.agregar_compra(id_producto, cantidad)  
    return jsonify({'id_compra': nueva_compra.id_compra}), 201  

@compra.route('/find_by_id/<int:id>', methods=['GET'])  
def find_by_id(id):  
    compra = compra_services.get_compra_by_id(id)  
    if compra:  
        return jsonify({  
            'id_compra': compra.id_compra,  
            'id_producto': compra.id_producto,  
            'cantidad': compra.cantidad,  
            'fecha_compra': compra.fecha_compra.isoformat()  
        }), 200  
    return jsonify({'error': 'Compra no encontrada'}), 404  

@compra.route('/delete/<int:id>', methods=['DELETE'])  
def delete_compra(id):  
    eliminado = compra_services.delete_compra(id)  
    if eliminado:  
        return jsonify({'mensaje': 'Compra eliminada con éxito'}), 200  
    return jsonify({'error': 'Compra no encontrada'}), 404  

@compra.route('/all', methods=['GET'])  
def get_all_compras():  
    compras = compra_services.get_all_compras()  
    return jsonify([{  
        'id_compra': compra.id_compra,  
        'id_producto': compra.id_producto,  
        'cantidad': compra.cantidad,  
        'fecha_compra': compra.fecha_compra.isoformat()  
    } for compra in compras]), 200  

@compra.route('/update/<int:id>', methods=['PUT'])  
def update_compra(id):  
    data = request.get_json()  
    cantidad = data.get('cantidad')  
    id_producto = data.get('id_producto')

    if cantidad is None or not isinstance(cantidad, int):  
        return jsonify({'error': 'Falta agregar una cantidad'}), 400  
    
    producto_response = requests.get(f'{PRODUCTO_API_URL}/find_by_id/{id_producto}')  
    if producto_response.status_code != 200:  
        return jsonify({'error': 'Producto no encontrado'}), 404  

    compra_actualizada = compra_services.update_compra(id, cantidad)  
    if compra_actualizada:  
        return jsonify({  
            'id_compra': compra_actualizada.id_compra,  
            'id_producto': compra_actualizada.id_producto,  
            'cantidad': compra_actualizada.cantidad,  
            'fecha_compra': compra_actualizada.fecha_compra.isoformat()  
        }), 200  
    return jsonify({'error': 'Compra no encontrada o no actualizada'}), 404