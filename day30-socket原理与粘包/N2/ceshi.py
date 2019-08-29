
import codecs


def single_byte(data):
    if data < 0:
        value = 2 ** 8 + int(data)
    else:
        value = int(data)
    Val_hex = str(hex(value))[2:]
    while len(Val_hex) < 2:
        Val_hex = '0' + Val_hex
    return Val_hex


def count_frame(data):
    value = int(data, 16)
    value += 1
    value = single_byte(value)
    return value




if __name__ == '__main__':
    print(count_frame('ff'))