#write a program to generate the a random color Hex,

#import random

#print(random.randint(0,0xFFFFFF))

import random

rand = random.randint(0,0x00FF00)
hex_num = str(hex(rand))
hex_num = '#'+hex_num[2:]
print(hex_num)