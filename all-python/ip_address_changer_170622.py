"""Convert ip address to a 32 bit integer and vice versa

This function only supports ip 4.
6 is not supported.

Bit unit computation is squaring a circle to me.
Before pioneering the C way to do this,
I implement it in a Pythonic way first.

And after that, may be next time,
I'll make this function in a more efficient way

    This module has 2 methods.
        1. ip_to_integer
            ex) 255.255.255.1 -> 4294967041
        2. integer_to_ip
            ex) 4294967041 -> 255.255.255.1

    Let's go

Start date : 2017/06/22
End date   : 2017/06/23
"""


def _to_binary(n, length=None):
    """Change an integer to a binary number in a given length

    First element is an integer that you want to change to a binary format.
    It can be negative.
    And you can decide the length of a formatted string.

    For example, 5 is '101', but if length is 5, final format is '00101'.
    If length is shorter than formatted string, it is ignored

    This is a helper function for ip_to_integer function

    :input:
        n : An integer including negative numbers. Target to be changed
        length : final length of binary number. Blank spaces are filled with '0'.
                 And length is ignored if it is too small for the n
    :return:
        str. Binary format of n.
    """
    try:
        n = int(n)
    except:
        raise TypeError("First element should be a integer")
    if length is not None and (isinstance(length, int) and length < 0):
        raise TypeError("Length should be over 0")
    negative = True if n < 0 else False
    n = abs(n)

    value = ''

    while n > 1:
        n, residual = divmod(n, 2)
        value = '1' + value if residual else '0' + value
    value = '1' + value
    digits = len(value)

    if isinstance(length, int) and digits < length:
        value = ('0' * (length - digits)) + value
        if negative:
            value = '-' + value[1:]
    if negative and value[0] != '-':
        value = '-' + value

    return value


def ip_to_integer(ip):
    """Change ip address into a 4 byte integer

    Change ip address of version 4 to a interger.
    For example,
        '255.255.255.1' -> '4294967041'

    Final result is str, not integer

    :input:
        ip: ip address. It should pass validation re test
    :return:
        str. Integer format of ip address
    """
    value = ''
    ip = ip.split('.')
    if len(ip) != 4:
        raise ValueError("You should give me a 4 nibbles chained with '.'")
    elif not all(map(lambda x: x.isnumeric() and 0 <= int(x) <= 255, ip)):
        raise ValueError("Each nibble should be an integer between from 0 to 255")

    for byte in ip:
        value += _to_binary(byte, 8)

    value = int(value, 2)

    return value


def integer_to_ip(integer):
    """Change integer into an ip address

    It can be either str and integer.

    :input:
        integer : A target number to be a ip_address
                  It should be from 0 to 4294967295
    :return:
        str. ip address like '255.255.255.1'
    """
    try:
        integer = int(integer)
    except:
        raise ValueError("You should give me a value that can be a int")
    else:
        if not 0 <= integer <= 4294967295:
            raise ValueError("Integer should be int type and between 0 to 4294967295")

    ip_bytes = []
    for _ in range(4):
        integer, residual = divmod(integer, 256)
        ip_bytes.insert(0, str(residual))
    value = '.'.join(ip_bytes)

    return value
