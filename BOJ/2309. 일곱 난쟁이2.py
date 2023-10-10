arr = []
for _ in range(9):
    arr.append(int(input()))

sum_v = sum(arr)
new_arr = []

for i in range(8):
    for j in range(i+1, 9):
        if arr[i] + arr[j] == sum_v - 100:
            new_arr.append(arr[i])
            new_arr.append(arr[j])

arr.remove(new_arr[0])
arr.remove(new_arr[1])
arr.sort()
print(*arr, sep='\n')