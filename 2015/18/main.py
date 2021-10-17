






class LightArray:


    def __init__(self, input_str):
        self.input_str = input_str
        self.array = self.input_str.split('\n')[:-1]

        first_row_sub_corns = self.array[0][1:-1]
        self.array[0] = '#' + first_row_sub_corns + '#'

        last_row_sub_corns = self.array[-1][1:-1]
        self.array[-1] = '#' + last_row_sub_corns + '#'




        self.ny = len(self.array)
        self.nx = len(self.array[0])


    def count_on(self):

        sum_str = ''
        for row in self.array:
            sum_str += row

        return sum_str.count('#')

    def n_adj_on(self, x,y):
        

        n_on = 0
        xs = x-1, x, x+1
        ys = y-1, y, y+1

        for xpos in xs:
            for ypos in ys:
                if xpos ==x and ypos==y:
                    continue

                if xpos <0 or xpos >99 or ypos <0 or ypos>99:
                    continue

                if self.array[ypos][xpos]=='.':
                    continue

                if self.array[ypos][xpos]=='#':
                    n_on +=1
                    continue
        return n_on

    def iterate(self):

        new_array = []
        for iy in range(self.ny):
            new_row = ''
            for ix in range(self.nx):
                current_light = self.array[iy][ix]

                n_adj_on = self.n_adj_on(ix, iy)


                #corners on
                if (ix, iy) in [ (0,0), (self.nx-1, self.ny-1), (0, self.ny-1), (self.nx-1, 0)]:
                    new_row +='#'
                    continue
                    

                if current_light=='#':
                    if n_adj_on ==2 or n_adj_on==3:
                        new_row +='#'
                    else:
                        new_row +='.'
                else:
                    if n_adj_on==3:
                        new_row +='#'
                    else:
                        new_row +='.'

            new_array.append(new_row)

        self.array = new_array





if __name__ == "__main__":

    in_file = open('input.txt', 'r')
    lights_str = in_file.read()
    in_file.close()
    # print(lights_str)

    la = LightArray(lights_str)

    for i in range(100):
        print(f'iter {i}')
        la.iterate()

    print(la.count_on())


