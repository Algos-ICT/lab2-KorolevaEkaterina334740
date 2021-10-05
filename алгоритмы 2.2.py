import time
t_start = time.perf_counter()
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        b.append(j+1)


b = [1]
with open('input.txt') as f:
    n = int(f.readline())
    a = f.readline()
a = a.split()
for i in range(n):
    a[i] = int(a[i])
insertion_sort(a)
with open('output.txt', 'w') as f:
    f.write(str(b) + '\n')
    f.write(str(a))
print(b)
print(a)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
