"""
Generates a random key.
"""
import string
import random

def generate():
    """
    Generates the key.
    """
    uni = string.ascii_letters + string.digits + string.punctuation
    key = ''.join([random.SystemRandom().choice(uni) for i in range(random.randint(45, 50))])
    return key
