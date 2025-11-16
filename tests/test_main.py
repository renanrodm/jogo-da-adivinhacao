from src.jogo_da_adivinhacao_renan_martins.main import geraCartelas


def test_gera_cartelas_estrutura_correta():

    cartelas = geraCartelas()

    assert len(cartelas) == 6
