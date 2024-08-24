




def get_factors(n):

    factors = []

    max_factor = int(n**0.5) + 1

    for f in range(1, max_factor):

        if n%f==0:
            factors.append(int(n/f))
            factors.append(f)

    factors = set(factors)
    return factors


def sum_factors_x_10(house_n):

    factors = get_factors(house_n)
    pres = 0
    for factor in factors:
        pres +=factor*10

    return pres








# ###part 1
# puzzle_input = 29_000_000
# most_presents = 0
# i_house = 0

# while most_presents< puzzle_input:

    # current_house_presents = sum_factors_x_10(i_house)

    # if  most_presents < current_house_presents:
        # print(i_house, '\t', current_house_presents)
        # most_presents = current_house_presents

    # i_house +=1

###part 2


factors_used  = {}



puzzle_input = 29_000_000
most_presents = 0
i_house = 0

while most_presents< puzzle_input:

    house_factors = get_factors(i_house)

    factors_to_sum =[]
    for factor in house_factors:
        if factor in factors_used.keys():
            factors_used[factor] +=1
        else:
            factors_used[factor] = 1

        if factors_used[factor] <=50:
            factors_to_sum.append(factor*11)



    current_house_presents = sum(factors_to_sum)

    if  most_presents < current_house_presents:
        print(i_house, '\t', current_house_presents)
        most_presents = current_house_presents

    i_house +=1

print(factors_used)































