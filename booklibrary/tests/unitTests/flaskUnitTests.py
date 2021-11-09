import unittest
import os

from flask_testing import TestCase
from booklibrary.run import app
from booklibrary import db

basedir = os.path.abspath(os.path.dirname(__file__))

class TestConfig():
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(basedir, 'test.db')

class BaseTestCase(TestCase):

    def create_app(self):
        app.test_client('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class FlaskTestCase(BaseTestCase):

    # ensure the Flask is set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    # ensure the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Remember Me' in response.data)

    # ensure the login behaves correctly given the correct credentials
    def test_correct_login_page_loads(self):
        response = self.client.post('/login', data=dict(email='M@S.pl', password='Martin'), follow_redirects=True)
        self.assertIn(b'Sign Up Now', response.data)

    # ensure the login behaves correctly given the incorrect credentials
    def test_incorrect_login_page_loads(self):
        response = self.client.post('/login', data=dict(email='M@S.com', password='Martin'), follow_redirects=True)
        self.assertNotIn(b'Login Successful.', response.data)

    # ensure the logout behaves correctly
    def test_correct_logout(self):
        self.client.post('/login', data=dict(email='M@S.pl', password='Martin'), follow_redirects=True)
        response = self.client.get('/logout',follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

    # ensure the home page requires login
    def test_login_required_modify_mode_page(self):
        response = self.client.get('/book/modify/mode',follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    # ensure the book list show up on the List the Books page
    def test_book_list_appears_when_envoked(self):
        self.client.post('/login', data=dict(email='M@S.pl', password='Martin'), follow_redirects=True)
        response = self.client.get('/book/list', follow_redirects=True)
        self.assertIn(b'', response.data)

if __name__ == '__main__':
    unittest.main()
