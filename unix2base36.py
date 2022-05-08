import sys
import datetime
import time

def get_digit(d):
    ''' Convert a base 36 digit to the desired character '''
    if 0 <= d <= 9:
        # 0 - 9
        c = 48 + d
    elif 10 <= d <= 35:
        # A - Z
        c = (65-10) + d
    else:
        # We should never get here
        raise ValueError('Invalid digit for base 36: ' + str(d)) 
    return chr(c)

def encode(n):
    ''' Convert integer n to base 36 '''
    out = []
    while n:
        n, r = n // 36, n % 36
        out.append(get_digit(r))
    while len(out) < 6:
        out.append('0')
    return ''.join(out)[::-1]

def unix2base36():
    unix_now = time.time()
    #date_time = datetime.datetime(2000, 1, 1, 0, 0)
    #unix_start = time.mktime(date_time.timetuple())
    #ms = int( unix_now - unix_start )
    ms = int( unix_now )
    return encode(ms)

def timename():
    return unix2base36()
