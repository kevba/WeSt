import os
from flask import Flask

west = Flask(__name__)
west.config.from_object('app.config.default')

import app.views