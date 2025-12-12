

import numpy as np
import itertools
import matplotlib.pyplot as plt
import bisect

fname = './input.prod'





points = np.loadtxt(fname, delimiter=',', dtype=int)
points_loop = np.concat((points, [points[0,:]]), axis=0)



class LineSeg:

    def __init__(self, xs, ys):
        self.xs = np.array(xs)
        self.ys = np.array(ys)

        self.vertical = self.xs[0]==self.xs[1]
        self.horizontal = not self.vertical

        if self.vertical:
            self.start = self.ys.min()
            self.end = self.ys.max()
            self.c = self.xs[0]
        else:
            self.start = self.xs.min()
            self.end = self.xs.max()
            self.c = self.ys[0]

    def __str__(self):
        if self.horizontal:
            s =f'H line segment at y={self.ys[0]} from x={self.xs}'
        else:
            s =f'V line segment at x={self.xs[0]} from y={self.ys}'
        return s

    def plot(self, **kwargs):
        plt.plot(self.xs, self.ys, **kwargs)


    def intersection(self, ls):

        opp_dir = (self.vertical and ls.horizontal) or (self.horizontal and ls.vertical)



        if opp_dir:
            if ls.c >= self.start and ls.c <= self.end:
                return True
        else:
            return False







x_pts = points[:,0]
y_pts = points[:,1]

line_segs = []

for i, (x1y1, x2y2) in enumerate(itertools.pairwise(points_loop)):
    line_segs.append( LineSeg([x1y1[0], x2y2[0]], [x1y1[1], x2y2[1]]) )




if fname[-3:] =='prod':
    horizontal_line_segs = line_segs[::2]
    vertical_line_segs = line_segs[1::2]
else:
    horizontal_line_segs = line_segs[1::2]
    vertical_line_segs = line_segs[::2]

# plt.figure()
# for ls in horizontal_line_segs:
    # ls.plot(color=(1,0,0))

# for ls in vertical_line_segs:
    # ls.plot(color=(0,1,1))
# plt.show()

horizontal_line_segs.sort(key = lambda ls: ls.c)
vertical_line_segs.sort(key = lambda ls: ls.c)

pairs = list(itertools.combinations(points, 2))


max_area = 0

for p1, p2 in pairs:




    xmin = min(p1[0], p2[0])
    xmax = max(p1[0], p2[0])
    ymin = min(p1[1], p2[1])
    ymax = max(p1[1], p2[1])
    x = xmax-xmin +1
    y = ymax-ymin +1

    rect_linesegs = [
                    LineSeg( [xmin, xmax], [ymin, ymin]),
                    LineSeg( [xmin, xmax], [ymax, ymax]),
                    LineSeg( [xmin, xmin], [ymin, ymax]),
                    LineSeg( [xmax, xmax], [ymin, ymax]),
                    ]




    internals_detected = False
    for rect_line_seg in rect_linesegs:

        for line_seg in line_segs:
            cond1 = (line_seg.horizontal and rect_line_seg.vertical) or (rect_line_seg.horizontal and line_seg.vertical)
            cond2 = (rect_line_seg.c > line_seg.start) and (rect_line_seg.c < line_seg.end)
            cond3 = (rect_line_seg.start < line_seg.c) and (rect_line_seg.end > line_seg.c)

            if cond1 and cond2 and cond3:
                internals_detected=True


    for line_seg in vertical_line_segs:
        cond1 = ( line_seg.c > xmin ) and  (line_seg.c < xmax)
        cond2 = ( line_seg.start > ymin ) and (line_seg.end < ymax)
        if cond1 and cond2:
            internals_detected=True

    for line_seg in horizontal_line_segs:
        cond1 = ( line_seg.c > ymin ) and  (line_seg.c < ymax)
        cond2 = ( line_seg.start >= xmin ) and (line_seg.end <= xmax)
        if cond1 and cond2:
            internals_detected=True



#                 plt.figure()
                # for rect_line_segx in rect_linesegs:
                    # rect_line_segx.plot(color=(1,0,0), linestyle='dashed')
                # for line_segx in line_segs:
                    # line_segx.plot(color=(0.3,0.3,0.3))
                # line_seg.plot(color=(0,1,0))
                # plt.show()

    if not internals_detected:

        area = x*y

        if area>max_area:
            max_area = area
            print('New lap record')
            print(max_area)

          #   plt.figure()
            # plt.title(f'AREA: {max_area}')
            # for line_seg in line_segs:
                # line_seg.plot(color=(0.3,0.3,0.3))

            # for rect_line_seg in rect_linesegs:
                # rect_line_seg.plot(color=(1, 0,0), linestyle='dashed')

     
            # plt.show()






#1200858831 too low
#1534043700












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





