# Define digit mapping
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
    """Converts an integer to a Roman numeral and returns the numeral."""
    if not isinstance(n, int):
        raise NotIntegerError("decimals can not be converted.")
    if not (0 < n < 5000):
        raise OutOfRangeError("number out of range (must be 1... 5000")

    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
#    print result
    return result


def from_roman(s):
    """Convert a roman numeral to an integer and return the integer."""
    s = s.upper()
    result = 0
    s = remove_subtractives_roman(s)

    while s is not "":
        if "M" in s:
            result += 1000
            s = s.replace("M", "", 1)
        elif "D" in s:
            result += 500
            s = s.replace("D", "", 1)
        elif "C" in s:
            result += 100
            s = s.replace("C", "", 1)
        elif "L" in s:
            result += 50
            s = s.replace("L", "", 1)
        elif "X" in s:
            result += 10
            s = s.replace("X", "", 1)
        elif "V" in s:
            result += 5
            s = s.replace("V", "", 1)
        elif "I" in s:
            result += 1
            s = s.replace("I", "", 1)

#    print result
    return result


def subtract_roman(a, b):
    """Function to subtract a roman numeral from another
    roman numeral without converting to decimal.
    Returns the result of the subtraction.
    """
    a = a.upper()
    b = b.upper()
    a = remove_subtractives_roman(a)
    b = remove_subtractives_roman(b)
    while b is not "":
        for c in b:
            if c in a:
                a = a.replace(c, "", 1)
                b = b.replace(c, "", 1)
        if b is not "":
            if "M" in a:
                a = a.replace("M", "DD", 1)
            if "D" in a:
                a = a.replace("D", "CCCCC", 1)
            if "C" in a:
                a = a.replace("C", "LL", 1)
            if "L" in a:
                a = a.replace("L", "XXXXX", 1)
            if "X" in a:
                a = a.replace("X", "VV", 1)
            if "V" in a:
                a = a.replace("V", "IIIII", 1)
    a = shorten_roman(a)
#    print a
    return a


def remove_subtractives_roman(s):
    """Removes subtractives from the roman numeral and returns the numeral."""
    while "CM" in s:
        s = s.replace("CM", "DCCCC ", 1)
    while "CD" in s:
        s = s.replace("CD", "CCCC ", 1)
    while "XC" in s:
        s = s.replace("XC", "LXXXX ", 1)
    while "XL" in s:
        s = s.replace("XL", "XXXX ", 1)
    while "IX" in s:
        s = s.replace("IX", "VIIII ", 1)
    while "IV" in s:
        s = s.replace("IV", "IIII ", 1)
#    print s
    while " " in s:
        s = s.replace(" ", "", 1)
#    print s
    return s


def sort_roman(p):
    """Sorts the roman numerals from larges to smallest.
    Cannot sort subtractives.  Returns the sorted roman numeral.
    """
    my_alphabet = "MDCLXVI"
    p = "".join(sorted(
        p, key=lambda elem: [my_alphabet.index(c) for c in elem[0]]))
    return p


def shorten_roman(p):
    """Shortens the roman number by replacing smaller numbers
    with larger ones.  Returns the shortened roman numeral.
    """
    p = sort_roman(p)
    while 5 * "I" in p:
        p = p.replace("IIIII", "V", 1)
    while 2 * "V" in p:
        p = p.replace("VV", "X", 1)
    while 5 * "X" in p:
        p = p.replace("XXXXX", "L", 1)
    while 2 * "L" in p:
        p = p.replace("LL", "C", 1)
    while 5 * "C" in p:
        p = p.replace("CCCCC", "D", 1)
    while 2 * "D" in p:
        p = p.replace("DD", "M", 1)
#    print p
    return p

# Testing whether all functions work:
t1 = to_roman(1115)
print t1
t2 = to_roman(200)
print t2
t3 = subtract_roman(t1, t2)
print t3
t4 = from_roman(t3)
print t4
t5 = from_roman("x")
print t5
t6 = subtract_roman("xx", "v")
print t6