"""Realiza testes para garantir que o app está rodando corretamente."""


def test_app_foi_criado(app):
    """
    Testa se o app foi criado.

    Args:
        app (Flask): App referenciado na fixture "app" em "conftest.py".
    """
    assert app.name == 'teamomae.app'


def test_config_foi_carregada(config):
    """
    Testa se o app não está utilizando a configuração "DEBUG".

    Args:
        config: Fixture automaticamente criada pela biblioteca "pytest-flask".
    """
    assert config['DEBUG'] is False


def test_rota_inicial_retorna_ok(client):
    """
    Testa se a rota inicial (/) retorna o status HTTP "200 OK".

    Args:
        client: Fixture automaticamente criada pela biblioteca "pytest-flask".
    """
    assert client.get('/').status_code == 200


def test_rota_inexistente_retorna_not_found(client):
    """
    Testa se uma rota não existente retorna o status HTTP "404 Not Found".

    Args:
        client: Fixture automaticamente criada pela biblioteca "pytest-flask".
    """
    assert client.get('/uma_rota_que_não_existe').status_code == 404
