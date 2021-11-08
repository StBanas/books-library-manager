import os

# from flaskr import create_app
from booklibrary import create_app

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app()

app.config['SECRET_KEY'] = 'ac381138f988698c'
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'dbase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)

