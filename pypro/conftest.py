import pytest
from model_mommy import mommy


@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_model = mommy.make(django_user_model, email='admin@admin.com', first_name='Jacare')
    return usuario_model


@pytest.fixture
def client_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client
