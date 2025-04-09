import pytest
from email_validator import validar_email

@pytest.mark.parametrize("email_valido", [
    "usuario@exemplo.com",
    "nome.sobrenome@dominio.co",
    "user123@sub.dominio.com.br",
    "nome+tag@dominio.com",
    "nome_sobrenome@dominio.info",
    "user@localhost.com",
    "u" * 64 + "@dominio.com",     # limite parte local
    "user@" + "d" * 63 + ".com",   # domínio longo válido
])
def test_emails_validos(email_valido):
    assert validar_email(email_valido) is True

@pytest.mark.parametrize("email_invalido", [
    "usuario@",                  # sem domínio
    "@dominio.com",              # sem nome
    "usuario@.com",              # domínio incompleto
    "u" * 65 + "@dominio.com",   # parte local > 64
    "a" * 255 + "@gmail.com",    # email > 254
])

def test_emails_invalidos(email_invalido):
    assert validar_email(email_invalido) is False
