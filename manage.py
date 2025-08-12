from flask.cli import FlaskGroup
from app import create_app
from app.schemas import usuario_schema, proyecto_schema
from app.models import Usuario, Proyecto


cli = FlaskGroup(create_app=create_app)

@cli.command("run")
def create_user():
    user_data = {
        "nombre": "Diego Riquelme",
        "email": "rrdiegoisaac@gmail.com",
        "password": "admin123"
    }
    usuario = usuario_schema.load(user_data)
    usuario.set_email_lower(usuario.email)
    usuario.set_password(usuario.password)

    data = usuario_schema.dump(usuario)

    print(data)
    usuario.save_to_db()


@cli.command("run2")
def create_user():
    user_data = {
        "nombre": "Nuevo Proyecto",
        "descripcion": "Descripción del nuevo proyecto",
        "fecha_inicio": "2025-07-30",
        "fecha_fin" : "2025-09-18",
        "usuario_id" : 1
    }

    proyecto = proyecto_schema.load(user_data)
    data = proyecto_schema.dump(proyecto)
    
    print(data)

    proyecto.save_to_db()

@cli.command("find")
def find_usuario():
    usuario_id = 1  # ID del usuario a buscar
    usuario = Usuario.find_by_id(usuario_id)
    if usuario:
        data = usuario_schema.dump(usuario)
        print(data)
    else:
        print("usuario no encontrado")
 
@cli.command("find2")
def find_proyecto():
    proyecto_id = 1  # ID del proyecto a buscar
    proyecto = Proyecto.find_by_id(proyecto_id)
    if proyecto:
        data = proyecto_schema.dump(proyecto)
        print(data)
    else:
        print("proyecto no encontrado")


if __name__ == '__main__':
    cli()

