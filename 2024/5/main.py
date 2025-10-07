

with open('./input.prod', 'r') as f:
    cont = f.read().split('\n')[:-1]

rules = []
books = []

for line in cont:
    if '|' in line:
        rules.append(line)
    elif ',' in line:
        books.append(line.split(','))
        # books.append(line)


rules_dict = {}

for rule in rules:
    x, y = rule.split('|')

    if x in rules_dict.keys():
        rules_dict[x].append(y)
    else:
        rules_dict[x] = [y]



# print(rules_dict)





def get_mid_of_valid_book(book):

    rev_book = book[::-1]

    for i, current_page in enumerate(rev_book):
        if current_page not in rules_dict.keys():
            continue

        for j, check_page in enumerate(rev_book[i+1:]):

            if check_page in rules_dict[current_page]:
                print('Fail: ', current_page, check_page)
                return 0
            else:
                continue

    mid = len(book)//2
    return int(book[mid])



# count = sum(map(get_mid_of_valid_book, books))
# print(count)





def sort_invalid(book):
    rev_book = book[::-1]

    for i, current_page in enumerate(rev_book):
        if current_page not in rules_dict.keys():
            continue

        for j, check_page in enumerate(rev_book[i+1:]):

            if check_page in rules_dict[current_page]:

                # fail_i = book.index(check_page)
                # fail_page = book.pop(fail_i)
                # book.append(fail_page)

                fail_i = book.index(current_page)
                fail_page = book.pop(fail_i)
                book = [fail_page] + book

                return sort_invalid(book[:])


            else:
                continue

    return book[:]






def get_mid_of_invalid_book(book):

    rev_book = book[::-1]

    for i, current_page in enumerate(rev_book):
        if current_page not in rules_dict.keys():
            continue

        for j, check_page in enumerate(rev_book[i+1:]):

            if check_page in rules_dict[current_page]:
                print('Fail: ', current_page, check_page)
                try:
                    sorted_book = sort_invalid(book[:])
                except RecursionError:
                    print('RRRRR!!!')
                    print(book[:])
                    quit()
                mid = len(sorted_book)//2
                return int(sorted_book[mid])
            else:
                continue

    return 0



b = ['78', '34', '43', '71', '33', '77', '93', '22', '17', '74', '73', '75', '97']
print('book', b[:])
print('mid of valid', get_mid_of_valid_book(b[:]))
print('sorted', sort_invalid(b[:]))
print('mid of invalid', get_mid_of_invalid_book(b[:]))




count = sum(map(get_mid_of_invalid_book, books))
print(count)

