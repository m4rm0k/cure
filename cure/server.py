from flask import Flask
app = Flask(__name__)

# Simple spell, but quite unbreakable.

import cure.api.auth
import cure.api.base
import cure.api.board
import cure.api.user
import cure.api.tracker