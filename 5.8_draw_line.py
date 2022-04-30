

def draw_line(screen: list, width, x1, x2, y):
    if x2 - x1 > width  or x2 - x1 < 0:
        raise Exception("Nope")
    
    widthInBytes = int(width / 8)
    yBegins = y * widthInBytes

    lineLength = (x2 - x1) + 1
    base = (1 << lineLength) - 1 
    row = base << width - (x2 +1 )
    bytes = row.to_bytes(widthInBytes, byteorder='big')
    
    for idx, byte in enumerate(bytes):
        screen[yBegins + idx] = byte

    print(screen)


def main():
    # draw_line(bytearray(4), 16, 0, 3, 1)
    # draw_line(bytearray(32), 64, 0, 63, 3)
    draw_line(bytearray(32), 16, 0, 15, 1)


if __name__ == '__main__':
    main()