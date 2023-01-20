import unittest
from utils.test_functions import User
from utils.test_functions import login
from dotenv import load_dotenv
import requests, os

load_dotenv()

class Test(unittest.TestCase):
    def test_token_is_generated(self):
        """Testing if login with correct credentials is successful."""
        u = User(
            'notification.converter.bot@gmail.com',
            os.getenv('PASS_1'),
            os.getenv('GMAIL_PASS_1')
            )

        res = requests.post(
            'http://mp3converter.com/login',
            auth=(u.name, u.password))

        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.text)

    def test_token_is_not_generated(self):
        """Testing if login with incorrect credentials is not successful."""
        u = User(
            'notification.converter.bot@gmail.com',
            'wrongpassword',
            'wrongpassword'
            )

        res = requests.post(
            'http://mp3converter.com/login',
            auth=(u.name, u.password))

        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.text, 'Invalid credentials')

    def test_mp3_with_incorrect_link_is_not_downloaded(self):
        """Testing if mp3 with incorrect link is not downloaded."""
        u = User(
            'notification.converter.bot@gmail.com',
            os.getenv('PASS_1'),
            os.getenv('GMAIL_PASS_1')
            )

        token = login(u.name, u.password)

        res = requests.get(
            'http://mp3converter.com/download',
            headers={'Authorization': f'Bearer {token}'},
            params={'fid': 'incorrect_link'}
        )

        self.assertEqual(res.status_code, 500)
        self.assertEqual(res.text, 'Internal server error')

    def test_request_without_link_returns_error(self):
        """Testing if request without link returns an error."""
        u = User(
            'notification.converter.bot@gmail.com',
            os.getenv('PASS_1'),
            os.getenv('GMAIL_PASS_1')
            )

        token = login(u.name, u.password)

        res = requests.get(
            'http://mp3converter.com/download',
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'File ID (fid) is required')
