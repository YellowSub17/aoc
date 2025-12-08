


import numpy as np
import itertools
import math






fname = './input.prod'

# fname = './input.prod'

points = np.loadtxt(fname, delimiter=',')
point_ids = np.arange(len(points))


pair_ids  = itertools.combinations(point_ids, 2)

n_pairs = math.comb(len(points),2)



pre_calc_d = np.zeros( ( n_pairs, 3) )

for i, (id1, id2) in enumerate(pair_ids):
    d = np.linalg.norm(points[id1]-points[id2])
    pre_calc_d[i] = np.array([id1, id2, d])

pre_calc_d = pre_calc_d[pre_calc_d[:, 2].argsort()]
# print(pre_calc_d)


closest_pairs = pre_calc_d[:, :-1]
print('####')
# for id1, id2 in closest_pairs:
    # print(id1, id2, '\t', points[int(id1), :],'\t', points[int(id2),:])
print('####')

circuits = []
# visited_junctions = set([])


# count=0
for ixx, (id1, id2) in enumerate(closest_pairs):

    # print('Attempting to connect points:')
    # print(int(id1), int(id2), '\t', points[int(id1), :],'\t', points[int(id2),:])

    circ_id1 = None
    circ_id2 = None

    new_circuit = True


    for i_circ, circuit in enumerate(circuits):

        if id1 in circuit:
            print(f'id1={int(id1)} found in circuit {circuit}')
            print(f'adding id2={int(id2)} to circuit')
            circuit.add(int(id2))
            circ_id2 = i_circ
            new_circuit=False

        elif id2 in circuit:
            print(f'id2={int(id2)} found in circuit {circuit}')
            print(f'adding id1={int(id1)} to circuit')
            circuit.add(int(id1))
            circ_id1 = i_circ
            new_circuit=False
        else:
            continue

    if new_circuit:
        print('Ids were not matched in any existing circuit. Making new circuit.')
        circuits.append( set([int(id1),int(id2)]) )
        # visited_junctions.add(id1)
        # visited_junctions.add(id2)

    print(f'Circuit ids were: {circ_id1}, {circ_id2}')
    if circ_id1 is not None and circ_id2 is not None:
        print('Both circ ids not none...')
        if circ_id1 != circ_id2:
            print('And not equal to eachother!')
            print(f'need to combine sets: {circuits[circ_id1]}, {circuits[circ_id2]}')
            circuits[circ_id2] = circuits[circ_id2].union(circuits[circ_id1])
            circuits.pop(circ_id1)


    if len(circuits ) == 1 and len(circuits[0])==point_ids.shape[0]:
        print('%%%%%')
        print(ixx, points[int(id1)], points[int(id2)])
        print(points[int(id1)][0], points[int(id2)][0])
        print(points[int(id1)][0]* points[int(id2)][0])

        # if circ_id1==0 and circ_id2 is None:
        # print('BREAK')
        # breakpoint()
        break


    print('#Circuits:', len(circuits))
    print()
    # for c in circuits:
        # print(c)

    # breakpoint()




# circuits.sort(key = lambda s: len(s))
# for circuit in circuits:
    # print(circuit)

# print(len(circuits[-1])*len(circuits[-2])*len(circuits[-3]))

#4590 wrong


#394761294 too low
#1109399334 too low

#1895205564 too low
#2347225200









# print(pairs)

