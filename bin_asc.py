import binascii

def bin_ascii(str):
    i = int(str, base=2)
    return i.to_bytes((i.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'

def bin_ascii1(str):
    return ''.join(chr(int(str[i: i+8], 2)) for i in range(0, len(str), 8))

print(bin_ascii1('00110001001100000011000100110001'))
