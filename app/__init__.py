from app.common.math import lol
from config import Config


# simple example (replace the class with your Flask app)
class App(object):

    def __init__(self, config: Config):
        self.config = config

    def run(self):
        print(lol(self.config.ZEROS_SHAPE))


# config object to pass throw the app
config = Config()

app = App(config)
