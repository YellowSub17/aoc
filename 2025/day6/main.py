

#part1
#6.53 am
#7.04 am

#part2
#7.06 am






with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]


line1 = list(map(int, contents[0].split()))
line2 = list(map(int, contents[1].split()))
line3 = list(map(int, contents[2].split()))
line4 = list(map(int, contents[3].split()))
ops = contents[4].split()


count = 0
for x1,x2,x3,x4, op in zip(line1, line2, line3, line4, ops):

    if op =='*':
        count +=  x1*x2*x3*x4
    else:
        count +=  x1+x2+x3+x4

print(count)





def ceph_maths(x1,x2,x3,op):

    count = 0


    x1_dig =  list(map(int, str(x1)))
    x2_dig =  list(map(int, str(x2)))
    x3_dig =  list(map(int, str(x3)))

    print(x1_dig)
    print(x2_dig)
    print(x3_dig)
    print('#')

    max_len = max( len(x1_dig), len(x2_dig), len(x3_dig) )

    x1_dig +=  (max_len - len(x1_dig))*[0]
    x2_dig +=  (max_len - len(x2_dig))*[0]
    x3_dig +=  (max_len - len(x3_dig))*[0]



    # if op=='+':
        # x1_dig +=  (max_len - len(x1_dig))*[0]
        # x2_dig +=  (max_len - len(x2_dig))*[0]
        # x3_dig +=  (max_len - len(x3_dig))*[0]
    # else:
        # x1_dig = (max_len - len(x1_dig))*[0] + x1_dig
        # x2_dig = (max_len - len(x2_dig))*[0] + x2_dig
        # x3_dig = (max_len - len(x3_dig))*[0] + x3_dig




    print(x1_dig)
    print(x2_dig)
    print(x3_dig)



    # if op=='+':
        # count = 0
        # for i_dig in range(max_len):
            # print(x1_dig[i_dig]*100 + x2_dig[i_dig]*10 + x3_dig[i_dig])

            # count += x1_dig[i_dig]*100 + x2_dig[i_dig]*10 + x3_dig[i_dig]
    # else:
        # count = 1
        # for i_dig in range(max_len):
            # print(x1_dig[i_dig]*100 + x2_dig[i_dig]*10 + x3_dig[i_dig])
            # count *= x1_dig[i_dig]*100 + x2_dig[i_dig]*10 + x3_dig[i_dig]


  #   else:

        # x1_dig =  list(map(int, str(x1)))
        # x2_dig =  list(map(int, str(x2)))
        # x3_dig =  list(map(int, str(x3)))

        # max_len = max( len(x1_dig), len(x2_dig), len(x3_dig) )

        # x1_dig = (max_len - len(x1_dig))*[0] + x1_dig
        # x2_dig = (max_len - len(x2_dig))*[0] + x2_dig
        # x3_dig = (max_len - len(x3_dig))*[0] + x3_dig



        # print(x1_dig, '*')
        # print(x2_dig, '*')
        # print(x3_dig)
        # count = 1

        # for i_dig in range(max_len):
            # print(x1_dig[i_dig]*100 + x2_dig[i_dig]*10 + x3_dig[i_dig])
            # count *= x1_dig[i_dig]*100 + x2_dig[i_dig]*10 + x3_dig[i_dig]






    print('$$$$', count)
    return count






# with open('./input.test') as f:
    # contents = f.read().split('\n')[:-1]


# line1 = list(map(int, contents[0].split()))
# line2 = list(map(int, contents[1].split()))
# line3 = list(map(int, contents[2].split()))
# # line4 = list(map(int, contents[3].split()))
# ops = contents[3].split()


# count = 0
# for x1,x2,x3, op in zip(line1, line2, line3, ops):


    # count += ceph_maths(x1,x2,x3,op)


# print(count)







# print(ceph_maths(123, 45, 6, '*'))
# print(ceph_maths(328, 64, 98, '+'))
print(ceph_maths(51, 387, 215, '*'))
print(ceph_maths(64, 23, 314, '+'))





