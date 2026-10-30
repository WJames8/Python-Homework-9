
def encrypt(message, keyword):
    message = message.upper().replace(" ", "")
    keyword = keyword.upper()

    columns = len(keyword)
    rows = (len(message) + columns - 1) // columns

    while len(message) < rows * columns:
        message += "X"

    grid = []
    for row in range(rows):
        grid.append(list(message[row * columns:(row + 1) * columns]))

    order = sorted(range(columns), key=lambda i: keyword[i])

    ciphertext = ""

    for column in order:
        for row in range(rows):
            ciphertext += grid[row][column]

    return ciphertext


def decrypt(ciphertext, keyword):
    keyword = keyword.upper()

    columns = len(keyword)
    rows = len(ciphertext) // columns

    grid = [[''] * columns for _ in range(rows)]

    order = sorted(range(columns), key=lambda i: keyword[i])

    index = 0
    for column in order:
        for row in range(rows):
            grid[row][column] = ciphertext[index]
            index += 1

    plaintext = ""

    for row in range(rows):
        for column in range(columns):
            plaintext += grid[row][column]

    return plaintext

message = input("Enter a message: ")
keyword = input("Enter a keyword: ")

encrypted = encrypt(message, keyword)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, keyword)
print("Decrypted message:", decrypted)
