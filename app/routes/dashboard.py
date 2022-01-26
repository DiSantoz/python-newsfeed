from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# route to return dashboard template


@bp.route('/')
def dash():
    return render_template('dashboard.html')

# route to retun edit-post template


@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')
