from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "123456"
app.config["MYSQL_DB"] = "new_contacts"

mysql = MySQL(app)

app.secret_key = "mysecretkey"


@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", contacts=data)


# Crear contacto
@app.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)",
            (name, phone, email),
        )
        mysql.connection.commit()
        flash("Contacto creado correctamente")
        cur.close()
        return redirect(url_for("home"))


# Editar contacto
@app.route("/edit/<string:id>")
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts WHERE id = %s", (id,))
    data = cur.fetchall()
    cur.close()
    return render_template("edit_contact.html", contact=data[0])


# Actualizar contactos
@app.route("/update/<string:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    cur = mysql.connection.cursor()
    cur.execute(
        """
          UPDATE contacts SET
          name = %s,
          phone = %s,
          email  = %s
          WHERE id = %s
        """,
        (name, phone, email, id),
    )
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("home"))


# Eliminar contactos
@app.route("/delete/<string:id>")
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM contacts WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("home"))


if (__name__) == "__main__":
    app.run(debug=True, port=4000)
