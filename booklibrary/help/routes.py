from flask import  Blueprint
from flask import render_template
import booklibrary.books.forms
from flask_marshmallow import Marshmallow

helps = Blueprint('helps', __name__)

ma = Marshmallow(booklibrary)

# Help Page/Navigation
@helps.route('/help', methods=['GET'])
# @login_required
def help():
    return render_template('help.html', title='Help')

# Help Page/Navigation
@helps.route('/help/navigation', methods=['GET'])
def navigation():
    return render_template('navigation.html', title='Navigation')


# Help Page/Description
@helps.route('/help/description', methods=['GET'])
def description():
    return render_template('description.html', title='Help')


# Help Page/HowTo?
@helps.route('/help/howto', methods=['GET'])
def howTo():
    return render_template('howTo.html', title='HowTo')
