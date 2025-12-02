





with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]




def split_instr(instr):

    if instr[0] == 'L':
        d = -1
    else:
        d = 1
    return int(instr[1:])*d




current_ind = 50
zero_count = 0

for instr in contents:

    current_ind = current_ind+split_instr(instr)
    if current_ind%100 ==0:
        zero_count +=1
print(zero_count)






### edited reddit
current_ind = 50

zero_count_1 = 0
zero_count_2 = 0
print(current_ind)
for instr in contents:

    next_ind = current_ind +split_instr(instr)
    zero_count_1 += (next_ind %100==0)


    zero_count_2 += abs(next_ind//100 - current_ind//100)

    if next_ind < current_ind:
        zero_count_2 += ( next_ind %100 ==0) - (current_ind %100==0)


    current_ind = next_ind




    ####my attempt
   #  zero_passes = 0
    # if next_ind <= 0:
        # if current_ind!=0:
            # zero_passes = abs( int(next_ind/100) - 1 )
    # if next_ind >=100:
        # zero_passes = int(next_ind/100)
    # zero_count +=zero_passes
    # print(f'*Turning {instr} from {current_ind} to {next_ind%100}')
    # print(f'\t Passed zero {zero_passes} times')
    # current_ind = next_ind %100




#### what I found on reddit
print(zero_count_1, zero_count_2)

d, t1, t2 = 50, 0, 0
for l in contents:
    n = d + ( -1 if l[ 0 ] == 'L' else 1 ) * int( l[ 1 : ] )
    t1 += ( n % 100 == 0 )
    t2 += abs( n // 100 - d // 100 )
    if n < d: t2 += ( n % 100 == 0 ) - ( d % 100 == 0 )
    d = n
print( t1, t2 )

##2583
##3283
##5593 too low
##7491
##6298
