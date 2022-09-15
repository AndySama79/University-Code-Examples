from ctypes import *

#exceptions for bitvector.

class mybit_error(Exception):
    pass
class mybit_size_bad(mybit_error):
    def __init__(self, size, message="size not aligned or large"):
        self.size=size
        self.message=message
    def __str__(self):
        return f'{self.size} -> {self.message}'

class mybit_overflow(mybit_error):
    def __init__(self, size, bitv, message="bitindex larger than bitvector size"):
        self.size=size
        self.bitvectorsize=bitv.bit_total_bits
        self.message=message
    def __str__(self):
        return f'bitindex: {self.size} bitvector size: {self.bitvectorsize} -> {self.message}'

# bit vector implementation
# size in bytes
# bit vector allocates bits for every byte
# and sets state of 1 and 0 via
#  the methods set_bit, clear_bit, and is_free
# is_free returns 1 if bit is not set.
# is_set returns 1 if bit is set.

class mybit_vector:

# bit_vector -- byte array for states
# bit_nbytes - total bytes in the bit_vector
# bit_total_bits - size of the memory passed in the __init__
# bit_free - total bits that are free   
# bit_alloc - total bits that are alloced

    def __init__(self, size):
        if size % 8 != 0:
            raise mybit_size_bad(size)
        self.bit_vector=(c_ubyte * (size//8))()
        self.bit_nbytes=size//8
        self.bit_total_bits=size
        self.bit_free=size
        self.bit_alloc=0

# Returns 1 if the bit is 0 ie. free
# Returns  0 if the bit is 1
    
    def is_free(self, bit):
        if bit >= self.bit_total_bits:
            raise mybit_overflow(bit,self)
        # YOUR CODE 
        raise NotImplementedError 
# Returns 1 if the bit is set
# Returns 0 if the bit is not set

    def is_set(self, bit):
        if bit >= self.bit_total_bits:
            raise mybit_overflow(bit,self)
        # YOUR CODE 
        raise NotImplementedError 

#sets the bit passed in "bit" (used by mem_alloc in the mymemory class)
# if the bit is > bit_total_bits it raises the mybit_overflow exception 
#defined above.

    def set_bit(self, bit):
        if bit >= self.bit_total_bits:
            raise mybit_overflow(bit,self)
        # YOUR CODE 
        raise NotImplementedError 

#clears the bit passed in "bit" (used by mem_free in the mymemory class)
# if the bit is > bit_total_bits it raises the mybit_overflow exception 
#defined above.

    def clear_bit(self, bit):
        if bit >= self.bit_total_bits:
            raise mybit_overflow(bit,self)
        # YOUR CODE 
        raise NotImplementedError 

# prints the bit state. Dont print if the size is large. it will loop
# for ever trying to form the string. Do unit test with this though.

# the output of this function for say bit_nbytes = 6, and total_bits=48
# the bits are numbered from 0 till 23. If bits 0 and 23 are set :
# should be (without #used for comment):
# total_bytes: 6 total_bits: 48
#
# 10000000 00000000 00000000 00000000
# 00000000 00000001
# all the coding is done here except for the loop that prints the individual
# bytes above eg. 10000000 , etc.
# note the value of the words may vary depending on which bit is set or not.
# if no bit is set, ie. all are zeros then the output from here will be :
# total_bytes: 6 total_bits: 48
#
# 00000000 00000000 00000000 00000000
# 00000000 00000000

# the no. of lines of the output varies based on total bytes. atmost it prints
# 4 bytes in a line.

    def __str__(self):
        s=f'total_bytes: {self.bit_nbytes} total_bits: {self.bit_total_bits}'
        s=s+'\n'
        for i in range(0,self.bit_nbytes):
            if i%4==0:
                s=s+'\n'
            # APPEND the string of bits to s
            # for eg. if bit 0 and 1 are set
            # the string that will be appended will be
            # "11000000". Note this is not the way
            # it will be represented in the memory.
            # but as a human you will want to read
            # the printed state from left to right
            # in increasing order.

            #YOUR CODE for the above logic

            s=s+"  "
        return s

