import os
import subprocess
import unittest
from zipfile import ZipFile, BadZipFile
from ..ZipForce import ZipForce


class TestZipForce(unittest.TestCase):
    test_filepath_zip = f'/data/test.zip'
    test_filepath_jpg = f'/data/test.jpg'
    test_filepath_fake = f'/data/test_fake.zip'

    def test_passwords_list(self):
        self.assertEqual(ZipForce._passwords_list(ZipForce, 'testPwd'), ['testPwd'])
        self.assertEqual(ZipForce._passwords_list(ZipForce, '123'), ['123'])
        self.assertEqual(ZipForce._passwords_list(ZipForce, 'pass1\npass2\n'), ['pass1', 'pass2'])

        with self.assertRaises(TypeError):
            ZipForce._passwords_list(ZipForce)
        with self.assertRaises(ValueError):
            ZipForce._passwords_list(ZipForce, '')
        with self.assertRaises(TypeError):
            ZipForce._passwords_list(ZipForce, 11)

    def test_open_zip(self):
        filepath = os.path.dirname(__file__)
        self.assertIsInstance(ZipForce._open_zip(ZipForce, filepath + self.test_filepath_zip), ZipFile)

        with self.assertRaises(FileNotFoundError):
            ZipForce._open_zip(ZipForce, filepath + self.test_filepath_fake)
        with self.assertRaises(BadZipFile):
            ZipForce._open_zip(ZipForce, filepath + self.test_filepath_jpg)

    def test_check_password(self):
        filepath = os.path.dirname(__file__) + self.test_filepath_zip

        self.assertFalse(ZipForce._check_password(ZipForce, filepath, 'asd'))
        self.assertTrue(ZipForce._check_password(ZipForce, filepath, '123'))

        with self.assertRaises(TypeError):
            ZipForce._check_password(ZipForce)
        with self.assertRaises(TypeError):
            ZipForce._check_password(ZipForce, '')
        with self.assertRaises(ValueError):
            ZipForce._check_password(ZipForce, '', '')
        with self.assertRaises(ValueError):
            ZipForce._check_password(ZipForce, '', '')

    def test_parse(self):
        filepath = os.path.dirname(__file__) + self.test_filepath_zip
        self.assertEqual(ZipForce(filepath, '123\nasd\nsadas').parse(), '123')
        self.assertEqual(ZipForce(filepath, '\nasd\nsadas').parse(), '')
        self.assertEqual(ZipForce(filepath, '123').parse(), '123')
        with self.assertRaises(ValueError):
            ZipForce(filepath, '').parse()

        return ''
