

import regex



def mul_xy(s):
    x,y = regex.findall('\d+', s)
    return int(x)*int(y)



def part1():
    with open('./input.prod', 'r') as f:
        cont = f.read()


    muls = regex.findall('mul\(\d{1,3},\d{1,3}\)',cont)


    out = map(mul_xy, muls)

    print(sum(out))


def part2():

    with open('./input.prod', 'r') as f:
        cont = f.read()

    # cont = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    #get do() and don't()
    dos = [ ( m.start(0), True) for m in regex.finditer(r'do\(\)', cont)]
    donts = [ (m.start(0), False) for m in regex.finditer(r"don't\(\)", cont)]

    #input starts with do()
    dosdonts = [(0, True)] +dos+donts



    #sort dos and donts
    dosdonts.sort(key=lambda x: x[0])

    # if dos[-1][0] < donts[-1][0]:
        # dosdonts.append(



    #we want everytime we go do -> dont (True -> False)
    ##### or do -> do (True -> True)
    #we have a slice of cont that we want to search for mul
    good_areas = []
    for pairdosdonts_i, pairdosdonts_j in zip(dosdonts[:-1], dosdonts[1:]):
        # print(pairdosdonts_i, pairdosdonts_j)

        if pairdosdonts_i[1] and not pairdosdonts_j[1]:
            good_areas.append( (pairdosdonts_i[0], pairdosdonts_j[0]) )

        if pairdosdonts_i[1] and pairdosdonts_j[1]:
            good_areas.append( (pairdosdonts_i[0], pairdosdonts_j[0]) )


    # if the last found do/dont function is a "do, then the last dosdonts element
    # is (x, True) and we need to look at the remainder of the string

    if dosdonts[-1][1]:
        good_areas.append( ( dosdonts[-1][0], -1))

    sliced_cont = ''
    for good_area in good_areas:
        sliced_cont = sliced_cont + cont[good_area[0]: good_area[1]]

    muls = regex.findall('mul\(\d{1,3},\d{1,3}\)',sliced_cont)

    out = map(mul_xy, muls)

    print(sum(out))

    # print(sliced_cont)

   # 19941750 too low
   # 22443619 to low







if __name__=='__main__':

    part1()
    
    part2()

