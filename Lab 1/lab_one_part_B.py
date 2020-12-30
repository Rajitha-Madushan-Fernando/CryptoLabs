from Crypto.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from datetime import datetime
BLOCK_SIZE = 32 
plain_text = "HelloWorld789" 
cipher_text = b'\x90(\x00\xda\xde\xee\x83\xb8\xfac\x99\x9d\x10\n\xc08\xf9\x95\xad)\x01\xdb\xbe\xc6\xfbM\xbfy\xd7\xca~J'

data = plain_text.encode('utf-8')
start_date = datetime.now()
key = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def generate_key(position):
    for number in range(0,255):
        cipher = AES.new(bytes(key), AES.MODE_ECB)
        ciphered_data = cipher.encrypt(pad(data,BLOCK_SIZE))
        if cipher_text == ciphered_data:
            print([chr(c) for c in key])
            end_date = datetime.now()
            actual_time = end_date - start_date
            print(actual_time)

            exit()

        if position != 15:
            generate_key(position+1)
            key[position+1] = 0
            
            key[position] += 1

           
generate_key(12)
    