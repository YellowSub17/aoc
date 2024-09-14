




with open('./input.txt') as f:
    target_chemical = f.read().split('\n')[0]

with open('./rules.txt') as f:
    rules_input = f.read().split('\n')[:-1]




def generate_rules(rules_input):

    rules = {}
    for rule in rules_input:
        lhs, rhs = rule.split(' => ')

        if lhs not in rules.keys():
            rules[rhs] = lhs
        else:
            rules[rhs] = lhs
    return rules

rules = generate_rules(rules_input)



def replace_nth(sub, repl, txt, nth):
    arr = txt.split(sub)
    part1 = sub.join(arr[:nth])
    part2 = sub.join(arr[nth:])
    return part1+repl+part2





# x = 'ab_ab_abc_lmoabdef_123'
# y = replace_nth('lm', 'XY', x, 3)
# print(y)



def generate_leaves(chem):

    leaves = []

    for lhs in rules:
        rhs = rules[lhs]


        lhs_count = chem.count(lhs)

        if lhs_count >0:
            for n in range(lhs_count):
                leaf = replace_nth(lhs, rhs, chem, n+1)

                leaves.append(leaf)

    return leaves


# for lhs in rules:
    # print(lhs, '->', rules[lhs])

# target_chemical = 'HPB'
# print(generate_leaves(target_chemical))




LOWEST_N = 999

COUNTED_NS = 0

def go_deeper(chem, n):


    global COUNTED_NS
    global LOWEST_N

    if n>LOWEST_N+1:
        print('BREAKBREAKBREAK')
        return
    print('Lowest n so far: ', LOWEST_N)

    if chem =='e':
        print('BADABING: ', n)
        COUNTED_NS +=1
        if LOWEST_N > n:
            LOWEST_N =n
            print('New lowest n: ', LOWEST_N)







    leaves = generate_leaves(chem)

    print(chem, leaves, n)

    n_branch_on_leaf = {}
    for leaf in leaves:

        n_branch_on_leaf[leaf] =len(generate_leaves(leaf))



    sorted_leaves = sorted(leaves, key=lambda x:n_branch_on_leaf[x], reverse=True)


    for leaf in sorted_leaves:
        go_deeper(leaf, n+1)



go_deeper(target_chemical, 0)

##you can let it run, but it keeps printing 195 and that was it







