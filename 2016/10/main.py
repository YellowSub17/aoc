






class Node:

    def __init__(self, t, n):
        self.t = t
        self.n = n
        self.high_child = None
        self.low_child = None






with open('./input.prod', 'r') as f:
    cont= f.read().split('\n')



nodes = {}

for line in cont:
    words = line.split(' ')

    if words[0] == 'bot':
        nodes[f'{words[0]}{words[1]}'] = {'low': f'{words[5]}{words[6]}',
                                          'high': f'{words[10]}{words[11]}',
                                          'holding': set([]) }

        if words[5] =='output':
            nodes[f'{words[5]}{words[6]}'] = {'holding':set([])}

        if words[10] =='output':
            nodes[f'{words[10]}{words[11]}'] = {'holding':set([])}

    if words[0] == 'value':
        nodes[f'{words[0]}{words[1]}'] = {'bot': f'{words[4]}{words[5]}',
                                          'value': int(words[1])}


#initialise values
for key in nodes.keys():
    if 'value' in key:
        bot = nodes[key]['bot']
        value = nodes[key]['value']
        nodes[bot]['holding'].add(value)





flag = True
while flag:
    flag = False
    for key in nodes.keys():
        if 'bot' not in key: continue

        if len(nodes[key]['holding'])<2:
            flag=True

        elif len(nodes[key]['holding'])==2:
            # print(key, nodes[key])
            vals = list(nodes[key]['holding'])
            vals.sort()
            # print(key, nodes[key])

            high_bot = nodes[key]['high']
            low_bot = nodes[key]['low']

            if len(nodes[low_bot]['holding'])<2:
                nodes[low_bot]['holding'].add(vals[0])

            if len(nodes[high_bot]['holding'])<2:
                nodes[high_bot]['holding'].add(vals[1])



for key in nodes.keys():
    if 'bot' not in key:
        continue

    if set(nodes[key]['holding']) == {61, 17}:
        print(key, nodes[key])


i = nodes['output0']['holding'].pop()
j = nodes['output1']['holding'].pop()
k = nodes['output2']['holding'].pop()
print(i, j, k, i*j*k)

