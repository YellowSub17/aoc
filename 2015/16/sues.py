#!/usr/bin/env python3


PROPS = ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas',
              'vizslas', 'goldfish', 'trees', 'cars', 'perfumes']

class Sue:

    def __init__(self, s):
        self.s = s
        self.number = int(s.split()[1][:-1])
        self.the_one = False


        self.props_dict = {}

        for prop in PROPS:
            self.props_dict[prop] = get_num(prop, self.s)

        # self.children = get_num('children', self.s)
        # self.cats = get_num('cats', self.s)
        # self.samoyeds = get_num('samoyeds', self.s)
        # self.pomeranians = get_num('pomeranians', self.s)
        # self.akitas = get_num('akitas', self.s)
        # self.vizslas = get_num('vizslas', self.s)
        # self.goldfish = get_num('goldfish', self.s)
        # self.trees = get_num('trees', self.s)
        # self.cars = get_num('cars', self.s)
        # self.perfumes = get_num('perfumes', self.s)



def get_num(prop, s):


    prop_index = s.find(prop)

    if prop_index == -1:
        return None
    else:
        sub_s = s[prop_index+len(prop)+2:]
        comma_index = sub_s.find(',')
        if comma_index == -1:
            prop_num = int(sub_s.split()[-1])
        else:
            prop_num = int(sub_s[:comma_index])

        return prop_num




def check_sue(sue1, sue2):

    for prop in PROPS:
        if (sue1.props_dict[prop] is None) or (sue2.props_dict[prop] is None):
            continue
        if sue1.props_dict[prop] != sue2.props_dict[prop]:
            return False

    return True




def check_sue2(sue1, sue2):

    for prop in PROPS:
        if (sue1.props_dict[prop] is None) or (sue2.props_dict[prop] is None):
            continue
        if sue1.props_dict[prop] != sue2.props_dict[prop]:
            return False

    return True


def check_sue2(sue1, sue2):
    PROPSeq = ['children', 'samoyeds', 'akitas',
              'vizslas', 'cars', 'perfumes']

    # PROPS = ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas',
              # 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes']
    for prop in PROPSeq:
        if (sue1.props_dict[prop] is None) or (sue2.props_dict[prop] is None):
            continue
        if sue1.props_dict[prop] != sue2.props_dict[prop]:
            return False

    PROPSgt = ['cats', 'trees']
    for prop in PROPSgt:
        if (sue1.props_dict[prop] is None) or (sue2.props_dict[prop] is None):
            continue
        if sue1.props_dict[prop] <= sue2.props_dict[prop]:
            return False


    PROPSlt = ['pomeranians', 'goldfish']
    for prop in PROPSlt:
        if (sue1.props_dict[prop] is None) or (sue2.props_dict[prop] is None):
            continue
        if sue1.props_dict[prop] >= sue2.props_dict[prop]:
            return False


    return True




if __name__ == '__main__':


    file = open('input.prod', 'r')
    lines = file.read().split('\n')[:-1]
    file.close()


    s = 'Sue -1: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1'
    MAIN_SUE = Sue(s)


    for line in lines:
        sx = Sue(line)
        if check_sue2(sx, MAIN_SUE):
            print(sx.number, ':', check_sue2(sx, MAIN_SUE))


