






with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]




class Screen:


    def __init__(self, ):
        self.NX = 50
        self.NY = 6

        self.screen = []

        for y in range(self.NY):
            self.screen.append([' ']*self.NX)


    def add_rect(self, w,h):

        for i_h in range(h):
            for i_w in range(w):
                self.screen[i_h][i_w] = '#'

    def rotate_row(self, y, n):
        current_row =self.screen[y]
        new_row = roll_list(current_row, n)
        self.screen[y] = new_row



    def rotate_col(self, x, n):

        col = []

        for row in self.screen:
            col.append(row[x])

        new_col = roll_list(col, n)

        for i_row in range(self.NY):
            self.screen[i_row][x] = new_col[i_row]






    def print_screen(self):
        print('### Screen')
        for row in s.screen:
            print(row)


    def parse_inst(self, inst):

        match inst.split():
            case ['rotate', 'column', x_str, 'by', n_str]:
                x = int(x_str[2:])
                n = int(n_str)
                self.rotate_col(x, n)

            case ['rotate', 'row', y_str, 'by', n_str]:
                y = int(y_str[2:])
                n = int(n_str)
                self.rotate_row(y, n)

            case ['rect', wxh]:
                w, h, = map(int, wxh.split('x'))
                self.add_rect(w,h)

            case _ :

                raise


    def find_sum(self):
        count = 0

        for row in self.screen:
            count += row.count('#')

        return count





def roll_list(ls, n):
    doub_ls = ls +ls
    start_ind = len(ls)-n
    end_ind  = -n
    return doub_ls[start_ind:end_ind]


# l1 =[0,1,2,3,4,5,6,7]
# print(l1)
# l2 = roll_list(l1, 3)
# print(l2)


s  = Screen()



for inst in contents:
    s.parse_inst(inst)


s.print_screen()

print(s.find_sum())
# s.print_screen()
# s.parse_inst('rect 3x4')
# s.print_screen()
# s.parse_inst('rotate column x=1 by 2')
# s.print_screen()







