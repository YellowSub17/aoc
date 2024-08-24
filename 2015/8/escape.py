


import re




filename = './input.prod'


with open(filename,'r') as f:
    lines = f.read().split('\n')[:-1]



code = sum([len(x) for x in lines])
mem = sum([len(x.encode("utf-8").decode('unicode-escape'))-2 for x in lines])
print(code-mem)

extended = sum([len(re.sub('"', '"\"', repr(x))) for x in lines])

print(extended - code)


# hex_chars = '0123456789abcdef'


# hex_pairs = []
# for hex1 in hex_chars:
    # for hex2 in hex_chars:
        # hex_pairs.append( f'\\x{hex1}{hex2}')

# # print(hex_pairs)


# # "\"\xe8\"ec\xeah\"qo\\g\"iuqxy\"e\"y\xe7xk\xc6d"


# chrs_of_code_for_str_lit = 0
# chrs_in_memory = 0

# for string in strings:
    # print('##', string)
    

    
    # string_chars = 0
    # string_mem = 0





    # num_internal_qoutes = string.count('"')-2

    # num_hex_chars = 0
    # for hex_pair in hex_pairs:

        # num_hex_chars += string.count(f'{hex_pair}')
        # if string.count(f'{hex_pair}')>0:
            # print(f'found {string.count(hex_pair)} cases of {hex_pair}')


    # num_backslash = string.count('\\\\')



    # string_mem = len(string) -2 - num_hex_chars*(3) - num_internal_qoutes  - num_backslash

    # chrs_of_code_for_str_lit += len(string)
    # chrs_in_memory += string_mem

    # print(len(string), string_mem)
    # print()


# "\"\xe8\"ec\xeah\"qo\\g\"iuqxy\"e\"y\xe7xk\xc6d"

# print(chrs_of_code_for_str_lit - chrs_in_memory)


