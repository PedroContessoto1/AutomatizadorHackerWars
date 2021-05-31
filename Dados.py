## config do .env
from os.path import join, dirname
from dotenv import load_dotenv
from util import env

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Dados:
    def __init__(self):
        self.login = env('LOGIN')
        self.senha = env('SENHA')
        self.link = env('LINK')
        self.path_chrome = env('PATH_CHROME')
        self.path_driver = env('PATH_DRIVER')
