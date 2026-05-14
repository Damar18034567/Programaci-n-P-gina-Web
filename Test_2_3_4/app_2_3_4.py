# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_items = [
        {"nombre": "GTA 5", "categoria": "Acción"},
        {"nombre": "My Summer Car", "categoria": "Simulación"},
        {"nombre": "Fishing Planet", "categoria": "Simulación"}
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'items'
    return render_template("galeria.html", favoritos=mis_items)

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)