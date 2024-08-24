



import numpy as np
import itertools

weapons = np.array(
[
[ 8,     4,       0,],
[ 10,    5,       0,],
[ 25,    6,       0,],
[ 40,    7,       0,],
[ 74,    8,       0,],
]
)

armour = np.array(
[
[13,     0,       1,],
[31,     0,       2,],
[53,     0,       3,],
[75,     0,       4,],
[102,    0,       5,],
[0,      0,       0,],
]
)

rings = np.array(
[
[25,     1,       0,],
[50,     2,       0,],
[100,    3,       0,],
[20,     0,       1,],
[40,     0,       2,],
[80,     0,       3,],
[0,      0,       0,],
]
)




def calc_itemset(key):
    row = np.zeros((1, 3))
    row += weapons[int(key[0]), :]
    row += armour[int(key[1]), :]
    row += rings[int(key[2]), :]
    row += rings[int(key[3]), :]
    return row



def generate_all_itemset_keys():

    weapon_indices = [i for i in range(5)]
    armour_indices = [i for i in range(6)]
    ring_indices = [i for i in range(6)]

    wa_keys = itertools.product(weapon_indices, armour_indices)

    dr_keys = itertools.combinations(ring_indices, 2)
    sr_keys = itertools.product([6], ring_indices)
    nr_key = itertools.product([6], [6])

    ring_keys = itertools.chain(dr_keys, sr_keys, nr_key)

    keys = itertools.product(wa_keys, ring_keys)

    game_strs = []
    for key in keys:
        key_str = f'{key[0][0]}{key[0][1]}{key[1][0]}{key[1][1]}'
        game_strs.append(key_str)

    return game_strs



game_keys = generate_all_itemset_keys()
item_stats = np.zeros( (len(game_keys),  3))

for i, game_key in enumerate(game_keys):
    item_stats[i, :] = calc_itemset(game_key)



def play_game(key_i):

    boss_hps = 109
    play_hps = 100

    gold_spent = item_stats[key_i, 0]

    boss_dam = 8
    boss_arm = 2

    play_dam = item_stats[key_i, 1]
    play_arm= item_stats[key_i, 2]

    # print(f'Starting game {game_keys[key_i]}')
    # print(f'{results[key_i]}')



    while True:
        boss_hps -= max(1, play_dam-boss_arm)
        if boss_hps <= 0:
            # print('Player Wins!')
            return True, gold_spent
        play_hps -= max(1, boss_dam-play_arm)
        if play_hps <=0:
            # print('Player Loses!')
            return False, gold_spent
        # print(f'{boss_hps=}, {play_hps=}')



####part 1

print('PART1')
max_gold = 999999999

for key_i, game_key in enumerate(game_keys):

    pwins, gold_spent = play_game(key_i)

    if pwins and gold_spent < max_gold:
        max_gold = gold_spent
        print(key_i, max_gold)



####part 2

print('PART2')
min_gold = 0

for key_i, game_key in enumerate(game_keys):

    pwins, gold_spent = play_game(key_i)

    if not pwins and gold_spent > min_gold:
        min_gold = gold_spent
        print(key_i, min_gold)













# print(calc_item_set([0,0,6,6]))





