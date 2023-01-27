from flask import Flask

#apps configuration
app= Flask(__name__)

from apps.api import blueprint
app.register_blueprint(blueprint)

@app.route('/')
def index():
    return 'Hello Bye Bye'
