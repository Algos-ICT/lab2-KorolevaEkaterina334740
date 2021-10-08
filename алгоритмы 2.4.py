import time
t_start = time.perf_counter()
def linear_search(li, v):
    i = 0
    l = len(li)
    while i < l and v != li[i]:
        i += 1

    if i < l:
        b.append(-1)
    else: b.append(i)
    return i if i < l else None
b = []

with open('input.txt') as f:
   a = f.readline()
   v = f.readline()
a = a.split()
linear_search(a, v)
with open('output.txt', 'w') as f:
    if linear_search(a, v) == None:
        f.write('-1')
    else:
        f.write(str(b))
print(b)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
