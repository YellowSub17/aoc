#!/usr/bin/env python3

import hashlib



if __name__ == "__main__":


    seed = 'yzbqklnj'

    count = 0
    start = '000010'

    while start != '000000':
        hash_in = seed+str(count)
        print(f'hash_in: {hash_in}')

        hash_out = hashlib.md5(hash_in.encode('UTF-8'))
        print(f'hash_out: {hash_out.hexdigest()}')
        start = hash_out.hexdigest()[:6]
        print(start, count)
        count +=1
