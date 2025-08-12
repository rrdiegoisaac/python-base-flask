from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from ..models import db, Proyecto
 
ma = Marshmallow()
 
 
class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session
 
 
class ProyectoSchema(BaseSchema):
    """
    ### USUARIO SE INCLUYE PARA QUE NOS MUESTRE LA INFORMACION DEUL USUARIO AL TRAER EL PROYECTO
    ### EXCLUIMOS EL PROYECTO PARA EVITAR RECURSION
    """
    usuario = fields.Nested("UsuarioSchema", exclude=("proyectos"))
 
    class Meta(BaseSchema.Meta):
        model = Proyecto
        include_fk = True
 
## esquema para traer un solo proyecto
proyecto_schema = ProyectoSchema()
 
## esquema para traer una lista de proyectos
proyectos_schema = ProyectoSchema(many=True)
 
 