import numpy as np
x = []

a = np.linspace(1, 10, 10)
b = np.linspace(11, 20, 10)
c = np.linspace(21, 30, 10)
d = np.linspace(31, 40, 10)
e = np.linspace(41, 50, 10)
f = np.linspace(51, 60, 10)
g = np.linspace(61, 70, 10)
h = np.linspace(71, 80, 10)
i = np.linspace(81, 90, 10)
j = np.linspace(91, 100, 10)

y = np.array([(a),(b),(c),(d),(e),(f),(g),(h),(i),(j)])
z = np.square(y).astype(int)

n = 1
for v in range(10):
    for w in range(10):
        z[v][w] = n * n
        n+=1
        if z[v][w]%3 == 0:
            x.append(z[v][w])

x = np.array(x)
print(x)