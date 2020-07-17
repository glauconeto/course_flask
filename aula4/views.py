from flask import Flask, request

"""Extensão Flask"""

def init_app(app):
    """Inicialização de extensões"""
    @app.route('/')
    def index():
        print(request.args)
        return "Hello Codeshow"
        app.run(debug=True)

    @app.route("/contato")
    def contato():
        return "<form><input type='text'><\input><\form>"