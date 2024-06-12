from flask import Flask, render_template

app = Flask("Reserva App")

@app.route("/")
def principal():
    return render_template('principal.html')