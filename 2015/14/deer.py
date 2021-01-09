#!/usr/bin/env python3




class Deer:

    def __init__(self, s):
        words = s.split()
        self.s = s
        self.name = words[0]
        self.fly_v = int(words[3])
        self.fly_t = int(words[6])
        self.rest_t = int(words[-2])
        self.current_x = 0

        self.resting = False
        self.current_t = 0
        self.points = 0



    def fly_for(self, t):

        num_full_cycles =  int( t/(self.fly_t + self.rest_t) )
        self.current_x += num_full_cycles*self.fly_t*self.fly_v

        remainder_t = t - num_full_cycles*(self.fly_t + self.rest_t)

        if remainder_t < self.fly_t:
            self.current_x += remainder_t*self.fly_v
        else:
            self.current_x += self.fly_v*self.fly_t


        # print(f'After flying for {t} seconds, {self.name} is at a distance of {self.current_x} km.')
        
        return self.current_x

    def fly_1(self):

        if not self.resting:
            self.current_x += self.fly_v

            self.current_t +=1

            if self.current_t >= self.fly_t:
                self.current_t = 0
                self.resting =True

        else:
            self.current_t += 1

            if self.current_t >=self.rest_t:
                self.current_t = 0
                self.resting = False

                








def find_first(deers):
    current_firsts = []
    current_lead_x = 0

    for deer in deers:
        if deer.current_x > current_lead_x:
            current_firsts = []
            current_firsts.append(deer)
            current_lead_x = deer.current_x

        elif deer.current_x == current_lead_x:
            current_firsts.append(deer)


    for deer in current_firsts:
        deer.points +=1
        print(deer.name, deer.points)










if __name__ == '__main__':

    file = open('input.prod', 'r')

    cont = file.read()
    file.close()
    lines = cont.split('\n')[:-1]

    dx = Deer(lines[0])

    #######part1
    # furthest=0
    # for line in lines:
        # d1 = Deer(line)
        # x = d1.fly_for(2503)
        # if x >furthest:
            # furthest = x
            # print(d1.name, 'is in the lead!')


    ########part2
    deers = []
    for line in lines:
        d1 = Deer(line)
        deers.append(d1)

    for i in range(2503):
        for deer in deers:
            deer.fly_1()

        find_first(deers)



    for deer in deers:
        print(deer.name, deer.points)






