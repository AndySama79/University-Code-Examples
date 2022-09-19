from ctypes import *

size = 64
bit_vector = (c_ubyte * (size // 8))()
bit_nbytes = size // 8
bit_total_bits = size
bit_free = size
bit_alloc = 0

# print(bit_vector[1])
# print(bit_nbytes)
# print(bit_total_bits)
# print(bit_free)
# print(bit_alloc)

# bit_vector[1] = bit_vector[1] | (1 << (8-3))
# bit_vector[1] = bit_vector[1] | (1 << (3))
# print(bit_vector[1])

# bv = int("1101011000010110", 2)
# m = 1 << 3
# res =  bv | m
# print(f"{bv: 016b}")
# print(f"{m: 016b}")
# print(f"{res: 016b}")
# print(bin(res)[2:])
def set_bit(bit_vector, bit):
    if bit >= size:
        return "Overflow"
    byte_pos = (bit) // 8
    bit_pos = 8 * (byte_pos + 1) - (bit) - 1
    mask = 1 << bit_pos
    bit_vector[byte_pos] = bit_vector[byte_pos] | mask
    return bit_vector

def is_free(bit_vector, bit):
    if bit >= size:
        return "Overflow"
    byte_pos = (bit) // 8
    bit_pos = 8 * (byte_pos + 1) - (bit) - 1
    mask = 1 << bit_pos
    if bit_vector[byte_pos] & mask == 0:
        return 1
    return 0

def is_set(bit_vector, bit):
    if bit >= size:
        return "Overflow"
    byte_pos = (bit) // 8
    bit_pos = bit % 8
    mask = 1 << bit_pos
    if bit_vector[byte_pos] & mask != 0:
        return 1
    return 0

def clear_bit(bit_vector, bit):
    if bit >= size:
        return "Overflow"
    byte_pos = bit // 8
    bit_pos = 8 * (byte_pos + 1) - bit - 1
    mask = ~(1 << bit_pos)
    bit_vector[byte_pos] = bit_vector[byte_pos] & mask
    return bit_vector

def __str__(bit_vector):
    s = f'total_bytes: {bit_nbytes} total_bits: {bit_total_bits}'
    s = s + '\n'
    for i in range(0, bit_nbytes):
        if i % 4 == 0:
            s = s + '\n'
        
        for j in range(8 * i, 8 * (i + 1)):
            s = s + str(is_set(bit_vector, j))
        
        s = s + " "
    
    return s

# a, b = 3, 63

# print(__str__(bit_vector))

# bit_vector = set_bit(bit_vector, a)
# print(__str__(bit_vector))

# bit_vector = set_bit(bit_vector, b)
# print(__str__(bit_vector))

# print(is_set(bit_vector, a))
# print(is_free(bit_vector, a))

# print(is_set(bit_vector, b))
# print(is_free(bit_vector, b))

# print(__str__(bit_vector))
# bit_vector = clear_bit(bit_vector, b)
# bit_vector = clear_bit(bit_vector, a)

# print(__str__(bit_vector))

# bit_vector = clear_bit(bit_vector, a)

# print(__str__(bit_vector))