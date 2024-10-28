







with open('./input.prod') as f:
    contents = f.read().split('\n')[0]









def part1(s):

    index = 0
    while index < len(s):
        if s[index] == '(':

            inner_brackets = s[index:].split(')')[0][1:]

            brackets_len = len(inner_brackets) +2

            nchars, rep = map(int, inner_brackets.split('x'))

            start_ind = index+brackets_len
            end_ind = start_ind + nchars
            next_nchars = s[start_ind:end_ind]

            lhs = s[:index]
            rhs = s[end_ind:]

            s = lhs+next_nchars*rep+rhs

            index += rep*nchars



        else:
            index +=1


    return s





def part2(s):


    index = 0
    while index < len(s):

        print(f'{index}', end='\r')
        if s[index] == '(':

            inner_brackets = s[index:].split(')')[0][1:]

            brackets_len = len(inner_brackets) +2

            nchars, rep = map(int, inner_brackets.split('x'))

            start_ind = index+brackets_len
            end_ind = start_ind + nchars
            next_nchars = s[start_ind:end_ind]

            lhs = s[:index]
            rhs = s[end_ind:]

            s = lhs+next_nchars*rep+rhs

            # index += rep*nchars



        else:
            index +=1


    return s









def tests_p1():

    assert 'ADVENT' == part1('ADVENT')
    assert 'ABBBBBC' == part1('A(1x5)BC')
    assert 'XYZXYZXYZ' == part1('(3x3)XYZ')
    assert 'ABCBCDEFEFG' == part1('A(2x2)BCD(2x2)EFG')
    assert '(1x3)A' == part1('(6x1)(1x3)A')
    assert 'X(3x3)ABC(3x3)ABCY' == part1('X(8x2)(3x3)ABCY')

    assert part1('xyz(3x4)abc(2x2)opkl') == 'xyzabcabcabcabcopopkl'



    assert part1('xyz(5x4)(9x9)(2x2)opkl') == 'xyz(9x9)(9x9)(9x9)(9x9)opopkl'





print(contents)

print(len(part2(contents)))









