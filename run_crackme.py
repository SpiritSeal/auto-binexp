from pwn import *

# Path to the binary
binary_path = './artifacts/crackme0x03'

# Start the process
p = process(binary_path)

# Send the password
password = '337059'
p.sendline(password)

# Receive the output
output = p.recvall().decode()

# Print the output
print(output)
