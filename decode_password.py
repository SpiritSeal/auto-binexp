def reverse_shift(encoded_str):
    decoded_chars = []
    for char in encoded_str:
        decoded_chars.append(chr(ord(char) + 3))
    return ''.join(decoded_chars)

# Encoded password from the binary
encoded_password = '337059'
decoded_password = reverse_shift(encoded_password)
print(f'Decoded Password: {decoded_password}')
