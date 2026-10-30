
import random
import string


def create_grid(message, rows, columns):
    size = rows * columns

    if len(message) > size:
        raise ValueError("Message is too long for the selected grid.")

    while len(message) < size:
        message += random.choice(string.ascii_uppercase)

    grid = []

    for row in range(rows):
        grid.append(list(message[row * columns:(row + 1) * columns]))

    return grid


def get_keyword_order(keyword):
    return sorted(range(len(keyword)), key=lambda i: keyword[i])


def create_path(rows, columns, keyword):
    order = get_keyword_order(keyword)
    path = []

    for row in range(rows):
        if row % 2 == 0:
            for column in order:
                path.append((row, column))
        else:
            for column in reversed(order):
                path.append((row, column))

    return path


def encrypt(message, keyword, rows, columns):
    message = message.upper().replace(" ", "")
    keyword = keyword.upper()

    if len(keyword) != columns:
        raise ValueError("Keyword length must match the number of columns.")

    grid = create_grid(message, rows, columns)
    path = create_path(rows, columns, keyword)

    ciphertext = ""

    for row, column in path:
        ciphertext += grid[row][column]

    return ciphertext


def decrypt(ciphertext, keyword, rows, columns):
    keyword = keyword.upper()

    if len(keyword) != columns:
        raise ValueError("Keyword length must match the number of columns.")

    if len(ciphertext) != rows * columns:
        raise ValueError("Ciphertext length does not match grid size.")

    grid = [[''] * columns for _ in range(rows)]
    path = create_path(rows, columns, keyword)

    for i in range(len(path)):
        row, column = path[i]
        grid[row][column] = ciphertext[i]

    plaintext = ""

    for row in range(rows):
        for column in range(columns):
            plaintext += grid[row][column]

    return plaintext


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
keyword = input("Enter a keyword: ")
message = input("Enter a message: ")

encrypted = encrypt(message, keyword, rows, columns)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, keyword, rows, columns)
print("Decrypted message:", decrypted)
