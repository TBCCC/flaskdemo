import os
import flaskr
import unittest
import tempfile

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd,flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING']=True
        self.app = falskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unl
        os.unlink(flaskr.app.config["DATABASE"])


if __name__ == '__main__':
    unittest.main()
