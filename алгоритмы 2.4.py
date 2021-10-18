import time
t_start = time.perf_counter()
def linear_search(li, v):
    index = []
    for i in range(len(li)):
        if li[i] == v:
            index.append(i)
    if not index:
        index.append(-1)
    return index
with open('input.txt') as f:
   a = f.readline()
   v = f.readline()
a = a.split()
b = linear_search(a, v)
b = ' '.join(map(str, b))
with open('output.txt', 'w') as f:
    if linear_search(a, v) == None:
        f.write('-1')
    else:
        f.write(str(b))
print(b)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
