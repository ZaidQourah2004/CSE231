
def leap_year(x):
    x = int(x)
    if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0 ):
        return True
    else:
        return False

def rotate(s_str, n_int):
    str_length = len(s_str)
    if str_length == 1:
        return s_str
    else:
        return s_str[n_int + 2:] + s_str[:n_int +2]

def digit_count(n):
    n = int(n)
    even = 0 
    odd = 0
    zero = 0
    while True: 
        rem = n % 10
        if rem == 0:
            zero += 1
        elif rem % 2 == 0:
            even += 1 
        else:
            odd += 1
        n = int(n / 10)
        if n == 0:
            break

    return(even, odd, zero)

def float_check(s):
    letter = "abcdefghijklmnopqrstuvwxyz"
    decimal_counter = 0
    for s_float, ch in enumerate(s):
        if ch in letter:
            return False
        if ch == ".":
            decimal_counter += 1
            if decimal_counter > 1: 
                return False 

    s = s.replace(".","")
    if s.isdigit() == True:
        return True
    
