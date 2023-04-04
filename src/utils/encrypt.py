import bcrypt


def create_hashed_password(password):
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password


def validate_password(password, encrypt_password):
    validate_value = bcrypt.checkpw(password, encrypt_password)
    return validate_value

