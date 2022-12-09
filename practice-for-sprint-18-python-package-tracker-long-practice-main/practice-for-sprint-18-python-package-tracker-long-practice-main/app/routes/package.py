from flask import Blueprint, render_template
from app.forms import PackageForm
bp = Blueprint('new_package', __name__, url_prefix="")

@bp.route('/new_package', methods = ['GET', 'POST'])
def package():
    form = PackageForm()
    return render_template('shipping_request.html', form=form)
