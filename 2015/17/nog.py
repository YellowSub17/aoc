#!/usr/bin/env python3



import itertools

fname = 'input.prod'

store_cap = 150

f = open(fname, 'r')
cont = f.read().split('\n')[:-1]
print(cont)

all_containers = [ int(amount) for amount in cont]
print(all_containers)


valid_combos = []
for n in range(len(all_containers)):
    print(f"{n=}")

    for ith_combo_with_n in itertools.combinations(all_containers,n):

        sum_combo = sum(ith_combo_with_n)

        # print(ith_combo_with_n, sum_combo)

        if sum_combo==store_cap:
            valid_combos.append(ith_combo_with_n)


print(f"number of valid combos: {len(valid_combos)}")


min_num_containers = len(valid_combos[0])

for combo in valid_combos:
    if len(combo) < min_num_containers:
        min_num_containers=len(combo)



print(valid_combos)
print(min_num_containers)

num_containers_with_min = 0

for combo in valid_combos:
    if len(combo)==min_num_containers:
        num_containers_with_min +=1


print(num_containers_with_min)

























