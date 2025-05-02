from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits
from flask import Flask

app = Flask(__name__)

SPECIAL_CHARS = '#.,!@&^%*'

def generate_password():
    length = randint(8, 16)

    password = [
        choice(ascii_lowercase),
        choice(ascii_uppercase),
        choice(digits),
        choice(SPECIAL_CHARS)
    ]

    all_chars = ascii_lowercase + ascii_uppercase + digits + SPECIAL_CHARS
    password.extend(choice(all_chars) for _ in range(length - 4))

    return ''.join(password)

@app.route('/')
def password():
    return generate_password()

if __name__ == '__main__':
    app.run()
