keys = []

with open('field_list.txt') as f:
    for line in f:
        x = line.split('\t')[0]
        keys.append(x)

keys[0] = keys[0].lstrip('\ufeff')

print(keys)
