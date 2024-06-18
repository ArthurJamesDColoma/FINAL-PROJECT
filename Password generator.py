import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password_list = [random.choice(characters) for _ in range(length)]
    password = ''.join(password_list)
    return password

password = generate_password(10)
print(password)
