#!/usr/bin/env python3


if __name__ == '__main__':

    fname = 'input.test'
    
    store_cap = 25

    f = open(fname, 'r')
    cont = f.read().split('\n')[:-1]
    print(cont)


    all_containers = [ int(amount) for amount in cont]
    print(all_containers)


    def recurse_engine(container_choices=all_containers, containers_used=[], limit=25, known_codes=0):


        current_cap = 0
        code = ''
        for label, amount in enumerate(containers_used):
            current_cap +=x
            code += str(i)



        for label, amount in enumerate(container_choices):

            if current_cap + amount < limit
                current_cap +=x
                code += i


















