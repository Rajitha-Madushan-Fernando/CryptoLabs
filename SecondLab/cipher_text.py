cipher_text_one = bytes(
    [int(x, base= 16) for x in "46 32 5a 0c 90 d2 3e f1 4d 33 a6 cc 55 22 61 ca df 92 0b 02 a5 17 35 83 85 aa 93 fc ec 72 39 a0 42 b1 c7 c8 4f 4b f5 09 b8 38 07 41 f1 e6 68 b5 ac c8 e3 48 27 a5 0c 8e c6 35 ff f2 66 33 c5 91 c7 8f 27 5f 57 3d 65 a0 1c ef af b4".split(" ")]
)
print(cipher_text_one)

cipher_text_two = bytes(
    [int(x, base= 16) for x in "54 35 41 5f d3 c5 3f e4 4b 31 a1 de 5c 7b 76 c6 cd de 17 44 f2 0d 34 88 cd fe 98 f0 bc 79 33 bf 5c f2 89 98 4d 56 fd 19 b5 30 07 08 f0 e7 68 ad a2 d8 af 56 31 f0 1c 8a 88 7c f3 b7 35 31 d2 86 df c2 6f 59 52 3d 6b b0 02 b2 a1 b4".split(" ")]
)
print(cipher_text_two)

#wb is write binary
with open("file.bin", "wb") as file:
    file.write(cipher_text_one+cipher_text_two)
 