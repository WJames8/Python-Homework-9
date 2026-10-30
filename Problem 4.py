
import random
import string

ROWS = 5
COLS = 6
SIZE = ROWS * COLS

path = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
    (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)
]


def encrypt(message):
    message = message.upper().replace(" ", "")

    if len(message) > SIZE:
        raise ValueError("Message cannot exceed 30 characters.")

    while len(message) < SIZE:
        message += random.choice(string.ascii_uppercase)

    grid = []
    for row in range(ROWS):
        grid.append(list(message[row * COLS:(row + 1) * COLS]))

    ciphertext = ""

    for row, column in path:
        ciphertext += grid[row][column]

    return ciphertext


def decrypt(ciphertext):
    if len(ciphertext) != SIZE:
        raise ValueError("Ciphertext must contain exactly 30 characters.")

    grid = [[''] * COLS for _ in range(ROWS)]

    for i in range(SIZE):
        row, column = path[i]
        grid[row][column] = ciphertext[i]

    plaintext = ""

    for row in range(ROWS):
        for column in range(COLS):
            plaintext += grid[row][column]

    return plaintext


message = input("Enter a message (maximum 30 characters): ")

encrypted = encrypt(message)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted message:", decrypted)
