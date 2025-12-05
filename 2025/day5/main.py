


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

for start, stop in  sorted(fresh_ranges):
    print((start,stop), current_start, current_stop, start> current_stop)
    # breakpoint()
    if start> current_stop:
        current_start, current_stop = start, stop
        fresh_ranges_no_overlap.append( (start, stop) )
        print('appended',  (start, stop) )

    elif current_stop> stop:
        continue

    else:
        current_stop = max(current_stop, stop)
        fresh_ranges_no_overlap[-1] = (current_start, stop)

        print('moified end', (current_start, stop) )








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









count = 0

for fresh_range in fresh_ranges_no_overlap:
    print(fresh_range, 1+fresh_range[1]-fresh_range[0])
    count += 1+fresh_range[1]-fresh_range[0]

print(count)


# 316924510848106 too low
# 317225287022946 too low

# 331492094722011 wrong

# 340828799014220 too high




