
from bankioapp import app
from flask import render_template


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/', methods=['GET'])
def home():
    return render_template('home/index.html')
