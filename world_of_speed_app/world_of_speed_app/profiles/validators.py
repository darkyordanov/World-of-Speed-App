def username_validator(value):
    if not all(ch.isalnum() or ch == '_' for ch in value):
        raise ValueError('Username must contain only letters, digits, and underscores!')
    
