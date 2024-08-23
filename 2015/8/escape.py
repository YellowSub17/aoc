


filename = './input.test'


with open(filename,'r') as f:
    strings = f.read().split('\n')[:-1]



chrs_of_code_for_str_lit = 0
chrs_in_memory = 0

for string in strings:

    num_internal_qoutes = string.count('\"')-2
    num_hex_chars = string.count('\\x')

    string_mem = len(string) + 




    print(string, len(string), num_internal_qoutes, num_hex_chars )





