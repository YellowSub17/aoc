








with open('./input.prod', 'r') as f:
    codes = f.read().split('\n')[:-1]




# codes = codes[:15]





cols = [{}, {}, {}, {}, {}, {}, {}, {},]

for code in codes:

    for col_dir, char in zip(cols, code):

        if char not in col_dir.keys():
            col_dir[char] = 1
        else:
            col_dir[char] += 1




print()
password1 = ''
password2 = ''
for col in cols:

    keys_sorted_common = sorted(list(col.keys()), key=lambda x:col[x], reverse=True)
    password1 +=keys_sorted_common[0]

    keys_sorted_uncommon = sorted(list(col.keys()), key=lambda x:col[x])
    password2 +=keys_sorted_uncommon[0]

print('Password (most common letter):')
print(password1)

print('Password (least common letter):')
print(password2)







