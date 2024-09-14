







class StateMachine:


    def __init__(self, insts, a, b, instruction_index):

        self.insts = insts

        self.a = a
        self.b = b

        self.instruction_index = instruction_index
        self.max_instruction_index = len(insts)


    def run_inst(self):

        if self.instruction_index >= self.max_instruction_index:
            print('##################')
            print('Instruction index out of bounds. Ending program.')
            print(f'Reg. a: {self.a}')
            print(f'Reg. b: {self.b}')
            print('##################')
            self.instruction_index = -1

            return self.a, self.b, self.instruction_index


        inst = self.insts[self.instruction_index]
        print(f'Instruction: ', inst)

        fn = inst.split()[0]
        args = inst.split()[1:]


        if fn == 'hlf':
            reg = args[0]
            if reg=='a':
                self.a /= 2
                self.a = int(self.a)
            elif reg=='b':
                self.b /= 2
                self.b = int(self.b)
            self.jump(1)


        elif fn == 'tpl':
            reg = args[0]
            if reg=='a':
                self.a *=3
            elif reg=='b':
                self.b *=3
            self.jump(1)


        elif fn == 'inc':
            reg = args[0]
            if reg=='a':
                self.a+=1
            elif reg=='b':
                self.b+=1
            self.jump(1)


        elif fn == 'jmp':
            inc = int(args[0])
            self.jump(inc)


        elif fn == 'jie':
            reg = args[0][0]
            inc = int(args[1])
            if reg == 'a' and self.a%2==0:
                self.jump(inc)
            elif reg == 'b' and self.b%2==0:
                self.jump(inc)
            else:
                self.jump(1)

        elif fn == 'jio':
            reg = args[0][0]
            inc = int(args[1])
            if reg == 'a' and self.a==1:
                self.jump(inc)
            elif reg == 'b' and self.b==1:
                self.jump(inc)
            else:
                self.jump(1)

        

        return self.a, self.b, self.instruction_index




    def jump(self, inc):
        self.instruction_index += inc
        print(f'Instruction Index: {self.instruction_index}')





with open('./input.prod', 'r') as f:
    insts = f.read().split('\n')[:-1]




a = 1
b = 0
instruction_index = 0


count = 0
while instruction_index>=0:

    print(f'{count=}, {a=}, {b=}, {instruction_index=}')
    s = StateMachine(insts, a, b, instruction_index)

    a, b, instruction_index = s.run_inst()
    count +=1
    










