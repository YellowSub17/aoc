


filename = './input.test'


with open(filename,'r') as f:
    strings = f.read().split('\n')[:-1]




hex_chars = '0123456789abcdef'

chrs_of_code_for_str_lit = 0
chrs_in_memory = 0

for string in strings:
    print('##', string)


    string_chars = 0
    string_mem = 0


    
    chrs_of_code_for_str_lit += len(string)


    num_internal_qoutes = string.count('\"')-2

    num_hex_chars = string.count('\\x')

    if num_hex_chars>0:
        hex_pos = string.find('\\x')
        print('$', hex_pos)




    num_backslash = string.count('\\\\')

    string_mem = len(string) - 2 - num_hex_chars*(3) - num_internal_qoutes - num_backslash


    chrs_in_memory += string_mem
    print(len(string), string_mem)
    print()




print(chrs_of_code_for_str_lit - chrs_in_memory)





