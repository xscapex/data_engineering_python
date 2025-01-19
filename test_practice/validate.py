# Given a string, determine if it is a valid IP address

def validate(ip):
    valid_digit = set('0123456789')
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True