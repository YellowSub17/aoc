



with open('./input.prod') as f:
    WEIGHTS = sorted(list(map(int, f.read().split('\n')[:-1])), reverse=True)


MAX_WEIGHT = int(sum(WEIGHTS)/3)



# class Slay:




    # def __init__(self, weight_pool=WEIGHTS, paren=None, grp1=[], grp2=[], grp3=[]):


        # self.weight_pool = weight_pool

        # self.paren = paren

        # self.grp1 = grp1
        # self.grp2 = grp2
        # self.grp3 = grp3



    # def add_present(self, grp1


    # def make_children(self):

        # children = []


        # for grp in [self.grp1, self.grp2, self.grp3]:

            # for weight in self.weight_pool:
                # weights_cp = self.weight_pool[:]















s = Slay()


print(s.weight_pool)
print(s.grp1)














