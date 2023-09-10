def reversed(num):
    if not isinstance(num, int):
        return None

    reversed = ''
    negative = False

    if num < 0:
        num *= -1
        negative = True
    
    num_string = str(num)

    for i in range(len(num_string)):
        reversed = num_string[i] + reversed

    if negative:
        reversed = "-" + reversed

    return int(reversed)

def formatter(num):
    if not isinstance(num, int):
        return None

    res = (bin(num), oct(num))
    return (bin(num), oct(num))


    
    
