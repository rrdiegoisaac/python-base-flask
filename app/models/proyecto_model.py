from .db import Base, ReBase, db
import datetime as dt
 
 
class Proyecto(ReBase):
    """Model for project management."""
    __tablename__ = 'proyectos'

    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False, unique=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id', ondelete='CASCADE'), nullable=False)

    usuario = db.relationship('Usuario', back_populates='proyectos')