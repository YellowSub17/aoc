


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
current_start = -1
current_stop = -1

for start, stop in  fresh_ranges:
    if start> current_stop:
        fresh_ranges_no_overlap.append( (start, stop) )
        current_start, current_stop = start, stop

    else:
        fresh_ranges_no_overlap[-1] = (current_start, stop)
        current_stop = max(current_stop, stop)








# fresh_ranges.sort(key = lambda r: r[0])
# fresh_ranges_no_overlap = []
# for i, ( fresh_range_n, fresh_range_n1) in enumerate(zip(fresh_ranges, fresh_ranges[1:])):
    # print('#####')
    # print(fresh_range_n, fresh_range_n1)
    # x = range(fresh_range_n[0], fresh_range_n[1]+1)
    # y = range(fresh_range_n1[0], fresh_range_n1[1]+1)
    # inte = range(max(x[0], y[0]), min(x[-1], y[-1])+1)
    # print(inte)
    # print([i for i in inte])



    # if len(inte)==0:
        # fresh_ranges_no_overlap.append(fresh_range_n)
        # print('appended ', fresh_range_n)

    # else:

        # if x[0]< y[0] and x[1]>y
        # fresh_ranges_no_overlap.append((fresh_range_n[0], inte[0]-1))

        # print('appended ',(fresh_range_n[0], inte[0]-1))

# fresh_ranges_no_overlap.append(fresh_ranges[-1])

# print(fresh_ranges_no_overlap)






fresh_ranges.sort(key = lambda r: r[0])

count = 0
for i, fresh_range in enumerate(fresh_ranges):
    print(i, fresh_range)

    









# fresh_ranges.sort(key = lambda r: r[0]) #sort by the starts of the ranges

# fresh_ranges_no_overlap = []

# count  =0
# # while count <10:
# while len(fresh_ranges)>0:
    # count +=1

    # #find the smallest ending range value
    # fresh_ranges.sort(key = lambda r: r[1]) #sort by the starts of the ranges
    # smend = fresh_ranges[0][1]

    # #find the smallest starting range value
    # fresh_ranges.sort(key = lambda r: r[0]) #sort by the starts of the ranges
    # smstart = fresh_ranges[0][0]

    # fresh_ranges_no_overlap.append( (smstart, smend))
    
    # fresh_ranges.pop(0)


# for i in fresh_ranges_no_overlap:
    # print(i)


# fresh_ranges_no_overlap_comp = []

# skip_once=False
# for i, ( fresh_range_n, fresh_range_n1) in enumerate(zip(fresh_ranges_no_overlap[:-1], fresh_ranges_no_overlap[1:])):
    # if skip_once:
        # skip_once=False
        # continue

    # if fresh_range_n[1] < fresh_range_n1[0]:
        # fresh_ranges_no_overlap_comp.append(fresh_range_n)
    # else:
        # fresh_ranges_no_overlap_comp.append((fresh_range_n[0], fresh_range_n1[1]))
        # skip_once = True



# print('####')
# for i in fresh_ranges_no_overlap_comp:
    # print(i)











# skip_once=False
# for i, ( fresh_range_n, fresh_range_n1) in enumerate(zip(fresh_ranges[:-1], fresh_ranges[1:])):
    # if skip_once:
        # skip_once=False
        # continue

    # if fresh_range_n1[1] < fresh_range_n[1]:  #if the current range completly encloses the next range, skip the next one
        # fresh_ranges_no_overlap.append(fresh_range_n)
        # skip_once = True



    # elif fresh_range_n[1] < fresh_range_n1[0]: #if the current range stops before the next one begins
        # fresh_ranges_no_overlap.append(fresh_range_n)

    # else:
        # fresh_ranges_no_overlap.append( (fresh_range_n[0], fresh_range_n1[0]-1) )

# fresh_ranges_no_overlap.append(fresh_ranges[-1])






count = 0

for fresh_range in fresh_ranges_no_overlap:
    count += 1+fresh_range[1]-fresh_range[0]

print(count)


# 316924510848106 too low
# 317225287022946 too low

# 340828799014220 too high




