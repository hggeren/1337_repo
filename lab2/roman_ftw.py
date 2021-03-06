#Define digit mapping
roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def to_roman(n):
    """convert integer to Roman numeral"""
    if not isinstance(n, int):
        raise NotIntegerError("decimals can not be converted.")
    if not (0 < n < 5000):
        raise OutOfRangeError("number out of range (must be 1... 5000")
    
    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    print result
    return result

#def from_roman(s):
#    """convert roman numeral to integer"""
#    if not isinstance(s, str):
#        raise Not_string_error("string can not be converted.")
#    
#    result = ""
#    for numeral, integer in roman_numeral_map:
#        while s is not "":
#            result += str(integer)
#            print numeral
#            s = ""
#            s = s.replace(numeral, "", 1)
#    print result
#    return result

def from_roman(s):
    """convert roman numeral to integer """
    result = 0
    while s is not "":
        if "CM" in s:
            result += 900
            s = s.replace ("CM", "", 1)
        elif "CD" in s:
            result += 400
            s = s.replace ("CD", "", 1)
        elif "XC" in s:
            result += 90
            s = s.replace ("XC", "", 1)
        elif "XL" in s:
            result += 40 
            s = s.replace ("XL", "", 1)
        elif "IX" in s:
            result += 9 
            s = s.replace ("IX", "", 1)
        elif "IV" in s:
            result += 4
            s = s.replace ("IV", "", 1)
        elif "M" in s:
            result += 1000
            s = s.replace("M", "", 1)
        elif "D" in s:
            result += 500
            s = s.replace ("D", "", 1)
        elif "C" in s:
            result += 100 
            s = s.replace ("C", "", 1)
        elif "L" in s:
            result += 50
            s = s.replace ("L", "", 1)
        elif "X" in s:
            result += 10
            s = s.replace ("X", "", 1)
        elif "V" in s:
            result += 5
            s = s.replace ("V", "", 1)
        elif "I" in s:
            result += 1
            s = s.replace ("I", "", 1)

    print result
    return result

to_roman(1219)
from_roman("")
