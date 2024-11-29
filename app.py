from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta para la página de login (será la página de inicio)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Capturamos el nombre ingresado en el formulario
        nombre = request.form['nombre']
        # Redirigimos directamente a la página principal
        return redirect(url_for('inicio'))
    # Si es una solicitud GET, renderizamos la página de login
    return render_template('login.html')

# Ruta para la página principal (después del login)
@app.route('/inicio')  # Usamos solo '/inicio' en lugar de '/index' para simplificar
def inicio():
    return render_template('index.html')

# Rutas para las otras páginas
@app.route('/actividades')
def actividades():
    return render_template('actividades.html')

@app.route('/objetivo')
def objetivo():
    return render_template('objetivo.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
