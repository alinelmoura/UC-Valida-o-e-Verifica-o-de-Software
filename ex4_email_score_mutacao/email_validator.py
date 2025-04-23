# usei o cosmic-ray
import re

EMAIL_LOCAL_REGEX = re.compile(r'^[A-Za-z0-9!#$%&\'*+/=?^_`{|}~.-]+$')
EMAIL_DOMAIN_REGEX = re.compile(r'^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def validate(email: str) -> bool:
    if not isinstance(email, str) or not email or len(email) > 320:
        return False

    if email.count('@') != 1:
        return False

    local_part, domain = email.split('@', 1)

    if not local_part or not domain:
        return False

    if len(local_part) > 64 or len(domain) > 255:
        return False

    if ' ' in local_part or '..' in local_part or local_part.endswith('.'):
        return False

    domain_labels = domain.split('.')
    if any(not label or len(label) > 63 for label in domain_labels):
        return False

    if not EMAIL_LOCAL_REGEX.fullmatch(local_part):
        return False

    if not EMAIL_DOMAIN_REGEX.fullmatch(domain):
        return False

    return True
