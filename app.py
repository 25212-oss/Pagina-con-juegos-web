from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para guardar personas
personas = []

@app.route("/", methods=["GET", "POST"])
def index():
    global personas

    # GUARDAR PERSONA
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")

        if nombre and edad:
            personas.append({
                "nombre": nombre,
                "edad": edad
            })

    # BUSCADOR
    busqueda = request.args.get("buscar")

    if busqueda:
        resultados = [
            p for p in personas
            if busqueda.lower() in p["nombre"].lower()
        ]
    else:
        resultados = personas

    return render_template("index.html", personas=resultados)


if __name__ == "__main__":
    app.run(debug=True)