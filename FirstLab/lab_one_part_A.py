from Crypto.Cipher import AES 
from Crypto.Random  import get_random_bytes 
#Generate a random key using python inbuilt function (get_random_bytes)
random_key = get_random_bytes(3)
#Generate a key by joining both random key and first 12 bytes are zero
key = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) + random_key
#Create a new plain text
plain_text = "HelloWorld123456" 
#encode the plain text
#Since Python 3.0 string are store as unicode.
#By default, encode() method doesn't require any parameters.It returns utf-8 encoded version of the string. 
#But for security purpose i added utf-8 manually.
cipher_data = plain_text.encode('utf-8')
# === Encrypt ===
cipher_text = AES.new(key, AES.MODE_ECB)
ciphered_data = cipher_text.encrypt(cipher_data)
# === Decrypt ===
# Create the cipher object and decrypt the data
deciphered_text = cipher_text.decrypt(ciphered_data)
decrypted_data = deciphered_text.decode('utf-8')
# === Proving the data matches ===
print("Decrypted Data : "+ decrypted_data)
print(ciphered_data)
print(key)
