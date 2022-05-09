import time

def get_digit(d):
    ''' Convert a base 62 digit to the desired character '''
    if 0 <= d <= 9:
        # 0 - 9
        c = 48 + d
    elif 10 <= d <= 35:
        # A - Z
        c = (65-10) + d
    elif 36 <= d <= 61:
        # a - z
        c = (97-36) + d
    else:
        # We should never get here
        raise ValueError('Invalid digit for base 62: ' + str(d)) 
    return chr(c)

# Test `digit`
#print(''.join([get_digit(d) for d in range(62)]))

def encode(n):
    ''' Convert integer n to base 62 '''
    out = []
    while n:
        n, r = n // 62, n % 62
        out.append(get_digit(r))
    while len(out) < 6:
        out.append('0')
    return ''.join(out)[::-1]

def unix2base62():
    unix_now = time.time()
    #date_time = datetime.datetime(2000, 1, 1, 0, 0)
    #unix_start = time.mktime(date_time.timetuple())
    #ms = int( unix_now - unix_start )
    ms = int( unix_now )
    return encode(ms)

def timename():
    return unix2base62()
