from flask import Flask

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to the app!'

    return app
