import unittest
from booklibrary.run import app

class MyTestCase(unittest.TestCase):

# ensure the Flask is set up correctly
    def test_index(self):
        tester=app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(response.status_code, 200)

# ensure the login page loads correctly
    def test_login_page_loads(self):
        tester=app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Remember Me' in response.data)

# ensure the login behaves correctly given the correct credentials
    def test_correct_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email='M@S.pl', password='Martin'), follow_redirects=True)
        self.assertIn(b'Sign Up Now', response.data)

# ensure the login behaves correctly given the incorrect credentials
    def test_incorrect_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email='M@S.com', password='Martin'), follow_redirects=True)
        self.assertNotIn(b'Login Successful.', response.data)

# ensure the logout behaves correctly
    def test_correct_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email='M@S.pl', password='Martin'), follow_redirects=True)
        response = tester.get('/logout',follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

# ensure the home page requires login
    def test_login_required_modify_mode_page(self):
        tester=app.test_client(self)
        response = tester.get('/book/modify/mode',follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

# ensure the book list show up on the List the Books page
    def test_book_list_appears_when_envoked(self):
        tester=app.test_client(self)
        tester.post('/login', data=dict(email='M@S.pl', password='Martin'), follow_redirects=True)
        response = tester.get('/book/list', follow_redirects=True)
        self.assertIn(b'List of books in Library', response.data)

if __name__ == '__main__':
    unittest.main()
