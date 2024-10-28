







with open('./input.prod') as f:
    contents = f.read().split('\n')[0]







def p1decompress(s):


    # if there are no decompress markers
    if '(' not in s:
        return len(s) #return the length of the string


    # init a value for tracking the current length
    val = 0


    #while there is still a decomp marker:
    while '(' in s:

        val += s.find('(') # add the letters before the first marker

        s = s[s.find('('):] #remove everything in the string upto the first marker

        nchars, reps = map(int, s[1:s.find(')')].split('x')) # get the nchars and reps for the first marker

        s = s[s.find(')')+1:] # remove the marker

        val += nchars*reps #add the value after expanding the decomp marker

        s = s[nchars:]

    val += len(s)

    return val


## thanks reddit
def p2decompress(s):


    # if there are no decompress markers
    if '(' not in s:
        return len(s) #return the length of the string


    # init a value for tracking the current length
    val = 0


    #while there is still a decomp marker:
    while '(' in s:

        val += s.find('(') # add the letters before the first marker

        s = s[s.find('('):] #remove everything in the string upto the first marker

        nchars, reps = map(int, s[1:s.find(')')].split('x')) # get the nchars and reps for the first marker

        s = s[s.find(')')+1:] # remove the marker

        val += p2decompress(s[:nchars]*reps) #add the value after expanding the decomp marker

        s = s[nchars:]

        # print(val, end='\r')

    val += len(s)

    return val





# print(p1decompress(contents))








def tests_p1():

    assert len('ADVENT') == p1decompress('ADVENT')
    assert len('ABBBBBC') == p1decompress('A(1x5)BC')
    assert len('XYZXYZXYZ') == p1decompress('(3x3)XYZ')
    assert len('ABCBCDEFEFG') == p1decompress('A(2x2)BCD(2x2)EFG')
    assert len('(1x3)A') == p1decompress('(6x1)(1x3)A')
    assert len('X(3x3)ABC(3x3)ABCY') == p1decompress('X(8x2)(3x3)ABCY')


def tests_p2():

    assert len('XYZXYZXYZ') ==p2decompress('(3x3)XYZ')
    assert p2decompress('X(8x2)(3x3)ABCY') ==len('XABCABCABCABCABCABCY')
    assert 241920 ==p2decompress('(27x12)(20x12)(13x14)(7x10)(1x12)A')
    assert 445 == p2decompress('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')



# tests_p2()


print(p2decompress(contents))


















