




I = 3010
J = 3019

# I = 2
# J = 5





Ij0 = sum(range(I))+1

row_addends = [0] + [I+1+x for x in range(J-1)]

IJ = Ij0
for j, addend in enumerate(row_addends):
    IJ+= addend


# print(IJ)






def generate_n(n):


    IJn = 20151125
    for _ in range(n-1):

        multi = IJn*252533
        remainder = multi % 33554393
        IJn = remainder

    return IJn



print(generate_n(IJ))







