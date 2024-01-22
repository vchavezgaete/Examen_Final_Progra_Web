from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/calculocompras', methods=['GET', 'POST'])
def calculoCompra():
    if request.method == 'POST':

        nombre = str(request.form['nombre'])
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])

        resultado = round(numero2 * 9000)
        resultado2 = 0

        if numero1 >= 18 and numero1 <= 30:
            resultado2 = round(resultado * 0.15)

        elif numero1 > 30:
            resultado2 = round(resultado * 0.25)

        resultadototal = resultado - resultado2

        return render_template('calculocompras.html', nombre1=nombre, resultado1=resultado, resultado2=resultado2,
                               resultado3=resultadototal)
    return render_template('calculocompras.html')


@app.route('/iniciosesion', methods=['GET', 'POST'])
def largoNombre():
    if request.method == 'POST':

        nom1 = request.form['nombre']
        pass1 = request.form['password']
        resultado = 'Usuario o contraseña incorrectos'

        if nom1 == 'juan' and pass1 == 'admin':
            resultado = 'Bienvenido administrador juan'

        elif nom1 == 'pepe' and pass1 == 'user':
            resultado = 'Bienvenido usuario pepe'

        return render_template('iniciosesion.html', resultado1=resultado)
    return render_template('iniciosesion.html')


if __name__ == '__main__':
    app.run(debug=True)