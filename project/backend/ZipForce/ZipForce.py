import re
import subprocess
from typing import Union
from zipfile import ZipFile, BadZipFile, LargeZipFile


class ZipForceInterface(object):
    def _passwords_list(self, passwords: str) -> list[Union[str, int]]:
        """
            Convert string with passwords to dictionary
        :param passwords: string
        :return Dictionary:
        """
        pass

    def _open_zip(self, filepath: str) -> ZipFile:
        """
            Opening zip file
        :param filepath: string
        :return ZipFile:
        """
        pass

    def _check_password(self, filepath: str, password: str) -> bool:
        """
            Check if password match
        :param filepath: string
        :param password: string
        :return Boolean:
        """
        pass

    def parse(self) -> str:
        """
            Parse password list and try to get right password
        :return string:
        """
        pass


class ZipForce(ZipForceInterface):
    def __init__(self, filepath: str, passwords: str):
        self.filepath = filepath
        self.passwords = passwords

    def _passwords_list(self, passwords: str) -> list[Union[str, int]]:
        if 0 == len(passwords):
            raise ValueError('Empty passwords list')
        if not isinstance(passwords, str):
            raise TypeError('Passwords list is not a string type')

        linebreaks = re.split(r'\n', passwords, flags=re.IGNORECASE)

        return list(filter(None, linebreaks)) if linebreaks is not None else [passwords]

    def _open_zip(self, filepath: str) -> ZipFile:
        try:
            return ZipFile(filepath, mode='r')
        except FileNotFoundError:
            raise FileNotFoundError(f'Zip archive {filepath} was not found')
        except BadZipFile:
            raise BadZipFile(f'File: {filepath} is not ZIP archive')
        except LargeZipFile:
            raise LargeZipFile(f'ZIP file {filepath} Too large for open, MAX size 4GB')

    def _check_password(self, filepath: str, password: str) -> bool:
        if 0 == len(password) or 0 == len(filepath):
            raise ValueError('Empty arguments')
        if not isinstance(password, str) or not isinstance(filepath, str):
            raise TypeError('Arguments are not a string type')

        try:
            check_archive = subprocess.check_output(f'7z t -p{password}  {filepath}', shell=True)
            return str(check_archive).find('Everything is Ok') != -1
        except subprocess.SubprocessError as e:
            return False

    def parse(self) -> str:
        prepare_passwords_list = self._passwords_list(self.passwords)
        file_is_opened = self._open_zip(self.filepath)

        if not isinstance(file_is_opened, ZipFile):
            raise FileNotFoundError(f'File can not be opened')

        for password in prepare_passwords_list:
            if self._check_password(self.filepath, password):
                return password

        return ''
