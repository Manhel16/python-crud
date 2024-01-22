from flask import Flask
from routes.rutas import rutas
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://angeldaw1:Pal0meras@db4free.net/concesionario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Pal0meras'


app.register_blueprint(rutas)