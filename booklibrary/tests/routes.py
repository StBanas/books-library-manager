from flask import render_template
import booklibrary.books.forms
from flask_marshmallow import Marshmallow
from flask import Blueprint

test = Blueprint('test', __name__)

ma = Marshmallow(booklibrary)

# Help Page/tests
@test.route('/help/tests', methods=['GET'])
def tests():
    return render_template('tests.html', title='Tests')

@test.route('/help/tests/manual', methods=['GET'])
def manualTests():
    return render_template('manualTests.html', title='MT')

@test.route('/help/tests/automated', methods=['GET'])
def automatedTests():
    return render_template('automatedTests.html', title='AT')


@test.route('/help/tests/report', methods=['GET'])
def report():
    return render_template("report.html", title='Report')
