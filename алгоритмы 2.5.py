import time
t_start = time.perf_counter()
def selection_sort(q):
    for i in range(len(q)):
        m = q[i]
        for j in range(i, len(q)):
            if q[j] < m:
                m = q[j]
                h = q[i]
                q[i] = q[j]
                q[j] = h


with open('input.txt') as f:
    n = int(f.readline())
    a = f.readline()
a = a.split()
for i in range(len(a)):
         a[i] = int(a[i])
selection_sort(a)
with open('output.txt', 'w') as f:
    f.write(str(a))
print(a)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))