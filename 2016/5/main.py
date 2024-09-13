


import hashlib



# door_id = 'reyedfim'
# # door_id = 'abc'


# password = ''
# i = 0
# while len(password) < 8:
    # print(i, end='\r')

    # str2hash = f'{door_id}{i}'.encode()
    # result = hashlib.md5(str2hash).hexdigest()

    # if result[:5] == '00000':
        # print('#################################')
        # print(i)
        # print(result)
        # password += result[5]
        # print('Current Password:')
        # print(password)
        # print('#################################')
    # i +=1


# print('#################################')
# print('#################################')
# print('#################################')
# print('First door password:')
# print(password)






door_id = 'reyedfim'
# door_id = 'abc'

password = list('********')
i = 0

while '*' in password:
    print(i, end='\r')

    str2hash = f'{door_id}{i}'.encode()
    result = hashlib.md5(str2hash).hexdigest()

    if result[:5] == '00000':
        print('#################################')
        print('ID: ', i)
        print('Result: ', result)
        pos = result[5]
        if pos.isdigit():
            if int(pos) <8:
                if password[int(pos)] == '*':
                    password[int(pos)] = result[6]
                else:
                    print(f'Position {pos} already filled.')
        print('Current Password:')
        print(''.join(password))
        print('#################################')

    i +=1


print('#################################')
print('#################################')
print('#################################')
print('Second door password:')
print(''.join(password))


###863dde27













