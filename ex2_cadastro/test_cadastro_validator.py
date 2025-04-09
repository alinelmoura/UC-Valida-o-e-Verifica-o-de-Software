import pytest
from cadastro_validator import verificarCadastro  # supondo que está no arquivo cadastro.py

# Casos válidos
@pytest.mark.parametrize("participante", [
    {"idade": 12, "categoria": "infantil", "tempoEstimado": 60, "assinaturaTermo": True},
    {"idade": 15, "categoria": "juvenil", "tempoEstimado": 120, "assinaturaTermo": True},
    {"idade": 30, "categoria": "adulto", "tempoEstimado": 45, "assinaturaTermo": True},
    {"idade": 60, "categoria": "adulto", "tempoEstimado": 180, "assinaturaTermo": True},
])
def test_verificacao_valida(participante):
    assert verificarCadastro(participante) is True

# Casos inválidos
@pytest.mark.parametrize("participante", [
    {"idade": 9, "categoria": "infantil", "tempoEstimado": 60, "assinaturaTermo": True},        # idade abaixo
    {"idade": 61, "categoria": "adulto", "tempoEstimado": 60, "assinaturaTermo": True},         # idade acima
    {"idade": 14, "categoria": "juvenil", "tempoEstimado": 60, "assinaturaTermo": True},        # categoria errada para idade
    {"idade": 17, "categoria": "adulto", "tempoEstimado": 60, "assinaturaTermo": True},         # categoria errada para idade
    {"idade": 20, "categoria": "infantil", "tempoEstimado": 60, "assinaturaTermo": True},       # categoria errada
    {"idade": 20, "categoria": "adulto", "tempoEstimado": 25, "assinaturaTermo": True},         # tempo muito curto
    {"idade": 20, "categoria": "adulto", "tempoEstimado": 200, "assinaturaTermo": True},        # tempo muito longo
    {"idade": 20, "categoria": "adulto", "tempoEstimado": 60, "assinaturaTermo": False},        # não assinou termo
    {"idade": 20, "categoria": "master", "tempoEstimado": 60, "assinaturaTermo": True},         # categoria inválida
])
def test_verificacao_invalida(participante):
    assert verificarCadastro(participante) is False
