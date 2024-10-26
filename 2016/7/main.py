


import re



with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]





def has_abba(s):

    s_len = len(s)
    index = 0

    while index < s_len-4:

        outer_cond = s[index] == s[index+3]
        inner_cond = s[index+1] == s[index+2]

        if outer_cond and inner_cond:
            return True
        else:
            index +=1

    return False


def get_abas(s):

    s_len = len(s)

    abas = []
    for index in range(s_len-2):

        outer_cond = s[index] == s[index+2]
        inner_cond = s[index] != s[index+1]

        if outer_cond and inner_cond:
            abas.append(s[index:index+3])

    return abas


def calc_babs(abas):

    babs = []

    for aba in abas:
        babs.append(f'{aba[1]}{aba[0]}{aba[1]}')

    return babs


def supports_ssl(s):

    not_brackets = re.findall('\\][a-z]*\\[', s )
    lhs = s.split('[')[0]
    rhs = s.split(']')[-1]

    
    abas = []

    for not_bracket in not_brackets:
        abas += get_abas(not_bracket)

    abas += get_abas(lhs)
    abas += get_abas(rhs)

    print(f'{abas=}')



    calculated_babs = calc_babs(abas)


    print(f'{calculated_babs=}')



    babs = []
    brackets = re.findall('\\[[a-z]*\\]',s )
    for bracket in brackets:
        babs += get_abas(bracket)



    print(babs)
    print(f'{babs=}')


    for calculated_bab in calculated_babs:
        if calculated_bab in babs:
            return True

    return False


    








def supports_tls(s):

    brackets = re.findall('\\[[a-z]*\\]',s )
    for bracket in brackets:
        if has_abba(bracket[1:-1]):
            return False

    not_brackets = re.findall('\\][a-z]*\\[', s)

    for not_bracket in not_brackets:
        if has_abba(not_bracket[1:-1]):
            return True

    lhs = s.split('[')[0]
    if has_abba(lhs):
        return True

    rhs = s.split(']')[-1]
    if has_abba(rhs):
        return True

    return False


s ='hrllo[worold]thsisis[me]lifeshsould[beb]fun[forerery]oneen'
print(supports_tls(s))




### part 1

# ip_count = 0
# for ip in contents:
    # if supports_tls(ip):
        # ip_count +=1

# print(ip_count)






s ='aaa[bab]rewqt[sfyyew]tqopowryret[pop]'

s='zazbz[bzb]cdba'
print(supports_ssl(s))


### part 2


ip_count = 0
for ip in contents:
    print('########')

    x = supports_ssl(ip)
    print(x)

    if x:
        ip_count +=1

    print('########')

print(ip_count)





# 248 too low








