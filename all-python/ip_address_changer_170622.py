"""Convert ip address to a 32 bit integer and vice versa

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
End date   : 2017/06/22
"""


def _to_binary(n, length=None):
    # input validation
    # 1. n validation integer_to_ip
    # 2. length validation integer over 0

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
        value = '1' + value if residual == 1 else '0' + value
    value = '1' + value
    digits = len(value)

    if isinstance(length, int) and digits < length:
        value = ('0' * (length - digits)) + value
    if negative:
        value[0] = '-'

    return value


def ip_to_integer(ip):
    value = ''
    ip = ip.split('.')
    for byte in ip:
        value += _to_binary(byte, 8)

    value = int(value, 2)

    return value


def integer_to_ip(integer):
    ip_bytes = []
    for _ in range(4):
        integer, residual = divmod(integer, 256)
        ip_bytes.insert(0, str(residual))
    value = '.'.join(ip_bytes)

    return value
