import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a random password of length 12
random_password = generate_password()
print(f"Your random password is: {random_password}")
