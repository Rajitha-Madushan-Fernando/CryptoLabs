from Crypto.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
BLOCK_SIZE = 32 
#Generate a random key using python inbuilt function (get_random_bytes)
random_key = get_random_bytes(4)
#Generate a key by joining both random key and first 12 bytes are zero
key = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) + random_key
#Create a new plain text
plain_text = "HelloWorld789" 
#encode the plain text
#Since Python 3.0 string are store as unicode.
#By default, encode() method doesn't require any parameters.It returns utf-8 encoded version of the string. 
#But for security purpose i added utf-8 manually.
cipher_data = plain_text.encode('utf-8')
# === Encrypt ===
cipher = AES.new(key, AES.MODE_ECB)
ciphered_data = cipher.encrypt(pad(cipher_data,BLOCK_SIZE))
# === Decrypt ===
# Create the cipher object and decrypt the data
deciphered_bytes = cipher.decrypt(ciphered_data)
decrypted_data = deciphered_bytes.decode('utf-8')

# === Proving the data matches ===
print("Decrypted Data : "+ decrypted_data)
print(ciphered_data)
print(key)
