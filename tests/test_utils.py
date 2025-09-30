import pytest
from src.core.utils.normalizador import NivelNormalizer


def test_normalizar_nivel():
    assert NivelNormalizer.normalizar("1") == "1° básico"
    assert NivelNormalizer.normalizar("primero") == "1° básico"
    assert NivelNormalizer.normalizar("2do") == "2° básico"
    assert NivelNormalizer.normalizar("tercero") == "3° básico"
    assert NivelNormalizer.normalizar("4°") == "4° básico"


def test_nivel_invalido():
    with pytest.raises(ValueError):
        NivelNormalizer.normalizar("5")
