from flask import  Blueprint
from flask import  render_template
import booklibrary.users.forms
from flask_marshmallow import Marshmallow

main = Blueprint('main', __name__)

ma = Marshmallow(booklibrary)

@main.route("/")
def index():
    return render_template('index.html', title='Home')
