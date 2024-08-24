




def count_hexes(s):


    for i, char in enumerate(s[:-2]):
        if char =='\\':
            if char

    print('strip_hexes:', x_loc)

    # return new_s, n








filename = './input.test'


with open(filename,'r') as f:
    strings = f.read().split('\n')[:-1]



hex_chars = '0123456789abcdef'

chrs_of_code_for_str_lit = 0
chrs_in_memory = 0

for string in strings:
    print('>>', string)

    chrs_string_literal = len(string)
    print('chrs of code:', chrs_string_literal)
    strip_hexes(string)

    print()







