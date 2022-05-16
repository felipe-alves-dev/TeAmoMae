"""Instância e roda a aplicação."""
from flask import Flask


def cria_app() -> Flask:
    """
    Instância e configura a aplicação Flask.

    Returns:
        (Flask): Instancia do Flask que pode ser utilizada em outros arquivos.
    """
    app = Flask(__name__)

    @app.route('/')
    def inicio():
        return 'Olá, mundo!'

    return app


if __name__ == '__main__':
    app = cria_app()
    app.run()
