from zlib import crc32

data = open("../images/original_scissor.png", 'rb').read() # Put your image need to brute force

index = 12

ihdr = bytearray(data[index:index+17])
width_index = 7
height_index = 11

for x in range(1,2000):
    height = bytearray(x.to_bytes(2,'big'))
    for y in range(1,2000):
        width = bytearray(y.to_bytes(2,'big'))
        for i in range(len(height)):
            ihdr[height_index - i] = height[-i -1]
        for i in range(len(width)):
            ihdr[width_index - i] = width[-i -1]
        if hex(crc32(ihdr)) == '0xcc1373c6': # Put your CRC chunk to this condition (pngcheck -v <imagefile>)
            print("width: {} height: {}".format(width.hex(),height.hex()))
    for i in range(len(width)):
            ihdr[width_index - i] = bytearray(b'\x00')[0]