

with open('./input.prod') as f:
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
    len_s = len(s) # 1188511885 -> 10

    
    for len_part in range(1, len_s): #test length of part 1,2,3,4,5..., 9
        # print(f'length of part: {len_part}')

# if the partition length isn't divisible by the total length, try the next part
        if len_s % len_part !=0:
            continue

        n_parts = len_s//len_part
        # print('### nparts', n_parts)


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
        for i in range(n_parts):
            l = i*len_part
            r = (i+1)*len_part
            splts.append(s[l:r])


        not_this_splts = False
        for splt in splts[1:]:
            if splt != splts[0]:
                not_this_splts = True
                break

        if not_this_splts:
            continue
        else:
            # print(splts)
            return True

    return False




# print(is_invalid_str_p2('11851188511885'))




invalids = []
for range_start, range_end in ranges_ints:
    # print(f'###{range_start} {range_end}')
    for i in range(range_start, range_end+1):
        # print('\t', i, is_invalid_str_p2(str(i)))
        if is_invalid_str_p2(str(i)):
            invalids.append(i)

print(sum(invalids))








# invalids = []
# for range_start, range_end in ranges_ints:
    # for i in range(range_start, range_end+1):
        # # print(i, is_invalid_str(str(i)))
        # if is_invalid_str_p1(str(i)):
            # invalids.append(i)

# # print(invalids)
# print(sum(invalids))

