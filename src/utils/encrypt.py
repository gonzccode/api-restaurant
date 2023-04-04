import bcrypt


def create_hashed_password(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt).decode('utf-8')
    return hashed_password


def validate_password(password, encrypt_password):
    password_v = password.encode('utf-8')
    encrypt_password_v = encrypt_password.encode('utf-8')
    validate_value = bcrypt.checkpw(password_v, encrypt_password_v)
    return validate_value


