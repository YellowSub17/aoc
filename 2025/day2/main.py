

with open('./input.test') as f:
    contents = f.read()[:-1].split(',')[:]

    ranges_str =list( map(lambda s: s.split('-'), contents))
    ranges_ints = list(map(lambda r: (int(r[0]), int(r[1])), ranges_str))


def is_invalid_str_p1(s):

    len_s = len(s)
    if len_s % 2 ==1: #odd number of digits cant repeat
        return False

    p1, p2 =  s[:len(s)//2], s[len(s)//2:]

    if p1==p2:
        return True
    else:
        return False

def is_invalid_str_p2(s):
    len_s = len(s)

## count if all the digits appear an equal number of times:
    counts = {}
    for c in s:
        if c not in counts:
            counts[c]=1
        else:
            counts[c] +=1

    print(counts)
    n = None #number of partitions
    for c in counts:
        if n is None:
            n=counts[c]
        else:
            if counts[c] !=n:
                return False



    len_n = len(s)//n

    #if n is 2, the each char appears twice, so split str into two
    #if n is 3, the each char appears thrice, so split str into three

    # 0123 4567
    # abcd abcd 

    # 012 345 678 : n=3
    # abc abc abc

    # n=5, len_n=3
    #              11 111
    # 012 345 678 901 234
    # abc abc abc abc abc

    splts = []
    for i in range(n):
        l = i*len_n
        r = i*len_n+len_n
        # splts.append(s[l:r])
        splts.append((s[l:r], l, r))


    for splt in splts[1:]:
        if splt[0] != splts[0][0]:
            return False


    print('\t',s, splts)
    return True



print(is_invalid_str_p2('1188511885'))




# invalids = []
# for range_start, range_end in ranges_ints:
    # print(f'###{range_start} {range_end}')
    # for i in range(range_start, range_end+1):
        # # print('\t', i, is_invalid_str_p2(str(i)))
        # if is_invalid_str_p2(str(i)):
            # invalids.append(i)

# print(sum(invalids))








# invalids = []
# for range_start, range_end in ranges_ints:
    # for i in range(range_start, range_end+1):
        # # print(i, is_invalid_str(str(i)))
        # if is_invalid_str_p1(str(i)):
            # invalids.append(i)

# # print(invalids)
# print(sum(invalids))

