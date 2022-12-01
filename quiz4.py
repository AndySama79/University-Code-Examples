# PLEASE READ THE INSTRUCTIONS PROPERLY.
# IF YOU REMOVE ANY COMMENTS YOUR answers 
# will be INVALIDATED.
# ATTEMPT as many problems as you can !!
#

'''
PROBLEM 1
*********
Return the value of the execution of the following
script using the testrun assignment 2, part 2.
(just type the return value number you think in
the return part of the python program)
note: ">" is the shell command prompt below.

>./testrun.sh  add --test 9
Testno 9 added
Testno 9 file is : ./tests/test_9.sh
>./testrun.sh disable --test 9
testno: 9 disabled successfully
>x=`./testrun.sh disable --test 9`
testno: 9  already disabled
>echo $?

what will it print ? return that value you think
it should be .. in the python function. it should be only
one line.

'''

def find_trun_value():
    pass
# implement your return code.

'''
PROBLEM 2
**********

In the assignment 2 part2, I do the following:

    1. Add 100 tests successfully from 1 till 100.
    2. I disabled all test no.s that are divisible by 3
    3. I do a test list and check the following.

> count=`./testrun.sh list | tail -70  | grep -E "9" | wc -l`
> echo $count

what will be the count value printed above ? please
return that value as a number below.

'''

def find_count_value():
    pass

# implement your return code.


'''

PROBLEM 3
*********
You are given an integer. You need to find how many native data types
required to represent it in memory. You know the data type
sizes of long, integer, short, char. If the integer passed is less
than representation size of any  native data type ie., does not require
that many bytes, return 0 for that.

return four values  from this function. you can return four values from python 
function simply saying return a,b,c,d

find_native(0) - returns 0,0,0,1
find_native(240) - returns 0,0,0,1
find_native(55432) - returns 0,0,1,2
find_native(16777215) - returns 0,1,2,4

returns l,i,s,c

where l - no. of native longs required to represent it
i - no. of native integers required to represent it
s - no. of native shorts required to represent it
c - no. of native char required to represent it
'''

def find_native(a):
    size = len(bin(a)) - 2
    req = 8
    while size > req:
        req = req * 2
    c = int(req / 8)
    s = int(c / 2)
    i = int(s / 2)
    l = int(i / 2)
    # see return values above.
    return l,i,s,c

'''
PROBLEM 4
*********
You are given the offset in a file of contiguous bytes. File is 
organized as pages each page is 4096 bytes. Given the offset 
(it can start from zero) find the page index of that offset and
the offset within that page..(goes from 0 till 4095)
page index starts from 0 till whatever.

you can return two values from python function simply saying
return a,b

this function returns two values. first one page index,
second one offset within that page.

eg., 
find_index_off(4095) -> returns 0,4095
find_index_off(4096) -> returns 1,0
find_index_off(609) -> returns 0,609
find_index_off(6097) -> returns 1,2001
find_index_off(9000) -> returns 2,808
find_index_off(12288) -> returns 3,0

'''
def find_page_indexoff(offset):
    index = int(offset / 4096)
    off = int(offset % 4096)
    return index, off

'''
PROBLEM 5
*********

return the passed integers' all the bytes from most significant to
least significant byte . Assume maximum can be 6. If there are no 
leading bits, set that byte as zero to return six arguments .

Arguments: a is an integer, and max is the max value of the integer
that is passed.. in 0xffff.. (some f's  ).

find_bytes(0xffff, 0xffffffff) returns 0,0,0,0,0xff,0xff
find_bytes(0xffffffffffff, 0xffffffffffffffff) returns 0xff,0xff,0xff,0xff,0xff,0xff

'''

def find_bytes(a, max):
    # b1 is most significant byte
    if a > max:
        return -1
    binStr = bin(a)[2:]
    size = len(bin(a)) - 2
    for i in range(size, 48):
        binStr = '0' + binStr
    byte_list = []
    for i in range(6):
        byte_list.append(int(binStr[i*8:(i + 1) * 8], 2))
    b1 = byte_list[0]
    b2 = byte_list[1]
    b3 = byte_list[2]
    b4 = byte_list[3]
    b5 = byte_list[4]
    b6 = byte_list[5]
    return b1, b2, b3, b4, b5, b6

'''
PROBLEM 5
*********
Clear all the bits except the three most significant set bits.
Note that the three most significant bits need not be contiguous.
Max is the maximum value of the integer and will be of the form
0xfffff.. (some no. of f's no limit on the no. of f's).

eg.,

clearbits(4,0xf) --> returns 4
clearbits(7,0xf) --> returns 7
clearbits(15,0xf) --> returns 14 
clearbits(13,0xf) --> returns 13
clearbits(255,0xf) --> returns 224

return the integer with cleared bits.

'''

def clearbits(a,max):
    # return cleared value
    # if a > max:
    #     return -1
    binStr = bin(a)[2:]
    count = 0
    size = len(binStr)
    newStr = ''
    for i in range(size):
        if count >= 3:
            newStr = newStr + '0'
            continue
        if binStr[i] == '1':
            count = count + 1
        newStr = newStr + binStr[i]
    cleared = int(newStr, 2)
    return cleared

