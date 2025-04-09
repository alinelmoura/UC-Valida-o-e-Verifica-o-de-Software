import re

def validar_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    if len(email) > 254:
        return False

    padrao_regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(padrao_regex, email):
        return False

    try:
        parte_local, dominio = email.split("@")
    except ValueError:
        return False

    #antes @ deve ter até 64 caracteres
    if len(parte_local) > 64:
        return False

    return True
