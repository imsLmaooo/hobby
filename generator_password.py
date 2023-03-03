import random


# Генератор паролей
def generator_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    size = 10
    return ''.join(random.choice(chars) for x in range(size))