






with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]










class State:

    def __init__(self, instructions):

        self.instructions = instructions

        self.mem = {'a':0,
                    'b':0,
                    'c':1,
                    'd':0}

        self.index = 0


    def run(self):

        instruction = self.instructions[self.index]
        # print(f'#### {instruction}')
        # print(f'{self.mem}')


        match instruction.split():

            case ('inc', reg):
                self.incdec(reg, 1)

            case ('dec', reg):
                self.incdec(reg, -1)

            case ('cpy', val, reg):
                self.cpy(val, reg)

            case ('jnz', reg, jmp):
                self.jnz(reg, jmp)

            case _:
                print('Unknown')
                return


        # print(f'####')




    def jnz(self, val, jmp):
        # print(f'Jumping: {val} {jmp}')
        if val.isnumeric():
            if int(val) !=0:
                self.index += int(jmp)
            else:
                self.index += 1
            return


        if self.mem[val] != 0:
            self.index += int(jmp)
        else:
            self.index += 1



    def cpy(self, val, reg):
        # print(f'Copying: {val} {reg}')
        if val.isnumeric():
            self.mem[reg] = int(val)
        else:
            self.mem[reg] = int(self.mem[val])
        self.index += 1





    def incdec(self, reg, sf):
        # print(f'inc/dec: {reg} {sf}')
        self.mem[reg] += int(sf)
        self.index +=1




if __name__ == "__main__":


    s = State(contents)



    print(s.mem)
    while s.index < len(s.instructions):
        s.run()
    print(s.mem)

