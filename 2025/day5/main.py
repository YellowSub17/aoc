


with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]

contents_spl = contents.index('')

fresh_ranges = contents[:contents_spl]
fruit_ids = contents[contents_spl+1:]

def split_range(r):
    spl = r.split('-')
    return int(spl[0]), int(spl[1])



def is_fresh(fruit_id, fresh_range):
    return fresh_range[0] <= fruit_id <= fresh_range[1]


fresh_ranges = list(map(split_range, fresh_ranges))
# fruit_ids = list(map(int, fruit_ids))
# fresh_count = 0

# for fruit_id in fruit_ids:
    # print(fruit_id)
    # for fresh_range in fresh_ranges:
        # if is_fresh(fruit_id, fresh_range):
            # print('fresh!')
            # fresh_count +=1
            # break


# print(fresh_count)






# fresh_ranges.sort(key = lambda r: r[0])

# fresh_ranges_no_overlap = []
# for i, ( fresh_range_n, fresh_range_n1) in enumerate(zip(fresh_ranges, fresh_ranges[1:])):
    # print(fresh_range_n, fresh_range_n1)
    # if fresh_range_n[1] < fresh_range_n1[0]:
        # fresh_ranges_no_overlap.append(fresh_range_n)
    # else:
        # fresh_ranges_no_overlap.append( (fresh_range_n[0], fresh_range_n1[0]-1) )
# fresh_ranges_no_overlap.append(fresh_ranges[-1])





fresh_ranges.sort(key = lambda r: r[0])

fresh_ranges_no_overlap = []

# fresh_ranges_no_overlap.append(fresh_ranges[0])


# while len(fresh_ranges)>0:

    # fresh_ranges.sort(key = lambda r: r[0])

    # lhs = fresh_ranges[0]

    # fresh_ranges.sort(key = lambda r: r[1])

    # rhs = fresh_ranges[0]

    # fresh_ranges_no_overlap.append((lhs[0], rhs[1]))

    # fresh_ranges.pop(0)



    









for i, ( fresh_range_n, fresh_range_n1) in enumerate(zip(fresh_ranges[:-1], fresh_ranges[1:])):

    # print(fresh_range_n, fresh_range_n1)
    if fresh_range_n[1] < fresh_range_n1[0]:
        fresh_ranges_no_overlap.append(fresh_range_n)
    elif fresh_range_n[1] >= fresh_range_n1[1]:
        fresh_ranges_no_overlap.append(fresh_range_n)
    else:
        fresh_ranges_no_overlap.append( (fresh_range_n[0], fresh_range_n1[0]-1) )

fresh_ranges_no_overlap.append(fresh_ranges[-1])






for i, ( fresh_range_n, fresh_range_n1) in enumerate(zip(fresh_ranges_no_overlap, fresh_ranges_no_overlap[1:])):
    print(fresh_range_n, fresh_range_n1)
    print(fresh_range_n[1]< fresh_range_n1[0])




count = 0

for fresh_range in fresh_ranges_no_overlap:
    count += 1+fresh_range[1]-fresh_range[0]

print(count)


# 316924510848106 too low

# 340828799014220 too high




