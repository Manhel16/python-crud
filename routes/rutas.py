from flask import Blueprint,render_template,request,url_for,redirect,flash
from models.coches import Coches
from utils.db import db

rutas = Blueprint('rutas', __name__)

@rutas.route("/")
def index():
    coches = Coches.query.all()
    return render_template('index.html', coches = coches)
@rutas.route("/new", methods=['GET'])
def mostrar_formulario():
    return render_template('add_coche_form.html')
@rutas.route("/new", methods=['POST'])
def add_coche():
    
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        descripcion = request.form["descripcion"]
        anio = int(request.form["anio"])
        precio = int(request.form["precio"])
        imagen_nombre = request.files["imagen_nombre"]
        imagen_blob = request.files["imagen_blob"]

        imagen_nombre.save("static/img/" + imagen_nombre.filename)
        imagen_blob_data = imagen_blob.read()

        new_coche = Coches(marca,modelo,descripcion, anio,precio,imagen_nombre.filename,imagen_blob_data)
        print(new_coche)
        db.session.add(new_coche)
        db.session.commit()
        flash("coche aniadido correctamente!")
        return redirect(url_for("rutas.index"))

@rutas.route('/update/<id>', methods=['POST','GET'])
def actualizar(id):
    coches = Coches.query.get(id)

    if request.method == 'POST':
        coches.marca = request.form["marca"] if request.form["marca"] != request.form["marca_actual"] else coches.marca
        coches.modelo = request.form["modelo"] if request.form["modelo"] != request.form["modelo_actual"] else coches.modelo
        coches.descripcion = request.form["descripcion"] if request.form["descripcion"] != request.form["descripcion_actual"] else coches.descripcion
        coches.anio = int(request.form["anio"]) if int(request.form["anio"]) != int(request.form["anio_actual"]) else coches.anio
        coches.precio = int(request.form["precio"]) if int(request.form["precio"]) != int(request.form["precio_actual"]) else coches.precio

        # Manejar la actualización de la imagen_nombre
        nueva_imagen_nombre = request.files.get("imagen_nombre")
        if nueva_imagen_nombre:
            coches.imagen_nombre = nueva_imagen_nombre.filename
            nueva_imagen_nombre.save("static/img/" + nueva_imagen_nombre.filename)

        # Manejar la actualización de la imagen_blob
        nueva_imagen_blob = request.files.get("imagen_blob")
        if nueva_imagen_blob:
            coches.imagen_blob = nueva_imagen_blob.read()

        db.session.commit()
        flash("Coche Actualizado Correctamente.")
        return redirect(url_for('rutas.index'))
    else:
        return render_template('update.html', coches=coches)
@rutas.route('/eliminar/<id>')
def eliminar_coche(id):
    coches = Coches.query.get(id)
    db.session.delete(coches)
    db.session.commit()
    flash("Coche eliminado correctamente!")
    return redirect(url_for('rutas.index'))