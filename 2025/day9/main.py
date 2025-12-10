
import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib import colormaps
import bisect

fname = './input.prod'

plasma = colormaps['plasma']

# Take colors at regular intervals spanning the colormap.
# colors = cmap(np.linspace(0, 1, n_lines))





points = np.loadtxt(fname, delimiter=',', dtype=int)
points_loop = np.concat((points, [points[0,:]]), axis=0)



class LineSeg:

    def __init__(self, xs, ys):
        self.xs = np.array(xs)
        self.ys = np.array(ys)

        self.vertical = self.xs[0]==self.xs[1]
        self.horizontal = not self.vertical

        if self.vertical:
            self.start = self.ys[0]
            self.end = self.ys[1]
            self.c = self.xs[0]
        else:
            self.start = self.xs[0]
            self.end = self.xs[1]
            self.c = self.ys[0]

    def __str__(self):

        if self.horizontal:
            s =f'H line segment at y={self.ys[0]} from x={self.xs}'
        else:
            s =f'V line segment at x={self.xs[0]} from y={self.ys}'
        return s

    def plot(self, **kwargs):
        plt.plot(self.xs, self.ys, **kwargs)








x_pts = points[:,0]
y_pts = points[:,1]

line_segs = []

for i, (x1y1, x2y2) in enumerate(itertools.pairwise(points_loop)):
    line_segs.append( LineSeg([x1y1[0], x2y2[0]], [x1y1[1], x2y2[1]]) )

horizontal_line_segs = line_segs[1::2]
vertical_line_segs = line_segs[::2]

# horizontal_line_segs = line_sprod::2]
# vertical_line_segs = line_segs[1::2]

horizontal_line_segs.sort(key = lambda ls: ls.c)
vertical_line_segs.sort(key = lambda ls: ls.c)



pairs = list(itertools.combinations(points, 2))
print(len(pairs))


count =0
max_area =0

pair_start =4163
# for i, (p1, p2) in enumerate(pairs[::1]):
# for i, (p1, p2) in enumerate(pairs[pair_start::1]):
# [83075, 85213] [16219, 15814]
for i, (p1, p2) in enumerate([ [[83075, 85213], [16219, 15814]] ]):


    print(i, end='\r')

    xmin = min(p1[0], p2[0])
    xmax = max(p1[0], p2[0]) + 1

    ymin = min(p1[1], p2[1])
    ymax = max(p1[1], p2[1]) +1
    x = xmax-xmin
    y = ymax-ymin
    # print(xmin, xmax, ymin, ymax)


    vcrop = vertical_line_segs[:]
    # vcrop = list(filter(lambda ls:  ls.ys.min()<ymax and ls.ys.max()>ymin, vcrop))
    # vcrop = list(filter(lambda ls: ls.c>=xmin and ls.c<=xmax, vcrop))
    vcrop = list(filter(lambda ls: ls.c>=xmin and ls.c<=xmax, vcrop))
    vcrop = list(filter(lambda ls:  ls.ys.min()>ymin or ls.ys.max()<ymax, vcrop))

    hcrop = horizontal_line_segs[:]
    hcrop = list(filter(lambda ls: ls.c>=ymin and ls.c<=ymax, hcrop))
    hcrop = list(filter(lambda ls:  ls.xs.min()>xmin or  ls.xs.max()<xmax, hcrop))


    plt.figure()
    for ls in line_segs:
        ls.plot(color=(0.0, 0.0, 0.0))
    for ls in vcrop:
        ls.plot(color='r', linewidth=1)
    for ls in hcrop:
        ls.plot(color='r', linewidth=1)
    plt.plot( [p1[0], p2[0], p2[0], p1[0], p1[0]], [p1[1], p1[1], p2[1], p2[1], p1[1]], color='m', ls='dashed')
    plt.plot(p1[0], p1[1], 'g.', ms=25)
    plt.plot(p2[0], p2[1], 'm.', ms=25)
    plt.show()


    # plt.show()

    if len(hcrop)+len(vcrop)>3:
        continue

    print()
    print()
    count +=1
    area = x*y

    if area> max_area:
        max_area=area
        print('new max area!', p1, p2)
        print(max_area)

        # plt.figure()
        # for ls in line_segs:
            # ls.plot(color=(0.0, 0.0, 0.0))
        # for ls in vcrop:
            # ls.plot(color='r', linewidth=1)
        # for ls in hcrop:
            # ls.plot(color='r', linewidth=1)
        # plt.plot( [p1[0], p2[0], p2[0], p1[0], p1[0]], [p1[1], p1[1], p2[1], p2[1], p1[1]], color='m', ls='dashed')
        # plt.plot(p1[0], p1[1], 'g.', ms=25)
        # plt.plot(p2[0], p2[1], 'm.', ms=25)
        # plt.show()

    print()
    print()
print('###')
print(f'{count=}')
print(f'{max_area}')


#287881312 too low
#1528567740 too low

    # print(vcrop_start, vcrop_end, hcrop_start, hcrop_end)

    # plt.figure()
    # for ls in line_segs:
        # ls.plot(color=(0.0, 0.0, 0.0))


    # for ls in vcrop:
        # ls.plot(color='r', linewidth=1)

    # for ls in hcrop:
        # ls.plot(color='r', linewidth=1)


#     plt.plot( [p1[0], p2[0], p2[0], p1[0], p1[0]], [p1[1], p1[1], p2[1], p2[1], p1[1]], color='m', ls='dashed')
    # plt.plot(p1[0], p1[1], 'g.', ms=25)
    # plt.plot(p2[0], p2[1], 'm.', ms=25)


    # plt.show()


print(count)



    # bisect.bisect_left
















# plt.plot(50000, 75000, 'g.')









# lhs = bisect.bisect_left(vertical_line_segs, 50000, key=lambda ls: ls.c)
# print(lhs, vertical_line_segs[lhs])


# lhs = bisect.bisect_right(horizontal_line_segs, 75000, key=lambda ls: ls.ys[0])
# horizontal_line_segs[lhs].plot(color='k')

# rhs = bisect.bisect_right(horizontal_line_segs, 75000, key=lambda ls: ls.ys[0])
# horizontal_line_segs[rhs].plot(color='r')

# print(lhs, horizontal_line_segs[lhs])
# print(rhs, horizontal_line_segs[rhs])
  # for i, ls in enumerate(horizontal_line_segs):
        # ls.plot(color = colormaps['viridis'](np.linspace(0, 1, len(horizontal_line_segs))[i]))
    # for i, ls in enumerate(vertical_line_segs):
        # ls.plot(color = colormaps['viridis'](np.linspace(0, 1, len(vertical_line_segs))[i]))






















# ####part 1

# pairs = list(itertools.combinations(points, 2))

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


























