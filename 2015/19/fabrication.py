




with open('./input.txt') as f:
    target_chemical = f.read().split('\n')[0]

with open('./rules.txt') as f:
    rules_input = f.read().split('\n')[:-1]





rules = {}
for rule in rules_input:
    lhs, rhs = rule.split(' => ')

    if lhs not in rules.keys():
        rules[lhs] = [rhs]
    else:
        rules[lhs].append(rhs)



def replace_nth(sub, repl, txt, nth):
    arr = txt.split(sub)
    part1 = sub.join(arr[:nth])
    part2 = sub.join(arr[nth:])
    return part1+repl+part2






def generate_open_leaves(leaves):

    open_leaves = []

    for chem, steps in leaves:


        for lhs in rules.keys():

            lhs_count = chem.count(lhs)

            if lhs_count >0:
                for n in range(lhs_count):
                    for rhs in rules[lhs]:
                        open_leaf = replace_nth(lhs, rhs, chem, n+1)

                        if len(open_leaf) > len(target_chemical):
                            continue

                        if open_leaf == target_chemical:
                            print('FOUND!')
                            print('Number of steps: ', steps+1)
                            exit()

                        else:
                            open_leaves.append((open_leaf, steps+1))
    return open_leaves





open_leaves = [('e', 0)]


count = 0
while True:
    open_leaves = generate_open_leaves(open_leaves)
    print(open_leaves)
    print('Count: ', count )
    print('Number of leaves: ', len(open_leaves) )

    count +=1

    if count > 4:
        break
















