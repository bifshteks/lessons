import re


a = []
with open('dataset_3380_5(1).txt', 'r') as file:
    for line in file:
        a.append(re.split(r'\s+', line)[:-1])
classes = {}
for i in range(1, 12):
    classes.update([(i, [])])
for lst in a:
    classes[int(lst[0])].append(int(lst[2]))
for key, val in classes.items():
    if val == []:
        classes[key] = '-'
    else:
        classes[key] = sum(val) / len(val)

with open('res.txt', 'w') as f:
    for key, val in classes.items():
        f.write(str(key) + ' ' + str(val) + '\n')
