import pytest
from email_validator import validate


# Tipos inválidos
def test_should_not_accept_null():
    assert not validate(None)

def test_should_not_accept_non_string():
    assert not validate(123)
    assert not validate([])


# Strings vazias ou malformadas
def test_should_not_accept_empty_string():
    assert not validate('')

def test_should_not_accept_missing_at():
    assert not validate('userexample.com')

def test_should_not_accept_multiple_ats():
    assert not validate('user@@example.com')


# Tamanho máximo
def test_should_not_accept_more_than_320_chars_total():
    email = 'l' * 64 + '@' + 'd' * 128 + '.' + 'd' * 127
    assert not validate(email)

def test_should_not_accept_local_part_too_long():
    email = 'l' * 65 + '@example.com'
    assert not validate(email)

def test_should_not_accept_domain_too_long():
    email = 'a@' + 'd' * 256
    assert not validate(email)

def test_should_not_accept_domain_labels_too_long():
    email = 'user@' + 'd'*64 + '.com'
    assert not validate(email)


# Local part inválido
def test_should_not_accept_empty_local_part():
    assert not validate('@example.com')

def test_should_not_accept_spaces_in_local_part():
    assert not validate('user name@example.com')

def test_should_not_accept_local_with_two_dots():
    assert not validate('user..name@example.com')

def test_should_not_accept_local_with_ending_dot():
    assert not validate('user.@example.com')

def test_should_not_accept_invalid_chars_in_local():
    assert not validate('userç@example.com')


# Domain inválido
def test_should_not_accept_empty_domain_part():
    assert not validate('user@')

def test_should_not_accept_domain_without_dot():
    assert not validate('user@example')

def test_should_not_accept_domain_with_invalid_char():
    assert not validate('user@examplç.com')

def test_should_not_accept_domain_with_ending_dot_only():
    assert not validate('user@.com')


# Válidos
def test_should_accept_basic_valid_email():
    assert validate('user@example.com')

def test_should_accept_email_with_subdomain():
    assert validate('user@mail.example.com')

def test_should_accept_email_with_plus_sign():
    assert validate('user+label@example.co.uk')

def test_should_accept_email_with_special_chars():
    assert validate('user.name+filter@sub-domain.example.com')

def test_should_accept_minimum_valid_email():
    assert validate('a@b.co')

