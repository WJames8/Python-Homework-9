
checkerboard = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

def locate_letter(board, letter):
    letter = letter.upper()

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == letter:
                return (row + 1, column + 1)

    return None


def encrypt(message, board):
    ciphertext = ""

    for letter in message.upper():
        if letter.isalpha():
            if letter == 'J':
                letter = 'I'

            position = locate_letter(board, letter)

            if position:
                ciphertext += str(position[0]) + str(position[1])

    return ciphertext


def decrypt(ciphertext, board):
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        row, column = (int(ciphertext[i]), int(ciphertext[i + 1]))

        plaintext += board[row - 1][column - 1]

    return plaintext


message = input("Enter a message to encrypt: ")

encrypted = encrypt(message, checkerboard)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, checkerboard)
print("Decrypted message:", decrypted)
