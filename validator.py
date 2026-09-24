# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    import re
    pattern = r'\+?7[0-9]{10}'
    return bool(re.fullmatch(pattern, phone.replace('-', '').replace(' ', '')))


def validate_inn(inn: str) -> bool:
    """TODO: валидация ИНН."""
    pass
