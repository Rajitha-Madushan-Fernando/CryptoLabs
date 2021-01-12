from Crypto.Cipher import AES
from datetime import datetime
plain_text = "HelloWorld123456" 
cipher_text = b'\x01\x1aW]\xa6\x02\x8f\xed\xd0`\x84\x0cn\x9aW\x1f'

encoded_plain_text = plain_text.encode('utf-8')
start_date = datetime.now()
key = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def generate_key(position):
    for number in range(0,255):
        key[-1] = number
        cipher = AES.new(bytes(key), AES.MODE_ECB)
        ciphered_data = cipher.encrypt(encoded_plain_text)
        #print(ciphered_data)
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
    