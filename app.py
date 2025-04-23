from flask import Flask, render_template, request
import obtener_ip
from base_datos import bd
from enviar_correo import enviar_correo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", ip=obtener_ip.mi_ip)

@app.route("/seguridad-privacidad")
def seguridad_privacidad():
    return render_template("seguridad-privacidad.html", ip=obtener_ip.mi_ip)

@app.route("/tratamiento-informacion")
def tratamiento_informacion():
    return render_template("tratamiento-informacion.html", ip=obtener_ip.mi_ip)

@app.route("/almacenamiento-informacion")
def almacenamiento_informacion():
    return render_template("almacenamiento-informacion.html", ip=obtener_ip.mi_ip)

@app.route("/principales-amenazas")
def principales_amenazas():
    return render_template("principales-amenazas.html", ip=obtener_ip.mi_ip)

@app.route("/contraseñas")
def contrasenas():
    return render_template("contraseñas.html", ip=obtener_ip.mi_ip)

@app.route("/proteccion-trabajo")
def proteccion_trabajo():
    return render_template("proteccion-trabajo.html", ip=obtener_ip.mi_ip)

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    email = request.form['email']
    validacion = bd.insert_into("usuarios", ("nombre", "email"), (nombre, email))

    if validacion:
        mensaje = "Se ha inscrito correctamente a las noticias semanales."
        enviar_correo(email, nombre)
    else:
        mensaje = "No se ha podido inscribir a las noticias semanales. Este usuario ya está inscrito."

    return render_template("mensaje.html", mensaje=mensaje)
