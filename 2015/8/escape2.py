#!/usr/bin/env python3

import ast
memory_count = 0
raw_count = 0
fname = 'input.prod'

file = open(fname, 'r')
cont =  file.read().split('\n')[:-1]
print(len(cont))


for line in cont:
    raw = line.strip()
    parsed = ast.literal_eval(raw) # This is probably cheating

    raw_count += len(raw)
    memory_count += len(parsed)

print(raw_count - memory_count)
