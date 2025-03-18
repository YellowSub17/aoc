






class Node:

    def __init__(self, t, n):
        self.t = t
        self.n = n
        self.high_child = None
        self.low_child = None






with open('./input.prod', 'r') as f:
    cont= f.read().split('\n')


# nodes = {
        # 'bot59':    {
                    # 'low': 'bot176',
                    # 'high': 'bot120',
                    # },
        # 'val31':    'bot114',
        # 'bot142':   {
                    # 'low': 'out6',
                    # 'high': 'bot35',
                    # }
        # }

nodes = {}

for line in cont:
    words = line.split(' ')

    if words[0] == 'bot':
        nodes[f'{words[0]}{words[1]}'] = {'low': f'{words[5]}{words[6]}',
                                          'high': f'{words[10]}{words[11]}',
                                          'holding': [] }

        if words[5] =='output':
            nodes[f'{words[5]}{words[6]}'] = {'holding':[]}

        if words[10] =='output':
            nodes[f'{words[10]}{words[11]}'] = {'holding':[]}

    if words[0] == 'value':
        nodes[f'{words[0]}{words[1]}'] = {'bot': f'{words[4]}{words[5]}',
                                          'value': int(words[1])}


#initialise values
for key in nodes.keys():
    if 'value' in key:
        bot = nodes[key]['bot']
        value = nodes[key]['value']
        nodes[bot]['holding'].append(value)



for key in nodes.keys():
    print(key, nodes[key])



print('1111111111')
for key in nodes.keys():
    if 'bot' not in key: continue
    if len(nodes[key]['holding'])==2:
        print(key, nodes[key])
        nodes[key]['holding'].sort()
        print(key, nodes[key])

        high_bot = nodes[key]['high']
        low_bot = nodes[key]['low']

        nodes[low_bot]['holding'].append(nodes[key]['holding'][0])
        nodes[high_bot]['holding'].append(nodes[key]['holding'][1])

print('2222222222')


for key in nodes.keys():
    print(key, nodes[key])




# flag = True

# count = 0

# while flag:
    # count+=1
    # flag = False

    # for key in nodes.keys():
        # pass

        # if 'bot' in key:
            # if len(nodes[key]['holding']) <2:
                # holding_double_flag = True
            # elif len(nodes[key]['holding']) == 2:
                # high_bot = nodes[key]['high']
                # low_bot = nodes[key]['low']




                # nodes[key]['holding'].sort()

                # nodes[high_bot]['holding'].append(nodes[key]['holding'][1])
                # print(nodes[key]['holding'])
                # print('xxx', nodes[low_bot])
                # nodes[low_bot]['holding'].append(nodes[key]['holding'][0])


    # if count >10:
        # break













# print(nodes)








# print(nodes)






# print(nodes['value61'])


# while True:
    # print(key)
    # key = nodes[key]




# key = 'value61'

# print(key)

# print(nodes[key])

# print(nodes[nodes[key]])

















