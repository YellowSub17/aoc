


import itertools
import math




with open('./input.prod') as f:
    WEIGHTS = sorted(list(map(int, f.read().split('\n')[:-1])), reverse=True)


WEIGHTS=set(WEIGHTS)



def group_generator(weights, weight_p_group):

    for groupsize in range(1, len(weights)):
        for group in itertools.combinations(weights, groupsize):
            if sum(group) == weight_p_group:
                yield set(group)


def can_group(weights, n_groups, weight_p_group):
    if n_groups ==0:
        if len(weights)==0:
            return True
        else:
            return False

    for group in group_generator(weights, weight_p_group):


        if can_group(weights-group, n_groups-1, weight_p_group):
            return True

    return False





def ideal(weights, n_groups):


    prevgroupsize = len(weights)*10
    minQE=math.prod(weights)

    weight_p_group = sum(weights)/n_groups

    for group in group_generator(weights, weight_p_group):


        if minQE !=math.prod(weights) and prevgroupsize > len(group):
            break
        print(group)

        QE = math.prod(group)


        if QE < minQE and can_group(WEIGHTS-group, n_groups - 1, weight_p_group):
            minQE =QE
            print('BING!')
            print(minQE)

        prevgroupsize = len(group)

    return minQE

print(ideal(WEIGHTS, 3))




# count = 0
# for group in group_generator(WEIGHTS, MAX_WEIGHT):
    # print(count, group, can_group(WEIGHTS-group, 1, MAX_WEIGHT))

    # break

# print(group)



    # count +=1














# def generate_leaves(group, pool):

    # leaves = []

    # remaining_pools = []


    # for package in pool:

        # remaining_pool = pool[:]

        # if package in group:
            # continue
        # else:
            # leaves.append(group+[package])
            # remaining_pool.remove(package)
            # remaining_pools.append(remaining_pool)

    # return leaves, remaining_pools



# def generate_leaves(groups, pool):

    # leaves = []

    # remaining_pools = []


    # for package in pool:

        # remaining_pool = pool[:]

        # if package in group:
            # continue
        # else:
            # leaves.append(group+[package])
            # remaining_pool.remove(package)
            # remaining_pools.append(remaining_pool)

    # return leaves, remaining_pools





# groups0 = []
# pool0 = weights

# groups1, pool1 = generate_leaves(groups0, pool0)
# print(groups1[0])
# print(pool1[0])

# groups2, pool2 = generate_leaves(groups1[0], pool1[0])
# print(groups2[0])
# print(pool2[0])











