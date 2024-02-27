def year_validator(value):
    MIN_VALUE_YEAR = 1999
    MAX_VALUE_YEAR = 2030
    
    if value < MIN_VALUE_YEAR or value > MAX_VALUE_YEAR:
        raise ValueError('Year must be between 1999 and 2030!')