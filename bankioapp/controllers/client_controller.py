
from bankioapp import app
from flask import render_template, redirect, request


# --------------------------------------------------------------------------
# GET /client/add
# --------------------------------------------------------------------------
# Root resource
@app.route('/client/add', methods=['GET'])
def get_add_client():
    return render_template('customer/add.html')


# --------------------------------------------------------------------------
# POST /client/add
# --------------------------------------------------------------------------
# Root resource
@app.route('/client/add', methods=['POST'])
def post_add_client():
    name = request.form['nombre']
    customer_id = request.form['cedula']
    address = request.form['direccion']
    marital_status = request.form['estado_civil']

    return name + customer_id + marital_status

