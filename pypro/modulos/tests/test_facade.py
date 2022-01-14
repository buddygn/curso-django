import pytest
from model_mommy import mommy

from pypro.modulos import facade
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    lst = []
    for index, titulo in enumerate('Antes Depois'.split()):
        print(titulo, index)
        lst.append(mommy.make(Modulo, titulo=titulo, order=index))

    return lst


def test_list_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()
