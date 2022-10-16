
import sys
import numpy as np
import matplotlib.pyplot as plt


def number_of_presents(house_number):
    num_pres = 0
    # print(house_number)
    for elf_number in range(1, int(house_number)+1):
        if house_number%elf_number==0:
            num_pres +=elf_number*10
    print(f'{house_number=} {num_pres=}')
    return num_pres
        
if __name__=='__main__':


    # # house_count = 502760
    # # house_count = 952760
    # # house_count = 702760

    puzzle_input = 29000000
    house_count = int(sys.argv[1])
    num_pres_flag = 0

    # house_count = 748440
    # house_count = 695520

    # highter then 633547

    # lower then 606400


    while num_pres_flag < puzzle_input:
        house_count-=1
        num_pres_flag = number_of_presents(house_count)



    # xs = []
    # xs += [i*100 for i in range(1, 10)]
    # xs += [i*1000 for i in range(1, 10)]
    # xs += [i*10000 for i in range(1, 10)]
    # xs += [i*100000 for i in range(1, 10)]
    # xs += [i*1000000 for i in range(1, 10)]

    # xs = np.arange(1, 50)

    # print(number_of_presents(int(sys.argv[1])))

    # xs = np.logspace(10, 100000)

 #    ys = []
    # yerr = []
    # for x in xs:
        # print(x)
        # ave_range = np.arange(x-10, x+10)
        # ave_ys = []
        # for ave_x in ave_range:
            # ave_ys.append(number_of_presents(ave_x))

        # ys.append(np.mean(ave_ys))
        # yerr.append(np.std(ave_ys))

    # plt.figure()
    # plt.errorbar(xs, ys, yerr=yerr)
    # plt.vlines(145439, 0, 145439, color='red')
    # plt.hlines(29000000, 0, 29000000, color='green')
    # plt.show()

