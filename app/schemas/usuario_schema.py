from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from ..models import db, Usuario
 
ma = Marshmallow()
 
 
class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session
 
 
class UsuarioSchema(BaseSchema):
    proyectos = fields.Nested("ProyectoSchema", many=True, exclude=("usuario"))
    class Meta(BaseSchema.Meta):
        model = Usuario
        include_fk = True
 
    password = auto_field(load_only=True)
 
 
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)