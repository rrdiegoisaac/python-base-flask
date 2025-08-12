from .db import Base, ReBase, db
import datetime as dt
from werkzeug.security import (
    generate_password_hash,
    check_password_hash)


class Usuario(Base):
    """Model for user management."""
    __tablename__ = 'usuarios'
 
    usuario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False, default=lambda: dt.datetime.now(dt.UTC)-dt.timedelta(hours=4))
 
    proyectos = db.relationship('Proyecto', back_populates='usuario')
 
    @classmethod
    def find_by_id(cls, id):
        """Encuentra registro por ID"""
        return cls.query.filter_by(usuario_id=id).first()
 
    @classmethod
    def set_email_lower(cls, email):
        """Set email to lowercase."""
        cls.email = email.lower()
        return cls.email

    def set_password(self, password):
        """Set hashed password."""
        self.password = generate_password_hash(password)