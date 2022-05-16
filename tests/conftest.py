"""Prepara o ambiente de testes."""

import pytest

from teamomae.app import Flask, cria_app


@pytest.fixture(scope='module')
def app() -> Flask:
    """
    Garante que todos os testes terão o app.

    O "scope=module" garante que o mesmo app será usado para todas as funções.
    """
    return cria_app()
