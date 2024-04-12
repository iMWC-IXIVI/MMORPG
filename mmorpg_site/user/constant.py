"""Создание токена на случайной основе"""

import random


BASIC = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
RANDOM_STRING = ''.join([random.choice(BASIC) for _ in range(30)])
