from flask import Flask, render_template, redirect, abort
from models import CoffeeBar
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/coffeebar')


@app.route('/coffeebar')
def list():
    coffeebars = CoffeeBar.query.all()

    return render_template('index.html',coffeebars=coffeebars)


@app.route('/coffeebar/<id>')
def get(id):
    coffeebar = CoffeeBar.query.get(id)
    if coffeebar is None:
        abort(404)
    return render_template('detail.html',coffeebar=coffeebar)
