#!/usr/bin/env python3







def look_and_say(s):
    s_out = ''
    count=1
    for a, b in zip(s, s[1:]):
        if a==b:
            count+=1
        else:
            s_out += str(count)
            s_out += a
            count=1

    s_out += str(count)
    s_out += b


    return s_out


def look_and_say2(s):
    s = list(s)
    s_out = []
    unique = []
    count=1
    for a, b in zip(s, s[1:]):
        if a==b:
            count+=1
        else:
            unique.append(str(count))
            unique.append(a)
            count=1

    unique.append(str(count))
    unique.append(b)


    return str(unique)








if __name__ == '__main__':

    x = '1113222113'
    for i in range(50):
        print(i)
        x = look_and_say(x)

    print( '\n\n')
    print(len(x))




