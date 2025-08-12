from flask import Blueprint, jsonify
 
from ..models import Proyecto
from ..schemas import proyecto_schema
 
main = Blueprint('main', __name__)
 
@main.route('/', methods=['GET'])
def home():
 
    proyecto_id = 1  # ID del proyecto a buscar
    proyecto = Proyecto.find_by_id(proyecto_id)
    if proyecto:
        data = proyecto_schema.dump(proyecto)
        print(data)
    else:
        print("proyecto no encontrado")
 
    return jsonify(data), 200