#5 + 4 * 4 + 3 * 3
#5 + 16 + 9
#30

q = '5 + 4 * 4 + 3 * 3'.replace(" ", "")

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b


exp = []
for i in range(len(q)):
    exp.append(q[i])

for i in range(len(exp)):
    try:
        if int(exp[i]):
            exp[i] = int(exp[i])
    except:
        continue

print("exp before : ", exp)
copied = exp.copy()


for i in range(len(exp)):
    try:
        if copied[i] == '*':
            exp[i - 1] *= exp[i + 1]
            exp[i] = 'R'
            exp[i + 1] = 'R'
    except:
        break
while('R' in exp):
    exp.remove('R')

copied = exp.copy()

for i in range(len(exp)):
    try:
        if copied[i] == '+':
            exp[i - 1] += exp[i + 1]
            exp[i] = 'R'
            exp[i + 1] = 'R'
    except:
        break
while('R' in exp):
    exp.remove('R')

print("exp after: ", exp)
print("copied: ", copied)







