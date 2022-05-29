#importar la libreria flask,redirect
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
 
#Areglo que almacenara la lista de  tareas 
tareas = []
 # funcion del controlador 
@app.route("/")
def home():
	return render_template("index.html", tareas=tareas)


# se crean los metosos get y post que sirbe oara redirigir al controlador agregar
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
	if request.method == "GET":
		return render_template("agregar.html")
	else:
		tarea = request.form.get("tarea")
		tareas.append(tarea)
		return redirect("/")

#metodo principal
if __name__ == "__main__":
	app.run(debug=True)