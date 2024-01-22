from utils.db import db

class Coches(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    imagen_nombre = db.Column(db.String(255))  # Nombre del archivo en la carpeta static/img
    imagen_blob = db.Column(db.LargeBinary)  # Blob para almacenar la imagen en la base de datos

    def __init__(self, marca,modelo,descripcion,anio,precio,imagen_nombre,imagen_blob):
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.anio = anio
        self.precio = precio
        self.imagen_nombre = imagen_nombre
        self.imagen_blob = imagen_blob
