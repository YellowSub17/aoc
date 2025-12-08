


import numpy as np
import itertools
import math






fname = './input.test'
nconnections = 100

# fname = './input.prod'
# nconnections = 1000

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

closest_pairs = pre_calc_d[:nconnections, :-1]
print('####')
for id1, id2 in closest_pairs:
    print(id1, id2, '\t', points[int(id1), :],'\t', points[int(id2),:])
print('####')

circuits = []
visited_junctions = set([])


# count=0
for id1, id2 in closest_pairs:

    # if len(visited_junctions) >10:
        # break

    # if len(circuits) >10:
        # break
#     count+=1
    # if count>nconnections:
        # break

    circ_id1 = None
    circ_id2 = None

    new_circuit = True


    for i_circ, circuit in enumerate(circuits):

        if id1 in circuit:
            circuit.add(id2)
            visited_junctions.add(id2)
            circ_id2 = i_circ
            new_circuit=False

        elif id2 in circuit:
            circuit.add(id1)
            visited_junctions.add(id1)
            circ_id1 = i_circ
            new_circuit=False
        else:
            continue

    if new_circuit:
        circuits.append( set([id1,id2]) )
        visited_junctions.add(id1)
        visited_junctions.add(id2)


    if circ_id1 is not None and circ_id2 is not None:
        circuits[circ_id2] = circuits[circ_id2].union(circuits[circ_id2])
        circuits.pop(circ_id1)


    print(id1, id2, '\t', points[int(id1), :],'\t', points[int(id2),:])
    for c in circuits:
        print(c)

    breakpoint()




circuits.sort(key = lambda s: len(s))
for circuit in circuits:
    print(circuit)

print(len(circuits[-1])*len(circuits[-2])*len(circuits[-3]))

#4590 wrong












# print(pairs)

