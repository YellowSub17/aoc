
import numpy as np
import itertools
import matplotlib.pyplot as plt

fname = './input.test'





points = np.loadtxt(fname, delimiter=',', dtype=int)
pairs = list(itertools.combinations(points, 2))



ny = points[:,1].max()+1
nx = points[:,0].max()+1



# for p1, p2 in pairs:

    # total_floor = np.zeros( (ny, nx) )
    # print(p1, p2)
    # xmin = min(p1[0], p2[0])
    # xmax = max(p1[0], p2[0])
    # ymin = min(p1[1], p2[1])
    # ymax = max(p1[1], p2[1])
    # x = xmax-xmin+1
    # y = ymax-ymin+1

    # total_floor[ymin:ymin+y, xmin:xmin+x] = 1
    # print(total_floor)

    # floor = np.zeros( (y+1, x+1) )
    # print(floor)

    # plt.figure()
    # plt.title(f'{p1=}, {p2=} first')
    # plt.imshow(total_floor, aspect='equal', extent=[0, nx, ny, 0] )

    # plt.figure()
    # plt.imshow(floor, aspect='equal', extent=[0, x, y, 0])
    # # plt.show()
    # # break


    # for p1p, p2p in pairs:
        # print('\t', p1p, p2p)
        # xminp = min(p1p[0], p2p[0])
        # if xminp > xmax:
            # print('\tOUT OUT BOUNDS 0')
            # break
        # xmaxp = max(p1p[0], p2p[0])
        # if xmaxp < xmin:
            # print('\tOUT OUT BOUNDS 1')
            # break
        # yminp = min(p1p[1], p2p[1])
        # if yminp > ymax:
            # print('\tOUT OUT BOUNDS 2')
            # break
        # ymaxp = max(p1p[1], p2p[1])
        # if ymaxp < ymin:
            # print('\tOUT OUT BOUNDS 3')
            # break

        # xp = xmaxp -xminp+1
        # yp = ymaxp -yminp+1


        # xstart = max(0, xminp -xmin)
        # xend = min(x, xminp -xmin)


        # ystart = max(0, yminp -ymin)
        # yend = min(y, yminp -ymin)

        # floor[xstart:xend, ystart:yend] = 1


        # total_floor[xminp:xminp+xp, yminp:ymin+yp] = 1


        # plt.figure()
        # plt.imshow(total_floor, extent=[0, nx, ny, 0] )

        # plt.figure()
        # plt.imshow(floor, extent=[0, x, y, 0])

        # plt.show()





















# ####part 1

# # def find_area(p1, p2):

    # # xmin = min(p1[0], p2[0])
    # # xmax = max(p1[0], p2[0])
    # # ymin = min(p1[1], p2[1])
    # # ymax = max(p1[1], p2[1])
    # # x = xmax-xmin +1
    # # y = ymax-ymin +1

    # # return x*y
# # current_max = 0

# # for p1, p2 in pairs:

    # # area = find_area(p1,p2)
    # # if current_max<area:
        # # current_max = area
        # # # print(p1, p2)
        
# # print(f'{current_max=}')





























# # directions = [0,1,2,3] ## +x, -y, -x, +y
# current_direction = -1
# directions  =  np.ones(points.shape[0])*-1
# for i,  p1, p2 in enumerate(zip(points[:-1], points[1:])):
    
    # if p1[0] == p2[0] and p1[1]> p2[1]:
        # current_direction = 2
    # elif p1[0] == p2[0] and p1[1]> p2[1]:

    # elif p1[0] == p2[0] and p1[1]> p2[1]:

    # else:    # p1[0] == p2[0] and p1[1]> p2[1]:




















