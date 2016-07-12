import dill

name = 'cart69'

with open('./'+name+'.dill', 'rb') as f:
    out = dill.load(f)


# for set in range(0, 10):
data = out['problem_data']
sol = out['solution'][-1][-1]

sol.prepare(data)

writeList = []

for state in data['state_list']:
    x = sol.evaluate(state)
    writeList.append(x)
    # print(x)

# print(sol.evaluate('xb'))
# print(sol.evaluate('yb'))

u = sol.evaluate('w')
writeList.append(u)

t = sol.evaluate('t')
writeList.append(t)
# print(t)

# print(writeList)

with open(name+".txt", "w") as my_file:
    for set in writeList:
        for element in set:
             my_file.write(str(element) + '  ')
        my_file.write('\n\n')
