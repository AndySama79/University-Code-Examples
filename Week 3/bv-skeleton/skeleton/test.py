from mybit_vector import *
from os import sys


def bit_vector_tests():
    bv=mybit_vector(64)

# verify that all bits are zero

    print(bv)

    bv.set_bit(3)
    print(bv)

    bv.set_bit(63)
    print(bv)

    try:
        bv.set_bit(64)
        print(bv)

    except mybit_overflow:
        print("overflow test passed")

    if bv.is_set(63):
        print("63 set bit passed")
    else:
        print("63 set bit FAILED")
        sys.exit(1)

    if bv.is_free(63) == 0:
        print("63 ! clear bit passed")
    else:
        print("63 ! clear bit FAILED")
        sys.exit(1)

    if bv.is_set(3):
        print("3 set bit passed")
    else:
        print("3 set bit FAILED")
        sys.exit(1)
    if bv.is_free(3) == 0:
        print("3 ! clear bit passed")
    else:
        print("3 ! clear bit FAILED")
        sys.exit(1)

    print(bv)
    bv.clear_bit(63)
    bv.clear_bit(3)
    print(bv)
    print("PLEASE VERIFY THAT all bits are zero in the above VECTOR ")

def main():
    # bit vector tests
    # print running bit vector tests
    bit_vector_tests()

#    size=1024*1024*1024
#    mymemobj = getmemobj(size)

#    myint32_tests()
#    myint64_tests()
#    mystr_tests()
#    myint32_aray_tests()
#    myint64_aray_tests()

# verify memory allocated  is all zero


if __name__ == "__main__":
    main()

