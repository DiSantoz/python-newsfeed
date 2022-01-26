# import functions from FLASK module
from flask import Blueprint, render_template

bp = Blueprint("home", __name__, url_prefix='/')

# route to return homepage template


@bp.route('/')
def index():
    return render_template("homepage.html")

# route to return login template


@bp.route('/login')
def login():
    return render_template('login.html')

# route to return single-post template


@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')
