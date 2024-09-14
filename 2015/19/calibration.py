







class Factory:


    def __init__(self, input_str, rules_str):


        self.input_str = input_str[:-1]
        self.rules_str = rules_str

        self.rules_dict = {}
        

        for replacement in self.rules_str.split('\n')[:-1]:
            LHS = replacement.split(' ')[0]
            RHS = replacement.split(' ')[-1]


            if LHS in self.rules_dict.keys():

                self.rules_dict[LHS].append(RHS)
            else:
                self.rules_dict[LHS] = [RHS]






    def expand(self, molecule):

        replaced_strs = []

        for LHS in self.rules_dict.keys():
            n_replacements = molecule.count(LHS)
            if n_replacements == 0:
                continue

            RHS_sorted = self.rules_dict[LHS]
            RHS_sorted.sort()
            for RHS in RHS_sorted[::-1]:
                found_i = molecule.find(LHS)

                for n in range(n_replacements):
                    this_replacement = ''
                    this_replacement += molecule[:found_i]
                    this_replacement += RHS
                    this_replacement += molecule[found_i+len(LHS):]
                    replaced_strs.append(this_replacement)

                    found_i = molecule.find(LHS, found_i+1)


        replaced_strs = list(set(replaced_strs))

        return replaced_strs

    
    def calibrate(self):
        print(len(self.expand(self.input_str)))





class InverseFactory:

    def __init__(self, input_str, rules_str):

        self.input_str = input_str[:-1]
        self.rules_str = rules_str

        self.rules_dict = {}

        self.found_paths = []
        self.current_shortest_path = 99

        self.quit_flag = False
        

        for replacement in self.rules_str.split('\n')[:-1]:
            LHS = replacement.split(' ')[-1]
            RHS = replacement.split(' ')[0]


            self.rules_dict[LHS] = RHS


    
    def contract(self, molecule):

        rules_LHS = list(self.rules_dict.keys())
        rules_LHS.sort( key=lambda x : len(x))

        # return(rules_LHS)
        
        for LHS in rules_LHS[::-1]:


            n_replacements = molecule.count(LHS)
            print(LHS, n_replacements)























if __name__ == '__main__':



    input_file = open('input.txt', 'r')
    rules_file = open('rules.txt', 'r')

    input_str = input_file.read()
    rules_str = rules_file.read()

    input_file.close()
    rules_file.close()



    f = Factory(input_str, rules_str)

    #PART1
    f.calibrate()


    f = InverseFactory(input_str, rules_str)





#     #PART2
#     input_str = 'dy'
    # rules_dict = {
                    # 'e': ['ay', 'zz'],
                    # 'a': ['b'],
                    # 'b': ['c'],
                    # 'c': ['d'],
                    # 'zz': ['dy'],
                 # }
    # f.input_str = input_str
    # f.rules_dict = rules_dict


