






valid_tri_count = 0

with open('./input.prod', 'r') as f:
    triangles = f.read().split('\n')[:-1]




for tri in triangles:
    lens = tri.split()
    a, b, c = int(lens[0]), int(lens[1]), int(lens[2])

    valid = a+b>c and c+a>b and b+c>a
    if valid:
        valid_tri_count +=1

# print('Number of valid triangles (rows):')
# print(valid_tri_count)


# triangles = triangles[:21]
# for i in triangles:
    # print(i)

# for row1, row2, row3 in zip(triangles[::3], triangles[1::3], triangles[2::3]):
    # print(row1, row2, row3, sep='\n')



# print('#####')

valid_tri_count = 0

for row1, row2, row3 in zip(triangles[::3], triangles[1::3], triangles[2::3]):


    a_lens = row1.split()
    b_lens = row2.split()
    c_lens = row3.split()

    for col_i in range(3):
        a, b, c = int(a_lens[col_i]), int(b_lens[col_i]), int(c_lens[col_i])
        valid = a+b>c and c+a>b and b+c>a

        if valid:
            valid_tri_count +=1


#1823 too low


print('Number of valid triangles (cols):')
print(valid_tri_count)






    