'''
PROBLEM 6
*********
Return the sum of all the bits in the passed
integer a.

a is an integer and can have a max value passed
in the second argument max. You can assume max value
will be of the form 0xfffffff.. (some no. of f's., no
limit on the no. of f's)
if a is greater than max value, return -1.

eg., 

sumbits(4,0xf) --> returns 1
sumbits(15,0xf) --> returns 4
sumbits(20,0xf) --> returns -1

return the sum of bits.

'''

def sumbits(a, max):
    if a > max:
        return -1
    sum = 0
    while a > 0:
        sum += a % 2
        a = int(a / 2)
    return sum

'''
PROBLEM 7
*********

sum all the positive numbers in the list, and 
sum all the negative numbers in the list separately
and return two sums.
return pos, neg

passed arguments:

    mylist - mylist 
    mysize.

    you can access the individual elements of the list
    much like 'c' program using mylist[i], where i is
    the integer index ranging from 0 .. mysize-1.
'''


def find_sum(mylist, mysize):
    pos, neg = 0, 0
    for num in mylist:
        if num > 0:
            pos += num
        else:
            neg += num
    return pos, neg

'''
PROBLEM 8
*********

# do the given op on the 
# arguments a, b, c.
# a, b, c are integers with max value of 0xffffffffff.
(Note that the above has 10 f's..)
# op  is a string.
# will be one of the following:
# 
 for all the below example a,b,c no. of bits set in a, b and c
 are 8, 4, 2 respectively.
 
 Return value should not be float.

# "sum" - sum all the bits of all integers
            for the example it will return 14
# "mul" - multiply the three sums of bits in a, b, c.
#             for the example it will return 64
# "div" - integer divide the sum of bits in a with b, then the resulting value with c. 
                ie., sum of bits in a divided by sum of bits in b, and then by c.
                for the example it will return 1.
                should not return float value.
# "sub" - subtract sums of bits of b from sum of bits of a, then subtract sum of bits of c, and return
             the value.
             for the example it will return 2.
# "pow" - Returns the value of power of 2, of sum of all the bits in all of a,b,c. For the example
         it returns 2^14.

Hint: You can compare strings in python using simply if s1==s2. All strings should be in single quotes or
double quotes for python.
Hint: Use the sumbits function you implemented above.

'''

def do_bit_ops(a,b,c, op):

# return the value calculated.
    if op == 'sum':
        value = sumbits(a, 0xffffffffffffffff) + sumbits(b, 0xffffffffffffffff) + sumbits(c, 0xffffffffffffffff)
    elif op == 'mul':
        value = sumbits(a, 0xffffffffffffffff) * sumbits(b, 0xffffffffffffffff) * sumbits(c, 0xffffffffffffffff)
    elif op == 'div':
        value = int((sumbits(a, 0xffffffffffffffff) / sumbits(b, 0xffffffffffffffff)) / sumbits(c, 0xffffffffffffffff))
    elif op == 'sub':
        value = (sumbits(a, 0xffffffffffffffff) - sumbits(b, 0xffffffffffffffff)) - sumbits(c, 0xffffffffffffffff)
    elif op == 'pow':
        value = 2 ** do_bit_ops(a, b, c, 'sum')
    return value 


'''
PROBLEM 9
*********
There is one argument n, that says a math polynomial equation of order n.

You should print the output of the polynomial equation in string, assuming
a0, a1, a2... an as  the coeffcients, and the multiplication with the corresponding
x variable to the right power. Eg.
for n=2 you will print: a0+a1*x+a2*x^2

Hints: 
1. you can print a string with end of the line using print(f'plaksha', end='')
2. You can also concatenate two f strings using  s=f'plaksha' followed by s += 'university'
    that way s becomes 'plaksha university'

You return a "String of the polynomial equation with no spaces in between.
'''

def print_polynomial(n):
    polystring = ''
    for i in range(n+1):
        if i == 0:
            polystring += f'a{i}'
        elif i == 1:
            polystring += f'+a{i}*x'
        else:
            polystring += f'+a{i}*x^{i}'
    # return polynomial string
    return polystring

'''
PROBLEM 10
**********

Write a python program that takes any number of  arguments say a,b,c. (it could be any number)

each argument can be an integer or an op string.
op string can be "+", or "-" or "/" or "*"

Note: all three will be passed as strings to main function and you need to interpret appropriately.

a is a string of the form "+", or "-", "/", or "*".

You can compare strings in python using simply if s1==s2. All strings should be in single quotes or
double quotes for python.

You need to perform that operation in the order (dont worry about operator priority) sent.

eg., if the arguments are : 2 + 3 * 5 - 3 * 4 + -6 / 11
"2" "+" "3" "*" "5" "-" "3" "*" "4" "+" "-6" "/" "11"

the program will print  7. 

The above should be submitted separately.

The program should be submitted as p10.py


'''
